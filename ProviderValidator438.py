import pandas as pd
from pydantic import BaseModel, Field, ConfigDict, ValidationError, constr
from typing import Optional
import numpy as np

class ProviderEnforced(BaseModel):
	model_config = ConfigDict(coerce_numbers_to_str=True, allow_inf_nan=True)
	nationalprovideridcleaned : Optional[str] = Field(None, max_length=10) 
	nationalprovider2idcleaned : Optional[str] = Field(None, max_length=10)
	releaseid : Optional[int] = None
	linkingproviderdelegate : Optional[bool] = None 
	cmsprovidertype : Optional[str] = Field(None, max_length=23)
	submissionyearmonth : Optional[int] = None
	submissioncontrolid : Optional[int] = None
	providerid : Optional[int] = None
	orgid : Optional[int] = None
	linkingproviderid : Optional[int] = None
	dobdateyear : Optional[str] = Field(None, max_length=4)
	zipcode_5_lds : Optional[str] = Field(None, max_length=5)
	taxonomycleaned : Optional[str] = None
	provideridcodecleaned : Optional[str] = None



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


index = 0
while index < 781:
	filename = 'ProviderPart1_'+"%010d"% (index,)
	print("On file: "+ filename)
	
	df = pd.read_csv(filename, sep='*', names=['nationalprovideridcleaned','nationalprovider2idcleaned','releaseid','linkingproviderdelegate','cmsprovidertype','submissionyearmonth','submissioncontrolid','providerid','orgid','linkingproviderid','dobdateyear','zipcode_5_lds','taxonomycleaned','provideridcodecleaned'], 
				  dtype=str, header=None, low_memory=True)
	df = df.replace(np.nan, None)
	df = df.replace('----------', None)

	valid_data, invalid_data = validate_df_data(df, ProviderEnforced, index_offset=1)
	print(invalid_data)
	if invalid_data!=[]:
		print("Error")
		break
	outputFilename = 'FinishedProvider_'+"%010d"% (index,)
	index = index + 1
	df.to_csv(outputFilename, sep='*', index=False, header=False)

print("Done")
