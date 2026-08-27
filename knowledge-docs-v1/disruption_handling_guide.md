# Disruption Handling Guide

**Document ID:** KB-DIS-001  
**Version:** 4.1  
**Effective Date:** 01 March 2026  
**Last Reviewed:** 15 July 2026  
**Owner:** Operations Control Centre & Customer Care Division

---

## 1. Overview

This document provides comprehensive procedures for handling irregular operations (IROP), including flight cancellations, delays, diversions, and denied boarding. All customer-facing staff must follow these procedures to ensure compliance with EU Regulation 261/2004 and airline policies.

---

## 2. IROP (Irregular Operations) Classification

### 2.1 IROP Event Categories

| Code | Category | Description | Examples |
|------|----------|-------------|----------|
| **CXL** | Cancellation | Flight is cancelled and will not operate | Mechanical failure, crew shortage, low load |
| **DLY** | Delay | Flight departs later than scheduled | Weather, ATC, technical, late inbound aircraft |
| **DIV** | Diversion | Flight lands at an airport other than scheduled destination | Weather at destination, medical emergency, security threat |
| **DNB** | Denied Boarding | Passenger is denied boarding due to overbooking | Oversold flight, operational downgrade |
| **DNG** | Downgrade | Passenger is moved to a lower cabin class | Equipment change, seat defect |
| **SCH** | Schedule Change | Flight time changes by more than 2 hours | Network optimization, slot changes |

### 2.2 IROP Cause Codes

| Code | Cause | Airline Controllable? | EU261 Applicable? |
|------|-------|----------------------|-------------------|
| **TC** | Technical / Mechanical | Yes | Yes |
| **CR** | Crew shortage / illness | Yes | Yes |
| **OP** | Operational decision | Yes | Yes |
| **WX** | Weather | No | No (extraordinary) |
| **AT** | ATC restrictions | No | No (extraordinary) |
| **SE** | Security threat | No | No (extraordinary) |
| **ST** | Strike (external) | No | No (extraordinary) |
| **SI** | Strike (internal) | Yes | Yes |
| **MD** | Medical emergency | No | No (extraordinary) |
| **PA** | Passenger-related | No | No |

> **Critical:** The determination of whether an IROP is airline-controllable directly affects passenger compensation rights under EU261/2004. When in doubt, escalate to the IROP Coordinator.

---

## 3. Flight Cancellation Handling

### 3.1 Cancellation Notification Obligations

| Notification Timing | Passenger Rights |
|---------------------|-----------------|
| **>14 days before departure** | Rebooking or full refund. No compensation. |
| **7–14 days before departure** | Rebooking (departure no more than 2hrs earlier, arrival no more than 4hrs later) or full refund + compensation. |
| **<7 days before departure** | Rebooking (departure no more than 1hr earlier, arrival no more than 2hrs later) or full refund + compensation. |
| **Day of departure** | Full rights: rebooking or refund + compensation + care (meals, hotel if overnight). |

### 3.2 Cancellation Procedure

1. **Immediate Actions (within 30 minutes of cancellation decision):**
   - Activate AUTOREB (automatic rebooking engine) for all affected passengers.
   - Send mass notification via SMS, email, and app push notification.
   - Deploy additional staff to the departure gate and service desk.
   - Prepare meal and hotel vouchers.

2. **Passenger Communication:**
   - Inform passengers of their rights under EU261/2004 in writing.
   - Provide the standardized EU261 rights notice (Form EU261-INFO).
   - Offer three options:
     a. Rebooking on the next available flight (same airline or partner).
     b. Rebooking at a later date of the passenger's choosing.
     c. Full refund of the unused ticket (within 7 business days).

3. **Rebooking Priority:**
   - Follow the involuntary rebooking priority list (see Rebooking Policy KB-RBK-001, Section 3.3).
   - For long-haul cancellations, consider rebooking on competitor airlines if no same-airline flights are available within 8 hours.

4. **Documentation:**
   - Record the IROP event code in all affected PNRs.
   - Issue care vouchers with tracking numbers.
   - Log all passenger interactions in the CRM system.

---

## 4. Delay Handling

### 4.1 Delay Thresholds & Care Obligations

| Delay Duration | Short-Haul (<1,500 km) | Medium-Haul (1,500–3,500 km) | Long-Haul (>3,500 km) |
|---------------|------------------------|-------------------------------|------------------------|
| **>2 hours** | Meals & refreshments | Meals & refreshments | Meals & refreshments |
| **>3 hours** | Meals + 2 phone calls/emails | Meals + 2 phone calls/emails | Meals + 2 phone calls/emails |
| **>4 hours** | — | — | Meals + communication + lounge access (if available) |
| **>5 hours** | Right to full refund + return flight if at connecting point | Right to full refund + return flight | Right to full refund + return flight |
| **Overnight delay** | Meals + hotel + transport to/from hotel | Meals + hotel + transport to/from hotel | Meals + hotel + transport to/from hotel |

### 4.2 Meal Voucher Values

| Time of Day | Voucher Value |
|-------------|---------------|
| Breakfast (05:00–10:00) | EUR 8 |
| Lunch (10:00–15:00) | EUR 12 |
| Dinner (15:00–22:00) | EUR 15 |
| Late night (22:00–05:00) | EUR 10 |
| Refreshments (any time) | EUR 5 |

> **Note:** If airport restaurants are closed, the airline must arrange catering or provide packaged meals. Vouchers are redeemable at any participating airport outlet.

### 4.3 Hotel Accommodation

- **Eligibility:** Passengers requiring an overnight stay due to a delay or cancellation where the next available flight is the following day or later.
- **Standard:** Minimum 3-star hotel with breakfast included.
- **Transport:** Free transfer between airport and hotel (shuttle or taxi voucher).
- **Contracted Hotels:** Use the airline's contracted hotel list first. If contracted hotels are fully booked, authorize any nearby hotel up to:
  - EUR 120 per night per room (domestic/short-haul)
  - EUR 150 per night per room (medium/long-haul)
- **Family Considerations:** Families with children under 12 should be given priority for hotel rooms. Provide connecting rooms where available.

### 4.4 Delay Procedure

1. At the **30-minute mark**: Announce the delay and estimated new departure time.
2. At the **1-hour mark**: Update passengers. Begin preparing care vouchers if delay is expected to exceed 2 hours.
3. At the **2-hour mark**: Distribute meal/refreshment vouchers.
4. At the **3-hour mark**: Offer communication facilities. Update rebooking options.
5. At the **4-hour mark** (long-haul): Offer lounge access where available.
6. At the **5-hour mark**: Inform passengers of their right to a full refund and offer the refund option proactively.
7. **Overnight**: Arrange hotel accommodation and transport.

---

## 5. EU261/2004 Compensation

### 5.1 Compensation Table

Compensation is payable when the disruption is caused by an airline-controllable event and the passenger arrives at their final destination with a delay of:

| Flight Distance | Delay on Arrival | Compensation Amount |
|-----------------|------------------|---------------------|
| **Short-haul (≤1,500 km)** | ≥3 hours | **EUR 250** |
| **Medium-haul (1,500–3,500 km)** | ≥3 hours | **EUR 400** |
| **Long-haul (>3,500 km)** | ≥3 hours but <4 hours | **EUR 300** (50% of EUR 600) |
| **Long-haul (>3,500 km)** | ≥4 hours | **EUR 600** |

### 5.2 Cancellation Compensation

The same compensation amounts apply to cancellations, unless:
- The cancellation was notified **more than 14 days** before departure.
- The cancellation was notified **7–14 days** before departure AND the offered rebooking departs no more than 2 hours earlier and arrives no more than 4 hours later.
- The cancellation was notified **less than 7 days** before departure AND the offered rebooking departs no more than 1 hour earlier and arrives no more than 2 hours later.

### 5.3 Denied Boarding Compensation

- Same compensation amounts as above apply immediately upon denied boarding.
- Compensation is payable **in addition to** rebooking or refund.
- Passengers who voluntarily surrender their seats are not entitled to EU261 compensation but may accept alternative incentives offered by the airline (vouchers, upgrades, etc.).

### 5.4 Downgrade Compensation

If a passenger is downgraded to a lower cabin class, they are entitled to a refund of:

| Flight Distance | Refund Percentage |
|-----------------|-------------------|
| ≤1,500 km | 30% of the ticket price |
| 1,500–3,500 km | 50% of the ticket price |
| >3,500 km | 75% of the ticket price |

### 5.5 Extraordinary Circumstances (No Compensation)

Compensation is NOT payable when the disruption is caused by extraordinary circumstances that could not have been avoided even if all reasonable measures had been taken:

- Severe weather conditions (storms, fog, volcanic ash, snow/ice)
- Air traffic control restrictions or airspace closures
- Security threats or security-related airport closures
- Political instability or civil unrest
- External strikes (ATC, airport staff, government orders)
- Hidden manufacturing defects identified by the aircraft manufacturer
- Bird strikes (assessed case by case)

> **Important:** Internal airline strikes, routine technical issues, and crew scheduling problems are NOT extraordinary circumstances and DO require compensation.

### 5.6 Compensation Payment Methods

- **Bank transfer** (preferred): Processed within 7 business days.
- **Travel voucher**: 120% of the compensation value, valid for 24 months. Must be explicitly accepted by the passenger; cannot be imposed.
- **Cash/cheque**: Available at airport service desks for immediate payment.

---

## 6. Automatic Rebooking Rules (AUTOREB)

### 6.1 AUTOREB Logic

The automatic rebooking engine processes affected passengers in the following order and applies these rules:

1. **Same airline, same route, next departure:** Assign to the next available flight on the same route.
2. **Same airline, alternative routing:** If no direct flights are available within 4 hours, search for one-stop connections via the airline's hub.
3. **Alliance partner, same route:** Search for available seats on Star Alliance / partner airline direct flights.
4. **Other carrier, same route:** As a last resort, rebook on any available carrier.

### 6.2 AUTOREB Cabin Class Rules

- Rebook in the **same or higher** cabin class. Never downgrade automatically.
- If the only availability is in a lower cabin, flag the PNR for manual review.
- Business class passengers must remain in Business class or be offered a premium economy seat + downgrade compensation.

### 6.3 AUTOREB Exceptions

The following passengers are **excluded from AUTOREB** and must be handled manually:
- Unaccompanied minors (UMNR)
- Passengers with medical conditions (MEDA)
- Passengers requiring wheelchair assistance (WCHR/WCHC/WCHS)
- Group bookings (10+ passengers)
- VIP/CIP passengers
- Passengers with pets (PETC/AVIH)

---

## 7. Diversion Handling

### 7.1 Diversion Procedure

1. Upon landing at the diversion airport, the captain announces the situation and expected next steps.
2. Ground staff at the diversion airport coordinate with Operations Control Centre (OCC).
3. Options in priority order:
   a. **Re-dispatch:** Refuel and continue to the original destination when conditions permit.
   b. **Ground transport:** Arrange bus/train to the original destination if within 3 hours by ground.
   c. **Rebooking:** Rebook passengers on the next available flight to the destination.
4. Full care obligations apply at the diversion airport (meals, accommodation, communication).
5. EU261 compensation applies if the diversion results in a delay of 3+ hours at the final destination and the cause is airline-controllable.

---

## 8. Communication Templates for IROP

### 8.1 SMS Template — Delay

```
[Airline] Flight [XX123] on [DD MMM]: We regret to inform you of a delay. 
New estimated departure: [HH:MM]. We apologize for the inconvenience. 
For rebooking: airline.com/manage or call +XX XXX XXX XXXX. Your rights: airline.com/eu261
```

### 8.2 SMS Template — Cancellation

```
[Airline] Flight [XX123] on [DD MMM] has been cancelled. 
We have rebooked you on flight [XX456] departing [HH:MM on DD MMM]. 
To accept or change: airline.com/manage or call +XX XXX XXX XXXX. 
Meal/hotel vouchers available at the service desk. Your rights: airline.com/eu261
```

### 8.3 Email Template — EU261 Rights Notice

See Email Templates document (KB-EML-001) for the full EU261 rights notification email.

---

## 9. Reporting & Escalation

### 9.1 IROP Reporting

- All IROP events must be logged in the IROP Management System within **1 hour** of occurrence.
- Post-IROP report due within **24 hours** covering: root cause, passengers affected, compensation issued, customer feedback.

### 9.2 Escalation Matrix

| Situation | Escalate To | Timeline |
|-----------|-------------|----------|
| Single flight delay >3 hours | Duty Manager | Immediately |
| Multiple flight cancellations (3+) | IROP Coordinator + VP Operations | Within 30 minutes |
| Diversion | Captain + OCC + Station Manager | Immediately |
| Denied boarding >5 passengers | Duty Manager + Customer Relations | Immediately |
| Media/social media attention | Communications team + VP Customer | Within 1 hour |

---

*End of Document — KB-DIS-001 v4.1*
