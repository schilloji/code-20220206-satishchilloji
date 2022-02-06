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

		df['HeightM']=df['HeightCm'].apply(lambda x: x/100)
		df['BMI']=df['WeightKg']/df['HeightM']
		df['BMI_Category']=df['BMI'].apply(lambda x: bmi_category(x))
		df['Health_Risk']=df['BMI'].apply(lambda x: health_risk(x))

		return df



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
	print(data_.load())

	



	










