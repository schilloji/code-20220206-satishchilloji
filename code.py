from cmath import sqrt
import pandas as pd
import json
import argparse
import warnings
import os

from utils.calculations import bmi_category,health_risk

## Load the json data

class loadjson:

	def __init__(self,data):
		self.data=data


	def load(self):
		df=self.data

		df['Height_mt2']=df['HeightCm'].apply(lambda x: (x/100)*(x/100))
		df['BMI']=df['WeightKg']/df['Height_mt2']
		df['BMI_Category']=df['BMI'].apply(lambda x: bmi_category(x)) # Calling the functions from the calculations
		df['Health_Risk']=df['BMI'].apply(lambda x: health_risk(x)) # Calling the functions from the calculations
		df.to_csv('data/helth_risk.csv',index=False)
		Overweight=len(df[df['BMI_Category']=='Overweight'])
		return Overweight

if __name__=='__main__':
	warnings.filterwarnings("ignore")
	_path=os.getcwd()
	parser=argparse.ArgumentParser()
	parser.add_argument('--json_path',help='enter path to the json file')
	args=parser.parse_args()

	file=args.json_path
	file_path=os.path.join(_path,file)


	with open(file_path) as json_file:
		json_data=json.load(json_file)

	json_df=pd.json_normalize(json_data)

	data_=loadjson(json_df)
	Overweight=data_.load()
	print(f'There are {Overweight} Overweight people in the given data set')

	



	










