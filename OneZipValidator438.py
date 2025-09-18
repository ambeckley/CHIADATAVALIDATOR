import pandas as pd
from pydantic import BaseModel, Field, ConfigDict, ValidationError, constr
from typing import Optional
import numpy as np

class OneZipEnforced(BaseModel):
	model_config = ConfigDict(coerce_numbers_to_str=True, allow_inf_nan=True)
	orgid : Optional[int] = None
	chiacarrierspecificuniquememberid : Optional[int] = None
	memberzipcode_3_lds : Optional[int] = None
	memberstateorprovincelds : Optional[str] = Field(None, max_length=5) 
	calendaryear : Optional[int] = None
	submissionyear : Optional[int] = None 
	submissionmonth : Optional[str] = Field(None, max_length=2)




#https://github.com/Carobert85/pydantic_data_validation/blob/main/pydantic_data_validation_simple.ipynb
def validate_df_data(df: pd.DataFrame, model: BaseModel, index_offset: int = 2) -> tuple[list, list]:
	good_data = []
	bad_data = []
	df_rows = df.to_dict(orient='records')
	for index, row in enumerate(df_rows):
		try:
			model(**row)  #unpacks our dictionary into our keyword arguments
			good_data.append(row)  #appends valid data to a new list of dictionaries
		except ValidationError as e:
			# Adds all validation error messages associated with the error
			# and adds them to the dictionary
			row['Errors'] = [error_message['msg'] for error_message in e.errors()]
			# Python index starts at 0, excel at 1, and 1 row for the header in excel
			row['Error_row_num'] = index + index_offset#index + index_offset
			indexprinted = index + index_offset
			print("invalid row: "+ str(indexprinted))
			for i in e.errors():
				print(str(i['loc'])+', '+str(i['msg'])+', '+str(i['input']))
			#print([error_message['loc'] for error_message in e.errors()])
			#print([error_message['msg'] for error_message in e.errors()])
			#print([error_message['input'] for error_message in e.errors()])
			exit()
			print([error_message['msg'] for error_message in e.errors()])
			#print(row)
			bad_data.append(row)  #appends bad data to a different list of dictionaries
	return (good_data, bad_data)



#where to begin, starts at 0
index = 0
while index < 2089:
	filename = 'OneZipPart1_'+"%010d"% (index,)
	print("On file: "+ filename)
	df = pd.read_csv(filename, sep='*', names=['orgid','chiacarrierspecificuniquememberid','memberzipcode_3_lds','memberstateorprovincelds','calendaryear','submissionyear','submissionmonth'], 
				  dtype=str, header=None, low_memory=True)
	df = df.replace(np.nan, None)
	df = df.replace('----------', None)
	valid_data, invalid_data = validate_df_data(df, OneZipEnforced, index_offset=1)
	print(invalid_data)
	if invalid_data!=[]:
		print("Error")
		break
	outputFilename = 'FinishedOneZipPart1_'+"%010d"% (index,)
	index = index + 1
	df.to_csv(outputFilename, sep='*', index=False, header=False)

print("Done")
