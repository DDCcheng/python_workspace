

class InsurancePolicy:
    def __init__(self,price_of_item):
        self.price_of_insured_item=price_of_item

class VehicleInsurance(InsurancePolicy):
    def __init__(self, vehicle_Name):
        self.price_of_item=super().price_of_insured_item
        self.vehicle_Name=vehicle_Name
    def get_rate(self):
        return self.price_of_insured_item*0.01

class HomeInsurance(InsurancePolicy):
    def __init__(self, member_number):
        self.price_of_item=super().price_of_insured_item
        self.member_number=member_number
    def get_rate(self):
        return self.price_of_insured_item*0.00005
