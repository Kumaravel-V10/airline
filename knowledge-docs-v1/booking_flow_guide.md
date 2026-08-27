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
