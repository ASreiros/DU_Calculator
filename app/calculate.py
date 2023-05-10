from app.BruttoCalculator import BruttoCalculator
from fpdf import FPDF

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



def create_pdf():
	pdf = FPDF()
	pdf.add_page()
	pdf.set_margins(30, 10, 30)
	pdf.add_font(fname='app/static/font/DejaVuSansCondensed.ttf', family='dejavu', uni=True)
	pdf.set_font('dejavu', size=14)
	sodra_group = ['I grupė', 'II grupė', 'III grupė', 'IV grupė']
	work_group = ['Pilnai darbingas', 'Senatvės pensija', '30-55% darb.', '0-25% darb.']
	pdf.write_html(f"""
	  <h2 align="center">Atlyginimo skaičioklė</h2>
	  <section>
	    <h3 align="center">Resultatai</h3>
	    <table width="100%" align="center">
			  <thead>
			  </thead>
			  <tbody>
				<tr>
				  <td width="70%">Suma sutartyje:</td>
				  <td width="30%">{calculator.brutto}</td>
				</tr>
				<tr>
				  <td>Suma į rankas:</td>
				  <td>{round(calculator.netto, 2)}</td>
				</tr>
				<tr>
				  <td>Darbo vietos kaina:</td>
				  <td>{calculator.total}</td>
				</tr>
			  </tbody>
			</table>
	    <h3 align="center">Darbuotojo mokesčiai</h3>
	    <table width="100%" align="center">
		  <thead>
		  </thead>
		  <tbody>
				<tr>
				  <td width="70%">GPM</td>
				  <td width="30%">{calculator.GPM}</td>
				</tr>
				<tr>
				  <td>PSD</td>
				  <td>{calculator.PSD}</td>
				</tr>
				<tr>
				  <td>VSD</td>
				  <td>{calculator.VSD}</td>
				</tr>
				<tr>
				  <td>Papildoma įmoka pensijos kaupimui </td>
				  <td>{calculator.add_tax}</td>
				</tr>
		  </tbody>
		</table>
	    <h3 align="center">Darbdavio mokesčiai</h3>
	    	<table width="100%" align="center">
			  <thead>
			  </thead>
			  <tbody>
				<tr>
				  <td width="70%">Garantinis fondas</td>
				  <td width="30%">{calculator.garant}</td>
				</tr>
				<tr>
				  <td>Ilgalaikio darbo išmokų fondas</td>
				  <td>{calculator.longterm}</td>
				</tr>
				<tr>
				  <td>Nelaimingų atsitikimų darbe draudimas</td>
				  <td>{calculator.incident}</td>
				</tr>
				<tr>
				  <td>Nedarbo socialinis draudimas</td>
				  <td>{calculator.term_tax}</td>
				</tr>
				<tr>
				  <td>Mokesčio suma dėl Sodros 'grindų'</td>
				  <td>{calculator.sodra_floor_value}</td>
				</tr>
				<tr>
				  <td>Viso</td>
				  <td>{calculator.emp}</td>
				</tr>
			  </tbody>
			</table>
	    <h3 align="center">Pritaikyti nustatymai</h3>
	    	<table width="100%" align="center">
			  <thead>
			  </thead>
			  <tbody>
				<tr>
				  <td width="70%">Ar skaičiuoti NPD?</td>
				  <td width="30%">{'Taip' if calculator.NPD_setting is True else 'Ne' }</td>
				</tr>
				<tr>
				  <td>Papildoma pensijos įmoka</td>
				  <td>{'3%' if calculator.add_tax_setting is True else 'Ne' }</td>
				</tr>
				<tr>
				  <td>Darbingumas</td>
				  <td>{work_group[calculator.GPM_setting]}</td>
				</tr>
				<tr>
					<td>Ar yra Lietuvos pilietis</td>
				  	<td>{'Taip' if calculator.citizen is True else 'Ne' }</td>
				</tr>
				<tr>
				  	<td>Terminuota sutartis </td>
				  	<td>{'Taip' if calculator.agreement_term is True else 'Ne' }</td>
				</tr>
				<tr>
					<td>Sodros grindys taikomos?</td>
				  	<td>{'Taip' if calculator.floor_setting is True else 'Ne' }</td>
				</tr>
				<tr>
				  <td>Nelaimingų atsitikimų darbe grupė</td>
				  <td>{sodra_group[calculator.sodra_group]}</td>
				</tr>
			  </tbody>
			</table>
	    
	  </section>
	""")
	name = 'paskaičiavimas.pdf'
	pdf.output(f"app/{name}")
	return name
