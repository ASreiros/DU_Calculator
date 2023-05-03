from BruttoCalculator import BruttoCalculator

calculator = BruttoCalculator()
flag = True
while flag:
	# calculator.brutto = float(input("Brutto:  "))
	# print("netto:", calculator.run_calculation())

	flag_netto = False
	netto = float(input("Netto:  "))
	brutto = round(netto * 1.6529, 2)
	counter = 0
	while not flag_netto and counter < 30:
		calculator.brutto = brutto
		tryNetto = calculator.run_calculation()
		if tryNetto != netto:
			brutto = brutto - tryNetto + netto
			counter += 1
			print("counter", counter)
		else:
			flag_netto = True
			print("brutto: ", brutto)
