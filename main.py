from BruttoCalculator import BruttoCalculator

calculator = BruttoCalculator()
flag = True
while flag:
	calculator.brutto = float(input("Brutto:  "))
	calculator.run_calculation()

