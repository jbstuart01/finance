from fastapi import FastAPI
from pydantic import BaseModel

# create a class for the input to the API
class Input(BaseModel):
    initial_inv : float
    monthly_cont : float
    rate : float
    years : int

# instantiate an app object of type API
@app.put("/calculate")
def calculate(d:Input):
    monthly_rate = d.rate / 100

    # initialize future value to the initial investment amount
    future_value = d.initial_inv

    # apply compound interest formula for each period
    for i in range(d.years):
        # add on this year's contributions
        future_value += (d.monthly_cont * 12)
        # the future value is incremented by multiplying 1 + the monthly rate
        future_value *= (1 + monthly_rate)

    # return the final value of interest compounded over the given period
    return {'final_value' : round(future_value, 2)}
