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
