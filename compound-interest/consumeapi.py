import requests

# preset values to pass
initial_inv = 32000
monthly_cont = 1000
rate = 8
years = 30

# create a response object
response = requests.get(f"http://localhost:8000/calculate?initial_inv={initial_inv}&monthly_cont={monthly_cont}&rate={rate}&years={years}")
output = response.json()
print(output)
