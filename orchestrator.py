import json
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential

# Initialize the Azure AI Project Client
# Make sure you have set the AZURE_AI_PROJECT_ENDPOINT environment variable
project_client = AIProjectClient(
    credential=DefaultAzureCredential(),
    endpoint=os.environ.get("AZURE_AI_PROJECT_ENDPOINT", "https://<your-ai-foundry-endpoint>"),
    project_name="airline-service-center"
)

def route_customer_request(customer_message: str):
    """
    Main entry point for handling customer requests using the Supervisor-Orchestrator-Agent.
    """
    print(f"Customer: {customer_message}")
    
    # Get the Supervisor agent
    try:
        supervisor_agent = project_client.agents.get_agent("Supervisor-Orchestrator-Agent")
    except Exception as e:
        print(f"Error fetching Supervisor agent: {e}")
        return

    # Create a conversation thread
    thread = project_client.agents.threads.create()

    # Add the customer's message to the thread
    project_client.agents.messages.create(
        thread_id=thread.id,
        role="user",
        content=customer_message
    )

    print("Supervisor is processing...")
    # Run the supervisor agent
    run = project_client.agents.runs.create_and_process(
        thread_id=thread.id,
        agent_id=supervisor_agent.id
    )

    # Handle the supervisor's tool calls (routing to other agents)
    if run.status == "requires_action":
        tool_calls = run.required_action.submit_tool_outputs.tool_calls
        tool_outputs = []
        
        for tool_call in tool_calls:
            if tool_call.function.name == "route_to_agent":
                args = json.loads(tool_call.function.arguments)
                target_agent_name = args.get("target_agent")
                extracted_entities = args.get("extracted_entities", {})
                priority = args.get("priority", "medium")
                chain_next = args.get("chain_next")
                
                print(f"-> Routing to: {target_agent_name} (Priority: {priority})")
                print(f"-> Extracted Entities: {json.dumps(extracted_entities, indent=2)}")
                
                # Delegate to the specialized agent
                target_response = call_specialized_agent(target_agent_name, extracted_entities)
                
                # Format the result back for the supervisor
                tool_outputs.append({
                    "tool_call_id": tool_call.id,
                    "output": json.dumps({"status": "success", "agent_response": target_response})
                })
        
        # Submit the results of the specialized agents back to the supervisor to formulate the final answer
        if tool_outputs:
            print("Submitting specialized agent results back to supervisor...")
            final_run = project_client.agents.runs.submit_tool_outputs(
                thread_id=thread.id,
                run_id=run.id,
                tool_outputs=tool_outputs
            )
            # Fetch the final message
            messages = project_client.agents.messages.list(thread_id=thread.id)
            for msg in reversed(messages.data):
                if msg.role == "assistant":
                    print(f"\nFinal Response:\n{msg.content[0].text.value}")
    
    elif run.status == "completed":
        # If the supervisor answered directly without routing (e.g. asking a clarifying question)
        messages = project_client.agents.messages.list(thread_id=thread.id)
        for msg in reversed(messages.data):
             if msg.role == "assistant":
                print(f"\nSupervisor (Direct Reply):\n{msg.content[0].text.value}")
    else:
        print(f"Supervisor run ended with status: {run.status}")


def call_specialized_agent(agent_name: str, payload: dict) -> str:
    """
    Spins up a specialized agent, passes the context/entities, and returns its response.
    """
    try:
         target_agent = project_client.agents.get_agent(agent_name)
    except Exception as e:
         return f"Error: Agent {agent_name} not found. Details: {e}"

    target_thread = project_client.agents.threads.create()
    
    # Pass the structured entities to the specialized agent
    prompt = f"Please process this request based on the following extracted entities:\n{json.dumps(payload, indent=2)}"
    
    project_client.agents.messages.create(
        thread_id=target_thread.id,
        role="user",
        content=prompt
    )
    
    print(f"   [{agent_name}] processing request...")
    target_run = project_client.agents.runs.create_and_process(
        thread_id=target_thread.id,
        agent_id=target_agent.id
    )
    
    # In a fully realized system, the specialized agent might also return 'requires_action' here
    # to call the actual Amadeus APIs. For simplicity in this orchestrator script, we assume 
    # the agent handles it or we'd implement a similar tool_call loop here.
    
    if target_run.status == "completed":
        messages = project_client.agents.messages.list(thread_id=target_thread.id)
        # Return the last message from the assistant
        for msg in messages.data:
            if msg.role == "assistant":
                return msg.content[0].text.value
                
    elif target_run.status == "requires_action":
        # TODO: Implement API tool calling logic here for Amadeus APIs
        return f"Agent {agent_name} requested API actions which need to be executed."
        
    return f"Agent {agent_name} finished with status: {target_run.status}"


if __name__ == "__main__":
    # Test Example 1: Direct Routing
    # route_customer_request("Can you pull up my booking? PNR is ABC123")
    
    # Test Example 2: Multi-Intent
    # route_customer_request("I need to change my name from Sarah Johnson to Sarah Williams on booking XYZ789")
    pass
