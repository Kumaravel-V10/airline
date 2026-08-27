# Payment Processing Guide

**Document ID:** KB-PAY-001  
**Version:** 3.0  
**Effective Date:** 01 March 2026  
**Last Reviewed:** 15 July 2026  
**Owner:** Finance & Payment Operations Division

---

## 1. Overview

This document provides comprehensive guidance on payment processing for all airline transactions, including ticket purchases, ancillary services, change fees, and refunds. All customer service agents must follow these procedures to ensure secure, accurate, and compliant payment handling.

---

## 2. Supported Payment Methods

### 2.1 Credit & Debit Cards

| Card Type | Accepted | Surcharge | Notes |
|-----------|----------|-----------|-------|
| **Visa** (Credit & Debit) | ✅ Yes | None | All Visa cards worldwide |
| **Mastercard** (Credit & Debit) | ✅ Yes | None | All Mastercard cards worldwide |
| **American Express (Amex)** | ✅ Yes | 1.5% surcharge | Surcharge applies to bookings only, not ancillaries |
| **Diners Club** | ✅ Yes | 1.5% surcharge | Limited to certain markets |
| **JCB** | ✅ Yes | None | Primarily for Japan-originating bookings |
| **UnionPay** | ✅ Yes | None | Primarily for China-originating bookings |
| **Discover** | ❌ No | — | Not accepted |

### 2.2 Digital Wallets & Online Payments

| Method | Accepted | Surcharge | Notes |
|--------|----------|-----------|-------|
| **PayPal** | ✅ Yes | None | Available for online bookings and Manage My Booking only. Not available via Contact Centre. |
| **Apple Pay** | ✅ Yes | None | Available on airline app (iOS) and website (Safari) |
| **Google Pay** | ✅ Yes | None | Available on airline app (Android) and website (Chrome) |
| **Klarna** (Buy Now Pay Later) | ✅ Yes | None | Available for bookings >EUR 100. Installments over 3 months. Subject to Klarna credit check. |
| **iDEAL** | ✅ Yes | None | Netherlands only |
| **Bancontact** | ✅ Yes | None | Belgium only |
| **Sofort/Klarna Direct** | ✅ Yes | None | Germany, Austria, Switzerland |

### 2.3 Bank Transfer

| Type | Details |
|------|---------|
| **Availability** | Available for bookings made **more than 14 days** before departure |
| **Processing time** | 3–5 business days |
| **Minimum amount** | EUR 200 |
| **Currency** | EUR only |
| **Bank details** | Provided upon selection of bank transfer at checkout |
| **Reference** | Booking reference (PNR) must be included in the transfer reference |
| **Auto-cancellation** | If payment is not received within **5 business days**, the booking is automatically cancelled |
| **Confirmation** | Booking is confirmed and ticket issued upon receipt of funds |

### 2.4 Travel Vouchers & Credits

| Voucher Type | Details |
|-------------|---------|
| **Compensation voucher** | Issued for EU261 compensation (if accepted by passenger). Value as stated. Valid for 24 months. |
| **Service recovery voucher** | Issued by Customer Relations for service failures. Value as stated. Valid for 12 months. |
| **Refund voucher** | Issued when passenger opts for voucher instead of cash refund. Value = original fare + 20% bonus. Valid for 24 months. |
| **Gift voucher** | Purchasable at airline.com/gift. Values: EUR 25, EUR 50, EUR 100, EUR 250, EUR 500. Valid for 12 months. |

**Voucher Rules:**
- Vouchers can be used for ticket purchases, ancillary services, and seat upgrades.
- Multiple vouchers can be combined in a single transaction.
- If the booking value exceeds the voucher value, the remaining balance can be paid by card or other accepted methods.
- If the voucher value exceeds the booking value, the remaining balance stays on the voucher.
- Vouchers are **non-transferable** (unless gift voucher) and **non-refundable for cash**.
- Voucher codes are 16-character alphanumeric (format: XXXX-XXXX-XXXX-XXXX).

### 2.5 Corporate Billing

| Feature | Details |
|---------|---------|
| **Eligibility** | Companies with a signed corporate agreement and approved credit line |
| **Payment method** | Monthly consolidated invoice |
| **Invoice cycle** | 1st–last day of the month. Invoice issued by the 5th of the following month. |
| **Payment terms** | Net 30 days from invoice date |
| **Late payment** | 1.5% monthly interest on overdue amounts |
| **Credit limit** | Set individually per corporate account (minimum EUR 5,000) |
| **Booking process** | Corporate ID entered at booking. No upfront payment required. |
| **Contact** | corporate-accounts@airline.com / ext. 5100 |

### 2.6 Loyalty Miles Payment

| Feature | Details |
|---------|---------|
| **Award tickets** | Full payment in miles. Taxes and fees in EUR (card payment). |
| **Miles + Cash** | Partial miles, partial cash. Minimum 5,000 miles per transaction. |
| **Ancillaries with miles** | Available for seat selection, extra baggage, lounge access. |
| **Conversion rate** | Varies by product. Displayed at checkout. |

---

## 3. Currency Rules

### 3.1 Default Currency

- The airline's base currency is **EUR (Euro)**.
- All fares are filed and stored in EUR.
- Prices displayed on the website are in the currency of the point-of-sale country.

### 3.2 Multi-Currency Support

| Feature | Details |
|---------|---------|
| **Supported currencies** | EUR, GBP, USD, CHF, SEK, NOK, DKK, PLN, CZK, HUF, RON, BGN, TRY, and more (30+ currencies) |
| **Exchange rate** | IATA BSR (Bank Selling Rate) updated weekly (every Saturday at 00:00 UTC) |
| **Display currency** | Based on the passenger's country of residence or website language selection |
| **Billing currency** | The currency displayed at the time of booking confirmation |
| **Dynamic currency conversion** | Available at airport payment terminals. Passenger can choose to pay in their card's home currency. |

### 3.3 Currency Conversion Rules

- Once a booking is confirmed, the **billing currency is locked** and cannot be changed.
- Refunds are processed in the **original billing currency**.
- If the original payment method is in a different currency, the card issuer's exchange rate applies to the refund.
- For disputes involving currency conversion differences, the IATA BSR at the time of the original transaction is the reference rate.

---

## 4. 3D Secure Authentication

### 4.1 Overview

3D Secure (3DS) is a security protocol for online credit and debit card transactions. The airline supports **3D Secure 2.0** (3DS2) for all card payments.

### 4.2 3DS Authentication Flow

1. Passenger enters card details at checkout.
2. The payment gateway initiates 3DS authentication with the card issuer.
3. The card issuer performs a risk assessment:
   - **Frictionless flow:** Low-risk transactions are automatically approved without additional passenger action.
   - **Challenge flow:** Higher-risk transactions require the passenger to complete additional authentication (OTP via SMS, biometric, bank app confirmation).
4. Upon successful authentication, the payment is processed.
5. If authentication fails, the payment is declined.

### 4.3 3DS Exemptions

The following transactions may be exempted from 3DS challenge:

| Exemption | Condition |
|-----------|-----------|
| **Low value** | Transactions under EUR 30 |
| **Trusted beneficiary** | Passenger has whitelisted the airline with their bank |
| **Recurring payment** | Subsequent payments on a saved card (initial payment requires 3DS) |
| **Corporate cards** | Certain corporate/business cards may be exempt |

### 4.4 Contact Centre Payments

- For payments taken over the phone (MOTO — Mail Order / Telephone Order), 3DS is **not applicable**.
- Instead, agents must follow the **PCI DSS compliance** procedures:
  - Do not ask the passenger to read the full card number aloud; use the IVR (Interactive Voice Response) system for card entry.
  - Never write down card details.
  - Never store card details in the PNR, notes, or any unsecured system.
  - All Contact Centre calls involving payment are recorded and stored securely.

---

## 5. Failed Payment Recovery

### 5.1 Common Payment Failure Reasons

| Error Code | Reason | Resolution |
|-----------|--------|------------|
| **DECLINED** | Card issuer declined the transaction | Ask passenger to contact their bank or try a different card. |
| **INSUFFICIENT_FUNDS** | Not enough balance on the card | Suggest a different card or partial payment (if available). |
| **3DS_FAILED** | 3D Secure authentication failed | Ask passenger to retry or contact their bank to enable 3DS. |
| **EXPIRED_CARD** | Card has expired | Ask for a valid card. |
| **INVALID_CARD** | Card number is invalid | Ask passenger to re-enter card details carefully. |
| **FRAUD_SUSPECTED** | Fraud detection triggered | Escalate to Fraud team (ext. 6100). Do NOT retry. |
| **TIMEOUT** | Payment gateway timeout | Wait 5 minutes and retry. Check if the booking was created (avoid duplicate charges). |
| **CURRENCY_MISMATCH** | Payment currency not supported by card | Offer payment in EUR or suggest a different card. |
| **VELOCITY_LIMIT** | Too many transaction attempts in a short period | Wait 30 minutes before retrying. Maximum 3 attempts per card per hour. |

### 5.2 Payment Recovery Process

1. **Identify the error code** from the payment gateway response.
2. **Communicate clearly** to the passenger:
   - "Your payment could not be processed. The reason given by your bank is [reason]."
   - "No amount has been charged to your card."
3. **Offer alternatives:**
   - Try a different card.
   - Use a different payment method (PayPal, bank transfer).
   - Split the payment across two cards (if system allows).
4. **For bookings with time pressure** (e.g., last-minute), place a **temporary hold** on the booking (valid for 30 minutes) while the passenger resolves the payment issue.
5. **For suspected fraud**, do NOT inform the passenger of fraud suspicion. Simply state: "We are unable to process this payment at this time. Please contact your card issuer." Escalate to Fraud team immediately.
6. **Duplicate charge verification:** If the passenger claims they were charged but the booking was not confirmed, verify in the payment gateway. If a charge exists without a confirmed booking, initiate an **automatic reversal** (processed within 3–5 business days).

---

## 6. Partial Payment Rules

### 6.1 Split Payment

| Feature | Details |
|---------|---------|
| **Availability** | Online and Contact Centre only (not at airport desks) |
| **Maximum splits** | 2 payment methods per transaction |
| **Allowed combinations** | Card + Card, Card + Voucher, Card + PayPal, Voucher + Voucher |
| **Not allowed** | Bank transfer + any other method, PayPal + PayPal |
| **Minimum per method** | EUR 10 per payment method |

### 6.2 Deposit / Hold Payment

- Not available for standard bookings.
- Available for **group bookings** (10+ passengers):
  - 20% deposit at booking.
  - Remaining 80% due **30 days before departure**.
  - If the remaining balance is not paid by the deadline, the booking is automatically cancelled and the deposit is forfeited.

---

## 7. Refund Processing

### 7.1 Refund to Original Payment Method

| Rule | Detail |
|------|--------|
| **Primary rule** | Refunds are processed to the **original payment method** used for the booking. |
| **Card refund** | Refunded to the same card number used for payment. Processing time: 5–10 business days. |
| **PayPal refund** | Refunded to the same PayPal account. Processing time: 3–5 business days. |
| **Bank transfer refund** | Refunded to the originating bank account. Processing time: 7–14 business days. |
| **Voucher refund** | A new voucher is issued with the refund value. Original voucher (if partially used) retains its remaining balance. |
| **Cash refund** | Available at airport ticket offices only, for tickets purchased with cash. Maximum EUR 500 cash refund per transaction. |

### 7.2 Exceptions to Original Payment Method Refund

| Scenario | Alternative Refund Method |
|----------|--------------------------|
| Original card expired or cancelled | Refund to the same card number (banks typically redirect to the new card). If unsuccessful after 30 days, refund by bank transfer upon passenger request with proof of account ownership. |
| Original PayPal account closed | Refund by bank transfer upon passenger request. |
| Third-party payment (someone else paid) | Refund to the original payer's payment method. If the passenger requests refund to their own account, written authorization from the original payer is required. |
| Corporate booking | Refund to the corporate account (monthly credit note). |
| Travel agent booking | Refund to the travel agent's BSP (Billing and Settlement Plan) account. Passenger must contact their travel agent for the refund. |

### 7.3 Refund Processing Timeline

| Refund Type | Processing Time |
|-------------|----------------|
| Involuntary (IROP) – full refund | **7 business days** (EU261 requirement) |
| Voluntary – refundable fare | **14 business days** |
| Tax refund (non-refundable fare) | **30 business days** |
| EU261 compensation payment | **7 business days** from claim approval |
| Ancillary service refund | **14 business days** |
| Duplicate charge reversal | **3–5 business days** |

### 7.4 Refund Amount Calculation

| Fare Family | Refund Amount |
|-------------|---------------|
| **Light** | Taxes only (upon request). Fare is non-refundable. |
| **Classic** | Fare minus cancellation penalty (EUR 75–150 depending on route). Taxes fully refunded. |
| **Flex** | Full fare + taxes. No penalty. |
| **Business Saver** | Full fare + taxes. No penalty. |
| **Business Flex** | Full fare + taxes. No penalty. |

---

## 8. Fraud Prevention

### 8.1 Fraud Indicators

Agents should be alert to the following potential fraud indicators:

| Indicator | Risk Level |
|-----------|-----------|
| Multiple booking attempts with different cards in a short period | High |
| Billing address does not match card-issuing country | Medium |
| One-way ticket to high-risk destination, booked last-minute | Medium |
| Multiple passengers with different surnames on one card | Low–Medium |
| Email address appears randomly generated | Medium |
| Passenger requests ticket to be issued in a different name than the cardholder | High |
| Contact phone number is a VOIP or disposable number | Low |
| Card BIN (first 6 digits) indicates prepaid or virtual card | Low–Medium |

### 8.2 Fraud Escalation

If fraud is suspected:
1. **Do NOT** inform the passenger.
2. **Do NOT** process the booking.
3. Place the booking on **FRAUD HOLD** status.
4. Immediately escalate to the Fraud team (ext. 6100 or fraud@airline.com).
5. Fraud team reviews within **1 hour** (P1 priority).
6. The Fraud team will either:
   - Clear the transaction for processing.
   - Reject the transaction and notify the card issuer.
   - Request additional verification from the passenger (ID document, selfie with card, etc.).

### 8.3 Chargeback Handling

| Step | Action |
|------|--------|
| 1 | Chargeback notification received from the payment processor |
| 2 | Chargeback team reviews within 5 business days |
| 3 | Gather evidence: booking confirmation, check-in records, boarding pass scans, IP address logs |
| 4 | Submit representment (dispute response) within **30 days** |
| 5 | If representment fails, write off the amount and flag the passenger's profile |

---

## 9. PCI DSS Compliance

### 9.1 Agent Obligations

All agents handling payment information must:

- **Never** write down, photograph, or store card details on paper, in PNR remarks, or in unsecured systems.
- **Never** share card details with colleagues verbally or electronically.
- Use only **approved payment entry systems** (IVR for phone payments, secure payment page for online).
- Complete annual **PCI DSS awareness training** (certificate required).
- Report any suspected data breach to the Information Security team immediately (ext. 7000).

### 9.2 Card Data Masking

- In all systems, card numbers are displayed as masked: `**** **** **** 1234` (last 4 digits only).
- CVV/CVC codes are **never** stored in any system.
- Full card details are transmitted via encrypted channels only (TLS 1.2 minimum).

---

*End of Document — KB-PAY-001 v3.0*
