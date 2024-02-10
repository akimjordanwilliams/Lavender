# This is a summary of all the code for this tutorial
from coinbase.rest import RESTClient
from json import dumps
import math

api_key = "organizations/9cc6946c-4bb6-4d2b-8527-fcc42827f847/apiKeys/f04925b2-3c24-4121-b501-428f69274b49"
api_secret = "-----BEGIN EC PRIVATE KEY-----\nMHcCAQEEIBX3nKFHZAaJWnJLZeDVVQUlRuABRkUNUHlKWeyfnOx3oAoGCCqGSM49\nAwEHoUQDQgAEffRDCL/RJhIyuLIzdsWf+gOyteNR427ozh95eD83sPRPRntYi/Ja\n7KdC5wBZtYOZQTI+1LBwEO+iUnDouQ5skA==\n-----END EC PRIVATE KEY-----\n"

client = RESTClient(api_key=api_key, api_secret=api_secret)

product = client.get_product("SOL-USD")
sol_usd_price = float(product["price"])
adjusted_sol_usd_price = str(math.floor(sol_usd_price - (sol_usd_price * 0.05)))

limit_order = client.limit_order_gtc_buy(
    client_order_id="00000004",
    product_id="SOL-USD",
    base_size="5",
    limit_price=adjusted_sol_usd_price
)

limit_order_id = limit_order["order_id"]
# client.cancel_orders(order_ids=[limit_order_id])