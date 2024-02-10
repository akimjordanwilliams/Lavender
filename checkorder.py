# This is a summary of all the code for this tutorial
from coinbase.rest import RESTClient
from json import dumps
import math

api_key = "organizations/9cc6946c-4bb6-4d2b-8527-fcc42827f847/apiKeys/f04925b2-3c24-4121-b501-428f69274b49"
api_secret = "-----BEGIN EC PRIVATE KEY-----\nMHcCAQEEIBX3nKFHZAaJWnJLZeDVVQUlRuABRkUNUHlKWeyfnOx3oAoGCCqGSM49\nAwEHoUQDQgAEffRDCL/RJhIyuLIzdsWf+gOyteNR427ozh95eD83sPRPRntYi/Ja\n7KdC5wBZtYOZQTI+1LBwEO+iUnDouQ5skA==\n-----END EC PRIVATE KEY-----\n"

client = RESTClient(api_key=api_key, api_secret=api_secret)


fills = client.get_fills(order_id="00000004")

print(dumps(fills, indent=2))