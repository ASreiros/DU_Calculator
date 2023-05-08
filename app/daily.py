from app import app
import pandas as pd


def provide_dict():
	df = pd.read_excel('app/static/excel/daily.xlsx')
	daily_dict = {row.Country: row.euro for (index, row) in df.iterrows()}
	return daily_dict

def count_daily(obj):
	allowance = float(obj['daily']) * int(obj['days'])
	answer = {
		'daily': obj['daily'],
		'days': obj['days'],
		'allowance': allowance
	}
	return answer
