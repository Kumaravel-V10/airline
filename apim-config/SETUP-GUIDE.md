# ✈️ Azure APIM MCP Server — Complete Setup Guide

> **Purpose**: Step-by-step instructions to set up Azure API Management as an MCP Server for the Airline Service Center Multi-Agent System.
>
> **Time Required**: ~8-10 hours
>
> **Prerequisites**: Azure subscription, APIM instance (Developer/Basic v2/Standard v2/Premium v2 tier), Azure AI Foundry project with agents deployed.

---

## Table of Contents

1. [Prerequisites & Pre-Flight Checks](#1-prerequisites--pre-flight-checks)
2. [Phase 1: Import REST API into APIM](#2-phase-1-import-rest-api-into-apim)
3. [Phase 2: Import GraphQL APIs into APIM](#3-phase-2-import-graphql-apis-into-apim)
4. [Phase 3: Configure APIM Policies & Security](#4-phase-3-configure-apim-policies--security)
5. [Phase 4: Create the MCP Server](#5-phase-4-create-the-mcp-server)
6. [Phase 5: Connect Agents to MCP Server](#6-phase-5-connect-agents-to-mcp-server)
7. [Phase 6: Testing & Verification](#7-phase-6-testing--verification)
8. [Troubleshooting](#8-troubleshooting)

---

## 1. Prerequisites & Pre-Flight Checks

### 1.1 Verify APIM Tier

MCP Server feature requires one of these tiers:
- ✅ Developer
- ✅ Basic v2
- ✅ Standard v2
- ✅ Premium v2
- ❌ Consumption (NOT supported)
- ❌ Basic v1 (NOT supported)

**How to check:**
```
Azure Portal → API Management services → nevioservicecenterapim → Overview
→ Check "Pricing tier" field
```

If on an unsupported tier, upgrade:
```
Settings → Scale and pricing → Select supported tier → Save
```

### 1.2 Verify Required Files Are Ready

Ensure these config files are available (created by this project):

```
airline agent/
└── apim-config/
    ├── nevio-service-center-openapi.yaml     ← OpenAPI spec for REST API import
    ├── SETUP-GUIDE.md                        ← This guide
    ├── graphql-schemas/
    │   ├── cancel-and-refund.graphql          ← GraphQL SDL for refund API
    │   └── README.md                          ← Import instructions
    └── policies/
        ├── global-inbound-policy.xml          ← Global auth + rate limiting
        ├── search-flights-policy.xml          ← REST→GraphQL transform
        ├── create-cart-policy.xml             ← REST→GraphQL transform
        ├── retrieve-order-policy.xml          ← REST→GraphQL transform
        ├── checkout-confirm-policy.xml        ← REST→GraphQL transform
        └── graphql-validation-policy.xml      ← GraphQL request validation
```

### 1.3 Collect Required Values

| Value | Where to Find | Example |
|-------|--------------|---------|
| APIM Instance Name | Azure Portal → APIM | `nevioservicecenterapim` |
| APIM Gateway URL | APIM → Overview | `https://nevioservicecenterapim.azure-api.net` |
| Azure AD Tenant ID | Azure Portal → Entra ID → Overview | `xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx` |
| Agent App Registration ID | Entra ID → App registrations | `xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx` |
| Backend JWT Token | From `/token` endpoint | (JWT string) |
| Amadeus Token | From `/token/amadeus` endpoint | (JWT string) |
| GraphQL Backend URL | Backend team | `https://<backend-host>` |

---

## 2. Phase 1: Import REST API into APIM

> **Key Insight**: All Nevio endpoints are actually GraphQL-over-POST, but we create REST-style facades in APIM. The APIM policies handle the REST-to-GraphQL body transformation.

### Step 1: Navigate to API Import

```
Azure Portal
  → API Management services
    → nevioservicecenterapim
      → APIs (left sidebar, under "APIs" section)
        → + Add API
```

### Step 2: Select OpenAPI Import

1. In the "Add API" panel, click **OpenAPI**
2. Toggle to **Full** view (not Basic)
3. Click **Select a file** and upload:
   ```
   apim-config/nevio-service-center-openapi.yaml
   ```

### Step 3: Configure API Settings

| Field | Value |
|-------|-------|
| **Display name** | `Nevio Service Center API` |
| **Name** | `nevio-service-center` |
| **Description** | `Airline service center REST API - shopping, booking, orders, services` |
| **API URL suffix** | _(leave empty)_ |
| **Base URL** | `https://nevioservicecenterapim.azure-api.net` |
| **Tags** | `airline`, `booking`, `nevio` |
| **Products** | Select your product (or create one: `airline-mcp`) |

### Step 4: Click Create

After import, you should see all operations listed:

```
✅ POST /token                    → getJwtToken
✅ POST /token/amadeus            → getAmadeusToken
✅ POST /searchpanel              → getSearchPanel
✅ POST /shop/flights             → searchFlights
✅ POST /create-cart              → createCart
✅ POST /checkout/passengers      → addUpdatePassengers
✅ POST /cart/retrieve            → retrieveCart
✅ POST /services                 → getServiceCatalogue
✅ POST /seat/services            → manageSeatServices
✅ POST /seatmap                  → getSeatMap
✅ POST /checkoutConfirm          → checkoutConfirm
✅ POST /orders/retrieve          → retrieveOrder
```

### Step 5: Apply Per-Operation Policies

For each operation that needs REST→GraphQL transformation:

```
APIs → Nevio Service Center API → Select operation (e.g., "searchFlights")
  → Inbound processing → </> (Policy code editor)
    → Paste the content from the corresponding policy file
    → Save
```

| Operation | Policy File to Apply |
|-----------|---------------------|
| `searchFlights` | `policies/search-flights-policy.xml` |
| `createCart` | `policies/create-cart-policy.xml` |
| `retrieveOrder` | `policies/retrieve-order-policy.xml` |
| `checkoutConfirm` | `policies/checkout-confirm-policy.xml` |

> **TIP**: For operations not listed above (like `getServiceCatalogue`, `manageSeatServices`), create similar policies following the same pattern. See the existing policy files as templates.

---

## 3. Phase 2: Import GraphQL APIs into APIM

### 3A: Cancel and Refund API

#### Step 1: Navigate to API Import

```
APIs → + Add API → GraphQL
```

#### Step 2: Select Pass-through

Click **Pass-through GraphQL** (not Synthetic).

#### Step 3: Fill Configuration

| Field | Value |
|-------|-------|
| **Display name** | `Cancel and Refund API` |
| **Name** | `cancel-and-refund` |
| **GraphQL API endpoint** | `https://<your-backend-url>/cancelAndRefund` |
| **Upload schema** | Upload `apim-config/graphql-schemas/cancel-and-refund.graphql` |
| **API URL suffix** | `cancelAndRefund` |
| **Subscription required** | Yes |

#### Step 4: Click Create

After import, verify:
```
✅ Query: RetriveOrderRefundEligiblities
✅ Mutation: CancellationAndRefund
```

#### Step 5: Apply Validation Policy

```
APIs → Cancel and Refund API → All operations
  → Inbound processing → </> Policy editor
    → Paste content from policies/graphql-validation-policy.xml
    → Save
```

### 3B: App Config API

```
APIs → + Add API → GraphQL
```

| Field | Value |
|-------|-------|
| **Display name** | `App Configuration API` |
| **Name** | `app-config` |
| **GraphQL API endpoint** | `https://<your-backend-url>/appConfig` |
| **Import schema** | ✅ **Enable introspection** (auto-discover 77+ operations) |
| **API URL suffix** | `appConfig` |

Click **Create**.

---

## 4. Phase 3: Configure APIM Policies & Security

### 4.1 Create Named Values

```
API Management → nevioservicecenterapim
  → Named values (left sidebar)
    → + Add
```

Create these Named Values:

| # | Name | Type | Value / Source |
|---|------|------|----------------|
| 1 | `nevio-jwt-token` | 🔒 Key Vault Secret | Key Vault reference |
| 2 | `amadeus-token` | 🔒 Key Vault Secret | Key Vault reference |
| 3 | `azure-ad-tenant-id` | Plain text | Your tenant ID |
| 4 | `agent-client-id` | Plain text | App registration client ID |

> **IMPORTANT**: For production, use Key Vault references for tokens. This requires APIM managed identity with Key Vault access.

### 4.2 Apply Global Policy

```
APIs → All APIs → Inbound processing → </> Policy editor
  → Paste content from policies/global-inbound-policy.xml
  → Save
```

> **WARNING**: The global policy applies to ALL APIs. If you have other APIs, apply at individual API level instead.

### 4.3 Create a Product

```
Products (left sidebar) → + Add
```

| Field | Value |
|-------|-------|
| **Display name** | `Airline MCP Tools` |
| **Id** | `airline-mcp-tools` |
| **State** | Published |
| **Requires subscription** | Yes |
| **APIs** | ✅ All three APIs |

### 4.4 Create a Subscription

```
Subscriptions → + Add subscription
```

| Field | Value |
|-------|-------|
| **Name** | `ai-agents-subscription` |
| **Scope** | Product → Airline MCP Tools |
| **State** | Active |

**Save the Primary key** — needed for testing.

---

## 5. Phase 4: Create the MCP Server

### 5.1 Create MCP Server for Booking APIs

```
API Management → nevioservicecenterapim
  → MCP Servers (left sidebar)
    → + Create MCP server
```

| Field | Value |
|-------|-------|
| **Type** | Expose an API as an MCP server |
| **Select API** | `Nevio Service Center API` |
| **MCP server name** | `airline-booking-tools` |

**Select these operations as tools:**

| ✅ | Tool Name | Description |
|----|-----------|-------------|
| ✅ | `searchFlights` | Search available flights by origin, destination, dates, passengers, cabin class |
| ✅ | `createCart` | Create shopping cart with selected flight offer |
| ✅ | `addUpdatePassengers` | Add/update passenger details and contacts |
| ✅ | `retrieveCart` | Retrieve cart contents with pricing |
| ✅ | `getServiceCatalogue` | Get available ancillary services with pricing |
| ✅ | `manageSeatServices` | Add/remove seats and services |
| ✅ | `getSeatMap` | Get seat map layout for a flight |
| ✅ | `checkoutConfirm` | Finalize booking, issue PNR |
| ✅ | `retrieveOrder` | Retrieve confirmed order by PNR |
| ✅ | `getSearchPanel` | Get search panel configuration |
| ❌ | `getJwtToken` | _(Exclude — handled by APIM policy)_ |
| ❌ | `getAmadeusToken` | _(Exclude — handled by APIM policy)_ |

Click **Create**.

### 5.2 Create MCP Server for Refund APIs

```
MCP Servers → + Create MCP server
```

| Field | Value |
|-------|-------|
| **Select API** | `Cancel and Refund API` |
| **MCP server name** | `airline-refund-tools` |

| ✅ | Tool Name | Description |
|----|-----------|-------------|
| ✅ | `checkRefundEligibility` | Check refund eligibility, returns amounts and refundProposalIds |
| ✅ | `executeCancellationRefund` | Execute cancellation using refundProposalIds |

Click **Create**.

### 5.3 Note MCP Endpoints

After creation:
```
Booking Tools: https://nevioservicecenterapim.azure-api.net/mcp
Refund Tools:  https://nevioservicecenterapim.azure-api.net/mcp
Transport:     Streamable HTTP
```

---

## 6. Phase 5: Connect Agents to MCP Server

### 6.1 Add MCP Tool to Each Agent

Repeat for each agent:

```
Azure AI Foundry → Project → Agents → Select agent
  → Tools → + Add Tool → MCP Server
  → MCP Server URL: https://nevioservicecenterapim.azure-api.net/mcp
  → Authentication: Managed Identity or API Key
  → Select relevant tools (see matrix below)
  → Save
```

### 6.2 Agent-to-Tool Mapping

| # | Agent | MCP Tools |
|---|-------|-----------|
| 1 | **Supervisor-Orchestrator** | `retrieveOrder` |
| 2 | **Create-Booking** | `searchFlights`, `createCart`, `addUpdatePassengers`, `getServiceCatalogue`, `manageSeatServices`, `getSeatMap`, `checkoutConfirm`, `retrieveOrder`, `getSearchPanel` |
| 3 | **Booking-Retrieval** | `retrieveOrder`, `retrieveCart` |
| 4 | **Name-Change** | `retrieveOrder`, `addUpdatePassengers` |
| 5 | **Refund** | `retrieveOrder`, `checkRefundEligibility` |
| 6 | **Refund-Workflow** | `executeCancellationRefund` |
| 7 | **Change-Booking** | `retrieveOrder`, `searchFlights`, `getServiceCatalogue` |
| 8 | **Rebooking** | `retrieveOrder`, `searchFlights`, `createCart`, `addUpdatePassengers`, `checkoutConfirm` |
| 9 | **Disruption-Rebooking** | `retrieveOrder`, `searchFlights`, `createCart`, `addUpdatePassengers`, `checkoutConfirm` |
| 10 | **Ancillary-Sales** | `retrieveOrder`, `retrieveCart`, `getServiceCatalogue`, `manageSeatServices`, `getSeatMap` |
| 11 | **Passenger-SSR** | `retrieveOrder`, `manageSeatServices` |
| 12 | **Medical-Exception** | `retrieveOrder` |
| 13 | **Payment** | `retrieveOrder`, `checkoutConfirm` |
| 14 | **Case-Management** | `retrieveOrder` |
| 15 | **Communication-Summary** | `retrieveOrder` |

---

## 7. Phase 6: Testing & Verification

### Test 1: MCP Discovery

```bash
curl -X GET "https://nevioservicecenterapim.azure-api.net/mcp" \
  -H "Ocp-Apim-Subscription-Key: <key>" \
  -H "Accept: application/json"
```

### Test 2: Invoke retrieveOrder

```bash
curl -X POST "https://nevioservicecenterapim.azure-api.net/mcp" \
  -H "Ocp-Apim-Subscription-Key: <key>" \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","method":"tools/call","params":{"name":"retrieveOrder","arguments":{"orderId":"9DVWPJ"}},"id":1}'
```

### Test 3: Invoke checkRefundEligibility

```bash
curl -X POST "https://nevioservicecenterapim.azure-api.net/mcp" \
  -H "Ocp-Apim-Subscription-Key: <key>" \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","method":"tools/call","params":{"name":"checkRefundEligibility","arguments":{"input":{"targetAction":"cancelAndRefund","orderId":"9DVWPJ","lastName":"Smith","isEligible":true}}},"id":2}'
```

### Test 4: End-to-End Agent Flow

```python
route_customer_request("I want to cancel booking 9DVWPJ. Last name Smith.")
# Expected: Supervisor → Refund-Agent → MCP:retrieveOrder → MCP:checkRefundEligibility
```

### Verification Checklist

| # | Check | Status |
|---|-------|--------|
| 1 | All 3 APIs visible in APIM | ☐ |
| 2 | 12 REST operations imported | ☐ |
| 3 | 2 GraphQL operations imported | ☐ |
| 4 | Named Values configured (4) | ☐ |
| 5 | Global policy applied | ☐ |
| 6 | MCP Servers created (2) | ☐ |
| 7 | MCP discovery returns tools | ☐ |
| 8 | MCP tool invocation works | ☐ |
| 9 | Agents see MCP tools | ☐ |
| 10 | End-to-end flow works | ☐ |

---

## 8. Troubleshooting

| Issue | Cause | Fix |
|-------|-------|-----|
| MCP Servers not visible | Wrong APIM tier or preview not enabled | Upgrade tier or enable preview in Settings → Features |
| 401 Unauthorized | Invalid token/subscription key | Verify `Ocp-Apim-Subscription-Key` header |
| GraphQL errors in response | REST→GraphQL transform mismatch | Check APIM traces, compare with Postman collection |
| Agent can't discover tools | Wrong MCP URL or auth | Test URL with curl, verify managed identity |
| 429 Rate limit | Too many agent calls | Increase rate limit in global policy |
| Empty response from backend | Named Value not set | Verify `nevio-jwt-token` Named Value has valid token |
