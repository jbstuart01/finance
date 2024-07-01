# create a CD class
class CD:
    # initialize the object
    def __init__(self, deposit, rate, term):
        self._deposit = deposit
        # handle rates that are in the format '5' or '.05' for a 5.00% APY
        self._rate = rate if rate < 1 else rate / 100
        self._term = term   

    # Getter for deposit
    def get_deposit(self):
        return self._deposit

    # Setter for deposit
    def set_deposit(self, deposit):
        self._deposit = deposit

    # Getter for rate
    def get_rate(self):
        return self._rate

    # Setter for rate
    def set_rate(self, rate):
        # if the rate is 5.00%, we can handle inputs of 5 or .05
        self._rate = rate if rate < 1 else rate / 100

    # Getter for term
    def get_term(self):
        return self._term

    # Setter for term
    def set_term(self, term):
        self._term = term

    # get the amount the CD will earn at the end of the term
    def calculate_earnings(self):
        # get the principal amount invested
        principal = self.get_deposit()
        # get the APY
        rate = self.get_rate()
        # get the length of investment
        term = self.get_term() / 12  # Convert term from months to years

        # the number of annual compounds, 4 is quarterly
        annual_compounds = 4

        # use compound interest formula to calculate the amount earned
        total = principal * (1 + rate / annual_compounds) ** (annual_compounds * term)
        
        # subtract the principal from the total, and return the leftover
        return total - principal
    
    # Print CD information
    # def print_info(self):
    #     deposit = self.get_deposit()
    #     rate = self.get_rate() * 100  # Convert rate back to percentage
    #     term = self.get_term()
    #     earnings = self.calculate_earnings()
    #     final_amount = deposit + earnings

    #     print(f"{'CD Information':^40}")
    #     print("="*40)
    #     print(f"{'Initial Deposit:':>20} ${deposit:,.2f}")
    #     print(f"{'Rate:':>20} {rate:.2f}% APY")
    #     print(f"{'Term:':>20} {term} months")
    #     print(f"{'Earnings:':>20} ${earnings:,.2f}")
    #     print(f"{'Final Amount:':>20} ${final_amount:,.2f}")
    #     print("="*40)