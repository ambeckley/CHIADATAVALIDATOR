
import pandas as pd
from pydantic import BaseModel, Field, ConfigDict, ValidationError, constr
from typing import Optional
import numpy as np


class MedicalClaimEnforced(BaseModel):
	model_config = ConfigDict(coerce_numbers_to_str=True, allow_inf_nan=True)
	nationalserviceprovideridcleaned : Optional[str] = Field(None, max_length=10) 
	nationalbillingprovideridcleaned : Optional[str] = Field(None, max_length=10)
	nationalprovideridplanrenderingcleaned : Optional[str] = Field(None, max_length=10)
	submissionyear : Optional[int] = None
	medicalclaimid : Optional[int] = None
	submissioncontrolid : Optional[int] = None
	incurredyear : Optional[str] = None
	versionindicator : Optional[int] = None
	highestversiondenied : Optional[int] = None
	highestversionindicator : Optional[int] = None
	medicaidhsnindicator : Optional[bool] = None
	fullydeniedclaim : Optional[int] = None
	memberlinkeid : Optional[int] = None
	memberageatserviceinyearsredacted : Optional[int]= None 
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
	memberstateorprovincelds : Optional[str] = Field(None, max_length=2)
	dateserviceapprovedapdateyear : Optional[str] = Field(None, max_length=4) 
	admissiondateyear : Optional[str] = Field(None, max_length=4) 
	admissiontype : Optional[str] = Field(None, max_length=1)
	admissionsource : Optional[str] = Field(None, max_length=1)
	dischargestatuscleaned : Optional[str] = Field(None, max_length=2)
	serviceprovidernumber_linkage_id : Optional[int] = None
	serviceproviderentitytypequalifier : Optional[int] = None
	serviceprovidersuffix : Optional[str] = Field(None, max_length=1)
	serviceproviderspecialtycleaned : Optional[str] = Field(None, max_length=10)
	serviceproviderstatelds : Optional[str] = Field(None, max_length=2)
	serviceproviderzipcode_3_lds : Optional[str] = Field(None, max_length=3)
	typeofbillonfacilityclaims : Optional[str] = Field(None, max_length=2)
	siteofserviceonnsfcms1500claimscleaned : Optional[str] = Field(None, max_length=2)
	claimstatus : Optional[str] = Field(None, max_length=2)
	admittingdiagnosiscleaned : Optional[str] = Field(None, max_length=7)
	ecodecleaned : Optional[str] = Field(None, max_length=7)
	principaldiagnosiscleaned : Optional[str] = Field(None, max_length=7)
	otherdiagnosis1cleaned : Optional[str] = Field(None, max_length=7)
	otherdiagnosis2cleaned : Optional[str] = Field(None, max_length=7)
	otherdiagnosis3cleaned : Optional[str] = Field(None, max_length=7)
	otherdiagnosis4cleaned : Optional[str] = Field(None, max_length=7)
	otherdiagnosis5cleaned : Optional[str] = Field(None, max_length=7)
	otherdiagnosis6cleaned : Optional[str] = Field(None, max_length=7)
	otherdiagnosis7cleaned : Optional[str] = Field(None, max_length=7)
	otherdiagnosis8cleaned : Optional[str] = Field(None, max_length=7)
	otherdiagnosis9cleaned : Optional[str] = Field(None, max_length=7)
	otherdiagnosis10cleaned : Optional[str] = Field(None, max_length=7)
	otherdiagnosis11cleaned : Optional[str] = Field(None, max_length=7)
	otherdiagnosis12cleaned : Optional[str] = Field(None, max_length=7)
	revenuecodecleaned : Optional[str] = Field(None, max_length=4)
	procedurecodecleaned : Optional[str] = Field(None, max_length=10)
	proceduremodifier1 : Optional[str] = Field(None, max_length=2)
	proceduremodifier2 : Optional[str] = Field(None, max_length=2)
	icdcmprocedurecodecleaned : Optional[str] = Field(None, max_length=7)
	dateofservicefromyear : Optional[str] = Field(None, max_length=4)
	dateofservicetoyear : Optional[str] = Field(None, max_length=4)
	quantity : Optional[int] = None
	chargeamountcleaned : Optional[float] = None
	paidamountcleaned : Optional[float] = None
	prepaidamountcleaned : Optional[float] = None 
	copayamountcleaned : Optional[float] = None
	coinsuranceamount : Optional[float] = None
	deductibleamount : Optional[float] = None
	dischargedateyear : Optional[str] = Field(None, max_length=4)
	billingprovidernumber_linkage_id : Optional[int] = None
	productidnumber_linkage_id : Optional[int] = None
	capitatedencounterflag : Optional[str] = Field(None, max_length=1)
	othericdcmprocedurecode1cleaned : Optional[str] = Field(None, max_length=7)
	othericdcmprocedurecode2cleaned : Optional[str] = Field(None, max_length=7)
	othericdcmprocedurecode3cleaned : Optional[str] = Field(None, max_length=7)
	othericdcmprocedurecode4cleaned : Optional[str] = Field(None, max_length=7)
	othericdcmprocedurecode5cleaned : Optional[str] = Field(None, max_length=7)
	othericdcmprocedurecode6cleaned : Optional[str] = Field(None, max_length=7)
	paiddateyear : Optional[str] = Field(None, max_length=4)
	coinsurancedays : Optional[int] = None
	covereddays : Optional[int] = None
	noncovereddays : Optional[int] = None 
	typeofclaimcleaned : Optional[str] = Field(None, max_length=3)
	coordinationofbenefitstplliabilityamount : Optional[str] = Field(None, max_length=10)
	otherinsurancepaidamountcleaned : Optional[float] = None
	medicarepaidamountcleaned : Optional[float] = None
	allowedamountcleaned : Optional[float] = None
	noncoveredamountcleaned : Optional[float] = None
	delegatedbenefitadministratororganizationidcleaned : Optional[int] = None
	icdindicator : Optional[str] = Field(None, max_length=1)
	proceduremodifier3 : Optional[str] = Field(None, max_length=2)
	proceduremodifier4 : Optional[str] = Field(None, max_length=2)
	diagnosticpointer : Optional[str] = Field(None, max_length=4)
	referringproviderid_linkage_id : Optional[int] = None
	paymentarrangementtypecleaned : Optional[str] = None
	excludedexpensescleaned : Optional[str] = Field(None, max_length=10)
	medicareindicator : Optional[int] = None
	withholdamount : Optional[float] = None
	referralindicator : Optional[str] = Field(None, max_length=1)
	pcpindicator : Optional[str] = Field(None, max_length=1)
	patienttotaloutofpocketamount : Optional[float] = None
	globalpaymentflag : Optional[int] = None
	deniedflag : Optional[str] = Field(None, max_length=1)
	attendingprovider_linkage_id : Optional[int] = None
	accidentindicator : Optional[str] = Field(None, max_length=1)
	innetworkindicator : Optional[str] = Field(None, max_length=1)
	billfrequencycode : Optional[str] = Field(None, max_length=1)
	planrenderingprovideridentifier_linkage_id : Optional[int] = None
	providerlocation_linkage_id : Optional[int] = None
	dischargediagnosiscleaned : Optional[str] = Field(None, max_length=7)
	chiacarrierspecificuniquememberid : Optional[int] = None
	claimlinetype : Optional[str] = Field(None, max_length=1)
	chiaformerclaimnumber : Optional[int] = None
	chiacarrierspecificuniquesubscriberid : Optional[int] = None
	otherdiagnosis13cleaned : Optional[str] = Field(None, max_length=7)
	otherdiagnosis14cleaned : Optional[str] = Field(None, max_length=7)
	otherdiagnosis15cleaned : Optional[str] = Field(None, max_length=7)
	otherdiagnosis16cleaned : Optional[str] = Field(None, max_length=7)
	otherdiagnosis17cleaned : Optional[str] = Field(None, max_length=7)
	otherdiagnosis18cleaned : Optional[str] = Field(None, max_length=7)
	otherdiagnosis19cleaned : Optional[str] = Field(None, max_length=7)
	otherdiagnosis20cleaned : Optional[str] = Field(None, max_length=7)
	otherdiagnosis21cleaned : Optional[str] = Field(None, max_length=7)
	otherdiagnosis22cleaned : Optional[str] = Field(None, max_length=7)
	otherdiagnosis23cleaned : Optional[str] = Field(None, max_length=7)
	otherdiagnosis24cleaned : Optional[str] = Field(None, max_length=7)
	presentonadmission1 : Optional[str] = Field(None, max_length=1)
	presentonadmission2 : Optional[str] = Field(None, max_length=1)
	presentonadmission3 : Optional[str] = Field(None, max_length=1)
	presentonadmission4 : Optional[str] = Field(None, max_length=1)
	presentonadmission5 : Optional[str] = Field(None, max_length=1)
	presentonadmission6 : Optional[str] = Field(None, max_length=1)
	presentonadmission7 : Optional[str] = Field(None, max_length=1)
	presentonadmission8 : Optional[str] = Field(None, max_length=1)
	presentonadmission9 : Optional[str] = Field(None, max_length=1)
	presentonadmission10 : Optional[str] = Field(None, max_length=1)
	presentonadmission11 : Optional[str] = Field(None, max_length=1)
	presentonadmission12 : Optional[str] = Field(None, max_length=1)
	presentonadmission13 : Optional[str] = Field(None, max_length=1)
	presentonadmission14 : Optional[str] = Field(None, max_length=1)
	presentonadmission15 : Optional[str] = Field(None, max_length=1)
	presentonadmission16 : Optional[str] = Field(None, max_length=1)
	presentonadmission17 : Optional[str] = Field(None, max_length=1)
	presentonadmission18 : Optional[str] = Field(None, max_length=1)
	presentonadmission19 : Optional[str] = Field(None, max_length=1)
	presentonadmission20 : Optional[str] = Field(None, max_length=1)
	presentonadmission21 : Optional[str] = Field(None, max_length=1)
	presentonadmission22 : Optional[str] = Field(None, max_length=1)
	presentonadmission23 : Optional[str] = Field(None, max_length=1)
	presentonadmission24 : Optional[str] = Field(None, max_length=1)
	presentonadmission25 : Optional[str] = Field(None, max_length=1)
	drugcodecleaned : Optional[str] = Field(None, max_length=11)
	employmentrelatedindicator : Optional[int] = None
	epsdtindicator : Optional[int] = None
	procedurecodetype : Optional[int] = None
	apcdidcode : Optional[int] = None
	claimlinepaidflag : Optional[int] = None
	typeoffacility : Optional[int] = None
	masshealthclaimtype : Optional[str] = Field(None, max_length=1)





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



index = 650
while index < 17073:
	filename = 'MedicalClaimPart1_'+"%010d"% (index,)
	print("On file: "+ filename)
	
	df = pd.read_csv(filename, sep='*', names=['nationalserviceprovideridcleaned','nationalbillingprovideridcleaned','nationalprovideridplanrenderingcleaned','submissionyear','medicalclaimid','submissioncontrolid','incurredyear','versionindicator','highestversiondenied','highestversionindicator','medicaidhsnindicator','fullydeniedclaim','memberlinkeid','memberageatserviceinyearsredacted','linkorgidme','linkorgidpv','linkorgidpr','orgid','insurancetypecodeproduct','chiapayerclaimcontrolnumber','linecounter','versionnumber','individualrelationshipcodelds','membergendercleanedlds','memberstateorprovincelds','dateserviceapprovedapdateyear','admissiondateyear','admissiontype','admissionsource','dischargestatuscleaned','serviceprovidernumber_linkage_id','serviceproviderentitytypequalifier','serviceprovidersuffix','serviceproviderspecialtycleaned','serviceproviderstatelds','serviceproviderzipcode_3_lds','typeofbillonfacilityclaims','siteofserviceonnsfcms1500claimscleaned','claimstatus','admittingdiagnosiscleaned','ecodecleaned','principaldiagnosiscleaned','otherdiagnosis1cleaned','otherdiagnosis2cleaned','otherdiagnosis3cleaned','otherdiagnosis4cleaned','otherdiagnosis5cleaned','otherdiagnosis6cleaned','otherdiagnosis7cleaned','otherdiagnosis8cleaned','otherdiagnosis9cleaned','otherdiagnosis10cleaned','otherdiagnosis11cleaned','otherdiagnosis12cleaned','revenuecodecleaned','procedurecodecleaned','proceduremodifier1','proceduremodifier2','icdcmprocedurecodecleaned','dateofservicefromyear','dateofservicetoyear','quantity','chargeamountcleaned','paidamountcleaned','prepaidamountcleaned','copayamountcleaned','coinsuranceamount','deductibleamount','dischargedateyear','billingprovidernumber_linkage_id','productidnumber_linkage_id','capitatedencounterflag','othericdcmprocedurecode1cleaned','othericdcmprocedurecode2cleaned','othericdcmprocedurecode3cleaned','othericdcmprocedurecode4cleaned','othericdcmprocedurecode5cleaned','othericdcmprocedurecode6cleaned','paiddateyear','coinsurancedays','covereddays','noncovereddays','typeofclaimcleaned','coordinationofbenefitstplliabilityamount','otherinsurancepaidamountcleaned','medicarepaidamountcleaned','allowedamountcleaned','noncoveredamountcleaned','delegatedbenefitadministratororganizationidcleaned','icdindicator','proceduremodifier3','proceduremodifier4','diagnosticpointer','referringproviderid_linkage_id','paymentarrangementtypecleaned','excludedexpensescleaned','medicareindicator','withholdamount','referralindicator','pcpindicator','patienttotaloutofpocketamount','globalpaymentflag','deniedflag','attendingprovider_linkage_id','accidentindicator','innetworkindicator','billfrequencycode','planrenderingprovideridentifier_linkage_id','providerlocation_linkage_id','dischargediagnosiscleaned','chiacarrierspecificuniquememberid','claimlinetype','chiaformerclaimnumber','chiacarrierspecificuniquesubscriberid','otherdiagnosis13cleaned','otherdiagnosis14cleaned','otherdiagnosis15cleaned','otherdiagnosis16cleaned','otherdiagnosis17cleaned','otherdiagnosis18cleaned','otherdiagnosis19cleaned','otherdiagnosis20cleaned','otherdiagnosis21cleaned','otherdiagnosis22cleaned','otherdiagnosis23cleaned','otherdiagnosis24cleaned','presentonadmission1','presentonadmission2','presentonadmission3','presentonadmission4','presentonadmission5','presentonadmission6','presentonadmission7','presentonadmission8','presentonadmission9','presentonadmission10','presentonadmission11','presentonadmission12','presentonadmission13','presentonadmission14','presentonadmission15','presentonadmission16','presentonadmission17','presentonadmission18','presentonadmission19','presentonadmission20','presentonadmission21','presentonadmission22','presentonadmission23','presentonadmission24','presentonadmission25','drugcodecleaned','employmentrelatedindicator','epsdtindicator','procedurecodetype','apcdidcode','claimlinepaidflag','typeoffacility','masshealthclaimtype'], 
				  dtype=str, header=None, low_memory=True)
	df = df.replace(np.nan, None)
	df = df.replace('----------', None)
	
	valid_data, invalid_data = validate_df_data(df, MedicalClaimEnforced, index_offset=1)
	print(invalid_data)
	if invalid_data!=[]:
		print("Error")
		break
	outputFilename = 'FinishedMedicalClaimPart1_'+"%010d"% (index,)
	index = index + 1
	df.to_csv(outputFilename, sep='*', index=False, header=False)

print("Done")
