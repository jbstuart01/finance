# create a CD class
class CD:
    # initialize the object
    def __init__(self, deposit, rate, term):
        self.set_deposit(deposit)
        self.set_rate(rate if rate < 1 else rate / 100)
        self.set_term(term)

    # Getter for deposit
    def get_deposit(self):
        return self._deposit

    # Setter for deposit
    def set_deposit(self, deposit):
        # if we are given something other than an integer or float
        if not isinstance(deposit, (int, float)):
            raise TypeError("Deposit must be a number.")
        # if we are given a negative value
        elif deposit <= 0:
            raise ValueError()
        
        # once input is validated, set the deposit amount
        else:
            self._deposit = deposit

    # Getter for rate
    def get_rate(self):
        return self._rate

    # Setter for rate
    def set_rate(self, rate):
        # if we are given something other than an integer or float
        if not isinstance(rate, (int, float)):
            raise TypeError("Rate must be a number.")
        elif rate <= 0:
            raise ValueError("Rate must be a positive value.")
        
        # if the rate is 5.00%, we could handle inputs of 5 or .05
        elif rate > 1:
            # if it was given 5, set it to be .05
            self._rate = rate / 100
        else:
            self._rate = rate

    # Getter for term
    def get_term(self):
        return self._term

    # Setter for term
    def set_term(self, term):
        # we can only handle a positive integer for month
        if not isinstance(term, int):
            raise TypeError("Term must be an integer.")
        if term <= 0:
            raise ValueError("Term must be a positive value.")
        
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