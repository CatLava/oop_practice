
class PayrollSystem:
    # Must be passed in as a list
    def calculate_payroll(self, employees):
        print("calculating payroll")
        print("===========")
        for employee in employees:
            print(f'Payroll for : {employee.id} + {employee.name}')
            print(f'- Check Amount: {employee.calculate_payroll()}')
            print('')


