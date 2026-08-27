# Passenger Type Codes

**Document ID:** KB-PTC-001  
**Version:** 2.0  
**Effective Date:** 01 March 2026  
**Last Reviewed:** 15 July 2026  
**Owner:** Revenue Management & Pricing Division

---

## 1. Overview

Passenger Type Codes (PTCs) are standardized IATA codes used to classify passengers based on age, status, or special conditions. PTCs determine fare eligibility, pricing discounts, documentation requirements, and service entitlements. All customer service agents must correctly identify and apply the appropriate PTC at the time of booking to ensure accurate pricing and compliance.

---

## 2. Passenger Type Code Definitions

### 2.1 ADT — Adult

| Field | Detail |
|-------|--------|
| **Code** | ADT |
| **Full Name** | Adult |
| **Age Range** | 12 years and above (on the date of departure of the first flight segment) |
| **Pricing** | Standard fare — 100% of the published fare for the selected fare family |
| **Required Documentation** | Valid passport (international travel) or government-issued photo ID (domestic/Schengen travel) |
| **Passport Validity** | Must be valid for at least **6 months** beyond the date of return (for international travel outside Schengen). For Schengen travel: must be valid for the duration of travel. |
| **Booking Rules** | Standard booking rules apply. No restrictions. |
| **Seat** | Own seat required. |
| **Baggage** | Per fare family rules (see Fare Families KB-FAR-001). |
| **Loyalty** | Eligible for loyalty program membership and miles earning. |
| **Notes** | Default PTC. Applied when no other PTC is specified. |

### 2.2 CHD — Child

| Field | Detail |
|-------|--------|
| **Code** | CHD |
| **Full Name** | Child |
| **Age Range** | 2–11 years (on the date of departure of the first flight segment) |
| **Pricing** | **75% of the adult fare** (25% discount). Taxes and surcharges are the same as adult. |
| **Required Documentation** | Valid passport (international travel) + birth certificate or equivalent proof of age. Government-issued photo ID acceptable for domestic/Schengen travel if available. |
| **Travel Restriction** | **Must travel with at least one accompanying adult** (ADT, 18+ years). Maximum **2 children per adult**. |
| **Seat** | Own seat required. |
| **Baggage** | Same baggage allowance as the fare family booked. |
| **Meal** | Child meal (CHML) can be pre-ordered at no extra charge. |
| **Seat Restriction** | Cannot be seated in exit rows. Must be seated in the same cabin class as the accompanying adult. |
| **Loyalty** | Eligible for loyalty program membership (junior tier). Miles earned at 100% rate. |
| **Age Verification** | Age is verified at the time of check-in. If the child has turned 12 by the date of travel, the booking must be changed to ADT and the fare difference collected. |
| **Unaccompanied** | Children 5-11 traveling without an adult must be booked as UMNR (see SSR Codes Reference KB-SSR-001). Children under 5 cannot travel unaccompanied under any circumstances. |

### 2.3 INF — Infant

| Field | Detail |
|-------|--------|
| **Code** | INF |
| **Full Name** | Infant |
| **Age Range** | 0–23 months (under 2 years on the date of departure of the **last** flight segment in the itinerary) |
| **Pricing** | **10% of the adult fare**. No seat is assigned. Taxes may be reduced or waived. Airport taxes applicable. |
| **Required Documentation** | Birth certificate (mandatory, all travel). Valid passport for international travel. |
| **Travel Restriction** | Must travel with an accompanying adult (ADT, 18+ years). **Maximum 1 infant per adult**. If an adult is traveling with 2 infants, the second infant must be booked as CHD with a seat. |
| **Seat** | **No seat assigned** — infant sits on the accompanying adult's lap. An infant seatbelt (loop belt) is provided by the cabin crew. |
| **Bassinet** | Available on long-haul flights for infants under 11 kg and 75 cm. Subject to availability. Request via SSR code BSCT. Must be pre-requested at least 48 hours before departure. Bulkhead seats assigned. |
| **Baggage** | 1 checked bag (10 kg) included in all fare families. 1 collapsible stroller or car seat also accepted free of charge (gate-checked). |
| **Meal** | Baby meal (BBML) can be pre-ordered at no extra charge. |
| **Seat Restriction** | Adult with infant cannot sit in exit rows. |
| **Loyalty** | Not eligible for loyalty program. |
| **Age Transition** | If the infant turns 2 during the trip (between outbound and return flights), the infant must be rebooked as CHD for the return flight(s) with a seat and at the child fare. This should be handled at the time of booking. |
| **Minimum Age** | Infants less than **48 hours old** are not accepted for travel. Infants 48 hours – 7 days old require medical clearance (see Medical Clearance Guide KB-MED-001). |

### 2.4 YTH — Youth

| Field | Detail |
|-------|--------|
| **Code** | YTH |
| **Full Name** | Youth |
| **Age Range** | 12–25 years (on the date of departure) |
| **Pricing** | Special youth fares where available. Discount varies by route (typically 10–30% off the standard fare). Not available on all routes or fare families. When youth fares are not available, standard adult pricing applies. |
| **Required Documentation** | Valid passport or government-issued photo ID + proof of age (student ID, birth certificate, or ID showing date of birth). |
| **Travel Restriction** | None — youths 12+ can travel independently. |
| **Seat** | Own seat. No restrictions (eligible for exit rows if 16+). |
| **Baggage** | Per fare family rules. Youth fares may include an additional free checked bag on select routes (check fare rules). |
| **Loyalty** | Eligible for loyalty program (standard membership). |
| **Availability** | Youth fares are filed under separate fare basis codes (prefix `YTH` or `SD`). Agents should search for youth fares specifically in the GDS: entry `FQP[route]/PTC:YTH`. |
| **Combinability** | Youth fares can typically be combined with Classic and Flex fare families only (not Light). |
| **Notes** | Youth fare eligibility is verified at check-in. If the passenger is over 25 on the date of travel, the booking must be changed to ADT and the fare difference collected. |

### 2.5 SRC — Senior

| Field | Detail |
|-------|--------|
| **Code** | SRC |
| **Full Name** | Senior Citizen |
| **Age Range** | 65 years and above (on the date of departure) |
| **Pricing** | Senior discount where available. Discount varies by route (typically 5–15% off the standard fare). Not available on all routes or fare families. When senior fares are not available, standard adult pricing applies. |
| **Required Documentation** | Valid passport or government-issued photo ID showing date of birth. |
| **Travel Restriction** | None. |
| **Seat** | Own seat. No restrictions. |
| **Baggage** | Per fare family rules. |
| **Loyalty** | Eligible for loyalty program (standard membership). May qualify for accelerated tier earning on select promotions. |
| **Availability** | Senior fares filed under separate fare basis codes (prefix `SRC` or `SC`). Agents should search: `FQP[route]/PTC:SRC`. |
| **Combinability** | Senior fares can typically be combined with Classic and Flex fare families only (not Light). |
| **Special Assistance** | Senior passengers may request WCHR (wheelchair) or MAAS (meet and assist) at no charge if needed. |
| **Notes** | Age verification at check-in. If the passenger is under 65 on the date of travel, the booking must be changed to ADT and the fare difference collected. |

### 2.6 DIS — Disabled Passenger

| Field | Detail |
|-------|--------|
| **Code** | DIS |
| **Full Name** | Disabled Passenger / Passenger with Reduced Mobility (PRM) |
| **Age Range** | Any age |
| **Pricing** | Standard fare (no discount based on disability). Companion discount may be available (see Section 4). |
| **Required Documentation** | Valid passport or ID. Disability documentation may be required for specific services (e.g., medical certificate for MEDA, service animal documentation for SVAN). |
| **Travel Restriction** | None, subject to medical clearance if applicable (see Medical Clearance Guide KB-MED-001). |
| **Special Assistance** | Entitled to free assistance under EU Regulation 1107/2006: wheelchair, boarding assistance, seating assistance, communication assistance, guide for blind passengers. |
| **SSR Codes** | WCHR, WCHC, WCHS, WCBD, BLND, DEAF, DPNA, MAAS (see SSR Codes Reference KB-SSR-001). |
| **Companion Seat** | If the passenger requires a personal care attendant, the companion must be booked on the same flight. Some routes offer a companion discount (up to 50% off). |
| **Seat** | Assigned based on needs. Not in exit rows if mobility-impaired. Aisle seat preferred for WCHR/WCHS. |
| **Baggage** | Per fare family rules. Mobility aids (wheelchair, crutches, walking frame) are accepted as free additional checked items. |
| **Loyalty** | Eligible for loyalty program (standard membership). |
| **Notes** | The airline is committed to providing equal access to all passengers with disabilities in compliance with EU Regulation 1107/2006 and national accessibility laws. |

---

## 3. PTC Summary Table

| Code | Type | Age Range | Discount | Seat | Must Travel With |
|------|------|-----------|----------|------|-----------------|
| **ADT** | Adult | 12+ | None (100%) | Own seat | — |
| **CHD** | Child | 2–11 | 25% off (pays 75%) | Own seat | Adult (18+) |
| **INF** | Infant | 0–23 months | 90% off (pays 10%) | No seat (lap) | Adult (18+) |
| **YTH** | Youth | 12–25 | 10–30% off (where available) | Own seat | — |
| **SRC** | Senior | 65+ | 5–15% off (where available) | Own seat | — |
| **DIS** | Disabled | Any | None (standard fare) | Own seat | Companion (if required) |

---

## 4. Discount Codes & Mappings

### 4.1 Internal Discount Codes

| Discount Code | Description | PTC | Discount | Conditions |
|--------------|-------------|-----|----------|------------|
| **CD25** | Child discount | CHD | 25% off published fare | Age 2–11, travel with adult |
| **IN90** | Infant discount | INF | 90% off published fare | Age 0–23 months, no seat |
| **YD10** | Youth discount (standard) | YTH | 10% off | Age 12–25, ID required |
| **YD20** | Youth discount (promotional) | YTH | 20% off | Age 12–25, specific routes only |
| **YD30** | Youth discount (student) | YTH | 30% off | Age 12–25, valid ISIC student card |
| **SC05** | Senior discount (standard) | SRC | 5% off | Age 65+, ID required |
| **SC10** | Senior discount (promotional) | SRC | 10% off | Age 65+, specific routes only |
| **SC15** | Senior discount (loyalty members) | SRC | 15% off | Age 65+, Silver tier or above |
| **CMP50** | Companion of disabled passenger | ADT | 50% off | Traveling with DIS passenger, same booking |
| **MIL10** | Military discount | ADT | 10% off | Active military, valid military ID |
| **GOV15** | Government / Diplomatic | ADT | 15% off | Valid diplomatic passport |
| **GRP05** | Group discount (10–19 pax) | ADT | 5% off | Group booking, 10+ passengers |
| **GRP10** | Group discount (20–49 pax) | ADT | 10% off | Group booking, 20+ passengers |
| **GRP15** | Group discount (50+ pax) | ADT | 15% off | Group booking, 50+ passengers |
| **STAFF** | Staff travel | ADT | 90% off | Airline employees, standby basis |
| **ID50** | Industry discount | ADT | 50% off | Travel industry professionals, IATA card required |

### 4.2 Discount Stacking Rules

- **Only one PTC discount** can be applied per passenger.
- PTC discounts (CD25, IN90, YD, SC) are applied to the **base fare** before taxes and surcharges.
- Promotional discounts (promo codes, sale fares) **cannot be combined** with PTC discounts unless explicitly stated in the promotion terms.
- Loyalty tier discounts **can be combined** with PTC discounts (e.g., Senior + Silver tier).
- Corporate contract rates are applied **instead of** PTC discounts (not in addition to).

---

## 5. Age Validation Rules

### 5.1 Age Calculation

- Age is determined on the **date of departure of the first flight segment** in the itinerary.
- For return trips, the age on the outbound departure date is used for the **entire itinerary**, except for INF passengers who turn 2 during the trip (see Section 2.3).

### 5.2 Age Verification Process

| Stage | Verification |
|-------|-------------|
| **Booking** | Agent selects the appropriate PTC based on the passenger's stated date of birth. Date of birth is recorded in the PNR. |
| **Check-in (online)** | System validates the PTC against the date of birth in the PNR. Discrepancies flag an alert. |
| **Check-in (airport)** | Agent verifies date of birth against the travel document (passport/ID). |
| **Boarding** | Final visual verification. If a passenger appears to be outside the declared age range, the gate agent may request to see the travel document. |

### 5.3 Age Discrepancy Handling

| Discrepancy | Action |
|-------------|--------|
| Child (CHD) has turned 12 | Change PTC to ADT. Collect fare difference (25% of base fare). Reissue ticket. |
| Infant (INF) has turned 2 | Change PTC to CHD for remaining segments. Assign a seat. Collect fare difference. Reissue ticket. |
| Youth (YTH) is over 25 | Change PTC to ADT. Collect fare difference. Reissue ticket. |
| Senior (SRC) is under 65 | Change PTC to ADT. Collect fare difference. Reissue ticket. |
| Adult (ADT) is actually under 12 | Change PTC to CHD. Refund fare difference to the original payment method. Reissue ticket. |

### 5.4 Date of Birth Format

- Dates of birth must be entered in the PNR in the format: **DDMMMYY** (e.g., 15JAN90).
- For infants, the full year must be recorded to avoid ambiguity: use DDMMMYYYY (e.g., 15JAN2024).
- The date of birth must **exactly match** the travel document. Any discrepancy may result in denied boarding.

---

## 6. Booking System Entries

### 6.1 GDS PTC Entry Formats

| GDS | Entry Format | Example |
|-----|-------------|---------|
| **Amadeus** | `FXP/R,PTC:CHD` | Price as child |
| **Sabre** | `WPPC‡CHD` | Price as child |
| **Galileo/Travelport** | `FQ:CHD` | Price as child |
| **NDC API** | `passengerType: "CHD"` | JSON payload |

### 6.2 Multiple PTC Booking

When booking passengers with different PTCs in the same PNR:

1. Enter all passengers with their names and dates of birth.
2. Price the itinerary with mixed PTCs:
   - Amadeus: `FXP/R,PTC:ADT*CHD*INF`
   - Sabre: `WPPC‡ADT/1‡CHD/1‡INF/1`
3. Verify that each passenger is priced correctly with the appropriate discount.
4. Confirm that infant passengers are associated with the correct adult.

### 6.3 Infant Association

- Each infant must be **associated with a specific adult** in the PNR.
- In Amadeus: `SSR INFT [airline] [infant name]/[DOB]/[associated adult segment]`
- Maximum 1 infant per adult. If there are more infants than adults, excess infants must be booked as CHD with seats.

---

## 7. Regulatory Compliance

### 7.1 Non-Discrimination

- Fares and services must be offered equally to all passengers regardless of nationality, ethnicity, gender, religion, or disability.
- PTC discounts are based solely on **age** and **documented status**.
- Disability (DIS) is not a basis for surcharges or fare increases.

### 7.2 Data Protection

- Dates of birth and age-related data are classified as **personal data** under GDPR.
- Age data is collected for the purpose of **fare calculation** and **safety compliance** (e.g., exit row restrictions).
- Age data must not be used for marketing purposes without explicit consent.

### 7.3 IATA Standards

- All PTC codes comply with IATA Resolution 787.
- Fare calculations follow IATA Pricing Unit (PU) and Fare Construction Point (FCP) rules.
- Discount percentages are set by the airline and filed with ATPCO.

---

*End of Document — KB-PTC-001 v2.0*
