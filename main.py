from BruttoCalculator import BruttoCalculator

calculator = BruttoCalculator()
flag = True
while flag:
	calculator.add_tax_setting = True
	calculator.brutto = float(input("Brutto:  "))
	calculator.run_calculation()

