# ✈️ Azure AI Foundry — Complete Setup Guide: Knowledge Bases & Agents

> **Goal**: Create 15 knowledge bases + 15 agents in Azure AI Foundry for the Airline Multi-Agent Orchestrator System  
> **Platform**: Azure AI Foundry (https://ai.azure.com)

---

## Table of Contents

1. [Execution Order — What to Do First](#1-execution-order)
2. [How to Create a Knowledge Base — Field-by-Field Guide](#2-knowledge-base-creation-guide)
3. [All 15 Knowledge Bases — Exact Configuration](#3-all-15-knowledge-bases)
4. [Knowledge Source Documents — Content to Upload](#4-knowledge-source-documents)
5. [How to Create an Agent — Field-by-Field Guide](#5-agent-creation-guide)
6. [All 15 Agents — Exact Configuration](#6-all-15-agents)
7. [Testing Each Agent](#7-testing)

---

## 1. Execution Order

> **IMPORTANT**: Follow this exact order. Knowledge bases must be created BEFORE agents, because agents reference knowledge bases.

```
Phase 1: Prepare Knowledge Documents (local files)
   ↓
Phase 2: Create Knowledge Bases in Azure AI Foundry (upload documents)
   ↓
Phase 3: Deploy a Chat Completions Model (GPT-4o or GPT-4.1)
   ↓
Phase 4: Create Agents (link to knowledge bases + add tools)
   ↓
Phase 5: Create Supervisor-Orchestrator-Agent (links to all other agents)
   ↓
Phase 6: Test each agent individually
   ↓
Phase 7: Test end-to-end orchestration flows
```

### Phase 1 Checklist — Prepare Documents First

Before touching Azure, create these files on your local machine:

- [ ] `airline_policies.md`
- [ ] `intent_classification_examples.json`
- [ ] `escalation_matrix.md`
- [ ] `booking_flow_guide.md`
- [ ] `fare_families.md`
- [ ] `passenger_type_codes.md`
- [ ] `name_change_policy.md`
- [ ] `refund_policy.md`
- [ ] `refund_graphql_schemas.md`
- [ ] `change_booking_rules.md`
- [ ] `rebooking_policy.md`
- [ ] `disruption_handling_guide.md`
- [ ] `ancillary_services_catalogue.md`
- [ ] `ssr_codes_reference.md`
- [ ] `medical_clearance_guide.md`
- [ ] `payment_processing_guide.md`
- [ ] `case_management_sla.md`
- [ ] `email_templates.md`
- [ ] `api_reference.md`

> The content for each of these files is provided in [Section 4](#4-knowledge-source-documents) below.

---

## 2. Knowledge Base Creation Guide

### How to Navigate

```
Azure AI Foundry → Your Project → Knowledge bases (left sidebar) → + Create
```

### Field-by-Field Explanation

When you click **"Create a new knowledge base"**, Azure shows you these fields:

| # | Field | What It Means | How to Fill It |
|---|-------|--------------|----------------|
| 1 | **Name*** | Unique identifier for this knowledge base | Use the naming convention: `kb-{agent-name}` (e.g., `kb-name-change-agent`) |
| 2 | **Description** | Human-readable summary | Describe what documents are in this KB and which agent uses it |
| 3 | **Chat completions model** | The LLM model used to reason over retrieved documents | Select your deployed model: **GPT-4o** or **GPT-4.1** (must be deployed first) |
| 4 | **Retrieval reasoning effort*** | How much reasoning the model applies to retrieved chunks | See table below |
| 5 | **Output mode*** | How the model formats its answers | See table below |
| 6 | **Retrieval instructions** | Custom instructions telling the KB how to prioritize/search documents | Natural language instructions for retrieval behavior |
| 7 | **Knowledge sources*** | The actual documents/files to upload | Upload `.md`, `.json`, `.txt`, `.pdf` files |

### Retrieval Reasoning Effort — When to Use Each

| Level | When to Use | Best For |
|-------|------------|----------|
| **Minimal** | Simple factual lookups, exact data retrieval | Booking-Retrieval (just look up PNR data) |
| **Low** | Straightforward Q&A with minimal interpretation | SSR codes lookup, airport codes |
| **Medium** | Moderate reasoning needed, some policy interpretation | ✅ **Recommended for most agents** — name change rules, refund policies |
| **High** | Complex reasoning, multi-document synthesis | Supervisor (intent classification), Disruption handling (EU261 + rebooking logic) |

### Output Mode — When to Use Each

| Mode | When to Use | Best For |
|------|------------|----------|
| **Extractive data** | Return exact quotes/data from documents | API reference lookups, policy text extraction |
| **Grounded generation** | Generate natural language answers grounded in documents | ✅ **Recommended for most agents** — agent responses to customers |
| **Ungrounded generation** | Free-form generation (not tied to documents) | NOT recommended for airline operations |

---

## 3. All 15 Knowledge Bases — Exact Configuration

### KB #1: Supervisor Orchestrator Knowledge Base

```
┌─────────────────────────────────────────────────────────┐
│  CREATE KNOWLEDGE BASE                                   │
├─────────────────────────────────────────────────────────┤
│  Name*:           kb-supervisor-orchestrator              │
│                                                          │
│  Description:     Master knowledge base for the          │
│                   Supervisor-Orchestrator-Agent.          │
│                   Contains airline policies, intent       │
│                   classification examples, and            │
│                   escalation rules for routing            │
│                   customer requests to specialized        │
│                   agents.                                 │
│                                                          │
│  Chat completions                                        │
│  model:           gpt-4o (select your deployed model)    │
│                                                          │
│  Retrieval                                               │
│  reasoning        High                                   │
│  effort*:         (needs complex intent classification)  │
│                                                          │
│  Output mode*:    Grounded generation                    │
│                                                          │
│  Retrieval        "You are the routing brain of an       │
│  instructions:    airline service center. When a         │
│                   customer request arrives, search        │
│                   'intent_classification_examples.json'   │
│                   FIRST to match the intent. Then check  │
│                   'airline_policies.md' for any policy    │
│                   constraints. Check                     │
│                   'escalation_matrix.md' to determine    │
│                   if human escalation is needed."         │
│                                                          │
│  Knowledge        📄 airline_policies.md                 │
│  sources*:        📄 intent_classification_examples.json │
│                   📄 escalation_matrix.md                │
│                   📄 api_reference.md                    │
└─────────────────────────────────────────────────────────┘
```

---

### KB #2: Create Booking Knowledge Base

```
┌─────────────────────────────────────────────────────────┐
│  Name*:           kb-create-booking                      │
│                                                          │
│  Description:     Knowledge base for the Create-Booking  │
│                   -Agent. Contains the complete           │
│                   Amadeus-Nevio 10-step booking flow,     │
│                   fare families, passenger types, and     │
│                   cabin class information.                │
│                                                          │
│  Chat completions                                        │
│  model:           gpt-4o                                 │
│                                                          │
│  Retrieval                                               │
│  reasoning        Medium                                 │
│  effort*:                                                │
│                                                          │
│  Output mode*:    Grounded generation                    │
│                                                          │
│  Retrieval        "Follow the booking_flow_guide.md      │
│  instructions:    step-by-step when executing a new      │
│                   booking. Reference fare_families.md     │
│                   for fare rules and                     │
│                   passenger_type_codes.md for             │
│                   passenger validation. Always follow     │
│                   the exact API sequence: search →        │
│                   create cart → add travelers →           │
│                   contacts → services → seats →           │
│                   checkout."                              │
│                                                          │
│  Knowledge        📄 booking_flow_guide.md               │
│  sources*:        📄 fare_families.md                    │
│                   📄 passenger_type_codes.md             │
│                   📄 api_reference.md                    │
└─────────────────────────────────────────────────────────┘
```

---

### KB #3: Booking Retrieval Knowledge Base

```
┌─────────────────────────────────────────────────────────┐
│  Name*:           kb-booking-retrieval                   │
│                                                          │
│  Description:     Knowledge base for the Booking-        │
│                   Retrieval-Agent. Contains PNR format    │
│                   rules and order status codes.           │
│                                                          │
│  Chat completions                                        │
│  model:           gpt-4o                                 │
│                                                          │
│  Retrieval                                               │
│  reasoning        Minimal                                │
│  effort*:         (simple lookups, no complex reasoning) │
│                                                          │
│  Output mode*:    Extractive data                        │
│                                                          │
│  Retrieval        "Use api_reference.md to find the      │
│  instructions:    correct endpoint for retrieving        │
│                   orders. Validate PNR format (6          │
│                   alphanumeric characters) before         │
│                   making API calls."                      │
│                                                          │
│  Knowledge        📄 api_reference.md                    │
│  sources*:        📄 airline_policies.md                 │
└─────────────────────────────────────────────────────────┘
```

---

### KB #4: Name Change Knowledge Base

```
┌─────────────────────────────────────────────────────────┐
│  Name*:           kb-name-change                         │
│                                                          │
│  Description:     Knowledge base for the Name-Change-    │
│                   Agent. Contains name change policies,   │
│                   fee structures, identity verification   │
│                   requirements, and allowed vs            │
│                   disallowed changes.                     │
│                                                          │
│  Chat completions                                        │
│  model:           gpt-4o                                 │
│                                                          │
│  Retrieval                                               │
│  reasoning        Medium                                 │
│  effort*:         (policy interpretation needed)         │
│                                                          │
│  Output mode*:    Grounded generation                    │
│                                                          │
│  Retrieval        "ALWAYS check name_change_policy.md    │
│  instructions:    FIRST to determine if a name change    │
│                   is allowed. Classify the change as      │
│                   'minor correction' or 'full name        │
│                   change' based on the rules. Check       │
│                   departure time constraints before       │
│                   proceeding. Reference api_reference.md  │
│                   for the correct API endpoint."          │
│                                                          │
│  Knowledge        📄 name_change_policy.md               │
│  sources*:        📄 api_reference.md                    │
│                   📄 airline_policies.md                 │
└─────────────────────────────────────────────────────────┘
```

---

### KB #5: Change Booking Knowledge Base

```
┌─────────────────────────────────────────────────────────┐
│  Name*:           kb-change-booking                      │
│                                                          │
│  Description:     Knowledge base for the Change-Booking  │
│                   -Agent. Contains change fee rules,      │
│                   fare difference calculations, and       │
│                   same-day change policies.               │
│                                                          │
│  Chat completions model:  gpt-4o                         │
│  Retrieval reasoning effort*:  Medium                    │
│  Output mode*:  Grounded generation                      │
│                                                          │
│  Retrieval        "Check change_booking_rules.md for     │
│  instructions:    change fees and fare difference         │
│                   policies before processing any          │
│                   modifications. Reference                │
│                   fare_families.md for fare family        │
│                   restrictions."                          │
│                                                          │
│  Knowledge        📄 change_booking_rules.md             │
│  sources*:        📄 fare_families.md                    │
│                   📄 api_reference.md                    │
└─────────────────────────────────────────────────────────┘
```

---

### KB #6: Refund Agent Knowledge Base

```
┌─────────────────────────────────────────────────────────┐
│  Name*:           kb-refund-agent                        │
│                                                          │
│  Description:     Knowledge base for the RefundAgent.    │
│                   Contains refund eligibility rules,      │
│                   EU261 regulations, 24-hour rule, and    │
│                   GraphQL query/mutation schemas for      │
│                   the cancelAndRefund API.                │
│                                                          │
│  Chat completions model:  gpt-4o                         │
│  Retrieval reasoning effort*:  High                      │
│  Output mode*:  Grounded generation                      │
│                                                          │
│  Retrieval        "ALWAYS check refund_policy.md first   │
│  instructions:    to determine eligibility rules. Use    │
│                   refund_graphql_schemas.md for the       │
│                   exact GraphQL query structure.          │
│                   Calculate penalties based on fare       │
│                   type and time-to-departure."            │
│                                                          │
│  Knowledge        📄 refund_policy.md                    │
│  sources*:        📄 refund_graphql_schemas.md           │
│                   📄 api_reference.md                    │
│                   📄 airline_policies.md                 │
└─────────────────────────────────────────────────────────┘
```

---

### KB #7: Refund Workflow Knowledge Base

```
┌─────────────────────────────────────────────────────────┐
│  Name*:           kb-refund-workflow                     │
│                                                          │
│  Description:     Knowledge base for the Refund-workflow │
│                   Agent. Contains the cancellation and    │
│                   refund execution process, GraphQL       │
│                   mutation schemas, and payment           │
│                   reversal procedures.                    │
│                                                          │
│  Chat completions model:  gpt-4o                         │
│  Retrieval reasoning effort*:  Medium                    │
│  Output mode*:  Grounded generation                      │
│                                                          │
│  Retrieval        "Use refund_graphql_schemas.md for     │
│  instructions:    the CancellationAndRefund mutation.     │
│                   Always include refundProposalIds from   │
│                   the eligibility check response."        │
│                                                          │
│  Knowledge        📄 refund_graphql_schemas.md           │
│  sources*:        📄 refund_policy.md                    │
│                   📄 api_reference.md                    │
└─────────────────────────────────────────────────────────┘
```

---

### KB #8: Rebooking Knowledge Base

```
┌─────────────────────────────────────────────────────────┐
│  Name*:           kb-rebooking                           │
│                                                          │
│  Description:     Knowledge base for the Rebooking-Agent │
│                   . Covers voluntary rebooking policies,  │
│                   standby rules, and fare difference      │
│                   handling.                               │
│                                                          │
│  Chat completions model:  gpt-4o                         │
│  Retrieval reasoning effort*:  Medium                    │
│  Output mode*:  Grounded generation                      │
│                                                          │
│  Retrieval        "Check rebooking_policy.md for         │
│  instructions:    voluntary rebooking rules. Calculate   │
│                   fare differences before confirming."    │
│                                                          │
│  Knowledge        📄 rebooking_policy.md                 │
│  sources*:        📄 fare_families.md                    │
│                   📄 api_reference.md                    │
└─────────────────────────────────────────────────────────┘
```

---

### KB #9: Disruption Rebooking Knowledge Base

```
┌─────────────────────────────────────────────────────────┐
│  Name*:           kb-disruption-rebooking                │
│                                                          │
│  Description:     Knowledge base for the Disruption-     │
│                   Rebooking-Agent. Contains IROP          │
│                   handling procedures, EU261              │
│                   compensation rules, and auto-rebook     │
│                   logic.                                  │
│                                                          │
│  Chat completions model:  gpt-4o                         │
│  Retrieval reasoning effort*:  High                      │
│  Output mode*:  Grounded generation                      │
│                                                          │
│  Retrieval        "Prioritize disruption_handling_guide   │
│  instructions:    .md for IROP procedures. Apply EU261   │
│                   compensation rules based on distance    │
│                   and delay duration. Always waive fees   │
│                   for airline-caused disruptions."        │
│                                                          │
│  Knowledge        📄 disruption_handling_guide.md        │
│  sources*:        📄 rebooking_policy.md                 │
│                   📄 airline_policies.md                 │
│                   📄 api_reference.md                    │
└─────────────────────────────────────────────────────────┘
```

---

### KB #10: Ancillary Sales Knowledge Base

```
┌─────────────────────────────────────────────────────────┐
│  Name*:           kb-ancillary-sales                     │
│                                                          │
│  Description:     Knowledge base for the Ancillary-Sales │
│                   -Agent. Contains the full service       │
│                   catalogue, seat types, pricing, and     │
│                   promotion codes.                        │
│                                                          │
│  Chat completions model:  gpt-4o                         │
│  Retrieval reasoning effort*:  Low                       │
│  Output mode*:  Extractive data                          │
│                                                          │
│  Retrieval        "Search ancillary_services_catalogue   │
│  instructions:    .md for available services and          │
│                   pricing. Use promotion code SCUISEATP   │
│                   for seat promotions. Reference          │
│                   api_reference.md for service and        │
│                   seat API endpoints."                    │
│                                                          │
│  Knowledge        📄 ancillary_services_catalogue.md     │
│  sources*:        📄 api_reference.md                    │
└─────────────────────────────────────────────────────────┘
```

---

### KB #11: Passenger SSR Knowledge Base

```
┌─────────────────────────────────────────────────────────┐
│  Name*:           kb-passenger-ssr                        │
│                                                          │
│  Description:     Knowledge base for the Passenger-SSR-  │
│                   Agent. Contains IATA SSR codes,         │
│                   special meal codes, wheelchair types,   │
│                   and unaccompanied minor rules.          │
│                                                          │
│  Chat completions model:  gpt-4o                         │
│  Retrieval reasoning effort*:  Low                       │
│  Output mode*:  Extractive data                          │
│                                                          │
│  Retrieval        "Look up SSR codes in                  │
│  instructions:    ssr_codes_reference.md. Match           │
│                   customer requests to the correct IATA   │
│                   code. Check age rules for UMNR          │
│                   (unaccompanied minors)."                │
│                                                          │
│  Knowledge        📄 ssr_codes_reference.md              │
│  sources*:        📄 airline_policies.md                 │
│                   📄 api_reference.md                    │
└─────────────────────────────────────────────────────────┘
```

---

### KB #12: Medical Exception Knowledge Base

```
┌─────────────────────────────────────────────────────────┐
│  Name*:           kb-medical-exception                   │
│                                                          │
│  Description:     Knowledge base for the Medical-        │
│                   Exception-Agent. Contains MEDIF form    │
│                   requirements, fit-to-fly rules, and     │
│                   medical equipment approval policies.    │
│                                                          │
│  Chat completions model:  gpt-4o                         │
│  Retrieval reasoning effort*:  Medium                    │
│  Output mode*:  Grounded generation                      │
│                                                          │
│  Retrieval        "Reference medical_clearance_guide.md  │
│  instructions:    for all medical clearance decisions.    │
│                   Check if a MEDIF form is required       │
│                   based on the medical condition."        │
│                                                          │
│  Knowledge        📄 medical_clearance_guide.md          │
│  sources*:        📄 airline_policies.md                 │
└─────────────────────────────────────────────────────────┘
```

---

### KB #13: Payment Knowledge Base

```
┌─────────────────────────────────────────────────────────┐
│  Name*:           kb-payment                             │
│                                                          │
│  Description:     Knowledge base for the Payment-Agent.  │
│                   Contains supported payment methods,     │
│                   currency rules, and payment processing  │
│                   procedures.                             │
│                                                          │
│  Chat completions model:  gpt-4o                         │
│  Retrieval reasoning effort*:  Low                       │
│  Output mode*:  Extractive data                          │
│                                                          │
│  Retrieval        "Reference payment_processing_guide    │
│  instructions:    .md for supported payment methods and  │
│                   processing rules."                     │
│                                                          │
│  Knowledge        📄 payment_processing_guide.md        │
│  sources*:        📄 api_reference.md                   │
└─────────────────────────────────────────────────────────┘
```

---

### KB #14: Case Management Knowledge Base

```
┌─────────────────────────────────────────────────────────┐
│  Name*:           kb-case-management                     │
│                                                          │
│  Description:     Knowledge base for the Case-Management │
│                   -Agent. Contains case priority matrix,  │
│                   SLA timelines, and escalation paths.    │
│                                                          │
│  Chat completions model:  gpt-4o                         │
│  Retrieval reasoning effort*:  Medium                    │
│  Output mode*:  Grounded generation                      │
│                                                          │
│  Retrieval        "Check case_management_sla.md for      │
│  instructions:    priority classification and SLA         │
│                   timelines. Use escalation_matrix.md     │
│                   to determine when human escalation      │
│                   is required."                           │
│                                                          │
│  Knowledge        📄 case_management_sla.md              │
│  sources*:        📄 escalation_matrix.md                │
└─────────────────────────────────────────────────────────┘
```

---

### KB #15: Communication Summary Knowledge Base

```
┌─────────────────────────────────────────────────────────┐
│  Name*:           kb-communication-summary               │
│                                                          │
│  Description:     Knowledge base for the Communication-  │
│                   Case-Summary-Agent. Contains email      │
│                   templates, communication guidelines,    │
│                   and GDPR data handling rules.           │
│                                                          │
│  Chat completions model:  gpt-4o                         │
│  Retrieval reasoning effort*:  Low                       │
│  Output mode*:  Grounded generation                      │
│                                                          │
│  Retrieval        "Use email_templates.md for generating │
│  instructions:    customer communications. Always follow │
│                   the correct template based on the       │
│                   communication type (confirmation,       │
│                   cancellation, disruption, etc.)."       │
│                                                          │
│  Knowledge        📄 email_templates.md                  │
│  sources*:        📄 airline_policies.md                 │
└─────────────────────────────────────────────────────────┘
```

---

## 4. Knowledge Source Documents — Content to Upload

> **TIP**: Create each of these files locally, then upload them as Knowledge Sources when creating each KB.

---

### 📄 Document 1: `airline_policies.md`
**Upload to**: kb-supervisor-orchestrator, kb-booking-retrieval, kb-name-change, kb-refund-agent, kb-disruption-rebooking, kb-passenger-ssr, kb-medical-exception, kb-communication-summary

```markdown
# Airline Operations Policy Manual

## 1. General Booking Policies

### 1.1 Booking Validity
- Bookings are valid for travel within 365 days from date of issue
- Tickets must be issued within the ticketing time limit (TTL)
- Group bookings (10+ passengers) follow separate policies

### 1.2 Passenger Types
| Code | Type | Age Range | Documentation |
|------|------|-----------|--------------|
| ADT | Adult | 12+ years | Valid ID/Passport |
| CHD | Child | 2-11 years | Birth certificate + Passport |
| INF | Infant | 0-23 months | Birth certificate (no seat) |
| YTH | Youth | 12-25 years | Valid ID + age proof |

### 1.3 Contact Requirements
- Valid email address mandatory for all bookings
- Phone number required (mobile preferred)
- Emergency contact for unaccompanied minors

## 2. Name Change Policy
- Minor corrections (<=3 character changes): FREE
- Full name change: Fee per airline policy (EUR50-EUR150)
- Name transfer to different person: NOT ALLOWED (must cancel + rebook)
- Deadline: Must be done >=24 hours before departure
- Not allowed after check-in opens
- Required documents: Valid passport/ID, marriage certificate (if applicable)

## 3. Cancellation & Refund Policy

### 3.1 24-Hour Rule
- Full refund available within 24 hours of booking (if departure >7 days away)
- Applies to all fare types

### 3.2 Refund by Fare Type
| Fare Family | Voluntary Cancel | Refund Amount | Penalty |
|------------|-----------------|---------------|---------|
| Light/Basic | Not refundable | Tax refund only | 100% fare |
| Classic | Refundable | Full minus penalty | EUR75-EUR150 |
| Flex | Fully refundable | Full refund | None |
| Business Flex | Fully refundable | Full refund | None |

### 3.3 Involuntary Refund (Airline Cancellation)
- Full refund within 7 days
- No penalty applied
- Choice: refund OR rebooking on next available

### 3.4 EU261/2004 Compensation
| Distance | Delay | Compensation |
|----------|-------|-------------|
| <=1500 km | >=3 hours | EUR250 |
| 1500-3500 km | >=3 hours | EUR400 |
| >3500 km | >=4 hours | EUR600 |

## 4. Change Booking Policy
- Voluntary changes subject to fare difference + change fee
- Flex fares: No change fee (fare difference may apply)
- Same-day changes: Subject to availability, reduced fee
- Deadline: Changes must be made >=3 hours before departure

## 5. Special Services (SSR)
- Wheelchair: Must be requested >=48 hours before departure
- Special meals: Must be requested >=24 hours before departure
- Unaccompanied minor (UMNR): Ages 5-11, mandatory service, fee applies
- Pet in cabin (PETC): Subject to aircraft type approval

## 6. Ancillary Services
- Extra baggage can be purchased up to 1 hour before departure
- Seat selection available from booking until check-in closes
- Lounge access: Available for purchase or with eligible fare/status

## 7. Escalation Rules
- ALWAYS escalate to human agent for:
  - Suspected fraud
  - VIP/Loyalty Platinum+ passengers
  - Legal threats or regulatory complaints
  - Medical emergencies
  - Bookings with >=10 passengers
  - Revenue impact > EUR5,000
```

---

### 📄 Document 2: `name_change_policy.md`
**Upload to**: kb-name-change

```markdown
# Passenger Name Change — Complete Policy & Procedures

## 1. Types of Name Changes

### 1.1 Minor Correction (NO FEE)
Definition: A correction of <=3 characters in the passenger name.

Examples:
- "Jhon Smith" -> "John Smith" (1 character)
- "Maria Gonzalez" -> "Maria Gonzalez" (accent added)
- "ROBERT BROWN" -> "Robert Brown" (case correction)
- Adding/removing middle name
- Correcting title (Mr -> Mrs)

Rules:
- No fee charged
- No supporting documentation required
- Can be done up to 2 hours before departure
- Available for all fare types

### 1.2 Full Name Change (FEE APPLIES)
Definition: A change of >3 characters, or a complete first/last name change.

Examples:
- "Sarah Johnson" -> "Sarah Williams" (married name)
- "Michael Chen" -> "Mike Chen" (shortened name - treated as full change)

Rules:
- Fee: EUR50 (domestic) / EUR100 (international) / EUR150 (intercontinental)
- Required >=24 hours before departure
- Must provide supporting documentation:
  - Marriage certificate (married name change)
  - Court order (legal name change)
  - Corrected passport/ID
- Not available for Light/Basic fares without waiver

### 1.3 Name Transfer (NOT ALLOWED)
- Transferring a booking to a completely different person is NOT a name change
- Must cancel existing booking and create new booking
- Original cancellation policy applies

## 2. Verification Requirements
Before any name change, verify passenger identity:
1. Date of birth (must match booking)
2. Original booking email address
3. Passport/ID number (if available in booking)
4. Last 4 digits of payment card used

## 3. Processing Steps
1. Retrieve booking using PNR + last name
2. Verify passenger identity (DOB, email)
3. Classify change type (minor vs full)
4. Check departure time constraint (>=24hrs)
5. Check if check-in is open (must be closed)
6. Apply fee if full name change
7. Update passenger name via API
8. Generate confirmation email
9. Create case note for audit trail

## 4. Blocked Scenarios
- Departure in less than 24 hours
- Check-in already opened
- Passenger already boarded
- Ticket already used (partially flown)
- Name transfer to different person
- Booking in cancelled/suspended status

## 5. Waiver Authority
- Supervisor Level 1: Can waive fee up to EUR100
- Supervisor Level 2: Can waive fee up to EUR150
- Manager: Can waive any fee + override time restrictions
- Waiver reason must be documented in case notes
```

---

### 📄 Document 3: `booking_flow_guide.md`
**Upload to**: kb-create-booking

```markdown
# Amadeus-Nevio Booking Flow — Step-by-Step Guide

## Prerequisites
- Valid Amadeus Token (obtained via /token/amadeus)
- Valid JWT Token (obtained via /token)

## Complete 10-Step Booking Flow

### Step 1: Search Flights
- Endpoint: POST /shop/flights
- Input: origin (IATA), destination (IATA), departureDate, returnDate, paxCount, cabinClass
- Output: Array of air bounds with airBoundId, prices, schedules
- Notes: Response may contain direct and connecting flights

### Step 2: Create Cart
- Endpoint: POST /create-cart
- Input: Selected airBoundId from Step 1
- Output: cartId, passengerId(s)
- Notes: Creates an empty cart with passenger placeholders

### Step 3: Add Travelers
- Endpoint: POST /checkout/passengers
- Input: cartId, for each passenger: firstName, lastName, dateOfBirth, gender, passengerTypeCode
- Output: Traveler confirmation
- Notes: Must match the passenger count from Step 1

### Step 4: Add Contacts
- Endpoint: PATCH /checkout/passengers
- Input: cartId, email, phoneNumber, countryCode
- Output: Contact confirmation
- Notes: At least one email and one phone number required

### Step 5: Get Service Catalogue (OPTIONAL)
- Endpoint: GET /services?cartId={{cartId}}&promotionCode=SCUISEATP
- Output: Available services (baggage, meals, lounge, etc.) with SKU IDs and prices
- Notes: Only call if customer wants ancillary services

### Step 6: Add Services (OPTIONAL)
- Endpoint: POST /seat/services
- Input: cartId, serviceSelections (array of SKU IDs + passenger IDs)
- Output: Services added confirmation
- Notes: Can add multiple services in one call

### Step 7: Get Seat Map (OPTIONAL)
- Endpoint: GET /seatmap?cartId={{cartId}}&flightId={{flightId}}&promoCode=SCUISEATP&promotionAirlineCode=AY
- Output: Seat map layout with available/occupied seats and prices
- Notes: flightId comes from Step 1 response

### Step 8: Add Seats (OPTIONAL)
- Endpoint: POST /seat/services
- Input: cartId, seatSelections (array of seatId + passengerId)
- Output: Seat assignment confirmation

### Step 9: Create Order (Checkout Confirm)
- Endpoint: POST /checkoutConfirm
- Input: cartId
- Output: orderRecLocId (PNR), orderId
- Notes: This finalizes the booking and issues the PNR

### Step 10: Retrieve Order
- Endpoint: GET /orders/retrieve?orderRecLocId={{PNR}}&lastName={{lastName}}&showOrderEligibilities=true
- Output: Full order details with all segments, passengers, services, seats, payment info
- Notes: Use this to confirm the booking to the customer

## Mandatory vs Optional Steps
| Step | Mandatory? | When to Skip |
|------|-----------|-------------|
| 1-4 | YES | Never skip |
| 5-6 | Optional | Skip if customer doesnt want ancillaries |
| 7-8 | Optional | Skip if customer doesnt want seat selection |
| 9-10 | YES | Never skip |

## Error Handling
- If any step fails, do NOT proceed to next step
- Cart expires after 30 minutes of inactivity
- If cart expires, restart from Step 1
```

---

### 📄 Document 4: `refund_policy.md`
**Upload to**: kb-refund-agent, kb-refund-workflow

```markdown
# Refund Policy & Procedures

## 1. Refund Eligibility Check
Before processing any refund, call the RetriveOrderRefundEligiblities query.
The response will contain:
- refundStatus: "refundable" or "non-refundable"
- totalRefundAmounts: Amount to be refunded
- totalPaidAmount: Original payment amount
- totalUsedAmount: Value of used segments
- totalPenalty: Cancellation penalty
- nonEligibilityReasons: Why refund is blocked (if applicable)

## 2. Refund Calculation
Net Refund = totalPaidAmount - totalUsedAmount - totalPenalty

## 3. Processing Steps
1. Call RetriveOrderRefundEligiblities with orderId + lastName
2. Check refundStatus
3. If refundable: present breakdown to customer
4. Get customer confirmation
5. Call CancellationAndRefund mutation with refundProposalIds
6. Confirm refund processing

## 4. Refund Timeline
- Credit card: 5-10 business days
- Bank transfer: 10-15 business days
- Travel voucher: Immediate

## 5. Non-Eligibility Reasons
| Code | Meaning |
|------|---------|
| TICKET_USED | Passenger has already flown |
| NON_REFUNDABLE_FARE | Fare type does not allow refunds |
| TIME_LIMIT_EXCEEDED | Past refund deadline |
| SUSPENDED_BOOKING | Booking is in suspended state |
```

---

### 📄 Document 5: `refund_graphql_schemas.md`
**Upload to**: kb-refund-agent, kb-refund-workflow

```markdown
# Refund GraphQL Schemas — API Reference

## Query: Check Refund Eligibility

Endpoint: POST {{APIM_URL}}/cancelAndRefund

GraphQL Query:
query RetriveOrderRefundEligiblities($input: RefundEligiblitiesInput!) {
  RetriveOrderRefundEligiblities(input: $input) {
    type
    data {
      orderId
      refundStatus
      totalRefund {
        totalRefundAmounts {
          total { value, currencyCode }
        }
        totalPaidAmount {
          total { value, currencyCode }
        }
        totalUsedAmount {
          total { value, currencyCode }
        }
        totalPenalty {
          total { currencyCode, value }
        }
      }
      travelers {
        travelerId
        totalRefund {
          totalRefundAmounts { total { value, currencyCode } }
          totalPaidAmount { total { value, currencyCode } }
          totalUsedAmount { total { value, currencyCode } }
          totalPenalty { total { currencyCode, value } }
        }
        travelDocuments {
          travelDocumentId
          documentType
          status
          refundAmounts {
            base { value, currencyCode }
            taxes { value, currencyCode, code, category }
            totalTaxes { value, currencyCode }
            total { value, currencyCode }
          }
          paidAmount {
            base { value, currencyCode }
            total { value, currencyCode }
          }
          penalty { value, currencyCode }
          refundMethodOptions {
            id
            paymentDetails {
              paymentMethod { paymentType, vendorCode, cardNumber, expiryDate }
              amount { value, currencyCode }
            }
          }
        }
      }
      refundProposalReferences { refundProposalId }
      nonEligibilityReasons { code, title }
    }
  }
}

Variables:
{
  "input": {
    "targetAction": "cancelAndRefund",
    "orderId": "<PNR>",
    "lastName": "<passenger_last_name>",
    "isEligible": true
  }
}

## Mutation: Execute Cancellation & Refund

GraphQL Mutation:
mutation CancellationAndRefund($input: CancellationAndRefundInput!) {
  CancellationAndRefund(input: $input) {
    orderId
    totalRefund {
      totalRefundAmounts { total { value, currencyCode } }
      totalPaidAmount { total { value, currencyCode } }
      totalUsedAmount { total { value, currencyCode } }
    }
    travelers {
      travelerId
      travelDocuments {
        travelDocumentId
        documentType
        status
        refundAmounts { total { value, currencyCode } }
        paymentDetails {
          paymentMethod { paymentType, vendorCode, cardNumber, expiryDate }
          amount { value, currencyCode }
        }
      }
    }
    errors { code, title, detail }
  }
}

Variables:
{
  "input": {
    "refundProposalIds": ["<from_eligibility_response>"],
    "orderId": "<PNR>",
    "lastName": "<passenger_last_name>"
  }
}
```

---

### 📄 Document 6: `api_reference.md`
**Upload to**: All knowledge bases

```markdown
# Amadeus-Nevio Service Center — API Reference

Base URL: https://nevioservicecenterapim.azure-api.net
Airline Code: AY

## Authentication
| Endpoint | Method | Purpose |
|----------|--------|---------|
| /token | POST | Get JWT Token |
| /token/amadeus | POST | Get Amadeus Token |

## Shopping & Booking APIs
| Endpoint | Method | Purpose |
|----------|--------|---------|
| /searchpanel | GET | Get search panel configuration |
| /shop/flights | POST | Search available flights |
| /create-cart | POST | Create shopping cart with selected flight |
| /checkout/passengers | POST | Add passenger details |
| /checkout/passengers | PATCH | Update passenger details / Add contacts |
| /cart/retrieve | GET | Retrieve cart contents |
| /services | GET | Get service catalogue for cart |
| /seat/services | POST | Add seats or services |
| /seat/services | DELETE | Remove seats or services |
| /seatmap | GET | Get seat map for flight |
| /checkoutConfirm | POST | Confirm checkout / create order |
| /orders/retrieve | GET | Retrieve confirmed order by PNR |

## Post-Order APIs
| Endpoint | Method | Purpose |
|----------|--------|---------|
| /services | POST | Post-order service catalogue |
| /seatmap | GET | Post-order seat map |
| /seat/services | POST | Post-order add seats/services |

## GraphQL APIs
| Endpoint | Operations | Purpose |
|----------|-----------|---------|
| /appConfig | CRUD mutations/queries | Application configuration |
| /cancelAndRefund | RetriveOrderRefundEligiblities, CancellationAndRefund | Refund operations |

## Key Parameters
| Parameter | Description | Example |
|-----------|-------------|---------|
| cartId | Shopping cart identifier | auto-generated |
| orderRecLocId | PNR / Order locator | 6-char alphanumeric (e.g., 9DVWPJ) |
| airBoundId | Selected flight offer ID | from /shop/flights response |
| flightId | Flight identifier | from air bound response |
| promotionCode | Promo code for services | SCUISEATP |
| promotionAirlineCode | Airline code for promotions | AY |
```

---

### 📄 Document 7: `escalation_matrix.md`
**Upload to**: kb-supervisor-orchestrator, kb-case-management

```markdown
# Escalation Matrix — When to Involve Human Agents

## Immediate Escalation (Priority: CRITICAL)
| Scenario | Escalation Target |
|----------|------------------|
| Suspected fraud or stolen payment card | Security Team |
| Medical emergency in-flight or at airport | Operations + Medical |
| Legal threats or regulatory complaint | Legal Department |
| Media/social media escalation risk | PR + Customer Relations |
| VIP / Loyalty Platinum+ passenger complaint | VIP Service Desk |
| Safety or security concern | Security Team |

## High Priority Escalation
| Scenario | Escalation Target |
|----------|------------------|
| Revenue impact > EUR5,000 | Revenue Management |
| Group booking (10+ passengers) issues | Group Desk |
| Codeshare/partner airline issues | Interline Desk |
| Repeated failed API calls (system issue) | IT Support |
| Customer threatening legal action | Legal Department |

## Standard Escalation
| Scenario | Escalation Target |
|----------|------------------|
| Agent unable to resolve after 3 attempts | Supervisor Level 2 |
| Waiver request exceeding agent authority | Supervisor Level 2 |
| Complex multi-segment itinerary changes | Ticketing Desk |
| Disability or accessibility complaint | Accessibility Team |
```

---

### 📄 Document 8: `intent_classification_examples.json`
**Upload to**: kb-supervisor-orchestrator

```json
{
  "examples": [
    {
      "input": "I need to book a flight from Helsinki to London next Friday",
      "intent": "NEW_BOOKING",
      "agent": "Create-Booking-Agent",
      "entities": { "origin": "HEL", "destination": "LHR", "date": "next Friday" }
    },
    {
      "input": "Can you pull up my booking? PNR is ABC123",
      "intent": "RETRIEVE_BOOKING",
      "agent": "Booking-Retrieval-Agent",
      "entities": { "pnr": "ABC123" }
    },
    {
      "input": "I need to change my name from Sarah Johnson to Sarah Williams on booking XYZ789",
      "intent": "NAME_CHANGE",
      "agent": "Name-Change-Agent",
      "entities": { "pnr": "XYZ789", "old_name": "Sarah Johnson", "new_name": "Sarah Williams" }
    },
    {
      "input": "My name is spelled wrong on the ticket. It says Jhon but should be John",
      "intent": "NAME_CHANGE",
      "agent": "Name-Change-Agent",
      "entities": { "old_name": "Jhon", "new_name": "John", "change_type": "minor_correction" }
    },
    {
      "input": "I want to cancel my booking 9DVWPJ and get a refund",
      "intent": "CANCEL_AND_REFUND",
      "agent": "RefundAgent",
      "entities": { "pnr": "9DVWPJ", "action": "cancelAndRefund" }
    },
    {
      "input": "Can I change my flight to the next day?",
      "intent": "CHANGE_BOOKING",
      "agent": "Change-Booking-Agent",
      "entities": { "change_type": "date_change" }
    },
    {
      "input": "My flight was cancelled, I need to be rebooked",
      "intent": "DISRUPTION_REBOOKING",
      "agent": "Disruption-Rebooking-Agent",
      "entities": { "disruption_type": "cancellation" }
    },
    {
      "input": "I want to add extra baggage to my booking",
      "intent": "ANCILLARY_SERVICE",
      "agent": "Ancillary-Sales-Agent",
      "entities": { "service_type": "baggage" }
    },
    {
      "input": "I need a wheelchair at the airport",
      "intent": "SSR_REQUEST",
      "agent": "Passenger-SSR-Agent",
      "entities": { "ssr_type": "WCHR" }
    },
    {
      "input": "I have a medical condition and need clearance to fly",
      "intent": "MEDICAL_EXCEPTION",
      "agent": "Medical-Exception-Agent",
      "entities": { "request_type": "fit_to_fly" }
    },
    {
      "input": "My payment didnt go through for the booking",
      "intent": "PAYMENT_ISSUE",
      "agent": "Payment-Agent",
      "entities": { "issue_type": "payment_failure" }
    },
    {
      "input": "Whats the status of my complaint case?",
      "intent": "CASE_INQUIRY",
      "agent": "Case-Management-Agent",
      "entities": { "action": "status_check" }
    },
    {
      "input": "Can you send me a confirmation email for my booking?",
      "intent": "COMMUNICATION",
      "agent": "Communication-Case-Summary-Agent",
      "entities": { "comm_type": "confirmation_email" }
    },
    {
      "input": "I want to select seat 12A on my flight",
      "intent": "SEAT_SELECTION",
      "agent": "Ancillary-Sales-Agent",
      "entities": { "service_type": "seat", "seat_preference": "12A" }
    },
    {
      "input": "Book me HEL to LHR with extra bag and seat 5C",
      "intent": "NEW_BOOKING_WITH_ANCILLARY",
      "agent": "Create-Booking-Agent then Ancillary-Sales-Agent",
      "entities": { "origin": "HEL", "destination": "LHR", "services": ["baggage", "seat:5C"] }
    }
  ]
}
```

---

### 📄 Remaining Documents to Create

| File | Key Content to Include |
|------|----------------------|
| `change_booking_rules.md` | Change fee matrix by fare family, same-day change rules, deadline rules |
| `rebooking_policy.md` | Voluntary rebooking fees, standby rules, fare difference handling |
| `disruption_handling_guide.md` | IROP procedures, EU261 compensation table, hotel/meal voucher rules |
| `ancillary_services_catalogue.md` | All services (baggage tiers, meals, lounge, WiFi, insurance) with prices |
| `ssr_codes_reference.md` | WCHR/WCHC/WCHS, VGML/DBML/AVML, UMNR, PETC/AVIH — all IATA codes |
| `medical_clearance_guide.md` | MEDIF form, fitness-to-fly, oxygen equipment, stretcher requests |
| `payment_processing_guide.md` | Supported cards, currency rules, 3DS, failed payment recovery |
| `case_management_sla.md` | Priority P1-P4, response SLAs, resolution SLAs, auto-close rules |
| `email_templates.md` | Templates: booking confirmation, name change, cancellation, disruption |
| `fare_families.md` | Light, Classic, Flex, Business — included services, change/cancel rules |
| `passenger_type_codes.md` | ADT, CHD, INF, YTH — age boundaries, discount codes, documentation |

---

## 5. Agent Creation Guide

### How to Navigate

```
Azure AI Foundry → Your Project → Agents (left sidebar) → + New Agent
```

### Agent Configuration Fields

When you create or edit an agent, you will see these fields:

| # | Field | What It Means | How to Fill It |
|---|-------|---------------|----------------|
| 1 | **Name*** | Agent identifier | Use exact names from your existing list |
| 2 | **Instructions*** | System prompt — the agent's brain | Detailed role + rules + API context |
| 3 | **Model*** | The LLM deployment to use | Select your deployed GPT-4o or GPT-4.1 |
| 4 | **Tools** | Functions the agent can call | Add API tools as function definitions |
| 5 | **Knowledge** | Link to knowledge base(s) | Connect the KB(s) created in Phase 2 |
| 6 | **Actions** | Code interpreter, file search, etc. | Enable as needed |

---

## 6. All 15 Agents — Exact Configuration

### Agent #1: Supervisor-Orchestrator-Agent

```
Name*:          Supervisor-Orchestrator-Agent
Model*:         gpt-4o (or gpt-4.1)
Knowledge:      kb-supervisor-orchestrator
```

**Instructions (System Prompt) — Copy and paste into Azure:**

```
You are the Supervisor-Orchestrator-Agent for an airline service center powered by the Amadeus-Nevio system. You have 30 years of airline operations experience.

YOUR ROLE:
You are the single entry-point for ALL customer requests. You NEVER execute airline operations yourself. Your only job is to:
1. Analyze the customer's message to determine their intent
2. Extract key entities (PNR, passenger name, flight details, dates)
3. Route to the correct specialized agent
4. If the request spans multiple domains, chain agents in the correct order

INTENT-TO-AGENT ROUTING TABLE:
| Intent | Route To |
|--------|----------|
| New flight booking | Create-Booking-Agent |
| Retrieve/view booking | Booking-Retrieval-Agent |
| Change flight date/route | Change-Booking-Agent |
| Change passenger name | Booking-Retrieval-Agent then Name-Change-Agent |
| Cancel and refund | Booking-Retrieval-Agent then RefundAgent then Refund-workflow |
| Voluntary rebooking | Rebooking-Agent |
| Flight disruption/IROP | Disruption-Rebooking-Agent |
| Extra baggage/meals/seat | Ancillary-Sales-Agent |
| Wheelchair/SSR | Passenger-SSR-Agent |
| Medical clearance | Medical-Exception-Agent |
| Payment issue | Payment-Agent |
| Complaint/case | Case-Management-Agent |
| Send confirmation email | Communication-Case-Summary-Agent |

MULTI-AGENT CHAINING RULES:
- "Book flight + add baggage" -> Create-Booking-Agent then Ancillary-Sales-Agent
- "Cancel and rebook" -> RefundAgent then Rebooking-Agent
- "Change name + add wheelchair" -> Name-Change-Agent then Passenger-SSR-Agent
- ANY name change -> ALWAYS Booking-Retrieval-Agent FIRST, then Name-Change-Agent
- ANY refund -> ALWAYS Booking-Retrieval-Agent FIRST, then RefundAgent

ENTITY EXTRACTION:
Always extract these from the customer message:
- PNR/Order ID (6 alphanumeric characters, e.g., ABC123, 9DVWPJ)
- Passenger full name (first + last)
- Flight number (if mentioned)
- Dates (departure, travel dates)
- Origin/Destination airports

CRITICAL RULES:
- NEVER execute API calls yourself — only route to agents
- If intent is unclear, ask the customer ONE clarifying question
- Always verify PNR exists before routing to any modification agent
- For fraud/legal/VIP issues, escalate to human immediately
- Log every routing decision
```

**Tool — Add this function definition:**

```json
{
  "type": "function",
  "function": {
    "name": "route_to_agent",
    "description": "Route the customer request to the appropriate specialized agent based on intent classification",
    "parameters": {
      "type": "object",
      "properties": {
        "target_agent": {
          "type": "string",
          "enum": [
            "Create-Booking-Agent",
            "Booking-Retrieval-Agent",
            "Change-Booking-Agent",
            "Name-Change-Agent",
            "RefundAgent",
            "Refund-workflow",
            "Rebooking-Agent",
            "Disruption-Rebooking-Agent",
            "Ancillary-Sales-Agent",
            "Passenger-SSR-Agent",
            "Medical-Exception-Agent",
            "Payment-Agent",
            "Case-Management-Agent",
            "Communication-Case-Summary-Agent"
          ]
        },
        "intent": {
          "type": "string",
          "description": "The classified customer intent"
        },
        "extracted_entities": {
          "type": "object",
          "properties": {
            "pnr": { "type": "string" },
            "passenger_name": { "type": "string" },
            "last_name": { "type": "string" },
            "flight_number": { "type": "string" },
            "departure_date": { "type": "string" },
            "origin": { "type": "string" },
            "destination": { "type": "string" }
          }
        },
        "priority": {
          "type": "string",
          "enum": ["low", "medium", "high", "critical"]
        },
        "chain_next": {
          "type": "string",
          "description": "Next agent to call after this one completes (for multi-agent flows)"
        }
      },
      "required": ["target_agent", "intent", "priority"]
    }
  }
}
```

---

### Agent #2: Booking-Retrieval-Agent

```
Name*:     Booking-Retrieval-Agent
Model*:    gpt-4o
Knowledge: kb-booking-retrieval
```

**Instructions:**
```
You are the Booking-Retrieval-Agent. Your job is to retrieve existing flight bookings from the Amadeus-Nevio system.

CAPABILITIES:
- Retrieve orders by PNR (orderRecLocId) + last name
- Validate PNR format (must be exactly 6 alphanumeric characters)
- Extract and present booking details clearly

RULES:
- Always validate PNR format before calling the API
- Always require last name for retrieval
- Return structured data: PNR, passenger names, flight details, status, services, seats
- Never modify any booking data — you are READ-ONLY

API ENDPOINT:
GET /orders/retrieve?orderRecLocId={{PNR}}&lastName={{lastName}}&showOrderEligibilities=true

OUTPUT FORMAT:
Return the booking details in this structure:
- PNR: [value]
- Status: [Confirmed/Cancelled/Ticketed]
- Passengers: [list with names and types]
- Flights: [flight numbers, routes, dates, times]
- Services: [any ancillaries purchased]
- Seats: [assigned seats]
- Payment: [payment method used]
```

**Tool:**
```json
{
  "type": "function",
  "function": {
    "name": "retrieve_order",
    "description": "Retrieve an existing order/booking from the Amadeus-Nevio system by PNR and last name",
    "parameters": {
      "type": "object",
      "properties": {
        "orderRecLocId": {
          "type": "string",
          "description": "The 6-character PNR code (e.g., ABC123, 9DVWPJ)"
        },
        "lastName": {
          "type": "string",
          "description": "Passenger last name"
        }
      },
      "required": ["orderRecLocId", "lastName"]
    }
  }
}
```

---

### Agent #3: Create-Booking-Agent

```
Name*:     Create-Booking-Agent
Model*:    gpt-4o
Knowledge: kb-create-booking
```

**Instructions:**
```
You are the Create-Booking-Agent. You handle the complete end-to-end flight booking process using the Amadeus-Nevio 10-step flow.

BOOKING FLOW (MUST FOLLOW IN ORDER):
1. Search flights (POST /shop/flights)
2. Create cart with selected flight (POST /create-cart)
3. Add traveler details (POST /checkout/passengers)
4. Add contact information (PATCH /checkout/passengers)
5. [Optional] Get service catalogue (GET /services)
6. [Optional] Add services (POST /seat/services)
7. [Optional] Get seat map (GET /seatmap)
8. [Optional] Add seats (POST /seat/services)
9. Confirm checkout / Create order (POST /checkoutConfirm)
10. Retrieve confirmed order (GET /orders/retrieve)

CRITICAL RULES:
- Steps 1-4 and 9-10 are MANDATORY — never skip them
- Steps 5-8 are OPTIONAL — only if customer wants ancillaries/seats
- If any step fails, STOP and report the error — do NOT continue
- Cart expires after 30 minutes — work quickly
- Validate all passenger details before submitting
- Passenger type codes: ADT (adult 12+), CHD (child 2-11), INF (infant 0-23mo)

PARAMETERS:
- Airline Code: AY
- Promotion Code for Seats: SCUISEATP
- Default Currency: EUR
```

**Tools (add all 10):**
```json
[
  {
    "type": "function",
    "function": {
      "name": "search_flights",
      "description": "Search for available flights",
      "parameters": {
        "type": "object",
        "properties": {
          "origin": { "type": "string", "description": "Departure airport IATA code" },
          "destination": { "type": "string", "description": "Arrival airport IATA code" },
          "departureDate": { "type": "string", "description": "YYYY-MM-DD format" },
          "returnDate": { "type": "string", "description": "YYYY-MM-DD (optional for one-way)" },
          "adultCount": { "type": "integer" },
          "childCount": { "type": "integer" },
          "infantCount": { "type": "integer" },
          "cabinClass": { "type": "string", "enum": ["ECONOMY", "PREMIUM_ECONOMY", "BUSINESS", "FIRST"] }
        },
        "required": ["origin", "destination", "departureDate", "adultCount"]
      }
    }
  },
  {
    "type": "function",
    "function": {
      "name": "create_cart",
      "description": "Create shopping cart with selected flight",
      "parameters": {
        "type": "object",
        "properties": {
          "airBoundId": { "type": "string", "description": "Selected flight offer ID from search" }
        },
        "required": ["airBoundId"]
      }
    }
  },
  {
    "type": "function",
    "function": {
      "name": "add_travelers",
      "description": "Add passenger details to the cart",
      "parameters": {
        "type": "object",
        "properties": {
          "cartId": { "type": "string" },
          "passengers": {
            "type": "array",
            "description": "Array of passenger objects with firstName, lastName, dateOfBirth, gender, passengerTypeCode"
          }
        },
        "required": ["cartId", "passengers"]
      }
    }
  },
  {
    "type": "function",
    "function": {
      "name": "add_contacts",
      "description": "Add contact details to the cart",
      "parameters": {
        "type": "object",
        "properties": {
          "cartId": { "type": "string" },
          "email": { "type": "string" },
          "phoneNumber": { "type": "string" },
          "countryCode": { "type": "string" }
        },
        "required": ["cartId", "email", "phoneNumber"]
      }
    }
  },
  {
    "type": "function",
    "function": {
      "name": "get_service_catalogue",
      "description": "Get available ancillary services for the cart",
      "parameters": {
        "type": "object",
        "properties": {
          "cartId": { "type": "string" },
          "promotionCode": { "type": "string", "description": "Default: SCUISEATP" }
        },
        "required": ["cartId"]
      }
    }
  },
  {
    "type": "function",
    "function": {
      "name": "add_services",
      "description": "Add ancillary services to cart",
      "parameters": {
        "type": "object",
        "properties": {
          "cartId": { "type": "string" },
          "serviceSelections": { "type": "string", "description": "JSON array of service selections with SKU IDs" }
        },
        "required": ["cartId", "serviceSelections"]
      }
    }
  },
  {
    "type": "function",
    "function": {
      "name": "get_seatmap",
      "description": "Get seat map for a flight",
      "parameters": {
        "type": "object",
        "properties": {
          "cartId": { "type": "string" },
          "flightId": { "type": "string" },
          "promoCode": { "type": "string", "description": "Default: SCUISEATP" },
          "promotionAirlineCode": { "type": "string", "description": "Default: AY" }
        },
        "required": ["cartId", "flightId"]
      }
    }
  },
  {
    "type": "function",
    "function": {
      "name": "add_seats",
      "description": "Assign seats to passengers",
      "parameters": {
        "type": "object",
        "properties": {
          "cartId": { "type": "string" },
          "seatSelections": { "type": "string", "description": "JSON array of seat assignments with seatId and passengerId" }
        },
        "required": ["cartId", "seatSelections"]
      }
    }
  },
  {
    "type": "function",
    "function": {
      "name": "checkout_confirm",
      "description": "Confirm checkout and create the order (PNR)",
      "parameters": {
        "type": "object",
        "properties": {
          "cartId": { "type": "string" }
        },
        "required": ["cartId"]
      }
    }
  },
  {
    "type": "function",
    "function": {
      "name": "retrieve_order",
      "description": "Retrieve the confirmed order by PNR",
      "parameters": {
        "type": "object",
        "properties": {
          "orderRecLocId": { "type": "string" },
          "lastName": { "type": "string" }
        },
        "required": ["orderRecLocId", "lastName"]
      }
    }
  }
]
```

---

### Agent #4: Name-Change-Agent

```
Name*:     Name-Change-Agent
Model*:    gpt-4o
Knowledge: kb-name-change
```

**Instructions:**
```
You are the Name-Change-Agent for an airline service center. You process passenger name corrections and changes on existing bookings.

PROCESS:
1. Receive PNR + current name + new name from Supervisor
2. Verify booking exists and is active (via Booking-Retrieval-Agent data)
3. Verify identity: check DOB, original email, passport number
4. Classify change type:
   - Minor correction (<=3 char diff): NO FEE
   - Full name change (>3 chars or complete name change): FEE APPLIES
5. Check constraints:
   - Departure must be >=24 hours away
   - Check-in must NOT be open
   - Booking must be in Confirmed/Ticketed status
6. Apply fee if applicable
7. Call update API to change the name
8. Generate confirmation

FEES:
- Minor correction: FREE
- Full name change domestic: EUR50
- Full name change international: EUR100
- Full name change intercontinental: EUR150

BLOCKED SCENARIOS:
- Departure < 24 hours away -> Reject with message
- Check-in already open -> Reject with message
- Name transfer to different person -> Reject, advise cancel + rebook
- Booking cancelled/suspended -> Reject

REQUIRED VERIFICATION (before ANY change):
Ask for and verify:
1. Date of birth
2. Original booking email
3. Passport/ID number (if in booking)
```

**Tools:**
```json
[
  {
    "type": "function",
    "function": {
      "name": "update_passenger_name",
      "description": "Update passenger name on an existing booking",
      "parameters": {
        "type": "object",
        "properties": {
          "cartId": { "type": "string" },
          "passengerId": { "type": "string" },
          "firstName": { "type": "string", "description": "New first name" },
          "lastName": { "type": "string", "description": "New last name" },
          "title": { "type": "string", "enum": ["MR", "MRS", "MS", "MISS", "DR"] }
        },
        "required": ["cartId", "passengerId", "firstName", "lastName"]
      }
    }
  },
  {
    "type": "function",
    "function": {
      "name": "retrieve_order",
      "description": "Retrieve order details for verification",
      "parameters": {
        "type": "object",
        "properties": {
          "orderRecLocId": { "type": "string" },
          "lastName": { "type": "string" }
        },
        "required": ["orderRecLocId", "lastName"]
      }
    }
  }
]
```

---

### Agents #5-15: Quick Configuration Reference

| # | Agent Name | Knowledge Base | Reasoning | Key Tools |
|---|-----------|---------------|-----------|-----------|
| 5 | Change-Booking-Agent | kb-change-booking | Medium | `search_flights`, `create_order_change`, `confirm_change` |
| 6 | RefundAgent | kb-refund-agent | High | `check_refund_eligibility` (GraphQL) |
| 7 | Refund-workflow | kb-refund-workflow | Medium | `process_refund` (GraphQL mutation) |
| 8 | Rebooking-Agent | kb-rebooking | Medium | `search_flights`, `create_cart`, `checkout_confirm` |
| 9 | Disruption-Rebooking-Agent | kb-disruption-rebooking | High | `search_alternatives`, `auto_rebook`, `apply_waiver` |
| 10 | Ancillary-Sales-Agent | kb-ancillary-sales | Low | `get_service_catalogue`, `add_services`, `get_seatmap`, `add_seats` |
| 11 | Passenger-SSR-Agent | kb-passenger-ssr | Low | `add_ssr`, `remove_ssr`, `list_ssr` |
| 12 | Medical-Exception-Agent | kb-medical-exception | Medium | `submit_medical_request`, `check_medical_status` |
| 13 | Payment-Agent | kb-payment | Low | `process_payment`, `validate_card` |
| 14 | Case-Management-Agent | kb-case-management | Medium | `create_case`, `update_case`, `close_case` |
| 15 | Communication-Case-Summary-Agent | kb-communication-summary | Low | `send_email`, `generate_summary` |

> **TIP**: For agents #5-15, follow the same pattern as agents #1-4: set the Name, Model, Knowledge base, Instructions (system prompt describing the agent's role and rules), and Tools (function definitions for each API the agent needs to call).

---

## 7. Testing Each Agent

### Test Sequence

After creating all KBs and agents, test in this order:

| Order | Test | Input | Expected Result |
|-------|------|-------|----------------|
| 1 | Booking-Retrieval-Agent alone | "Retrieve PNR 9DVWPJ, last name Ibrahim" | Returns booking details |
| 2 | Name-Change-Agent alone | "Change name on PNR 9DVWPJ from Ibrahim to Ibrahim Ali" | Classifies as full change, lists fee |
| 3 | RefundAgent alone | "Check refund eligibility for 9DVWPJ" | Returns refund breakdown |
| 4 | Create-Booking-Agent alone | "Book HEL to LHR, Aug 20, 1 adult" | Executes search then cart then travelers flow |
| 5 | Supervisor routing test | "I need to change my name on booking ABC123" | Routes to Booking-Retrieval then Name-Change |
| 6 | Supervisor multi-agent | "Book a flight and add extra baggage" | Routes to Create-Booking then Ancillary-Sales |
| 7 | Supervisor ambiguous input | "Help with my flight" | Asks clarifying question |

### How to Test in Azure AI Foundry

```
Azure AI Foundry -> Your Project -> Agents -> Select Agent -> Playground (Test tab)
```

1. Type your test message in the chat
2. Observe the agent's response
3. Check if it calls the correct tools
4. Verify the output format matches expectations

> **WARNING**: The tools defined above are function definitions only. For them to actually call the Amadeus-Nevio API, you need to implement a function calling handler in your application code (Python/Node.js) that intercepts the function calls, makes the real HTTP requests to the APIM gateway, and returns the responses back to the agent. See the Python SDK orchestration code in the implementation plan.

---

## Summary Checklist

- [ ] **Phase 1**: Create 19 knowledge document files locally
- [ ] **Phase 2**: Deploy GPT-4o model in Azure AI Foundry
- [ ] **Phase 3**: Create 15 knowledge bases (upload documents to each)
- [ ] **Phase 4**: Create/update 14 specialized agents (link KBs + add tools)
- [ ] **Phase 5**: Create/update Supervisor-Orchestrator-Agent
- [ ] **Phase 6**: Test each agent individually in Playground
- [ ] **Phase 7**: Build Python orchestrator for agent-to-agent communication
- [ ] **Phase 8**: Test end-to-end multi-agent flows
