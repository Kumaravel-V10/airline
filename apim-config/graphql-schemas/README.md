# GraphQL Schemas for Azure APIM

This directory contains GraphQL SDL schema files used to import **Pass-through GraphQL** APIs into Azure API Management (APIM).

---

## Schema Inventory

| Schema File | APIM API Name | Backend Endpoint | Notes |
|---|---|---|---|
| `cancel-and-refund.graphql` | Cancel & Refund API | `https://<backend-host>/cancel-refund/graphql` | 2 operations (1 Query, 1 Mutation) |
| _(introspection)_ | appConfig API | `https://<backend-host>/appconfig/graphql` | ~77 operations – imported via introspection |

> **Note — appConfig API:**
> The appConfig GraphQL API exposes approximately **77 operations**. Writing and maintaining an SDL file by hand for that many operations is impractical and error-prone. Instead, import the appConfig API into APIM using the **introspection endpoint** (`POST` the introspection query to the backend or let APIM auto-discover the schema). APIM will pull the full schema automatically.

---

## How to Import a Pass-through GraphQL API into APIM

Follow these steps to register a GraphQL schema as a Pass-through API in Azure API Management.

### Prerequisites

- An Azure API Management instance (Developer tier or higher).
- The backend GraphQL service is deployed and reachable from APIM.
- You have the `.graphql` SDL file (from this directory) or an introspection endpoint URL.

### Step-by-Step Instructions

1. **Open the Azure Portal** and navigate to your **API Management** instance.

2. **Add a new API**
   - Go to **APIs** in the left menu.
   - Click **+ Add API**.
   - Under _Define a new API_, select **GraphQL**.

3. **Choose Pass-through**
   - Select **Pass-through GraphQL** (APIM proxies requests to the backend without resolver logic).

4. **Provide API details**
   - **Display name**: e.g., `Cancel & Refund API`
   - **Name** (URL slug): e.g., `cancel-and-refund`
   - **GraphQL API endpoint** (backend URL): the upstream GraphQL service URL.

5. **Upload the schema**
   - For SDL-based import: click **Select a file** and upload the `.graphql` schema file from this directory.
   - For introspection-based import (e.g., appConfig): enter the introspection endpoint URL and let APIM discover the schema automatically.

6. **Configure products & subscriptions**
   - Assign the API to an APIM **Product** (e.g., _Unlimited_, _Starter_, or a custom product).
   - Enable or disable **Subscription required** as needed.

7. **Set inbound policies** (optional but recommended)
   - Add authentication policies (e.g., `validate-jwt`, `set-header` for API keys).
   - Add rate limiting or quota policies if needed.
   - Example policy snippet:
     ```xml
     <inbound>
         <base />
         <set-header name="Ocp-Apim-Subscription-Key" exists-action="delete" />
         <set-backend-service base-url="https://<backend-host>/cancel-refund/graphql" />
     </inbound>
     ```

8. **Save and test**
   - Click **Save**.
   - Go to the **Test** tab in APIM.
   - Run a sample query to verify end-to-end connectivity.

---

## Updating a Schema

If the backend GraphQL API changes:

1. **SDL-based APIs**: Update the `.graphql` file in this directory, then re-upload it via the APIM portal (API → Schema tab → Upload).
2. **Introspection-based APIs**: Re-run the import from the introspection endpoint to pick up the latest schema.

---

## Directory Structure

```
graphql-schemas/
├── README.md                      # This file
├── cancel-and-refund.graphql      # SDL schema for Cancel & Refund API
└── (future schemas go here)
```
