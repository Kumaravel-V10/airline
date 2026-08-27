# Amadeus-Nevio Service Center — API Reference

Base URL: https://nevioservicecenterapim.azure-api.net
Airline Code: AY

## Authentication
| Endpoint | Method | Purpose |
|----------|--------|---------|
| /token | POST | Get JWT Token |
| /token/amadeus | POST | Get Amadeus Token |

## Shopping & Booking APIs
| Endpoint | Method | Purpose |
|----------|--------|---------|
| /searchpanel | GET | Get search panel configuration |
| /shop/flights | POST | Search available flights |
| /create-cart | POST | Create shopping cart with selected flight |
| /checkout/passengers | POST | Add passenger details |
| /checkout/passengers | PATCH | Update passenger details / Add contacts |
| /cart/retrieve | GET | Retrieve cart contents |
| /services | GET | Get service catalogue for cart |
| /seat/services | POST | Add seats or services |
| /seat/services | DELETE | Remove seats or services |
| /seatmap | GET | Get seat map for flight |
| /checkoutConfirm | POST | Confirm checkout / create order |
| /orders/retrieve | GET | Retrieve confirmed order by PNR |

## Post-Order APIs
| Endpoint | Method | Purpose |
|----------|--------|---------|
| /services | POST | Post-order service catalogue |
| /seatmap | GET | Post-order seat map |
| /seat/services | POST | Post-order add seats/services |

## GraphQL APIs
| Endpoint | Operations | Purpose |
|----------|-----------|---------|
| /appConfig | CRUD mutations/queries | Application configuration |
| /cancelAndRefund | RetriveOrderRefundEligiblities, CancellationAndRefund | Refund operations |

## Key Parameters
| Parameter | Description | Example |
|-----------|-------------|---------|
| cartId | Shopping cart identifier | auto-generated |
| orderRecLocId | PNR / Order locator | 6-char alphanumeric (e.g., 9DVWPJ) |
| airBoundId | Selected flight offer ID | from /shop/flights response |
| flightId | Flight identifier | from air bound response |
| promotionCode | Promo code for services | SCUISEATP |
| promotionAirlineCode | Airline code for promotions | AY |
