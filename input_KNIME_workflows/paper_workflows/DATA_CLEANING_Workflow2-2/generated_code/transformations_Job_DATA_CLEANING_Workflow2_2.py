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
	rowFilterMissing_marital_status__input_dataDictionary_df=pd.read_parquet('/wf_validation_python/data/output/rowFilterMissing_input_dataDictionary.parquet')
	
	common_invalid_list=['inf', '-inf', 'nan']
	common_missing_list=['', '?', '.','null','none','na']
	
	
	data_smells.check_missing_invalid_value_consistency(data_dictionary=rowFilterMissing_marital_status__input_dataDictionary_df, 
														missing_invalid_list=[], common_missing_invalid_list=common_missing_list, field='marital-status', origin_function="Row Filter (deprecated)")
	
	data_smells.check_integer_as_floating_point(data_dictionary=rowFilterMissing_marital_status__input_dataDictionary_df, field='marital-status', origin_function="Row Filter (deprecated)")
	data_smells.check_types_as_string(data_dictionary=rowFilterMissing_marital_status__input_dataDictionary_df, field='marital-status', expected_type=DataType.STRING, origin_function="Row Filter (deprecated)")
	data_smells.check_suspect_precision(data_dictionary=rowFilterMissing_marital_status__input_dataDictionary_df, field='marital-status', origin_function="Row Filter (deprecated)")
	data_smells.check_date_as_datetime(data_dictionary=rowFilterMissing_marital_status__input_dataDictionary_df, field='marital-status', origin_function="Row Filter (deprecated)")
	data_smells.check_ambiguous_datetime_format(data_dictionary=rowFilterMissing_marital_status__input_dataDictionary_df, field='marital-status', origin_function="Row Filter (deprecated)")
	data_smells.check_suspect_distribution(data_dictionary=rowFilterMissing_marital_status__input_dataDictionary_df, min_value=0.0, max_value=1.0, field='marital-status', origin_function="Row Filter (deprecated)")
	data_smells.check_intermingled_data_type(data_dictionary=rowFilterMissing_marital_status__input_dataDictionary_df, field='marital-status', origin_function="Row Filter (deprecated)")
	data_smells.check_separating_consistency(data_dictionary=rowFilterMissing_marital_status__input_dataDictionary_df, decimal_sep='.',  field='marital-status', origin_function="Row Filter (deprecated)")
			
	

	rowFilterMissing_marital_status__input_dataDictionary_transformed=rowFilterMissing_marital_status__input_dataDictionary_df.copy()
	columns_rowFilterMissing_param_filter=['marital-status']
	dicc_rowFilterMissing_param_filter={'marital-status':{'missing': []}}
	
	rowFilterMissing_marital_status__input_dataDictionary_transformed=data_transformations.transform_filter_rows_special_values(data_dictionary=rowFilterMissing_marital_status__input_dataDictionary_transformed,
																											cols_special_type_values=dicc_rowFilterMissing_param_filter,
																											filter_type=FilterType(0))
	rowFilterMissing_marital_status__output_dataDictionary_df=rowFilterMissing_marital_status__input_dataDictionary_transformed
	rowFilterMissing_marital_status__output_dataDictionary_df.to_parquet('/wf_validation_python/data/output/rowFilterMissing_output_dataDictionary.parquet')
	rowFilterMissing_marital_status__output_dataDictionary_df=pd.read_parquet('/wf_validation_python/data/output/rowFilterMissing_output_dataDictionary.parquet')
	
	#-----------------New DataProcessing-----------------
	rowFilterPrimitive_marital_status__input_dataDictionary_df=pd.read_parquet('/wf_validation_python/data/output/rowFilterMissing_output_dataDictionary.parquet')

	
	common_invalid_list=['inf', '-inf', 'nan']
	common_missing_list=['', '?', '.','null','none','na']
	
	list_invalid=['Never-married']
	
	data_smells.check_missing_invalid_value_consistency(data_dictionary=rowFilterPrimitive_marital_status__input_dataDictionary_df, 
														missing_invalid_list=list_invalid, common_missing_invalid_list=common_invalid_list, field='marital-status', origin_function="Row Filter (deprecated)")
	
	data_smells.check_integer_as_floating_point(data_dictionary=rowFilterPrimitive_marital_status__input_dataDictionary_df, field='marital-status', origin_function="Row Filter (deprecated)")
	data_smells.check_types_as_string(data_dictionary=rowFilterPrimitive_marital_status__input_dataDictionary_df, field='marital-status', expected_type=DataType.STRING, origin_function="Row Filter (deprecated)")
	data_smells.check_suspect_precision(data_dictionary=rowFilterPrimitive_marital_status__input_dataDictionary_df, field='marital-status', origin_function="Row Filter (deprecated)")
	data_smells.check_date_as_datetime(data_dictionary=rowFilterPrimitive_marital_status__input_dataDictionary_df, field='marital-status', origin_function="Row Filter (deprecated)")
	data_smells.check_ambiguous_datetime_format(data_dictionary=rowFilterPrimitive_marital_status__input_dataDictionary_df, field='marital-status', origin_function="Row Filter (deprecated)")
	data_smells.check_suspect_distribution(data_dictionary=rowFilterPrimitive_marital_status__input_dataDictionary_df, min_value=9.0, max_value=202.0, field='marital-status', origin_function="Row Filter (deprecated)")
	data_smells.check_intermingled_data_type(data_dictionary=rowFilterPrimitive_marital_status__input_dataDictionary_df, field='marital-status', origin_function="Row Filter (deprecated)")
	data_smells.check_separating_consistency(data_dictionary=rowFilterPrimitive_marital_status__input_dataDictionary_df, decimal_sep='.',  field='marital-status', origin_function="Row Filter (deprecated)")
			
	

	rowFilterPrimitive_marital_status__input_dataDictionary_transformed=rowFilterPrimitive_marital_status__input_dataDictionary_df.copy()
	columns_rowFilterPrimitive_param_filter=['marital-status']
	filter_fix_value_list_rowFilterPrimitive_param_filter=['Never-married']
	
	rowFilterPrimitive_marital_status__input_dataDictionary_transformed=data_transformations.transform_filter_rows_primitive(data_dictionary=rowFilterPrimitive_marital_status__input_dataDictionary_transformed,
																											columns=columns_rowFilterPrimitive_param_filter,
																		                                    filter_fix_value_list=filter_fix_value_list_rowFilterPrimitive_param_filter,
																											filter_type=FilterType(1))
	rowFilterPrimitive_marital_status__output_dataDictionary_df=rowFilterPrimitive_marital_status__input_dataDictionary_transformed
	rowFilterPrimitive_marital_status__output_dataDictionary_df.to_parquet('/wf_validation_python/data/output/rowFilterPrimitive_output_dataDictionary.parquet')
	rowFilterPrimitive_marital_status__output_dataDictionary_df=pd.read_parquet('/wf_validation_python/data/output/rowFilterPrimitive_output_dataDictionary.parquet')
	
	#-----------------New DataProcessing-----------------
	rowFilterRange_age__input_dataDictionary_df=pd.read_parquet('/wf_validation_python/data/output/rowFilterPrimitive_output_dataDictionary.parquet')

	
	common_invalid_list=['inf', '-inf', 'nan']
	common_missing_list=['', '?', '.','null','none','na']
	
	
	data_smells.check_missing_invalid_value_consistency(data_dictionary=rowFilterRange_age__input_dataDictionary_df, 
														missing_invalid_list=[], common_missing_invalid_list=common_missing_list, field='age', origin_function="Row Filter (deprecated)")
	
	data_smells.check_integer_as_floating_point(data_dictionary=rowFilterRange_age__input_dataDictionary_df, field='age', origin_function="Row Filter (deprecated)")
	data_smells.check_types_as_string(data_dictionary=rowFilterRange_age__input_dataDictionary_df, field='age', expected_type=DataType.STRING, origin_function="Row Filter (deprecated)")
	data_smells.check_suspect_precision(data_dictionary=rowFilterRange_age__input_dataDictionary_df, field='age', origin_function="Row Filter (deprecated)")
	data_smells.check_date_as_datetime(data_dictionary=rowFilterRange_age__input_dataDictionary_df, field='age', origin_function="Row Filter (deprecated)")
	data_smells.check_ambiguous_datetime_format(data_dictionary=rowFilterRange_age__input_dataDictionary_df, field='age', origin_function="Row Filter (deprecated)")
	data_smells.check_suspect_distribution(data_dictionary=rowFilterRange_age__input_dataDictionary_df, min_value=20.0, max_value=40.0, field='age', origin_function="Row Filter (deprecated)")
	data_smells.check_intermingled_data_type(data_dictionary=rowFilterRange_age__input_dataDictionary_df, field='age', origin_function="Row Filter (deprecated)")
	data_smells.check_separating_consistency(data_dictionary=rowFilterRange_age__input_dataDictionary_df, decimal_sep='.',  field='age', origin_function="Row Filter (deprecated)")
			
	

	rowFilterRange_age__input_dataDictionary_transformed=rowFilterRange_age__input_dataDictionary_df.copy()
	columns_rowFilterRange_param_filter=['age']
	filter_range_left_values_list_rowFilterRange_param_filter=[20.0]
	filter_range_right_values_list_rowFilterRange_param_filter=[40.0]
	closure_type_list_rowFilterRange_param_filter=[Closure(3)]
	
	rowFilterRange_age__input_dataDictionary_transformed=data_transformations.transform_filter_rows_range(data_dictionary=rowFilterRange_age__input_dataDictionary_transformed,
																											columns=columns_rowFilterRange_param_filter,
																											left_margin_list=filter_range_left_values_list_rowFilterRange_param_filter,
																											right_margin_list=filter_range_right_values_list_rowFilterRange_param_filter,
																											filter_type=FilterType(1),
																											closure_type_list=closure_type_list_rowFilterRange_param_filter)
	rowFilterRange_age__output_dataDictionary_df=rowFilterRange_age__input_dataDictionary_transformed
	rowFilterRange_age__output_dataDictionary_df.to_parquet('/wf_validation_python/data/output/rowFilterRange_output_dataDictionary.parquet')
	rowFilterRange_age__output_dataDictionary_df=pd.read_parquet('/wf_validation_python/data/output/rowFilterRange_output_dataDictionary.parquet')
	



set_logger("transformations")
generateWorkflow()
