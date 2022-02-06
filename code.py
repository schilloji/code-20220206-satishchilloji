import pandas as pd
import json
import argparse
import warnings
import os


## Load the json data

'''class loadjson(dataset):

	def __init__(self,data):
		self.data=data


	def load(self):'''


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
	print(json_df)


	










