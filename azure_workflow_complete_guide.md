# Azure AI Architecture Agents — Complete Setup & Workflow Guide

> A step-by-step guide to create, connect, publish, and trigger the multi-agent architecture workflow in Azure AI Foundry.

---

## Table of Contents

1. [Overview: How the Workflow Works](#1-overview-how-the-workflow-works)
2. [Prerequisites](#2-prerequisites)
3. [Step 1: Upload Knowledge Files](#step-1-upload-knowledge-files)
4. [Step 2: Create the 9 Specialist Agents](#step-2-create-the-9-specialist-agents)
5. [Step 3: Create the Orchestrator Agent](#step-3-create-the-orchestrator-agent)
6. [Step 4: Wire Connected Agents](#step-4-wire-connected-agents)
7. [Step 5: Test the Workflow](#step-5-test-the-workflow)
8. [Step 6: Publish the Workflow as an API](#step-6-publish-the-workflow-as-an-api)
9. [Step 7: Trigger the Workflow](#step-7-trigger-the-workflow)
10. [Agent Prompts Reference](#agent-prompts-reference)
11. [Troubleshooting](#troubleshooting)

---

## 1. Overview: How the Workflow Works

```
  ┌──────────────────────────────────────────────────────────────────┐
  │                    USER SENDS REQUIREMENTS                       │
  │          "Design an e-commerce platform on Azure..."             │
  └───────────────────────────┬──────────────────────────────────────┘
                              ▼
  ┌──────────────────────────────────────────────────────────────────┐
  │              CHIEF ARCHITECT ORCHESTRATOR 🎯                     │
  │         (10th Agent — receives all requests)                     │
  │         Uses "Connected Agents" to call the 9 specialists        │
  └───────────────────────────┬──────────────────────────────────────┘
                              │
          ┌───────────────────┼───────────────────────┐
          ▼                   ▼                       ▼
  ┌─── PHASE 1 ───┐  ┌─── PHASE 2 ───────┐  ┌─── PHASE 3 ──┐
  │  EXTRACTION    │  │  EVALUATION        │  │  DESIGN       │
  │                │  │                    │  │               │
  │ 1. Component   │  │ 3. Security 🔐    │  │ 6. Architect  │
  │    Extract 📋  │  │ 4. Performance ⚡  │  │    Design 🏗️  │
  │ 2. Azure       │  │ 5. Cost 💰        │  │ 7. Connection │
  │    Reference🏛️ │  │                    │  │    Expert 🔗  │
  └───────┬────────┘  └────────┬───────────┘  └──────┬────────┘
          │                    │                      │
          └────────────────────┼──────────────────────┘
                               ▼
                   ┌─── PHASE 4 ───────────┐
                   │  VALIDATION            │
                   │                        │
                   │ 8. Requirements        │
                   │    Validation ✅       │
                   │ 9. Architecture        │
                   │    Review 🔍           │
                   └───────────┬────────────┘
                               ▼
                   ┌────────────────────────┐
                   │  IF "NEEDS_CORRECTION" │──► Re-run Phase 3 + 4
                   │  IF "APPROVED"         │──► Return Final Output
                   └───────────┬────────────┘
                               ▼
  ┌──────────────────────────────────────────────────────────────────┐
  │                    FINAL ARCHITECTURE JSON                       │
  │    services, connections, containers, security, performance,     │
  │    cost, validation scores, WAF pillar assessment                │
  └──────────────────────────────────────────────────────────────────┘
```

### How Each Agent Reports to the Orchestrator

Every specialist agent returns its output as **JSON**. The orchestrator:
1. **Calls** Agent 1, receives JSON output
2. **Passes** that output as context when calling Agent 2
3. **Accumulates** all outputs and passes the full context to Agent 6 (Architecture Design)
4. **Collects** the final review from Agent 9
5. **Compiles** everything into a single final architecture response

The orchestrator does NOT store state — it passes data between agents through the **Thread messages**. Each agent reads the conversation thread, does its work, and writes its JSON response back to the thread.

---

## 2. Prerequisites

Before starting, make sure you have:

- [ ] An **Azure subscription** with an active Azure AI Foundry project
- [ ] A **gpt-4o** model deployed in your project (Models + endpoints → Deploy model)
- [ ] Your **Project connection string** (Project → Overview → Project details)
- [ ] (Optional) Your `azure_architecture_training_data.json` file for the knowledge base

---

## Step 1: Upload Knowledge Files

1. Open your project in [Azure AI Foundry Portal](https://ai.azure.com/)
2. On the left menu, click **Vector Stores** (or **Data** → **Vector Stores**)
3. Click **+ Create Vector Store**
4. **Name:** `architecture-knowledge-base`
5. Click **Upload files** and select your training data files (JSON, PDF, or TXT)
6. Click **Create** — Azure will process and index the files
7. **Save the Vector Store name** — you will attach it to each agent

> [!NOTE]
> If you don't see "Vector Stores" in the menu, look under **Tools** → **File Search** → **Manage Vector Stores**. The exact location may vary slightly depending on your portal version.

---

## Step 2: Create the 9 Specialist Agents

For **each** of the 9 agents below, repeat these steps:

1. Go to **Agents** on the left menu
2. Click **+ New Agent** (or **+ Create**)
3. Fill in the fields:
   - **Name:** (see table below)
   - **Model:** Select `gpt-4o`
   - **Instructions:** Paste the system prompt (see [Agent Prompts Reference](#agent-prompts-reference) below)
4. Under **Tools**, enable **File Search**
   - Attach the `architecture-knowledge-base` vector store you created in Step 1
5. Under **Configuration** (if available):
   - **Temperature:** `0.1`
   - **Max Tokens:** `3000` (use `6000` for ArchitectureDesignAgent)
6. Click **Save**

### Agents to Create (in this order):

| # | Agent Name | Role |
|---|-----------|------|
| 1 | `ComponentExtractionAgent` | 📋 Extracts APIs, NFRs, tech stack from requirements |
| 2 | `AzureReferenceAgent` | 🏛️ Maps components to Azure reference architectures |
| 3 | `SecurityAgent` | 🔐 Zero Trust analysis, threat modeling, compliance |
| 4 | `PerformanceAgent` | ⚡ Scaling strategy, caching, latency optimization |
| 5 | `CostOptimizationAgent` | 💰 FinOps analysis, RI/Savings Plans, SKU sizing |
| 6 | `ArchitectureDesignAgent` | 🏗️ Designs the complete Azure topology |
| 7 | `ConnectionExpertAgent` | 🔗 Validates and optimizes service connections |
| 8 | `RequirementsValidationAgent` | ✅ Verifies 100% requirements coverage |
| 9 | `ArchitectureReviewAgent` | 🔍 Final WAF 5-pillar quality gate |

> [!IMPORTANT]
> After creating each agent, **copy its Agent ID** (shown on the agent's detail page). You will need these IDs when setting up the orchestrator.

---

## Step 3: Create the Orchestrator Agent

This is the **10th agent** — the master controller that calls all 9 specialists.

1. Go to **Agents** → **+ New Agent**
2. **Name:** `ChiefArchitectOrchestrator`
3. **Model:** `gpt-4o`
4. **Instructions:** Paste this prompt:

```
You are the Chief Architect Orchestrator 🎯.

You coordinate a team of 9 specialist agents to generate and validate Azure architectures.
Follow this EXACT execution order:

PHASE 1 — EXTRACTION (Sequential):
1. extract_components → Extract and categorize all requirements
2. match_reference_architectures → Map to Azure Architecture Center patterns

PHASE 2 — EVALUATION (Run all three with the same context):
3. analyze_security → Security & compliance analysis
4. analyze_performance → Performance & scaling analysis
5. analyze_cost → Cost optimization analysis

PHASE 3 — DESIGN (Sequential):
6. design_architecture → Design the full Azure topology using ALL upstream findings
   Pass component extraction, reference patterns, security recommendations,
   performance recommendations, and cost recommendations as context.
7. optimize_connections → Validate and optimize the connection topology

PHASE 4 — VALIDATION (Sequential):
8. validate_requirements → Check 100% requirements coverage
9. review_architecture → Final WAF 5-pillar quality gate

CORRECTION LOOP:
If review_architecture returns "NEEDS_CORRECTION":
- Take the correction_tasks from the review
- Re-invoke design_architecture with the corrections as additional context
- Re-run optimize_connections, validate_requirements, and review_architecture
- Maximum 2 correction iterations

RULES:
- Always pass accumulated context between phases as JSON.
- For Phase 2, you can invoke all 3 agents with the same input — they analyze independently.
- Each agent returns JSON. Parse and forward relevant findings to downstream agents.
- If any agent fails, log the error and continue with remaining agents.
- Your final output must be the complete architecture with all findings combined.

FINAL OUTPUT FORMAT:
Return a JSON object containing:
{
  "project_name": "...",
  "architecture_pattern": "...",
  "services": [...],
  "connections": [...],
  "containers": [...],
  "primary_flow": [...],
  "security_findings": {...},
  "performance_findings": {...},
  "cost_findings": {...},
  "validation_result": {...},
  "review_result": {...},
  "overall_score": 0
}
```

5. **Do NOT click Save yet** — proceed to Step 4 to add the Connected Agents first.

---

## Step 4: Wire Connected Agents

While still editing the `ChiefArchitectOrchestrator`:

1. Scroll down to the **Tools** section
2. Click **+ Add Tool** → Select **Connected Agent** (or look for "Agent" in the tool types)
3. For each of the 9 agents, add them as a connected tool:

| Tool Name | Select Agent | Description |
|-----------|-------------|-------------|
| `extract_components` | ComponentExtractionAgent | Decompose user requirements into APIs, NFRs, tech stack |
| `match_reference_architectures` | AzureReferenceAgent | Map components to Azure Architecture Center patterns |
| `analyze_security` | SecurityAgent | Zero Trust analysis, STRIDE threat modeling, compliance |
| `analyze_performance` | PerformanceAgent | Workload analysis, scaling, caching, latency targets |
| `analyze_cost` | CostOptimizationAgent | FinOps analysis, Reserved Instances, SKU rightsizing |
| `design_architecture` | ArchitectureDesignAgent | Design complete Azure topology with services and connections |
| `optimize_connections` | ConnectionExpertAgent | Validate connections, fix orphans, enforce layer hierarchy |
| `validate_requirements` | RequirementsValidationAgent | Verify 100% requirements coverage |
| `review_architecture` | ArchitectureReviewAgent | Final WAF 5-pillar quality gate |

4. After adding all 9 connected agents, click **Save**

> [!TIP]
> The **Tool Name** must match the names used in the orchestrator's instructions (e.g., `extract_components`, `analyze_security`). This is how the orchestrator knows which tool to call.

---

## Step 5: Test the Workflow

Now test the entire pipeline directly in the Azure Portal:

1. Go to **Agents** and click on `ChiefArchitectOrchestrator`
2. You will see a **Chat / Playground** panel on the right side
3. Type a test prompt like:

```
Design a scalable e-commerce platform on Azure with:
- React frontend
- Node.js microservices backend
- PostgreSQL database
- Redis caching
- User authentication with Azure AD B2C
- Payment processing integration
- Must handle 10,000 concurrent users
- GDPR compliant
- Multi-region deployment
```

4. Click **Send** and watch the orchestrator work!

You will see in the thread:
- The orchestrator calling `extract_components` first
- Then calling `match_reference_architectures`
- Then calling `analyze_security`, `analyze_performance`, `analyze_cost`
- Then calling `design_architecture` with all the accumulated context
- Then calling `optimize_connections`
- Then calling `validate_requirements` and `review_architecture`
- Finally returning the complete architecture JSON

> [!NOTE]
> The first run may take 2-5 minutes because all 9 agents run sequentially. This is normal.

---

## Step 6: Publish the Workflow as an API

Once testing is successful, you can expose the orchestrator as an API endpoint that your frontend or other services can call.

### Option A: Use the Azure AI Agent Service REST API (Recommended)

The agents you created are **already accessible via REST API**. No additional publishing step is needed! You just call the Azure AI Agent Service API directly.

**Base URL:**
```
https://<your-ai-foundry-endpoint>/agents/v1.0
```

**Authentication:** Bearer token from your Service Principal or `az login`

### Option B: Wrap in an Azure Function (For production)

For a production-grade API with custom logic:

1. Go to the Azure Portal → Create an **Azure Function App**
2. Create an HTTP-triggered function
3. In the function code, use the Azure AI SDK to:
   - Create a Thread
   - Send the user's requirements as a message
   - Run the orchestrator agent
   - Return the result

### Option C: Use Prompt Flow (For visual deployment)

1. In Azure AI Foundry, go to **Prompt Flow** → **+ Create**
2. Create a flow that calls the orchestrator agent
3. Click **Deploy** → Choose **Managed online endpoint**
4. Azure will give you a REST API URL you can call

---

## Step 7: Trigger the Workflow

### Method 1: From the Azure Portal (Manual Testing)
- Go to **Agents** → Click `ChiefArchitectOrchestrator` → Type in the Chat panel

### Method 2: Via REST API (From your app / Postman)

```bash
# Step 1: Create a Thread
curl -X POST "https://<endpoint>/agents/v1.0/threads" \
  -H "Authorization: Bearer <token>" \
  -H "Content-Type: application/json" \
  -d '{}'

# Step 2: Send a Message (replace THREAD_ID)
curl -X POST "https://<endpoint>/agents/v1.0/threads/<THREAD_ID>/messages" \
  -H "Authorization: Bearer <token>" \
  -H "Content-Type: application/json" \
  -d '{
    "role": "user",
    "content": "Design a scalable e-commerce platform on Azure with React frontend, Node.js backend, PostgreSQL, Redis caching, Azure AD B2C auth, payment processing, 10000 concurrent users, GDPR compliant, multi-region."
  }'

# Step 3: Run the Orchestrator (replace THREAD_ID and AGENT_ID)
curl -X POST "https://<endpoint>/agents/v1.0/threads/<THREAD_ID>/runs" \
  -H "Authorization: Bearer <token>" \
  -H "Content-Type: application/json" \
  -d '{
    "assistant_id": "<ORCHESTRATOR_AGENT_ID>"
  }'

# Step 4: Get the Result (poll until status is "completed")
curl -X GET "https://<endpoint>/agents/v1.0/threads/<THREAD_ID>/runs/<RUN_ID>" \
  -H "Authorization: Bearer <token>"

# Step 5: Get the Final Messages
curl -X GET "https://<endpoint>/agents/v1.0/threads/<THREAD_ID>/messages" \
  -H "Authorization: Bearer <token>"
```

### Method 3: Via Python SDK (From your backend code)

```python
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

# Connect
client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str="<YOUR_PROJECT_CONNECTION_STRING>"
)

# Create a thread
thread = client.agents.create_thread()

# Send user requirements
client.agents.create_message(
    thread_id=thread.id,
    role="user",
    content="Design a scalable e-commerce platform on Azure..."
)

# Run the orchestrator (use the orchestrator's agent ID)
run = client.agents.create_and_process_run(
    thread_id=thread.id,
    agent_id="<ORCHESTRATOR_AGENT_ID>"
)

# Get the result
messages = client.agents.list_messages(thread_id=thread.id)
for msg in messages:
    if msg.role == "assistant":
        print(msg.content)
```

### Method 4: From Your Existing Frontend

In your existing Next.js frontend, update the API call to include the Azure AI agents flag:

```javascript
const response = await fetch('/api/generate', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    requirements: "Design a scalable e-commerce platform...",
    use_azure_ai_agents: true  // This triggers the Azure AI workflow
  })
});
```

---

## Agent Prompts Reference

> [!TIP]
> All agent prompts are stored in the file `azure-ai-agents/agents/prompts.py`. You can also find a formatted version in the [Manual Setup Guide](file:///C:/Users/Agentassist/.gemini/antigravity/brain/800dca6b-fadb-4680-b195-dbf221e6d501/azure_agents_manual_setup_guide.md) artifact.

### Quick Reference Table

| # | Agent | Prompt Summary | Max Tokens |
|---|-------|---------------|------------|
| 1 | ComponentExtractionAgent | "You are a Principal Requirements Analyst 📋..." | 3000 |
| 2 | AzureReferenceAgent | "You are a Principal Azure Reference Specialist 🏛️..." | 3000 |
| 3 | SecurityAgent | "You are a Principal Security Architect 🔐..." | 3000 |
| 4 | PerformanceAgent | "You are a Principal Performance Engineer ⚡..." | 3000 |
| 5 | CostOptimizationAgent | "You are a Principal Azure FinOps Architect 💰..." | 3000 |
| 6 | ArchitectureDesignAgent | "You are a Principal Azure Solutions Architect 🏗️..." | 6000 |
| 7 | ConnectionExpertAgent | "You are a Principal Integration Architect 🔗..." | 3000 |
| 8 | RequirementsValidationAgent | "You are a Principal Quality Assurance Architect ✅..." | 3000 |
| 9 | ArchitectureReviewAgent | "You are a Principal Architecture Reviewer 🔍..." | 3000 |
| 10 | ChiefArchitectOrchestrator | "You are the Chief Architect Orchestrator 🎯..." | 6000 |

---

## Troubleshooting

### "Connected Agents" option not visible
- Make sure your Azure AI Foundry project is in a supported region (East US, West US 2, Sweden Central, etc.)
- The feature may be in preview — check the Azure AI Foundry documentation for your region's availability

### Agent takes too long
- Each agent call adds ~15-30 seconds. The full 9-agent pipeline takes 2-5 minutes
- This is normal for a sequential multi-agent workflow

### Agent returns empty or invalid JSON
- Check the agent's Temperature is set to `0.1` (not the default `1.0`)
- Check the system prompt includes the line: "Return ONLY valid JSON"
- Try increasing Max Tokens if the output is being truncated

### Authentication errors
- Make sure you have the **Azure AI Developer** role assigned to your user or Service Principal
- If using Service Principal, verify `AZURE_TENANT_ID`, `AZURE_CLIENT_ID`, and `AZURE_CLIENT_SECRET` are correct in your `.env`

### How to update an agent's prompt
- Go to **Agents** → Click on the agent → Edit the **Instructions** field → Click **Save**
- No redeployment needed — changes take effect immediately on the next run
