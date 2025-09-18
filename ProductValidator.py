import pandas as pd
from pydantic import BaseModel, Field, ConfigDict, ValidationError, constr
from typing import Optional
import numpy as np

class ProductEnforced(BaseModel):
	model_config = ConfigDict(coerce_numbers_to_str=True, allow_inf_nan=True)
	releaseid : Optional[int] = None
	medicaidhsnindicator : Optional[bool] = None 
	linkingproductdelegate : Optional[bool] = None 
	submissionyearmonth : Optional[int] = None
	submissioncontrolid : Optional[int] = None
	productid : Optional[int] = None 
	orgid : Optional[int] = None
	linkingproductid : Optional[int] = None
	carrierlicensetype : Optional[str] = Field(None, max_length=3)
	productlineofbusinessmodel : Optional[str] = Field(None, max_length=2)
	insuranceplanmarketcleaned : Optional[str] = Field(None, max_length=4)
	productbenefittype : Optional[int] = None
	risktype : Optional[int] = None
	productstartdateyear : Optional[str] = Field(None, max_length=4)
	productstartdatemonth : Optional[str] = Field(None, max_length=2)
	productenddateyear : Optional[str] = Field(None, max_length=4)
	productenddatemonth : Optional[str] = Field(None, max_length=2)
	productactiveflagcleaned : Optional[int] = None
	annualperpersondeductiblecodecleaned : Optional[str] = Field(None, max_length=3)
	annualperfamilydeductiblecodecleaned : Optional[str] = Field(None, max_length=3)
	coordinatedcaremodel : Optional[int] = None
	naiccode : Optional[int] = None
	situs : Optional[str] = Field(None, max_length=2)



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
			
			print([error_message['msg'] for error_message in e.errors()])
			#print(row)
			bad_data.append(row)  #appends bad data to a different list of dictionaries
	return (good_data, bad_data)


index = 0
while index < 11:
	filename = 'ProductPart1_'+"%010d"% (index,)
	print("On file: "+ filename)
	
	df = pd.read_csv(filename, sep='*', names=['releaseid','medicaidhsnindicator','linkingproductdelegate','submissionyearmonth','submissioncontrolid','productid','orgid','linkingproductid','carrierlicensetype','productlineofbusinessmodel','insuranceplanmarketcleaned','productbenefittype','risktype','productstartdateyear','productstartdatemonth','productenddateyear','productenddatemonth','productactiveflagcleaned','annualperpersondeductiblecodecleaned','annualperfamilydeductiblecodecleaned','coordinatedcaremodel','naiccode','situs'], 
				  dtype=str, header=None, low_memory=True)
	df = df.replace(np.nan, None)
	df = df.replace('----------', None)

	valid_data, invalid_data = validate_df_data(df, ProductEnforced, index_offset=1)
	print(invalid_data)
	if invalid_data!=[]:
		print("Error")
		break
	outputFilename = 'FinishedProduct_'+"%010d"% (index,)
	index = index + 1
	df.to_csv(outputFilename, sep='*', index=False, header=False)

print("Done")
