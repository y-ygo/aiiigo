class Patient:
    def __init__(self, name, bill_amount):
        self.name = name
        self.bill_amount = bill_amount
    def get_name(): #############
        return "Patient Name: " + self.name
    def set_name():
        self.name = name
    def get_bill_amount():
        return self.bill_amount
    def set_bill_amount():
        self.bill_amount = bill_amount
    def calculate_bill():
        new_bill = bill_amount * discount 

class Senior_Patient(Patient):
    discount = .8
    def __init__(self, name, bill_amount):
        self.name = name
        self.bill_amount = bill_amount

class PhilHealth_Patient(Patient):
    discount = .85
    def __init__(self, name, bill_amount):
        self.name = name
        self.bill_amount = bill_amount

Patient1 = Patient("Audrey Canto", 20000)
Patient2 = PhilHealth_Patient("Andy Cera", 10000)
Patient3 = Senior_Patient("Hyrall Sevilla", 13000)

print("Hospital Billing System")
print("-----------------------")
Patient1.get_name() ##########
