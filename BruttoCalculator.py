

class BruttoCalculator:
	def __init__(self):
		self.brutto = 0
		self.netto = 0
		self.GPM = 0
		self.GPM_setting = 0  # (0:"Pilnai darbingas", 1:"Gaunu senatvės pensija" 2:"30-55 procentų darbingumo lygis"3:"0-25 procentų darbingumo lygis"4:Netaikyti GPM )
		self.SODRA = 0
		self.NPD = 0
		self.EMP = 0
		self.garant = 0
		self.longterm = 0
		self.incident = 0
		self.agreement_term_tax = 0
		self.sodra_floor_value = 0

	def run_calculation(self):
		self.calculate_NPD()
		self.calculate_GPM()
		print("-------------")


	def calculate_NPD(self):
		if self.GPM_setting == 0:
			if self.brutto <= 730:
				self.NPD = 540
			elif self.brutto <= 1704:
				self.NPD = 540 - 0.34*(self.brutto - 730)
			else:
				self.NPD = 400-0.18*(self.brutto - 642)
		elif self.GPM_setting == 1:
			self.NPD = 870
		elif self.GPM_setting == 2:
			self.NPD = 810
		elif self.GPM_setting == 3:
			self.NPD = 870
		else:
			self.NPD = 0

		if self.NPD < 0:
			self.NPD = 0
		else:
			self.NPD = round(self.NPD, 2)
		print("NPD:", self.NPD)

	def calculate_GPM(self):
		self.GPM = round((self.brutto - self.NPD)*0.2, 2)
		if self.GPM < 0:
			self.GPM = 0
		print("GPM:", self.GPM)
