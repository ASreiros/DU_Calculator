
class BruttoCalculator:
	def __init__(self):
		self.brutto = 0
		self.netto = 0
		self.tbrutto = 0
		self.total = 0
		self.hour = 160

		self.NPD = 0
		self.GPM = 0
		self.NPD_setting = True
		self.GPM_setting = 0  # (0:"Pilnai darbingas", 1:"Gaunu senatvės pensija" 2:"30-55 procentų darbingumo lygis"3:"0-25 procentų darbingumo lygis"4:Netaikyti GPM )
		self.citizen = True # Ar yra Lietuvos pilietis. įtakuoja PSD
		self.add_tax_setting = False # Ar taikyti pensijos kaupima itakuoja self.add_tax 0.
		self.agreement_term = False
		self.floor_setting = True
		self.sodra_group = 0

		self.PSD = 0
		self.VSD = 0
		self.add_tax = 0
		self.SODRA = 0
		self.emp = 0
		self.garant = 0
		self.longterm = 0
		self.incident = 0
		self.term_tax = 0
		self.sodra_floor_value = 0

	def clean_state(self):
		self.brutto = 0
		self.netto = 0
		self.tbrutto = 0
		self.total = 0

		self.NPD = 0
		self.GPM = 0
		self.NPD_setting = True
		self.GPM_setting = 0
		self.citizen = True
		self.add_tax_setting = False
		self.agreement_term = False
		self.floor_setting = True
		self.sodra_group = 0

		self.PSD = 0
		self.VSD = 0
		self.add_tax = 0
		self.SODRA = 0
		self.emp = 0
		self.garant = 0
		self.longterm = 0
		self.incident = 0
		self.term_tax = 0
		self.sodra_floor_value = 0

	def run_calculation(self):
		self.calculate_GPM()
		self.caclucate_Sodra()
		self.netto = self.brutto - self.GPM - self.SODRA
		self.calculate_employer_taxes()
		self.total = round(self.brutto + self.emp, 2)
		return {
			'amount-brutto': round(self.brutto, 2),
			'amount-netto': round(self.netto, 2),
			'amount-brutto-hour': round(self.brutto/self.hour, 2),
			'amount-netto-hour': round(self.netto/self.hour, 2),
			'amount-total': self.total,
			'NPD': self.NPD,
			"sodra": self.SODRA,
			'taxes': {
			'GPM': self.GPM,
			'PSD': self.PSD,
			'VSD': self.VSD,
			'add_tax': self.add_tax,
			"garant": self.garant,
			"longterm": self.longterm,
			"incident": self.incident,
			"term": self.term_tax,
			"floor": self.sodra_floor_value,
			"emp": self.emp,
			}
		}

	def calculate_NPD(self):
		if self.NPD_setting:
			if self.GPM_setting == 0:
				if self.brutto <= 840:
					self.NPD = 625
				elif self.brutto <= 1704:
					self.NPD = 625 - 0.42*(self.brutto - 840)
				else:
					self.NPD = 400-0.18*(self.brutto - 642)
			elif self.GPM_setting == 1:
				self.NPD = 1005
			elif self.GPM_setting == 2:
				self.NPD = 935
			elif self.GPM_setting == 3:
				self.NPD = 1005
			else:
				self.NPD = 0

			if self.NPD < 0:
				self.NPD = 0
			else:
				self.NPD = round(self.NPD, 2)

	def calculate_GPM(self):
		self.calculate_NPD()
		self.GPM = round((self.brutto - self.NPD)*0.2, 2)
		if self.GPM < 0:
			self.GPM = 0


	def calculate_add_tax(self):
		if self.add_tax_setting:
			self.add_tax = round(self.brutto * 0.03, 2)
		else:
			self.add_tax = 0

	def calculate_VSD(self):
		self.VSD = round(self.brutto*0.1252, 2)
		if self.VSD > 11298.20:
			self.VSD = 11298.20

	def calculate_PSD(self):
		if self.citizen:
			self.PSD = round(self.brutto*0.0698, 2)
		else:
			self.PSD = 0

	def caclucate_Sodra(self):
		self.calculate_add_tax()
		self.calculate_VSD()
		self.calculate_PSD()
		self.SODRA = round(self.add_tax + self.VSD + self.PSD, 2)

	def calculate_employer_taxes(self):
		if 840 > self.brutto > 0:
			self.tbrutto = 840
		elif self.brutto > 840:
			self.tbrutto = self.brutto
		self.calculate_garant()
		self.calculate_term_tax()
		self.calculate_longterm()
		self.calculate_incident()
		self.calculate_sodra_floor()
		self.emp = round(self.garant + self.term_tax + self.longterm + self.incident + self.sodra_floor_value, 2)



	def calculate_garant(self):
		self.garant = round(self.tbrutto * 0.0016, 2)

	def calculate_term_tax(self):
		if self.agreement_term:
			coeficent = 0.0203
		else:
			coeficent = 0.0131
		self.term_tax = round(self.tbrutto * coeficent, 2)

	def calculate_longterm(self):
		self.longterm = round(self.tbrutto * 0.0016, 2)

	def calculate_incident(self):
		s_gr = 0
		if self.sodra_group == 0:
			s_gr = 0.0014
		elif self.sodra_group == 1:
			s_gr = 0.0047
		elif self.sodra_group == 2:
			s_gr = 0.007
		elif self.sodra_group == 3:
			s_gr = 0.014
		self.incident = round(self.tbrutto * s_gr, 2)

	def calculate_sodra_floor(self):
		if self.floor_setting is True and self.tbrutto != self.brutto:
			if self.citizen:
				base = 163.80
			else:
				base = 105.17
			self.sodra_floor_value = round(base - self.PSD - self.VSD, 2)
			if self.sodra_floor_value < 0:
				self.sodra_floor_value = 0





