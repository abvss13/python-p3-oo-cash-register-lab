import io
import sys


from cash_register import CashRegister


class TestCashRegister:
    cash_register = CashRegister()
    cash_register_with_discount = CashRegister(20)

    def reset_register_totals(self):
        self.cash_register.total = 0
        self.cash_register_with_discount.total = 0

    def test_discount_attribute(self):
        '''Test the discount attribute.'''
        assert self.cash_register.discount == 0
        assert self.cash_register_with_discount.discount == 20

    def test_total_attribute(self):
        '''Test the total attribute.'''
        assert self.cash_register.total == 0
        assert self.cash_register_with_discount.total == 0

    def test_items_attribute(self):
        '''Test the items attribute.'''
        assert self.cash_register.items == []
        assert self.cash_register_with_discount.items == []

    # Define and implement your other test cases here...

if __name__ == '__main__':
    test_runner = TestCashRegister()
    test_runner.test_discount_attribute()
    test_runner.test_total_attribute()
    test_runner.test_items_attribute()
    # Call other test methods here...