from fastapi import FastAPI

# initialize a FastAPI object
app = FastAPI()

# calculate compound interest given an initial investment, monthly contribution,
# rate of return, compounds per year, and total years of investing
@app.get("/calculate")
def calculate_model(initial_inv: int, monthly_cont: int, rate: float, years: int):
    monthly_rate = rate / 100

    # initialize future value to the initial investment amount
    future_value = initial_inv

    # apply compound interest formula for each period
    for i in range(years):
        # add on this year's contributions
        future_value += (monthly_cont * 12)
        # the future value is incremented by multiplying 1 + the monthly rate
        future_value *= (1 + monthly_rate)

    # return the final value of interest compounded over the given period
    return {'final_value' : round(future_value, 2)}

def main():
    calculate_model(25000, 750, 10, 35)

if __name__ == "__main__":
    main()