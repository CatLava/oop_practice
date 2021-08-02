
# Make this a singleton to be only called once
class _PayrollSystem:
    def __init__(self):
        # Policy already set with parameters
        # This is storing the objects, value returned
        self._employee_policies = {
            1: SalaryPolicy(3000),
            2: SalaryPolicy(1000),
            3: CommissionPolicy(1000, 100),
            4: HourlyPolicy(15),
            5: HourlyPolicy(9)
        }
    # Need a class associated with this
    def get_policy(self, policy_id):
        # Checking the policy
        policy = self._employee_policies.get(policy_id)
        if not policy:
            raise ValueError("Invalid policy ID")
        return policy

    # Must be passed in as a list
    def calculate_payroll(self, employees):
        print("calculating payroll")
        print("===========")
        for employee in employees:
            print(f'Payroll for : {employee.id} + {employee.name}')
            print(f'- Check Amount: {employee.calculate_payroll()}')
            if employee.address:
                print(f'Sent to Address: {employee.address}')
            print('')

# Base class to various other policies
# All other policies can derive from this

# Long term disability policy
class LTDPolicy:
    def __init__(self):
        self._base_policy = None

    def _check_base_policy(self):
        if not self._base_policy:
            raise RuntimeError('Base policy missing')

    def track_work(self, hours):
        self._check_base_policy()
        return self._check_base_policy()

    def calculate_payroll(self):
        self._check_base_policy()
        base_salary = self._base_policy.calculate_payroll()
        return base_salary * .6

    def apply_to_policy(self, base_policy):
        self._base_policy = base_policy




class PayrollPolicy:
    def __init__(self):
        self.hours_worked = 0

    def track_work(self, hours):
        self.hours_worked += hours


class SalaryPolicy(PayrollPolicy):
    def __init__(self, weekly_salary):
        super().__init__()
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary

class HourlyPolicy(PayrollPolicy):
    def __init__(self,  hour_rate):
        super().__init__()
        self.hour_rate = hour_rate

    def calculate_payroll(self):
        return self.hours_worked * self.hour_rate


class CommissionPolicy(SalaryPolicy):
    def __init__(self, weekly_salary, commission_per_sale):
        # Inherits from the other
        super().__init__(weekly_salary)
        self.commission_per_sale = commission_per_sale

    def commission(self):
        sales = self.hours_worked / 5
        return sales * self.commission_per_sale


    def calculate_payroll(self):
        fixed = super().calculate_payroll()
        return fixed + self.commission()

_payroll_system = _PayrollSystem()

def get_policy(policy_id):
    return _payroll_system.get_policy(policy_id)

def calculate_hours(employees):
    _payroll_system.calculate_payroll(employees)