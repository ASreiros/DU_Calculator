from app.BruttoCalculator import BruttoCalculator

calculator = BruttoCalculator()

def calculate_netto(obj):
	calculator.clean_state()
	calculator.brutto = float(obj["brutto"])
	return calculator.run_calculation()


def calculate_brutto(obj):
	calculator.clean_state()
	flag_netto = False
	netto = obj['netto']
	brutto = round(netto * 1.6529, 2)
	counter = 0
	result = {}
	while not flag_netto and counter < 30:
		calculator.brutto = brutto
		result = calculator.run_calculation()
		try_netto = result['netto']
		if try_netto != netto:
			brutto = brutto - try_netto + netto
			counter += 1
		else:
			flag_netto = True
			return result
	return result
