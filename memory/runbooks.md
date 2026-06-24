# Checkout Incident Runbook

## PaymentGatewayTimeout
If checkout-service logs show PaymentGatewayTimeout:
1. Check payment provider status.
2. Check retry configuration.
3. Verify recent deploy changes in payment-client.
4. If provider returns 503, activate fallback payment route.

## Checkout 500 errors
If POST /checkout returns 500:
1. Check checkout-service logs.
2. Check payment-client dependency.
3. Check inventory-service.
4. Check auth-service.