import pandas as pd
from pydantic import BaseModel, Field, ConfigDict, ValidationError, constr
from typing import Optional
import numpy as np

class MemberEligEnforced(BaseModel):
	model_config = ConfigDict(coerce_numbers_to_str=True, allow_inf_nan=True)
	submissionmonth : Optional[str] = Field(None, max_length=2)
	submissionyear : Optional[str] = Field(None, max_length=4)
	membereligibilityid : Optional[int] = None 
	submissioncontrolid : Optional[int] = None 
	medicaidhsnindicator : Optional[bool] = None 
	memberlinkeid : Optional[int] = None 
	memberageyearsasofsubredacted : Optional[int] = None 
	linkorgidpv : Optional[int] = None 
	linkorgidpr : Optional[int] = None 
	orgid : Optional[int] = None 
	insurancetypecodeproduct : Optional[str] = Field(None, max_length=2) 
	coveragelevelcode : Optional[str] = Field(None, max_length=3) 
	individualrelationshipcodelds : Optional[str] = Field(None, max_length=10)
	membergendercleanedlds : Optional[str] = Field(None, max_length=1) 
	memberstateorprovincelds : Optional[str] = Field(None, max_length=2) 
	medicalcoverage : Optional[int] = None 
	prescriptiondrugcoverage : Optional[int] = None 
	dentalcoverage : Optional[int] = None 
	primaryinsuranceindicator : Optional[int] = None 
	coveragetype : Optional[str] = Field(None, max_length=3)
	marketcategorycode : Optional[str] = Field(None, max_length=4)
	specialcoverage : Optional[str] = Field(None, max_length=3)
	healthcarehomeassignedflag : Optional[int] = None 
	healthcarehomenumber_linkage_id : Optional[int] = None 
	healthcarehomenationalprovideridcleaned : Optional[str] = Field(None, max_length=10)
	productidnumber_linking_id : Optional[int] = None 
	productenrollmentstartdateyear : Optional[str] = Field(None, max_length=4) 
	productenrollmentstartdatemonth : Optional[str] = Field(None, max_length=2)
	productenrollmentenddateyear : Optional[str] = Field(None, max_length=4) 
	productenrollmentenddatemonth : Optional[str] = Field(None, max_length=2)
	purchasedthroughmassachusettsexchangeflag : Optional[int] = None 
	memberpcpid_linkage_id : Optional[int] = None 
	memberpcpeffectivedateyear : Optional[str] = Field(None, max_length=4)
	memberpcpeffectivedatemonth : Optional[str] = Field(None, max_length=2) 
	memberpcpterminationdateyear : Optional[str] = Field(None, max_length=4)
	memberpcpterminationdatemonth : Optional[str] = Field(None, max_length=2) 
	memberdeductible : Optional[float] = None
	memberdeductibleused : Optional[float] = None 
	behavioralhealthbenefitflag : Optional[int] = None 
	laboratorybenefitflag : Optional[int] = None 
	diseasemanagementenrolleeflag : Optional[int] = None 
	businesstypecode : Optional[int] = None 
	lastactivitydate : Optional[int] = None 
	lastactivitydateyear : Optional[str] = Field(None, max_length=4)
	lastactivitydatemonth : Optional[str] = Field(None, max_length=2)
	benefitstatus : Optional[str] = Field(None, max_length=1)
	cobrastatus : Optional[int] = None 
	fullyinsuredmember : Optional[int] = None 
	medicarecode : Optional[str] = Field(None, max_length=1)
	chiacarrierspecificuniquememberid : Optional[int] = None 
	subscriberstateorprovincelds : Optional[str] = Field(None, max_length=2)
	medicaldeductible : Optional[float] = None
	pharmacydeductible : Optional[float] = None
	medicalandpharmacydeductible : Optional[float] = None
	behavioralhealthdeductible : Optional[float] = None
	dentaldeductible : Optional[float] = None
	visiondeductible : Optional[float] = None 
	chiacarrierspecificuniquesubscriberid : Optional[int] = None 
	visionbenefit : Optional[int] = None 
	actuarialvalue : Optional[float] = None
	metallevel : Optional[int] = None 
	coinsurancemaximum : Optional[int] = None 
	monthlypremium : Optional[float] = None 
	attributedpcpproviderid_linkage_id : Optional[int] = None 
	tmeproviderorgid : Optional[int] = None 
	riskadjustmentcoveredbenefitplan : Optional[int] = None 
	billablemember : Optional[int] = None 
	memberbenefitplancontractenrollmentstartdateyear : Optional[str] = Field(None, max_length=4)
	memberbenefitplancontractenrollmentstartdatemonth : Optional[str] = Field(None, max_length=2) 
	memberbenefitplancontractenrollmentenddateyear : Optional[str] = Field(None, max_length=4)
	memberbenefitplancontractenrollmentenddatemonth : Optional[str] = Field(None, max_length=2)
	tmeglobalbudgetpaymentindicator : Optional[int] = None 
	totalcontribution : Optional[float] = None
	apcdidcode : Optional[str] = Field(None, max_length=1)




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



#where to begin, starts at 0
index = 0
while index < 2895:
	filename = 'MemberEligibilityPart1_'+"%010d"% (index,)
	print("On file: "+ filename)
	df = pd.read_csv(filename, sep='*', names=['submissionmonth','submissionyear','membereligibilityid','submissioncontrolid','medicaidhsnindicator','memberlinkeid','memberageyearsasofsubredacted','linkorgidpv','linkorgidpr','orgid','insurancetypecodeproduct','coveragelevelcode','individualrelationshipcodelds','membergendercleanedlds','memberstateorprovincelds','medicalcoverage','prescriptiondrugcoverage','dentalcoverage','primaryinsuranceindicator','coveragetype','marketcategorycode','specialcoverage','healthcarehomeassignedflag','healthcarehomenumber_linkage_id','healthcarehomenationalprovideridcleaned','productidnumber_linking_id','productenrollmentstartdateyear','productenrollmentstartdatemonth','productenrollmentenddateyear','productenrollmentenddatemonth','purchasedthroughmassachusettsexchangeflag','memberpcpid_linkage_id','memberpcpeffectivedateyear','memberpcpeffectivedatemonth','memberpcpterminationdateyear','memberpcpterminationdatemonth','memberdeductible','memberdeductibleused','behavioralhealthbenefitflag','laboratorybenefitflag','diseasemanagementenrolleeflag','businesstypecode','lastactivitydate','lastactivitydateyear','lastactivitydatemonth','benefitstatus','cobrastatus','fullyinsuredmember','medicarecode','chiacarrierspecificuniquememberid','subscriberstateorprovincelds','medicaldeductible','pharmacydeductible','medicalandpharmacydeductible','behavioralhealthdeductible','dentaldeductible','visiondeductible','chiacarrierspecificuniquesubscriberid','visionbenefit','actuarialvalue','metallevel','coinsurancemaximum','monthlypremium','attributedpcpproviderid_linkage_id','tmeproviderorgid','riskadjustmentcoveredbenefitplan','billablemember','memberbenefitplancontractenrollmentstartdateyear','memberbenefitplancontractenrollmentstartdatemonth','memberbenefitplancontractenrollmentenddateyear','memberbenefitplancontractenrollmentenddatemonth','tmeglobalbudgetpaymentindicator','totalcontribution','apcdidcode'], 
				  dtype=str, header=None, low_memory=True)
	df = df.replace(np.nan, None)
	df = df.replace('----------', None)
	valid_data, invalid_data = validate_df_data(df, MemberEligEnforced, index_offset=1)
	print(invalid_data)
	if invalid_data!=[]:
		print("Error")
		break
	outputFilename = 'FinishedMemberEligibility_'+"%010d"% (index,)
	index = index + 1
	df.to_csv(outputFilename, sep='*', index=False, header=False)

print("Done")
