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
