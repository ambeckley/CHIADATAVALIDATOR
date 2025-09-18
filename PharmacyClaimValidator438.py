import pandas as pd
from pydantic import BaseModel, Field, ConfigDict, ValidationError, constr
from typing import Optional
import numpy as np

class PharmacyClaimEnforced(BaseModel):
	model_config = ConfigDict(coerce_numbers_to_str=True, allow_inf_nan=True)
	prescribingphysiciannpicleaned : Optional[str] = Field(None, max_length=10)
	submissionyear : Optional[str] = Field(None, max_length=4)
	pharmacyclaimid : Optional[int] = None
	submissioncontrolid : Optional[int] = None
	incurreddateyear : Optional[str] = Field(None, max_length=4)
	medicaidhsnindicator : Optional[bool] = None 
	memberlinkeid : Optional[int] = None
	memberageatserviceinyearsredacted : Optional[int] = None 
	versionindicator : Optional[int] = None 
	linkorgidme : Optional[int] = None
	linkorgidpv : Optional[int] = None
	linkorgidpr : Optional[int] = None 
	orgid : Optional[int] = None
	insurancetypecodeproduct : Optional[str] = Field(None, max_length=2)
	chiapayerclaimcontrolnumber : Optional[int] = None
	linecounter : Optional[int] = None
	versionnumber : Optional[int] = None
	individualrelationshipcodelds : Optional[str] = Field(None, max_length=10) 
	membergendercleanedlds : Optional[str] = Field(None, max_length=1)
	memberstatelds : Optional[str] = Field(None, max_length=2) 
	dateserviceapprovedapdateyear : Optional[str] = Field(None, max_length=4)
	nationalpharmacyidnumbercleaned : Optional[str] = Field(None, max_length=10)
	pharmacylocationstatelds : Optional[str] = Field(None, max_length=7)  
	pharmacylocationzipcode_3_lds : Optional[str] = Field(None, max_length=3)
	claimstatuscleaned : Optional[str] = Field(None, max_length=2)
	drugcodecleaned : Optional[str] = Field(None, max_length=11) 
	newprescriptionorrefillcleaned : Optional[str] = Field(None, max_length=3) 
	genericdrugindicatorcleaned : Optional[str] = Field(None, max_length=2)
	dispenseaswrittencode : Optional[int] = None 
	compounddrugindicatorcleaned : Optional[int] = None
	dateprescriptionfilledyear : Optional[str] = Field(None, max_length=4)
	quantitydispensed : Optional[str] = Field(None, max_length=10)
	quantitydispensed_decimal : Optional[float] = None 
	dayssupply : Optional[float] = None 
	chargeamountcleaned : Optional[float] = None 
	paidamountcleaned : Optional[float] = None 
	ingredientcostlistprice : Optional[float] = None 
	postageamountclaimed : Optional[float] = None
	dispensingfeecleaned : Optional[float] = None
	copayamountcleaned : Optional[float] = None
	coinsuranceamount : Optional[float] = None
	deductibleamount : Optional[float] = None
	prescribingproviderid_linkage_id : Optional[int] = None 
	prescribingphysicianstatelds : Optional[str] = Field(None, max_length=7)
	prescribingphysicianzipcode_3_lds : Optional[str] = Field(None, max_length=3)
	productidnumber_linkage_id : Optional[int] = None
	mailorderpharmacy : Optional[int] = None
	recipientpcpid_linkage_id : Optional[int] = None
	singlemultiplesourceindicator : Optional[int] = None
	paiddateyear : Optional[int] = None
	dateprescriptionwrittenyear : Optional[int] = None
	otherinsurancepaidamountcleaned : Optional[str] = Field(None, max_length=10)
	allowedamountcleaned : Optional[str] = Field(None, max_length=11) 
	memberselfpayamount : Optional[str] = Field(None, max_length=10)
	rebateindicator : Optional[int] = None
	statesalestax : Optional[str] = Field(None, max_length=10)
	delegatedbenefitadministratororganizationidcleaned : Optional[str] = Field(None, max_length=6)
	formularycode : Optional[int] = None
	routeofadministrationcleaned : Optional[str] = Field(None, max_length=2)
	drugunitofmeasure : Optional[str] = Field(None, max_length=3)
	chiacarrierspecificuniquememberid : Optional[int] = None
	chiacarrierspecificuniquesubscriberid : Optional[int] = None
	claimlinetypecleaned : Optional[str] = Field(None, max_length=1) 
	chiaformerclaimnumber : Optional[int] = None 
	medicareindicator : Optional[int] = None
	diagnosiscleaned : Optional[str] = Field(None, max_length=7)
	icdindicator : Optional[str] = Field(None, max_length=1) 
	deniedflag : Optional[int] = None
	paymentarrangementtype : Optional[str] = Field(None, max_length=2)
	apcdidcode : Optional[str] = Field(None, max_length=1)
	coordinationofbenefitstplliabilityamount : Optional[str] = Field(None, max_length=10)
	claimlinepaidflag : Optional[int] = None



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
			#print(e.errors())
			for i in e.errors():
				print(str(i['loc'])+', '+str(i['msg'])+', '+str(i['input']))
			#print([error_message['loc'] for error_message in e.errors()])
			#print([error_message['msg'] for error_message in e.errors()])
			#print([error_message['input'] for error_message in e.errors()])
			exit()
			#print(row)
			bad_data.append(row)  #appends bad data to a different list of dictionaries
	return (good_data, bad_data)



index = 0
while index < 9574:
	filename = 'PharmacyClaimPart1_'+"%010d"% (index,)
	print("On file: "+ filename)
	
	df = pd.read_csv(filename, sep='*', names=['prescribingphysiciannpicleaned','submissionyear','pharmacyclaimid','submissioncontrolid','incurreddateyear','medicaidhsnindicator','memberlinkeid','memberageatserviceinyearsredacted','versionindicator','linkorgidme','linkorgidpv','linkorgidpr','orgid','insurancetypecodeproduct','chiapayerclaimcontrolnumber','linecounter','versionnumber','individualrelationshipcodelds','membergendercleanedlds','memberstatelds','dateserviceapprovedapdateyear','nationalpharmacyidnumbercleaned','pharmacylocationstatelds','pharmacylocationzipcode_3_lds','claimstatuscleaned','drugcodecleaned','newprescriptionorrefillcleaned','genericdrugindicatorcleaned','dispenseaswrittencode','compounddrugindicatorcleaned','dateprescriptionfilledyear','quantitydispensed','quantitydispensed_decimal','dayssupply','chargeamountcleaned','paidamountcleaned','ingredientcostlistprice','postageamountclaimed','dispensingfeecleaned','copayamountcleaned','coinsuranceamount','deductibleamount','prescribingproviderid_linkage_id','prescribingphysicianstatelds','prescribingphysicianzipcode_3_lds','productidnumber_linkage_id','mailorderpharmacy','recipientpcpid_linkage_id','singlemultiplesourceindicator','paiddateyear','dateprescriptionwrittenyear','otherinsurancepaidamountcleaned','allowedamountcleaned','memberselfpayamount','rebateindicator','statesalestax','delegatedbenefitadministratororganizationidcleaned','formularycode','routeofadministrationcleaned','drugunitofmeasure','chiacarrierspecificuniquememberid','chiacarrierspecificuniquesubscriberid','claimlinetypecleaned','chiaformerclaimnumber','medicareindicator','diagnosiscleaned','icdindicator','deniedflag','paymentarrangementtype','apcdidcode','coordinationofbenefitstplliabilityamount','claimlinepaidflag'], 
				  dtype=str, header=None, low_memory=True)
	df = df.replace(np.nan, None)
	df = df.replace('----------', None)

	valid_data, invalid_data = validate_df_data(df, PharmacyClaimEnforced, index_offset=1)
	print(invalid_data)
	if invalid_data!=[]:
		print("Error")
		break
	outputFilename = 'FinishedPharmacyClaim_'+"%010d"% (index,)
	index = index + 1
	df.to_csv(outputFilename, sep='*', index=False, header=False)

print("Done")
