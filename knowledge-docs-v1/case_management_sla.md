# Case Management SLA

**Document ID:** KB-CAS-001  
**Version:** 2.2  
**Effective Date:** 01 March 2026  
**Last Reviewed:** 15 July 2026  
**Owner:** Customer Relations & Quality Assurance Division

---

## 1. Overview

This document defines the Service Level Agreements (SLAs) for all customer cases managed through the airline's case management system. It establishes priority levels, response and resolution targets, escalation paths, and case lifecycle rules. All agents, supervisors, and managers must adhere to these SLAs to ensure consistent and timely customer service.

---

## 2. Priority Levels

### 2.1 Priority Classification Matrix

| Priority | Level | Description | Examples |
|----------|-------|-------------|----------|
| **P1** | **Critical** | Issues involving immediate safety risk, fraud, legal liability, or major reputational risk. Requires immediate action. | Suspected fraud/stolen card, safety incident report, medical emergency during travel, data breach involving passenger PII, bomb threat, aircraft incident |
| **P2** | **High** | Significant disruption to the passenger's journey, VIP/high-value customer issues, or time-sensitive matters requiring prompt attention. | Flight cancellation/major delay affecting travel plans, denied boarding incident, VIP/Platinum member complaint, lost passport at airport, unaccompanied minor issue, media/social media escalation |
| **P3** | **Medium** | Standard customer complaints, booking changes, service recovery, and issues requiring investigation but not immediately urgent. | Formal complaint about service quality, booking change request requiring override, baggage damage/delay claim, refund request, loyalty miles dispute, name change request, ancillary service complaint |
| **P4** | **Low** | General inquiries, feedback, information requests, and issues that are not time-sensitive. | General policy inquiry, feedback/suggestion, frequent flyer enrollment, receipt request, marketing opt-out, seat preference note, general compliment |

### 2.2 SLA Response & Resolution Targets

| Priority | First Response | Resolution Target | Escalation Trigger |
|----------|---------------|--------------------|--------------------|
| **P1 — Critical** | **1 hour** | **4 hours** | If no response in 30 minutes → auto-escalate to Duty Manager |
| **P2 — High** | **4 hours** | **24 hours** | If no response in 2 hours → auto-escalate to Team Lead |
| **P3 — Medium** | **24 hours** | **72 hours** (3 business days) | If no response in 12 hours → flag for supervisor review |
| **P4 — Low** | **48 hours** | **7 business days** | If no response in 48 hours → auto-assign to available agent |

> **Note:** Response and resolution times are measured in **business hours** (Monday–Friday, 08:00–20:00 CET) unless the case is P1 (Critical), which uses **calendar hours** (24/7).

### 2.3 SLA Measurement Definitions

| Metric | Definition |
|--------|------------|
| **First Response Time** | The time from when the case is created to when the first **meaningful** response is sent to the customer. Auto-acknowledgement emails do NOT count as a first response. |
| **Resolution Time** | The time from case creation to when the case status is set to **Resolved**. Time spent in "Pending Customer" status is excluded from the resolution clock. |
| **SLA Compliance** | A case meets SLA if both first response and resolution occur within the target times. |
| **SLA Breach** | A case breaches SLA if either the first response or resolution exceeds the target time. |

---

## 3. Case Lifecycle

### 3.1 Case Status Flow

```
[New] → [Open] → [In Progress] → [Pending Customer] → [In Progress] → [Resolved] → [Closed]
                       ↓                                      ↑
                  [Escalated] ─────────────────────────────────┘
```

### 3.2 Case Status Definitions

| Status | Description | SLA Clock |
|--------|-------------|-----------|
| **New** | Case has been created but not yet assigned to an agent. | ⏱️ Running |
| **Open** | Case has been assigned to an agent but work has not yet started. | ⏱️ Running |
| **In Progress** | Agent is actively working on the case. | ⏱️ Running |
| **Pending Customer** | Agent is waiting for information or confirmation from the customer. | ⏸️ Paused |
| **Escalated** | Case has been escalated to a higher authority (supervisor, manager, specialist team). | ⏱️ Running |
| **Resolved** | The issue has been addressed and the customer has been informed of the resolution. | ⏹️ Stopped |
| **Closed** | Case is finalized. No further action required. | ⏹️ Stopped |
| **Reopened** | A previously resolved or closed case has been reopened due to customer follow-up. | ⏱️ Running (new SLA cycle) |

### 3.3 Status Transition Rules

| From | To | Conditions |
|------|----|------------|
| New | Open | Agent assigned (auto or manual) |
| Open | In Progress | Agent begins working on the case |
| In Progress | Pending Customer | Agent has sent a request for information to the customer |
| Pending Customer | In Progress | Customer responds with requested information |
| In Progress | Escalated | Agent escalates to supervisor/specialist |
| Escalated | In Progress | Escalation recipient takes action and returns case to the original agent or a new assignee |
| In Progress | Resolved | Issue is addressed. Resolution summary is documented. Customer is notified. |
| Resolved | Closed | Auto-closed after 7 days if no customer objection. Or manually closed by agent. |
| Resolved | Reopened | Customer responds within 7 days indicating the issue is not resolved. |
| Closed | Reopened | Only by supervisor approval. Customer contacts within 30 days. |

---

## 4. Auto-Close Rules

### 4.1 Automatic Closure — Pending Customer

If a case is in **Pending Customer** status and the customer does not respond:

| Reminder | Timing | Action |
|----------|--------|--------|
| **1st reminder** | 3 days after entering Pending Customer | Automated email: "We're waiting for your response to continue resolving your case [Case ID]." |
| **2nd reminder** | 7 days after entering Pending Customer | Automated email: "We still need your response. Your case will be closed in 7 days if we don't hear from you." |
| **Auto-close** | **14 days** after entering Pending Customer | Case automatically moved to Closed status with reason: "No customer response." |

### 4.2 Automatic Closure — Resolved

If a case is in **Resolved** status and the customer does not object:

| Timing | Action |
|--------|--------|
| **7 days** after entering Resolved | Case automatically moved to Closed status with reason: "Resolution accepted (no objection)." |

### 4.3 Reopening After Auto-Close

- Customers can reopen an auto-closed case by replying to the case email or contacting the Contact Centre within **30 days** of closure.
- After 30 days, a **new case** must be created, referencing the original case ID.

---

## 5. Escalation Matrix

### 5.1 Escalation Levels

| Level | Role | Authority | Use When |
|-------|------|-----------|----------|
| **Level 1** | Agent / Customer Service Representative | Standard case handling, apply documented policies | Default handling for all cases |
| **Level 2** | Team Lead / Senior Agent | Override fees up to EUR 100, approve exceptions within policy, reassign cases | Agent cannot resolve within policy, or customer requests supervisor |
| **Level 3** | Supervisor / Duty Manager | Override fees up to EUR 500, approve goodwill gestures (vouchers up to EUR 250), authorize interline rebooking | Team Lead cannot resolve, VIP customer, P2 cases |
| **Level 4** | Customer Relations Manager | Full policy override authority, approve compensation up to EUR 1,000, handle legal threats | Formal complaints, potential legal action, reputational risk |
| **Level 5** | Head of Customer Experience / VP | Unlimited authority, handle media cases, approve compensation >EUR 1,000 | Media/press involvement, CEO/board-level complaints, systemic failures |

### 5.2 Automatic Escalation Triggers

| Trigger | Action |
|---------|--------|
| P1 case not acknowledged within 30 minutes | Auto-escalate to Duty Manager + alert to VP |
| P2 case not responded within 2 hours | Auto-escalate to Team Lead |
| Any case breaches resolution SLA | Auto-escalate to Supervisor |
| Customer mentions "lawyer" or "legal action" | Auto-flag for Customer Relations Manager review |
| Customer mentions "media" or "journalist" | Auto-escalate to Communications team + VP Customer |
| Case reopened more than 2 times | Auto-escalate to Supervisor |
| CSAT rating ≤ 2/5 on a resolved case | Auto-flag for quality review |

### 5.3 VIP / High-Value Customer Identification

| Criteria | VIP Level | Handling |
|----------|-----------|----------|
| Platinum loyalty member | VIP-1 | Auto-assign to senior agent. P2 minimum priority. |
| Gold loyalty member | VIP-2 | Prioritize within queue. |
| Corporate account key contact | VIP-1 | Auto-assign to corporate desk. |
| Revenue >EUR 10,000 in past 12 months | VIP-2 | Flag in CRM. Prioritize within queue. |
| Influencer / Public figure | VIP-1 | Escalate to Communications team for awareness. |

---

## 6. Case Categories & Subcategories

### 6.1 Category Taxonomy

| Category | Subcategories | Default Priority |
|----------|---------------|------------------|
| **Booking** | New booking, change, cancellation, group booking, name change | P3 |
| **Payment** | Failed payment, refund request, duplicate charge, voucher issue | P3 |
| **Disruption** | Cancellation, delay, denied boarding, missed connection | P2 |
| **Baggage** | Lost, delayed, damaged, pilfered | P2 (lost/delayed), P3 (damaged) |
| **Ancillary** | Seat selection, extra baggage, meals, lounge, WiFi | P4 |
| **Special Services** | Wheelchair, UMNR, medical, pet transport | P3 |
| **Loyalty** | Miles query, tier status, partner earning, redemption issue | P3 (standard), P2 (Platinum) |
| **Complaint** | Service quality, staff behavior, facility, food quality | P3 |
| **Compliment** | Positive feedback about staff, service, experience | P4 |
| **Legal** | Legal claim, lawyer letter, court filing | P1 |
| **Fraud** | Suspected fraud, unauthorized booking, identity theft | P1 |
| **Safety** | Safety incident, injury, illness on board | P1 |
| **Data Privacy** | GDPR request, data access/deletion, data breach | P2 |
| **General** | Information request, feedback, suggestion | P4 |

---

## 7. Case Documentation Standards

### 7.1 Required Case Fields

Every case must contain the following information:

| Field | Required | Details |
|-------|----------|---------|
| **Case ID** | Auto-generated | Format: CAS-YYYYMMDD-NNNNN |
| **Customer name** | Yes | As per booking or loyalty account |
| **Contact information** | Yes | Email and/or phone number |
| **Booking reference (PNR)** | If applicable | 6-character code |
| **Category / Subcategory** | Yes | From taxonomy (Section 6) |
| **Priority** | Yes | P1, P2, P3, or P4 |
| **Description** | Yes | Detailed description of the issue |
| **Assigned agent** | Yes | Agent ID and name |
| **Channel** | Yes | Phone, email, chat, social media, airport, web form |
| **Resolution summary** | Required at resolution | What was done to resolve the issue |
| **Compensation / Goodwill** | If applicable | Type and value of any compensation provided |

### 7.2 Case Notes Standards

- All case notes must be **professional, factual, and objective**.
- Include **timestamps** for all significant actions.
- Record **customer sentiment** (satisfied, neutral, dissatisfied, escalated).
- Do NOT include personal opinions about the customer.
- Reference relevant **policy documents** (e.g., "Per KB-CHG-001, Section 2.1, Classic fare change fee is EUR 75").

---

## 8. Quality Assurance

### 8.1 Quality Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| **SLA Compliance (First Response)** | ≥95% | Monthly |
| **SLA Compliance (Resolution)** | ≥90% | Monthly |
| **Customer Satisfaction (CSAT)** | ≥4.0/5.0 | Per case survey |
| **First Contact Resolution (FCR)** | ≥70% | Monthly |
| **Case Reopen Rate** | ≤10% | Monthly |
| **Average Handling Time** | ≤15 minutes (phone) / ≤8 minutes (chat) | Weekly |

### 8.2 Quality Review Process

- **Random sampling:** 5% of closed cases reviewed weekly by Quality Assurance team.
- **Triggered review:** All cases with CSAT ≤ 2/5, all reopened cases, all P1 cases.
- **Calibration sessions:** Monthly calibration with agents and supervisors to align on quality standards.
- **Coaching:** Agents with quality scores below target receive 1:1 coaching within 7 days.

---

## 9. Reporting

### 9.1 Daily Reports

| Report | Audience | Content |
|--------|----------|---------|
| **Open Case Summary** | All agents, Team Leads | Count of open cases by priority and category |
| **SLA Breach Alert** | Supervisors, Managers | List of cases at risk of SLA breach |
| **P1/P2 Tracker** | Duty Manager, VP | Status of all active P1 and P2 cases |

### 9.2 Weekly Reports

| Report | Audience | Content |
|--------|----------|---------|
| **SLA Compliance Report** | Management | % compliance by priority, category, and team |
| **Volume Trend Report** | Workforce Management | Case volume trends, forecast vs. actual |
| **Top Issues Report** | Product, Operations | Most common case categories and root causes |

### 9.3 Monthly Reports

| Report | Audience | Content |
|--------|----------|---------|
| **Comprehensive Quality Report** | VP Customer Experience | All quality metrics, trends, benchmarks |
| **Compensation Report** | Finance, Customer Relations | Total compensation paid by category and reason |
| **Voice of Customer Report** | Executive Team | CSAT trends, NPS, key customer themes |

---

*End of Document — KB-CAS-001 v2.2*
