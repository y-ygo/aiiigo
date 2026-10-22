class Patient:
    def __init__(self, name, bill_amount):
        self.__name = name
        self.__bill_amount = bill_amount
    def get_name(self):
        return self.__name
    def set_name():
        self.__name = name
    def get_bill_amount(self):
        return self.__bill_amount
    def set_bill_amount():
        self.__bill_amount = bill_amount
    def calculate_bill(self):
        return self.__bill_amount 

class Senior_Patient(Patient):
    def calculate_bill(self):
        return self.get_bill_amount() * .80

class PhilHealth_Patient(Patient):
    def calculate_bill(self):
        return self.get_bill_amount() * .85

Patient1 = Patient("Audrey Canto", 20000)
Patient2 = PhilHealth_Patient("Andy Cera", 10000)
Patient3 = Senior_Patient("Hyrall Sevilla", 13000)

patients = [Patient1, Patient2, Patient3]

print("Hospital Billing System")
print("-----------------------")
for i in patients:
    print("Name:", i.get_name())
    print("Original Bill: ", i.get_bill_amount())
    print("Final Bill: ", i.calculate_bill())
    print()
