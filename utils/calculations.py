import pandas as pd
import json
import argparse
import warnings
import os

def bmi_category(x):
	if x<18.4:
		return 'Underweight'
	elif 18.5<x<24.9:
		return 'Normal Weight'
	elif 25<x<29.9:
		return 'Overweight'
	elif 30<x<34.9:
		return 'Moderately obese'
	elif 35<x<39.9:
		return 'Severely obese'
	elif x>40:
		return 'Very severely obese'
	

def health_risk(x):
	if x<18.4:
		return 'Malnutrition risk'
	elif 18.5<x<24.9:
		return 'Low risk'
	elif 25<x<29.9:
		return 'Enhanced risk'
	elif 30<x<34.9:
		return 'Medium risk'
	elif 35<x<39.9:
		return 'High risk'
	elif x>40:
		return 'Very high risk'