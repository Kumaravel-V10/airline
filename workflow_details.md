# ✈️ Airline Multi-Agent Orchestrator — Workflow Details

> **System**: Nevio Service Center — Azure AI Foundry + Amadeus-Nevio APIM  
> **Version**: 2.1.0  
> **Last Updated**: 2026-08-27

---

## Table of Contents

1. [System Architecture Overview](#1-system-architecture-overview)
2. [Orchestrator Workflow (Entry Point)](#2-orchestrator-workflow-entry-point)
3. [Supervisor-Orchestrator-Agent](#3-supervisor-orchestrator-agent)
4. [Agent Routing Table](#4-agent-routing-table)
5. [Multi-Agent Chaining Rules](#5-multi-agent-chaining-rules)
6. [Specialized Agent Workflows (Agents 2–15)](#6-specialized-agent-workflows)
7. [MCP Server — Booking Tool Pipeline](#7-mcp-server--booking-tool-pipeline)
8. [End-to-End Flow Examples](#8-end-to-end-flow-examples)
9. [Escalation & Exception Handling](#9-escalation--exception-handling)
10. [Request Lifecycle Statuses](#10-request-lifecycle-statuses)

---

## 1. System Architecture Overview

```
┌──────────────────────────────────────────────────────────────────────────────┐
│                            CUSTOMER REQUEST                                  │
└──────────────────────┬───────────────────────────────────────────────────────┘
                       │
                       ▼
┌──────────────────────────────────────────────────────────────────────────────┐
│                   orchestrator.py  (Python Entry Point)                       │
│  • Receives customer message                                                 │
│  • Creates Azure AI conversation thread                                      │
│  • Sends message to Supervisor-Orchestrator-Agent                            │
│  • Handles tool call routing (route_to_agent)                                │
│  • Collects specialized agent responses                                      │
│  • Returns final response to customer                                        │
└──────────────────────┬───────────────────────────────────────────────────────┘
                       │
                       ▼
┌──────────────────────────────────────────────────────────────────────────────┐
│              SUPERVISOR-ORCHESTRATOR-AGENT  (Azure AI Foundry)                │
│  • Intent classification                                                     │
│  • Entity extraction (PNR, names, dates, airports)                           │
│  • Agent routing via route_to_agent tool                                     │
│  • Multi-agent chaining decisions                                            │
│  • Escalation to human when required                                         │
└────────────┬─────────┬─────────┬─────────┬─────────┬─────────┬──────────────┘
             │         │         │         │         │         │
      ┌──────┘   ┌─────┘   ┌────┘   ┌─────┘   ┌─────┘   ┌────┘
      ▼          ▼         ▼        ▼         ▼         ▼
 ┌─────────┐┌────────┐┌────────┐┌────────┐┌────────┐┌────────────┐
 │ Create  ││Booking ││ Name   ││ Refund ││Change  ││ 9 more     │
 │ Booking ││Retriev.││ Change ││ Agent  ││Booking ││ agents...  │
 │ Agent   ││ Agent  ││ Agent  ││        ││ Agent  ││            │
 └────┬────┘└────────┘└────────┘└────────┘└────────┘└────────────┘
      │
      ▼
 ┌──────────────────────────────────────────────┐
 │   MCP SERVER  (sc-mcp-server v2.1.0)         │
 │   Transport: stdio | SSE (HTTP)              │
 │   10 Booking Tools → Amadeus-Nevio APIM      │
 └──────────────────────────────────────────────┘
```

---

## 2. Orchestrator Workflow (Entry Point)

The [`orchestrator.py`](file:///c:/Users/Agentassist/Downloads/airline%20agent/orchestrator.py) is the Python application that ties everything together.

### Step-by-Step Flow

```
START
  │
  ▼
┌─────────────────────────────────────────────┐
│ 1. Receive customer message                 │
└─────────────────────┬───────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────┐
│ 2. Get Supervisor-Orchestrator-Agent        │
│    from Azure AI Foundry                    │
└─────────────────────┬───────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────┐
│ 3. Create conversation thread               │
└─────────────────────┬───────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────┐
│ 4. Add customer message to thread           │
└─────────────────────┬───────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────┐
│ 5. Run Supervisor agent                     │
│    (create_and_process)                     │
└─────────────────────┬───────────────────────┘
                      │
              ┌───────┴───────┐
              │               │
              ▼               ▼
     ┌────────────────┐  ┌─────────────────┐
     │ requires_action │  │   completed     │
     │ (tool calls)    │  │ (direct reply)  │
     └───────┬────────┘  └────────┬────────┘
             │                    │
             ▼                    ▼
     ┌────────────────┐  ┌─────────────────┐
     │ Parse tool call │  │ Return response │
     │ route_to_agent  │  │ to customer     │
     └───────┬────────┘  └─────────────────┘
             │
             ▼
     ┌────────────────────────────────┐
     │ Extract:                       │
     │  • target_agent_name           │
     │  • extracted_entities          │
     │  • priority                    │
     │  • chain_next (if multi-agent) │
     └───────┬────────────────────────┘
             │
             ▼
     ┌────────────────────────────────┐
     │ call_specialized_agent()       │
     │  • Fetch target agent          │
     │  • Create new thread           │
     │  • Send entities as prompt     │
     │  • Run agent                   │
     │  • Collect response            │
     └───────┬────────────────────────┘
             │
             ▼
     ┌────────────────────────────────┐
     │ Submit tool outputs back to    │
     │ Supervisor for final response  │
     └───────┬────────────────────────┘
             │
             ▼
     ┌────────────────────────────────┐
     │ Return final response          │
     │ to customer                    │
     └────────────────────────────────┘
```

### Key Functions

| Function | Purpose |
|----------|---------|
| `route_customer_request(message)` | Main entry point — receives customer message, runs the full orchestration loop |
| `call_specialized_agent(name, payload)` | Creates a new thread for a specialized agent, sends extracted entities, returns its response |

---

## 3. Supervisor-Orchestrator-Agent

The Supervisor is the **brain** of the system. It never executes airline operations itself — it only **routes**.

### Responsibilities

| # | Responsibility | Details |
|---|---------------|---------|
| 1 | **Intent Classification** | Analyzes the customer message to determine what they need |
| 2 | **Entity Extraction** | Pulls out PNR, passenger names, flight numbers, dates, airports |
| 3 | **Agent Routing** | Calls `route_to_agent` tool with the correct target agent |
| 4 | **Multi-Agent Chaining** | Decides when multiple agents need to run sequentially |
| 5 | **Clarification** | If intent is unclear, asks the customer ONE clarifying question |
| 6 | **Escalation** | Flags critical issues (fraud, VIP, legal) for human escalation |

### The `route_to_agent` Tool

This is the **only tool** the Supervisor uses. It signals the orchestrator to delegate work:

```json
{
  "target_agent": "Name-Change-Agent",
  "intent": "NAME_CHANGE",
  "extracted_entities": {
    "pnr": "XYZ789",
    "passenger_name": "Sarah Johnson",
    "last_name": "Johnson"
  },
  "priority": "medium",
  "chain_next": "Communication-Case-Summary-Agent"
}
```

| Parameter | Type | Description |
|-----------|------|-------------|
| `target_agent` | string (enum) | One of 14 specialized agents |
| `intent` | string | Classified customer intent |
| `extracted_entities` | object | PNR, names, flights, dates, airports |
| `priority` | enum | `low`, `medium`, `high`, `critical` |
| `chain_next` | string | Next agent to call after this one completes |

---

## 4. Agent Routing Table

The Supervisor uses this mapping to decide where to send each request:

| Customer Intent | Primary Agent | Chained Agent(s) |
|----------------|---------------|-------------------|
| New flight booking | **Create-Booking-Agent** | — |
| Retrieve / view booking | **Booking-Retrieval-Agent** | — |
| Change passenger name | **Booking-Retrieval-Agent** | → Name-Change-Agent |
| Change flight date / route | **Change-Booking-Agent** | — |
| Cancel and refund | **Booking-Retrieval-Agent** | → RefundAgent → Refund-workflow |
| Voluntary rebooking | **Rebooking-Agent** | — |
| Flight disruption / IROP | **Disruption-Rebooking-Agent** | — |
| Extra baggage / meals / seat | **Ancillary-Sales-Agent** | — |
| Wheelchair / SSR | **Passenger-SSR-Agent** | — |
| Medical clearance | **Medical-Exception-Agent** | — |
| Payment issue | **Payment-Agent** | — |
| Complaint / case inquiry | **Case-Management-Agent** | — |
| Send confirmation email | **Communication-Case-Summary-Agent** | — |
| Book flight + add baggage | **Create-Booking-Agent** | → Ancillary-Sales-Agent |
| Cancel and rebook | **RefundAgent** | → Rebooking-Agent |
| Change name + add wheelchair | **Name-Change-Agent** | → Passenger-SSR-Agent |

---

## 5. Multi-Agent Chaining Rules

When a customer request spans multiple domains, the Supervisor triggers agents in a specific order:

```
RULE: Any name change
  ALWAYS → Booking-Retrieval-Agent FIRST → then Name-Change-Agent

RULE: Any refund
  ALWAYS → Booking-Retrieval-Agent FIRST → then RefundAgent → then Refund-workflow

RULE: Book flight + add baggage
  Create-Booking-Agent → then Ancillary-Sales-Agent

RULE: Cancel and rebook
  RefundAgent → then Rebooking-Agent

RULE: Change name + add wheelchair
  Name-Change-Agent → then Passenger-SSR-Agent
```

### Chaining Execution Model

```
 Customer: "Cancel booking 9DVWPJ and rebook me on the next flight"
                           │
                           ▼
              ┌──────────────────────────┐
              │   Supervisor classifies:  │
              │   Intent: CANCEL_REBOOK   │
              │   PNR: 9DVWPJ            │
              └─────────┬────────────────┘
                        │
          ┌─────────────┴─────────────┐
          │ Step 1                     │
          │ route_to_agent →           │
          │   Booking-Retrieval-Agent  │
          │   chain_next: RefundAgent  │
          └─────────────┬─────────────┘
                        │ (booking data returned)
                        ▼
          ┌─────────────────────────────┐
          │ Step 2                       │
          │ route_to_agent →             │
          │   RefundAgent                │
          │   chain_next: Rebooking-Agent│
          └─────────────┬───────────────┘
                        │ (refund processed)
                        ▼
          ┌─────────────────────────────┐
          │ Step 3                       │
          │ route_to_agent →             │
          │   Rebooking-Agent            │
          │   chain_next: null           │
          └─────────────┬───────────────┘
                        │ (rebooking confirmed)
                        ▼
          ┌─────────────────────────────┐
          │ Supervisor formulates       │
          │ final response to customer  │
          └─────────────────────────────┘
```

---

## 6. Specialized Agent Workflows

### Agent #2: Booking-Retrieval-Agent

**Role**: Read-only retrieval of existing bookings.

```
Input: PNR + Last Name
  │
  ├─ 1. Validate PNR format (6 alphanumeric chars)
  │     └─ If invalid → return error message
  │
  ├─ 2. Call API: GET /orders/retrieve?orderRecLocId={PNR}&lastName={lastName}
  │
  ├─ 3. Extract structured data:
  │     • PNR, Status, Passengers, Flights
  │     • Services, Seats, Payment info
  │
  └─ 4. Return structured booking details
```

**Tool**: `retrieve_order(orderRecLocId, lastName)`

---

### Agent #3: Create-Booking-Agent

**Role**: End-to-end flight booking using the 10-step Amadeus-Nevio flow.

```
┌─────────────────────────────────────────────────────────────────┐
│                  10-STEP BOOKING PIPELINE                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  MANDATORY STEPS:                                                │
│  ┌──────────────────────────────────────────────────────────┐    │
│  │ Step 1: search_flights                                    │    │
│  │   POST /shop/flights                                      │    │
│  │   → Returns airBoundId, prices, schedules                 │    │
│  └──────────────────┬───────────────────────────────────────┘    │
│                     ▼                                            │
│  ┌──────────────────────────────────────────────────────────┐    │
│  │ Step 2: create_cart                                       │    │
│  │   POST /create-cart                                       │    │
│  │   → Returns cartId, checkoutId, passengerIds              │    │
│  └──────────────────┬───────────────────────────────────────┘    │
│                     ▼                                            │
│  ┌──────────────────────────────────────────────────────────┐    │
│  │ Step 3: update_passengers                                 │    │
│  │   POST /checkout/passengers                               │    │
│  │   → Add identity + contact details                        │    │
│  └──────────────────┬───────────────────────────────────────┘    │
│                     ▼                                            │
│  OPTIONAL STEPS (if customer wants ancillaries/seats):           │
│  ┌──────────────────────────────────────────────────────────┐    │
│  │ Step 4: get_service_catalog                               │    │
│  │ Step 5: get_seat_map                                      │    │
│  │ Step 6: add_seats                                         │    │
│  │ Step 7: add_ancillaries                                   │    │
│  └──────────────────┬───────────────────────────────────────┘    │
│                     ▼                                            │
│  MANDATORY STEPS:                                                │
│  ┌──────────────────────────────────────────────────────────┐    │
│  │ Step 8: retrieve_cart                                     │    │
│  │   → Review full cart before confirming                    │    │
│  └──────────────────┬───────────────────────────────────────┘    │
│                     ▼                                            │
│  ┌──────────────────────────────────────────────────────────┐    │
│  │ Step 9: confirm_booking  ⚠️ IRREVERSIBLE                 │    │
│  │   POST /checkoutConfirm                                   │    │
│  │   → Returns orderId, PNR                                  │    │
│  └──────────────────┬───────────────────────────────────────┘    │
│                     ▼                                            │
│  ┌──────────────────────────────────────────────────────────┐    │
│  │ Step 10: retrieve_order                                   │    │
│  │   GET /orders/retrieve                                    │    │
│  │   → Full confirmation details                             │    │
│  └──────────────────────────────────────────────────────────┘    │
│                                                                  │
│  RULES:                                                          │
│  • If any step fails → STOP, do not continue                     │
│  • Cart expires after 30 minutes of inactivity                   │
│  • Thread checkoutId from step 2 through steps 3–9               │
│  • At least one passenger must have email + phone                │
│  • Airline Code: AY  |  Promo Code: SCUISEATP                   │
└─────────────────────────────────────────────────────────────────┘
```

---

### Agent #4: Name-Change-Agent

**Role**: Process passenger name corrections and changes on existing bookings.

```
Input: PNR + Current Name + New Name
  │
  ├─ 1. Verify booking exists and is active
  │
  ├─ 2. Identity verification:
  │     • Date of birth
  │     • Original booking email
  │     • Passport/ID number
  │
  ├─ 3. Classify change type:
  │     ├── Minor correction (≤3 char diff) → NO FEE
  │     └── Full name change (>3 chars)     → FEE APPLIES
  │
  ├─ 4. Check constraints:
  │     ├── Departure ≥ 24 hours away?
  │     ├── Check-in NOT open?
  │     └── Booking in Confirmed/Ticketed status?
  │
  ├─ 5. Apply fee if full change:
  │     • Domestic:         EUR 50
  │     • International:    EUR 100
  │     • Intercontinental: EUR 150
  │
  ├─ 6. Call update_passenger_name API
  │
  ├─ 7. Generate confirmation
  │
  └─ 8. BLOCKED SCENARIOS:
        • Departure < 24 hours → Reject
        • Check-in open → Reject
        • Name transfer to different person → Reject (advise cancel + rebook)
        • Booking cancelled/suspended → Reject
```

**Tools**: `update_passenger_name`, `retrieve_order`

---

### Agent #5: Change-Booking-Agent

**Role**: Modify existing bookings (date, time, route changes).

```
Input: PNR + Desired Changes
  │
  ├─ 1. Retrieve current booking
  ├─ 2. Check fare rules and reissue eligibility
  ├─ 3. Search alternate flights
  ├─ 4. Calculate: change fee + fare difference + taxes
  ├─ 5. Present quote to customer
  ├─ 6. Obtain customer acceptance
  ├─ 7. Trigger payment if collection required
  ├─ 8. Process change (create_order_change → confirm_change)
  ├─ 9. Send revised itinerary
  └─ 10. Log transaction
```

**Knowledge**: `change_booking_rules.md`, `fare_families.md`  
**Tools**: `search_flights`, `create_order_change`, `confirm_change`

---

### Agent #6: RefundAgent

**Role**: Check refund eligibility and present breakdown to customer.

```
Input: PNR + Last Name
  │
  ├─ 1. Call GraphQL: RetriveOrderRefundEligiblities
  │     • Input: orderId, lastName, targetAction: "cancelAndRefund"
  │
  ├─ 2. Parse response:
  │     • refundStatus: "refundable" | "non-refundable"
  │     • totalRefundAmounts
  │     • totalPaidAmount
  │     • totalUsedAmount
  │     • totalPenalty
  │     • nonEligibilityReasons
  │
  ├─ 3. Calculate: Net Refund = Paid - Used - Penalty
  │
  ├─ 4. Present breakdown to customer
  │
  └─ 5. Return refundProposalIds for Refund-workflow
```

**Knowledge**: `refund_policy.md`, `refund_graphql_schemas.md`  
**Tool**: `check_refund_eligibility` (GraphQL query)

---

### Agent #7: Refund-workflow

**Role**: Execute the actual cancellation and refund after eligibility is confirmed.

```
Input: refundProposalIds + orderId + lastName
  │
  ├─ 1. Call GraphQL mutation: CancellationAndRefund
  │     • Input: refundProposalIds, orderId, lastName
  │
  ├─ 2. Process response:
  │     • orderId
  │     • totalRefundAmounts
  │     • traveler document statuses
  │     • payment details for refund
  │     • errors (if any)
  │
  ├─ 3. Confirm refund timeline:
  │     • Credit card: 5-10 business days
  │     • Bank transfer: 10-15 business days
  │     • Travel voucher: Immediate
  │
  └─ 4. Return confirmation to Supervisor
```

**Knowledge**: `refund_graphql_schemas.md`, `refund_policy.md`  
**Tool**: `process_refund` (GraphQL mutation)

---

### Agent #8: Rebooking-Agent

**Role**: Handle voluntary rebooking on alternate flights.

```
Input: PNR + Desired new flight details
  │
  ├─ 1. Check rebooking policy & fare rules
  ├─ 2. Search available flights
  ├─ 3. Calculate fare differences
  ├─ 4. Present options to customer
  ├─ 5. Process rebooking (create_cart → checkout)
  └─ 6. Confirm new itinerary
```

**Knowledge**: `rebooking_policy.md`, `fare_families.md`  
**Tools**: `search_flights`, `create_cart`, `checkout_confirm`

---

### Agent #9: Disruption-Rebooking-Agent

**Role**: Handle IROP (Irregular Operations) — airline-caused disruptions.

```
Input: PNR + Disruption details
  │
  ├─ 1. Verify disruption type (cancellation, delay, misconnect)
  ├─ 2. Apply IROP procedures from disruption_handling_guide.md
  ├─ 3. Check EU261/2004 compensation eligibility:
  │     • ≤1500 km + ≥3h delay → EUR 250
  │     • 1500-3500 km + ≥3h delay → EUR 400
  │     • >3500 km + ≥4h delay → EUR 600
  ├─ 4. Search alternative flights (fees WAIVED for airline-caused)
  ├─ 5. Offer options: rebook / refund / hotel+meal voucher
  ├─ 6. Process selected option
  └─ 7. Issue compensation if eligible
```

**Knowledge**: `disruption_handling_guide.md`, `rebooking_policy.md`  
**Tools**: `search_alternatives`, `auto_rebook`, `apply_waiver`

---

### Agent #10: Ancillary-Sales-Agent

**Role**: Sell and add ancillary services (baggage, seats, meals, lounge, WiFi).

```
Input: PNR or cartId + Desired services
  │
  ├─ 1. Get service catalogue: GET /services?cartId={id}&promotionCode=SCUISEATP
  ├─ 2. Present available services with prices
  ├─ 3. Get seat map if seat selection requested
  ├─ 4. Add selected services: POST /seat/services
  ├─ 5. Trigger payment if post-booking purchase
  └─ 6. Confirm services added
```

**Knowledge**: `ancillary_services_catalogue.md`  
**Tools**: `get_service_catalogue`, `add_services`, `get_seatmap`, `add_seats`

---

### Agent #11: Passenger-SSR-Agent

**Role**: Manage Special Service Requests (wheelchair, meals, UMNR, pets).

```
Input: PNR + SSR Type
  │
  ├─ 1. Look up SSR code in ssr_codes_reference.md
  │     • WCHR/WCHC/WCHS (wheelchair types)
  │     • VGML/DBML/AVML (meal types)
  │     • UMNR (unaccompanied minor)
  │     • PETC/AVIH (pet in cabin/hold)
  │
  ├─ 2. Check time constraints:
  │     • Wheelchair: ≥48 hours before departure
  │     • Special meals: ≥24 hours before departure
  │
  ├─ 3. Check age rules (UMNR: 5-11 years)
  ├─ 4. Add SSR to booking
  └─ 5. Confirm and advise airport reporting requirements
```

**Knowledge**: `ssr_codes_reference.md`  
**Tools**: `add_ssr`, `remove_ssr`, `list_ssr`

---

### Agent #12: Medical-Exception-Agent

**Role**: Process medical clearance requests, MEDIF forms, and fitness-to-fly.

```
Input: Medical condition details
  │
  ├─ 1. Determine if MEDIF form is required
  ├─ 2. Check medical equipment approval (oxygen, stretcher)
  ├─ 3. Validate fitness-to-fly criteria
  ├─ 4. Submit medical request for airline medical team review
  ├─ 5. Track approval status
  └─ 6. Confirm clearance or rejection
```

**Knowledge**: `medical_clearance_guide.md`  
**Tools**: `submit_medical_request`, `check_medical_status`

---

### Agent #13: Payment-Agent

**Role**: Handle payment processing, failures, and retries.

```
Input: Payment issue details
  │
  ├─ 1. Check supported payment methods (credit/debit, bank transfer, voucher)
  ├─ 2. Validate card details format
  ├─ 3. Process payment or generate payment link
  ├─ 4. Handle failures:
  │     • Resend link if permitted
  │     • Offer alternate payment method
  │     • Cancel pending request after SLA timeout
  └─ 5. Confirm payment success
```

**Knowledge**: `payment_processing_guide.md`  
**Tools**: `process_payment`, `validate_card`

---

### Agent #14: Case-Management-Agent

**Role**: Create and manage customer service cases with SLA tracking.

```
Input: Case details / Case ID
  │
  ├─ 1. Classify priority (P1–P4):
  │     • P1 Critical: Response ≤1 hour
  │     • P2 High: Response ≤4 hours
  │     • P3 Medium: Response ≤24 hours
  │     • P4 Low: Response ≤72 hours
  │
  ├─ 2. Create / update case with documentation
  ├─ 3. Check escalation matrix for human escalation needs
  ├─ 4. Track SLA compliance
  └─ 5. Close case with documented disposition
```

**Knowledge**: `case_management_sla.md`, `escalation_matrix.md`  
**Tools**: `create_case`, `update_case`, `close_case`

---

### Agent #15: Communication-Case-Summary-Agent

**Role**: Generate customer communications using templates and summarize cases.

```
Input: Communication type + booking details
  │
  ├─ 1. Select correct email template:
  │     • Booking confirmation
  │     • Name change confirmation
  │     • Cancellation notice
  │     • Disruption notification
  │     • Refund confirmation
  │
  ├─ 2. Populate template with booking data
  ├─ 3. Apply GDPR data handling rules
  ├─ 4. Send communication via approved channel
  └─ 5. Generate case summary for audit
```

**Knowledge**: `email_templates.md`  
**Tools**: `send_email`, `generate_summary`

---

## 7. MCP Server — Booking Tool Pipeline

The [`server.py`](file:///c:/Users/Agentassist/Downloads/airline%20agent/mcp/server.py) MCP server provides the actual API integration layer for the Create-Booking-Agent.

### Server Configuration

| Setting | Value |
|---------|-------|
| Server Name | `sc-mcp-server` |
| Version | `2.1.0` |
| Transport | `stdio` (default) or `sse` (HTTP) |
| APIM Base URL | `https://nevioservicecenterapim.azure-api.net` |
| Default Port (SSE) | `3100` |
| Token TTL | 1700 seconds (~28 min) |
| Rate Limit | 100 req/min per IP |

### 10 MCP Tools

```
 ┌───────────────────────────────────────────────────────────────┐
 │                   MCP TOOL PIPELINE                           │
 │                                                               │
 │   1. search_flights(trip_type, departure, arrival, date,      │
 │                     passengers, fare_type, return_date)       │
 │                          │                                    │
 │                          ▼                                    │
 │   2. create_cart(sku_ids, airline_id, agent_id)               │
 │        → Returns: cartId, checkoutId, passengerIds            │
 │                          │                                    │
 │              ┌───────────┴──── checkoutId threaded ────┐      │
 │              ▼                                         │      │
 │   3. update_passengers(checkout_id, passengers[])      │      │
 │              │                                         │      │
 │              ▼                                         │      │
 │   4. get_service_catalog(checkout_id, promo?)  [OPT]   │      │
 │              │                                         │      │
 │              ▼                                         │      │
 │   5. get_seat_map(checkout_id, flight_id, promo?) [OPT]│      │
 │              │                                         │      │
 │              ▼                                         │      │
 │   6. add_seats(checkout_id, traveller[])  [OPT]        │      │
 │              │                                         │      │
 │              ▼                                         │      │
 │   7. add_ancillaries(checkout_id, traveller[])  [OPT]  │      │
 │              │                                         │      │
 │              ▼                                         │      │
 │   8. retrieve_cart(checkout_id)                        │      │
 │              │                                         │      │
 │              ▼                                         │      │
 │   9. confirm_booking(checkout_id)  ⚠️ IRREVERSIBLE     │      │
 │        → Returns: orderId                              │      │
 │              │                                         │      │
 │              ▼                                         │      │
 │  10. retrieve_order(order_id)                          │      │
 │        → Returns: Full order with PNR                  │      │
 │                                                               │
 └───────────────────────────────────────────────────────────────┘
```

### SSE Mode Endpoints

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/health` | GET | Server health check |
| `/api/tools` | GET | List all available tools |
| `/api/tools/{tool_name}` | POST | Execute a specific tool |
| `/sse` | GET | SSE stream connection |
| `/sse/messages` | POST | SSE message posting |

### Security Features

- **API Key Auth**: Bearer token required for SSE mode
- **Rate Limiting**: Configurable per-IP rate limit (default 100/min)
- **TLS Support**: Optional HTTPS via `SSL_CERTFILE` / `SSL_KEYFILE`
- **Mutation Guard**: `ALLOW_MUTATIONS=false` blocks `confirm_booking` by default

---

## 8. End-to-End Flow Examples

### Example 1: "Can you pull up my booking? PNR is ABC123"

```
Customer Message
      │
      ▼
Supervisor-Orchestrator-Agent
  • Intent: RETRIEVE_BOOKING
  • Entity: PNR = ABC123
  • Route: Booking-Retrieval-Agent
      │
      ▼
Booking-Retrieval-Agent
  • Validates PNR format ✓
  • Calls: GET /orders/retrieve?orderRecLocId=ABC123&lastName=...
  • Returns: Booking details (status, flights, passengers, services)
      │
      ▼
Supervisor formulates response
      │
      ▼
Customer receives booking summary
```

### Example 2: "I need to change my name from Sarah Johnson to Sarah Williams on booking XYZ789"

```
Customer Message
      │
      ▼
Supervisor-Orchestrator-Agent
  • Intent: NAME_CHANGE
  • Entities: PNR=XYZ789, old_name="Sarah Johnson", new_name="Sarah Williams"
  • Route: Booking-Retrieval-Agent FIRST (chain_next: Name-Change-Agent)
      │
      ├── Step 1: Booking-Retrieval-Agent
      │     • Retrieves booking XYZ789
      │     • Confirms booking is active
      │     • Returns booking data
      │
      ├── Step 2: Name-Change-Agent
      │     • Receives booking data + name change request
      │     • Classifies: "Johnson" → "Williams" = Full name change (>3 chars)
      │     • Checks: Departure ≥24h? ✓  Check-in closed? ✓
      │     • Fee: EUR 100 (international)
      │     • Requests identity verification
      │     • Processes name update via API
      │     • Returns confirmation
      │
      ▼
Supervisor formulates final response with:
  • Name change confirmed
  • Fee applied: EUR 100
  • Updated booking reference
```

### Example 3: "I want to cancel my booking 9DVWPJ and get a refund"

```
Customer Message
      │
      ▼
Supervisor-Orchestrator-Agent
  • Intent: CANCEL_AND_REFUND
  • Entity: PNR = 9DVWPJ
  • Route: Booking-Retrieval → RefundAgent → Refund-workflow
      │
      ├── Step 1: Booking-Retrieval-Agent
      │     • Retrieves booking 9DVWPJ
      │     • Returns booking data + order details
      │
      ├── Step 2: RefundAgent
      │     • Calls: RetriveOrderRefundEligiblities (GraphQL)
      │     • Returns: refundStatus, totalRefund, penalties
      │     • Presents breakdown to customer
      │
      ├── Step 3: Refund-workflow
      │     • Calls: CancellationAndRefund (GraphQL mutation)
      │     • Processes actual cancellation + refund
      │     • Returns confirmation + timeline
      │
      ▼
Supervisor formulates final response:
  • Booking cancelled
  • Refund amount: EUR XXX
  • Timeline: 5-10 business days (credit card)
```

### Example 4: "Book me HEL to LHR with extra bag and seat 5C"

```
Customer Message
      │
      ▼
Supervisor-Orchestrator-Agent
  • Intent: NEW_BOOKING_WITH_ANCILLARY
  • Entities: origin=HEL, destination=LHR, services=[baggage, seat:5C]
  • Route: Create-Booking-Agent (chain_next: Ancillary-Sales-Agent)
      │
      ├── Step 1: Create-Booking-Agent (via MCP Server)
      │     • search_flights(HEL → LHR)
      │     • create_cart(selected SKU)
      │     • update_passengers(details)
      │     • retrieve_cart (review)
      │     • confirm_booking → PNR generated
      │
      ├── Step 2: Ancillary-Sales-Agent
      │     • get_service_catalogue (for extra baggage)
      │     • get_seatmap (to find seat 5C)
      │     • add_seats (assign 5C)
      │     • add_ancillaries (add extra bag)
      │
      ▼
Supervisor confirms:
  • Booking created: PNR XXXXXX
  • Extra baggage added
  • Seat 5C assigned
```

---

## 9. Escalation & Exception Handling

### Immediate Escalation (CRITICAL Priority)

| Scenario | Escalation Target |
|----------|-------------------|
| Suspected fraud or stolen payment card | Security Team |
| Medical emergency in-flight or at airport | Operations + Medical |
| Legal threats or regulatory complaint | Legal Department |
| Media / social media escalation risk | PR + Customer Relations |
| VIP / Loyalty Platinum+ passenger complaint | VIP Service Desk |
| Safety or security concern | Security Team |

### High Priority Escalation

| Scenario | Escalation Target |
|----------|-------------------|
| Revenue impact > EUR 5,000 | Revenue Management |
| Group booking (10+ passengers) issues | Group Desk |
| Codeshare / partner airline issues | Interline Desk |
| Repeated failed API calls (system issue) | IT Support |
| Customer threatening legal action | Legal Department |

### Standard Escalation

| Scenario | Escalation Target |
|----------|-------------------|
| Agent unable to resolve after 3 attempts | Supervisor Level 2 |
| Waiver request exceeding agent authority | Supervisor Level 2 |
| Complex multi-segment itinerary changes | Ticketing Desk |
| Disability or accessibility complaint | Accessibility Team |

### Waiver Authority Levels

| Authority Level | Can Waive Up To | Can Override |
|----------------|-----------------|--------------|
| Supervisor Level 1 | EUR 100 | — |
| Supervisor Level 2 | EUR 150 | — |
| Manager | Any fee | Time restrictions |

---

## 10. Request Lifecycle Statuses

Every service request moves through these standardized statuses:

```
  Initiated
      │
      ▼
  Customer Verified
      │
      ▼
  Eligibility Checked
      │
      ├─── Documents Requested ──→ Documents Received
      │
      ▼
  Charges Calculated
      │
      ▼
  Payment Link Sent ──→ Payment Pending ──→ Payment Successful
      │                                          │
      │                                          ▼
      │                                   Service Fulfilled
      │
      ├── Payment Failed ──→ Retry / Escalate
      │
      ├── Escalated ──→ Back-office / Supervisor
      │
      ├── Rejected ──→ Inform customer
      │
      └── Closed
```

---

## Knowledge Base ↔ Agent Mapping

| Knowledge Base | Agent(s) Using It | Key Documents |
|---------------|-------------------|---------------|
| kb-supervisor-orchestrator | Supervisor-Orchestrator-Agent | airline_policies.md, intent_classification_examples.json, escalation_matrix.md, api_reference.md |
| kb-create-booking | Create-Booking-Agent | booking_flow_guide.md, fare_families.md, passenger_type_codes.md |
| kb-booking-retrieval | Booking-Retrieval-Agent | api_reference.md, airline_policies.md |
| kb-name-change | Name-Change-Agent | name_change_policy.md, api_reference.md, airline_policies.md |
| kb-change-booking | Change-Booking-Agent | change_booking_rules.md, fare_families.md |
| kb-refund-agent | RefundAgent | refund_policy.md, refund_graphql_schemas.md, api_reference.md |
| kb-refund-workflow | Refund-workflow | refund_graphql_schemas.md, refund_policy.md |
| kb-rebooking | Rebooking-Agent | rebooking_policy.md, fare_families.md |
| kb-disruption-rebooking | Disruption-Rebooking-Agent | disruption_handling_guide.md, rebooking_policy.md, airline_policies.md |
| kb-ancillary-sales | Ancillary-Sales-Agent | ancillary_services_catalogue.md |
| kb-passenger-ssr | Passenger-SSR-Agent | ssr_codes_reference.md, airline_policies.md |
| kb-medical-exception | Medical-Exception-Agent | medical_clearance_guide.md, airline_policies.md |
| kb-payment | Payment-Agent | payment_processing_guide.md, api_reference.md |
| kb-case-management | Case-Management-Agent | case_management_sla.md, escalation_matrix.md |
| kb-communication-summary | Communication-Case-Summary-Agent | email_templates.md, airline_policies.md |

---

## API Quick Reference

### Base URL
`https://nevioservicecenterapim.azure-api.net`

### Authentication
| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/token` | POST | Get JWT Token |
| `/token/amadeus` | POST | Get Amadeus Token |

### Key Endpoints
| Endpoint | Method | Used By |
|----------|--------|---------|
| `/shop/flights` | POST | Create-Booking, Change-Booking, Rebooking |
| `/create-cart` | POST | Create-Booking |
| `/checkout/passengers` | POST/PATCH | Create-Booking, Name-Change |
| `/services` | GET/POST | Ancillary-Sales |
| `/seatmap` | GET | Ancillary-Sales |
| `/seat/services` | POST/DELETE | Ancillary-Sales |
| `/checkoutConfirm` | POST | Create-Booking |
| `/orders/retrieve` | GET | Booking-Retrieval, all agents |
| `/cancelAndRefund` | POST (GraphQL) | RefundAgent, Refund-workflow |

---

> **Document generated from codebase analysis of orchestrator.py, mcp/server.py, README.md, and knowledge-docs-v1/.**
