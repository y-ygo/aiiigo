class Bill:
    def __init__(self, amount):
        self.amount = amount
    def pay(self, payment):
        self.amount -= payment.amount
        print("Payment made using", payment.mode)
        print("Remaining bill:", self.amount)
    
class Payment:
    mode = "Cash"
    def __init__(self, amount):
        self.amount = amount
        
class eWallet(Payment):
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

bigBeautifulBill = Bill(1000)
payment = Payment(800)
bigBeautifulBill.pay(payment)
GCash = eWallet("GCash", 200)
bigBeautifulBill.pay(GCash)

