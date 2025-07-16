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
	rowFilterMissing_Equipment__input_dataDictionary_df=pd.read_parquet('/wf_validation_python/data/output/rowFilterMissing_input_dataDictionary.parquet')

	
	common_invalid_list=['inf', '-inf', 'nan']
	common_missing_list=['', '?', '.','null','none','na']
	
	list_missing=[]
	list_invalid=[]
	
	data_smells.check_missing_invalid_value_consistency(data_dictionary=rowFilterMissing_Equipment__input_dataDictionary_df, 
														missing_invalid_list=[], common_missing_invalid_list=common_missing_list, field='Equipment', origin_function="Row Filter")
	
	data_smells.check_integer_as_floating_point(data_dictionary=rowFilterMissing_Equipment__input_dataDictionary_df, field='Equipment', origin_function="Row Filter")
	data_smells.check_types_as_string(data_dictionary=rowFilterMissing_Equipment__input_dataDictionary_df, field='Equipment', expected_type=DataType.STRING, origin_function="Row Filter")
	data_smells.check_special_character_spacing(data_dictionary=rowFilterMissing_Equipment__input_dataDictionary_df, field='Equipment', origin_function="Row Filter")
	data_smells.check_suspect_precision(data_dictionary=rowFilterMissing_Equipment__input_dataDictionary_df, field='Equipment', origin_function="Row Filter")
	data_smells.check_date_as_datetime(data_dictionary=rowFilterMissing_Equipment__input_dataDictionary_df, field='Equipment', origin_function="Row Filter")
	data_smells.check_ambiguous_datetime_format(data_dictionary=rowFilterMissing_Equipment__input_dataDictionary_df, field='Equipment', origin_function="Row Filter")
	data_smells.check_suspect_distribution(data_dictionary=rowFilterMissing_Equipment__input_dataDictionary_df, min_value=0.0, max_value=1.0, field='Equipment', origin_function="Row Filter")
	data_smells.check_separating_consistency(data_dictionary=rowFilterMissing_Equipment__input_dataDictionary_df, decimal_sep='.',  field='Equipment', origin_function="Row Filter")
	

	rowFilterMissing_Equipment__input_dataDictionary_transformed=rowFilterMissing_Equipment__input_dataDictionary_df.copy()
	columns_rowFilterMissing_param_filter=['Equipment']
	dicc_rowFilterMissing_param_filter={'Equipment':{'missing': []}}
	
	rowFilterMissing_Equipment__input_dataDictionary_transformed=data_transformations.transform_filter_rows_special_values(data_dictionary=rowFilterMissing_Equipment__input_dataDictionary_transformed,
																											cols_special_type_values=dicc_rowFilterMissing_param_filter,
																											filter_type=FilterType(1))
	rowFilterMissing_Equipment__output_dataDictionary_df=rowFilterMissing_Equipment__input_dataDictionary_transformed
	rowFilterMissing_Equipment__output_dataDictionary_df.to_parquet('/wf_validation_python/data/output/rowFilterMissing_output_dataDictionary.parquet')
	rowFilterMissing_Equipment__output_dataDictionary_df=pd.read_parquet('/wf_validation_python/data/output/rowFilterMissing_output_dataDictionary.parquet')
	

set_logger("transformations")
generateWorkflow()
