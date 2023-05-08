from app.BruttoCalculator import BruttoCalculator

calculator = BruttoCalculator()


def settings(obj):
	calculator.clean_state()
	calculator.hour = obj['hour']
	if obj['s-npd'] == '0':
		calculator.NPD_setting = False
	if obj['s-citizen'] == '0':
		calculator.citizen = False
	if obj['s-add'] == '1':
		calculator.add_tax_setting = True
	if obj['s-floor'] == '0':
		calculator.floor_setting = False
	if obj['s-term'] == '1':
		calculator.agreement_term = True
	calculator.GPM_setting = int(obj['s-percent'])
	calculator.sodra_group = int(obj['s-group'])


def calculate_netto(obj):
	settings(obj)
	calculator.brutto = float(obj["brutto"])
	return calculator.run_calculation()


def calculate_brutto(obj):
	settings(obj)
	flag_netto = False
	netto = obj['netto']
	brutto = round(netto * 1.6529, 2)
	counter = 0
	result = {}
	while not flag_netto and counter < 30:
		calculator.brutto = brutto
		result = calculator.run_calculation()
		try_netto = result['amount-netto']
		if try_netto != netto:
			brutto = brutto - try_netto + netto
			counter += 1
		else:
			flag_netto = True
			return result
	return result


def calculate_netto_hour(obj):
	obj['brutto'] = round(obj['bruttoHour'] * obj['hour'])
	return calculate_netto(obj)


def calculate_brutto_hour(obj):
	obj['netto'] = round(obj['nettoHour'] * obj['hour'])
	return calculate_brutto(obj)