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
