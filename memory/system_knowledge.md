# System Knowledge

The checkout flow depends on:
1. auth-service
2. inventory-service
3. payment-client
4. external payment provider PayFast

checkout-service calls payment-client during payment authorization.

If payment-client fails, checkout-service can return HTTP 500.