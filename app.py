from fastapi import FastAPI

# initialize a FastAPI object
app = FastAPI()

# calculate compound interest given an initial investment, monthly contribution,
# rate of return, compounds per year, and total years of investing
@app.get("/calculate")
def calculate_model(initial_inv: int, monthly_cont: int, rate: float, annual_comps: int, years: int):
    monthly_rate = rate / 100 / annual_comps

    # calculate the total number of compounding periods
    total_periods = annual_comps * years

    # initialize future value to the initial investment amount
    future_value = initial_inv

    # apply compound interest formula for each period
    for i in range(total_periods):
        # the future value is incremented by multiplying 1 + the monthly rate
        future_value *= (1 + monthly_rate)
        # add on this month's contribution
        future_value += monthly_cont

    # return the final value of interest compounded over the given period
    return {'value' : future_value}



