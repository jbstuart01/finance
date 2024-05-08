import requests
import json

payload = json.dumps({
    # preset values to pass
    "initial_inv" : 32000,
    "monthly_cont" : 1000,
    "rate" : 8,
    "years" : 30
})

# get the response
response = requests.put("http://127.0.0.1:8000/calculate", data = payload)
print(response.json())