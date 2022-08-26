
def get_credit(price, deposit):
    return price*(1-deposit/100)

def get_rate(a,b):
    return (a + b) / 2

def calc_payment(credit, term, rate):
    return credit * (1 + term * rate/12/100) / (term*12)

def get_validate_data(price, term, deposit):
    return price > 0 and term > 0 and (0 <= deposit <= 100)