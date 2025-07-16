import pandas as pd
import numpy as np
import functions.data_transformations as data_transformations
import functions.data_smells as data_smells
from helpers.enumerations import Belong, Operator, Operation, SpecialType, DataType, DerivedType, Closure, FilterType, MapOperation, MathOperator
from helpers.logger import set_logger
import pyarrow
from functions.PMML import PMMLModel

def generateWorkflow():
	#-----------------New DataProcessing-----------------
	columnFilter_Name__input_dataDictionary_df=pd.read_parquet('/wf_validation_python/data/output/columnFilter_input_dataDictionary.parquet')

	
	common_invalid_list=['inf', '-inf', 'nan']
	common_missing_list=['', '?', '.','null','none','na']
	
	list_missing=[]
	list_invalid=[]
	
	data_smells.check_missing_invalid_value_consistency(data_dictionary=columnFilter_Name__input_dataDictionary_df, 
														missing_invalid_list=[], common_missing_invalid_list=common_missing_list, field='Name', origin_function="Column Filter")
	
	data_smells.check_integer_as_floating_point(data_dictionary=columnFilter_Name__input_dataDictionary_df, field='Name', origin_function="Column Filter")
	data_smells.check_types_as_string(data_dictionary=columnFilter_Name__input_dataDictionary_df, field='Name', expected_type=DataType.STRING, origin_function="Column Filter")
	data_smells.check_special_character_spacing(data_dictionary=columnFilter_Name__input_dataDictionary_df, field='Name', origin_function="Column Filter")
	data_smells.check_suspect_precision(data_dictionary=columnFilter_Name__input_dataDictionary_df, field='Name', origin_function="Column Filter")
	data_smells.check_date_as_datetime(data_dictionary=columnFilter_Name__input_dataDictionary_df, field='Name', origin_function="Column Filter")
	data_smells.check_ambiguous_datetime_format(data_dictionary=columnFilter_Name__input_dataDictionary_df, field='Name', origin_function="Column Filter")
	data_smells.check_separating_consistency(data_dictionary=columnFilter_Name__input_dataDictionary_df, decimal_sep='.',  field='Name', origin_function="Column Filter")
	

	columnFilter_Name__input_dataDictionary_transformed=columnFilter_Name__input_dataDictionary_df.copy()
	field_list_columnFilter_param_field=['Name']
	columnFilter_Name__input_dataDictionary_transformed=data_transformations.transform_filter_columns(data_dictionary=columnFilter_Name__input_dataDictionary_transformed,
																	columns=field_list_columnFilter_param_field, belong_op=Belong.BELONG)
	
	columnFilter_Name__output_dataDictionary_df=columnFilter_Name__input_dataDictionary_transformed
	columnFilter_Name__output_dataDictionary_df.to_parquet('/wf_validation_python/data/output/columnFilter_output_dataDictionary.parquet')
	columnFilter_Name__output_dataDictionary_df=pd.read_parquet('/wf_validation_python/data/output/columnFilter_output_dataDictionary.parquet')
	

set_logger("transformations")
generateWorkflow()
