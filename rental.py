
class RentalProperty:
    def __init__(self, total_investment, monthly_income, monthly_expenses):
        self.total_investment = total_investment
        self.monthly_income = monthly_income
        self.monthly_expenses = monthly_expenses
    
    def cash_flow(self):
        annual_income = self.monthly_income * 12
        annual_expenses = self.monthly_expenses * 12
        annual_net_income = annual_income - annual_expenses
        return annual_net_income
    
    def calculate_roi(self):
        annual_cash_flow = self.cash_flow()
        return (annual_cash_flow / self.total_investment) * 100


def main():
    total_investment = int(input('Please enter your total investment for the property: '))
    monthly_income = int(input('Please enter your monthly income from the property: '))
    monthly_expenses = int(input('Please enter your monthly expenses for the property: '))

    property1 = RentalProperty(total_investment, monthly_income, monthly_expenses)

    roi = property1.calculate_roi()

    print(f"\nYour Return on Investment or ROI for this property is {roi}% ")

main()