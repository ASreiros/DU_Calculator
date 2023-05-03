
class BruttoCalculator:
	def __init__(self):
		self.brutto = 0
		self.netto = 0

		self.NPD = 0
		self.GPM = 0
		self.GPM_setting = 0  # (0:"Pilnai darbingas", 1:"Gaunu senatvės pensija" 2:"30-55 procentų darbingumo lygis"3:"0-25 procentų darbingumo lygis"4:Netaikyti GPM )

		self.citizen = True # Ar yra Lietuvos pilietis. įtakuoja PSD
		# self.add_tax_setting # True 3% / False 0%
		self.PSD = 0
		self.VSD = 0
		self.add_tax_setting = False # Ar taikyti pensijos kaupima itakuoja self.add_tax
		self.add_tax = 0
		self.SODRA = 0
		self.EMP = 0
		self.garant = 0
		self.longterm = 0
		self.incident = 0
		self.agreement_term_tax = 0
		self.sodra_floor_value = 0

	def clean_state(self):
		self.brutto = 0
		self.netto = 0
		self.NPD = 0
		self.GPM = 0
		self.GPM_setting = 0
		self.citizen = True
		self.PSD = 0
		self.VSD = 0
		self.add_tax_setting = False
		self.add_tax = 0
		self.SODRA = 0
		self.EMP = 0
		self.garant = 0
		self.longterm = 0
		self.incident = 0
		self.agreement_term_tax = 0
		self.sodra_floor_value = 0

	def run_calculation(self):
		self.calculate_GPM()
		self.caclucate_Sodra()
		self.netto = self.brutto - self.GPM - self.SODRA
		return {
			'brutto': round(self.brutto, 2),
			'netto': round(self.netto, 2),
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
			"term": self.agreement_term_tax,
			"floor": self.sodra_floor_value,
			"emp": self.EMP,
			}
		}

	def calculate_NPD(self):
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
		print("NPD:", self.NPD)

	def calculate_GPM(self):
		self.calculate_NPD()
		self.GPM = round((self.brutto - self.NPD)*0.2, 2)
		if self.GPM < 0:
			self.GPM = 0
		print("GPM:", self.GPM)


	def calculate_add_tax(self):
		if self.add_tax_setting:
			self.add_tax = round(self.brutto * 0.03, 2)
		else:
			self.add_tax = 0
		print("add tax:", self.add_tax)

	def calculate_VSD(self):
		self.VSD = round(self.brutto*0.1252,2)
		if self.VSD > 11298.20:
			self.VSD = 11298.20
		print("VSD", self.VSD)

	def calculate_PSD(self):
		if self.citizen:
			self.PSD = round(self.brutto*0.0698, 2)
		else:
			self.PSD = 0
		print("PSD:", self.PSD)

	def caclucate_Sodra(self):
		self.calculate_add_tax()
		self.calculate_VSD()
		self.calculate_PSD()
		self.SODRA = round(self.add_tax + self.VSD + self.PSD, 2)
		print("SODRA:", self.SODRA)
