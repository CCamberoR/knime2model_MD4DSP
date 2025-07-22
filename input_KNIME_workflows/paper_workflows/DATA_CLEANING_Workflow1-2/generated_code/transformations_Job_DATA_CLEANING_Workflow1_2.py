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
	binner_hours_per_week__input_dataDictionary_df=pd.read_parquet('/wf_validation_python/data/output/binner_input_dataDictionary.parquet')
	
	common_invalid_list=['inf', '-inf', 'nan']
	common_missing_list=['', '?', '.','null','none','na']
	
	
	data_smells.check_missing_invalid_value_consistency(data_dictionary=binner_hours_per_week__input_dataDictionary_df, 
														missing_invalid_list=[], common_missing_invalid_list=common_missing_list, field='hours-per-week', origin_function="Rule Engine")
	
	data_smells.check_integer_as_floating_point(data_dictionary=binner_hours_per_week__input_dataDictionary_df, field='hours-per-week', origin_function="Rule Engine")
	data_smells.check_types_as_string(data_dictionary=binner_hours_per_week__input_dataDictionary_df, field='hours-per-week', expected_type=DataType.INTEGER, origin_function="Rule Engine")
	data_smells.check_suspect_precision(data_dictionary=binner_hours_per_week__input_dataDictionary_df, field='hours-per-week', origin_function="Rule Engine")
	data_smells.check_date_as_datetime(data_dictionary=binner_hours_per_week__input_dataDictionary_df, field='hours-per-week', origin_function="Rule Engine")
	data_smells.check_ambiguous_datetime_format(data_dictionary=binner_hours_per_week__input_dataDictionary_df, field='hours-per-week', origin_function="Rule Engine")
	data_smells.check_suspect_distribution(data_dictionary=binner_hours_per_week__input_dataDictionary_df, min_value=0.0, max_value=8.0, field='hours-per-week', origin_function="Rule Engine")
	data_smells.check_intermingled_data_type(data_dictionary=binner_hours_per_week__input_dataDictionary_df, field='hours-per-week', origin_function="Rule Engine")
	data_smells.check_separating_consistency(data_dictionary=binner_hours_per_week__input_dataDictionary_df, decimal_sep='.',  field='hours-per-week', origin_function="Rule Engine")
			
	

	binner_hours_per_week__input_dataDictionary_transformed=binner_hours_per_week__input_dataDictionary_df.copy()
	binner_hours_per_week__input_dataDictionary_transformed=data_transformations.transform_derived_field(data_dictionary=binner_hours_per_week__input_dataDictionary_transformed,
																  data_type_output = DataType(0),
																  field_in = 'hours-per-week', field_out = 'prediction')
	
	binner_hours_per_week__output_dataDictionary_df=binner_hours_per_week__input_dataDictionary_transformed
	binner_hours_per_week__output_dataDictionary_df.to_parquet('/wf_validation_python/data/output/binner_output_dataDictionary.parquet')
	binner_hours_per_week__output_dataDictionary_df=pd.read_parquet('/wf_validation_python/data/output/binner_output_dataDictionary.parquet')
	binner_hours_per_week__input_dataDictionary_transformed=data_transformations.transform_interval_fix_value(data_dictionary=binner_hours_per_week__input_dataDictionary_transformed,
																  left_margin=40.0, right_margin=1.0E9,
																  closure_type=Closure(2),
																  fix_value_output='FULL-TIME',
							                                      data_type_output = DataType(0),
																  field_in = 'hours-per-week',
																  field_out = 'prediction')
	
	binner_hours_per_week__output_dataDictionary_df=binner_hours_per_week__input_dataDictionary_transformed
	binner_hours_per_week__output_dataDictionary_df.to_parquet('/wf_validation_python/data/output/binner_output_dataDictionary.parquet')
	binner_hours_per_week__output_dataDictionary_df=pd.read_parquet('/wf_validation_python/data/output/binner_output_dataDictionary.parquet')
	binner_hours_per_week__input_dataDictionary_transformed=data_transformations.transform_interval_fix_value(data_dictionary=binner_hours_per_week__input_dataDictionary_transformed,
																  left_margin=-1.0E9, right_margin=40.0,
																  closure_type=Closure(0),
																  fix_value_output='PART-TIME',
							                                      data_type_output = DataType(0),
																  field_in = 'hours-per-week',
																  field_out = 'prediction')
	
	binner_hours_per_week__output_dataDictionary_df=binner_hours_per_week__input_dataDictionary_transformed
	binner_hours_per_week__output_dataDictionary_df.to_parquet('/wf_validation_python/data/output/binner_output_dataDictionary.parquet')
	binner_hours_per_week__output_dataDictionary_df=pd.read_parquet('/wf_validation_python/data/output/binner_output_dataDictionary.parquet')
	
	#-----------------New DataProcessing-----------------
	mapping_native_country__input_dataDictionary_df=pd.read_parquet('/wf_validation_python/data/output/binner_output_dataDictionary.parquet')

	
	common_invalid_list=['inf', '-inf', 'nan']
	common_missing_list=['', '?', '.','null','none','na']
	
	
	data_smells.check_missing_invalid_value_consistency(data_dictionary=mapping_native_country__input_dataDictionary_df, 
														missing_invalid_list=[], common_missing_invalid_list=common_missing_list, field='native-country', origin_function="String Manipulation")
	
	data_smells.check_integer_as_floating_point(data_dictionary=mapping_native_country__input_dataDictionary_df, field='native-country', origin_function="String Manipulation")
	data_smells.check_types_as_string(data_dictionary=mapping_native_country__input_dataDictionary_df, field='native-country', expected_type=DataType.STRING, origin_function="String Manipulation")
	data_smells.check_suspect_precision(data_dictionary=mapping_native_country__input_dataDictionary_df, field='native-country', origin_function="String Manipulation")
	data_smells.check_date_as_datetime(data_dictionary=mapping_native_country__input_dataDictionary_df, field='native-country', origin_function="String Manipulation")
	data_smells.check_ambiguous_datetime_format(data_dictionary=mapping_native_country__input_dataDictionary_df, field='native-country', origin_function="String Manipulation")
	data_smells.check_number_string_size(data_dictionary=mapping_native_country__input_dataDictionary_df, field='native-country', origin_function="String Manipulation")
	data_smells.check_special_character_spacing(data_dictionary=mapping_native_country__input_dataDictionary_df, field='native-country', origin_function="String Manipulation")
	data_smells.check_string_casing(data_dictionary=mapping_native_country__input_dataDictionary_df, field='native-country', origin_function="String Manipulation")
	data_smells.check_intermingled_data_type(data_dictionary=mapping_native_country__input_dataDictionary_df, field='native-country', origin_function="String Manipulation")
	data_smells.check_contracted_text(data_dictionary=mapping_native_country__input_dataDictionary_df, field='native-country', origin_function="String Manipulation")
	data_smells.check_abbreviation_consistency(data_dictionary=mapping_native_country__input_dataDictionary_df, field='native-country', origin_function="String Manipulation")
	data_smells.check_syntactic_synonym(data_dictionary=mapping_native_country__input_dataDictionary_df, field='native-country', origin_function="String Manipulation")
	data_smells.check_ambiguous_value(data_dictionary=mapping_native_country__input_dataDictionary_df, field='native-country', origin_function="String Manipulation")
	data_smells.check_separating_consistency(data_dictionary=mapping_native_country__input_dataDictionary_df, decimal_sep='.',  field='native-country', origin_function="String Manipulation")
			
	

	input_values_list=['-']
	output_values_list=[' ']
	data_type_input_list=[DataType(0)]
	data_type_output_list=[DataType(0)]
	map_operation_list=[MapOperation(1)]
	mapping_native_country__output_dataDictionary_df=data_transformations.transform_fix_value_fix_value(data_dictionary=mapping_native_country__input_dataDictionary_df, input_values_list=input_values_list,
																  output_values_list=output_values_list,
							                                      data_type_input_list = data_type_input_list,
							                                      data_type_output_list = data_type_output_list,
																  map_operation_list = map_operation_list,
																  field_in = 'native-country', field_out = 'native-country')
	
	mapping_native_country__output_dataDictionary_df.to_parquet('/wf_validation_python/data/output/columnExpressions_output_dataDictionary.parquet')
	mapping_native_country__output_dataDictionary_df=pd.read_parquet('/wf_validation_python/data/output/columnExpressions_output_dataDictionary.parquet')
	
	#-----------------New DataProcessing-----------------
	mathOperation_year_of_birth__input_dataDictionary_df=pd.read_parquet('/wf_validation_python/data/output/columnExpressions_output_dataDictionary.parquet')

	
	common_invalid_list=['inf', '-inf', 'nan']
	common_missing_list=['', '?', '.','null','none','na']
	
	
	data_smells.check_missing_invalid_value_consistency(data_dictionary=mathOperation_year_of_birth__input_dataDictionary_df, 
														missing_invalid_list=[], common_missing_invalid_list=common_missing_list, field='age', origin_function="Math Formula")
	
	data_smells.check_integer_as_floating_point(data_dictionary=mathOperation_year_of_birth__input_dataDictionary_df, field='age', origin_function="Math Formula")
	data_smells.check_types_as_string(data_dictionary=mathOperation_year_of_birth__input_dataDictionary_df, field='age', expected_type=DataType.DOUBLE, origin_function="Math Formula")
	data_smells.check_suspect_precision(data_dictionary=mathOperation_year_of_birth__input_dataDictionary_df, field='age', origin_function="Math Formula")
	data_smells.check_date_as_datetime(data_dictionary=mathOperation_year_of_birth__input_dataDictionary_df, field='age', origin_function="Math Formula")
	data_smells.check_ambiguous_datetime_format(data_dictionary=mathOperation_year_of_birth__input_dataDictionary_df, field='age', origin_function="Math Formula")
	data_smells.check_suspect_distribution(data_dictionary=mathOperation_year_of_birth__input_dataDictionary_df, min_value=440.0, max_value=1600.0, field='age', origin_function="Math Formula")
	data_smells.check_intermingled_data_type(data_dictionary=mathOperation_year_of_birth__input_dataDictionary_df, field='age', origin_function="Math Formula")
	data_smells.check_separating_consistency(data_dictionary=mathOperation_year_of_birth__input_dataDictionary_df, decimal_sep='.',  field='age', origin_function="Math Formula")
			
	

	mathOperation_year_of_birth__input_dataDictionary_transformed=pd.read_parquet('/wf_validation_python/data/output/columnExpressions_output_dataDictionary.parquet')
	mathOperation_year_of_birth__input_dataDictionary_transformed=data_transformations.transform_derived_field(data_dictionary=mathOperation_year_of_birth__input_dataDictionary_transformed,
																  data_type_output = DataType(5),
																  field_in = 'age', field_out = 'year-of-birth')
	
	mathOperation_year_of_birth__output_dataDictionary_df=mathOperation_year_of_birth__input_dataDictionary_transformed
	mathOperation_year_of_birth__output_dataDictionary_df.to_parquet('/wf_validation_python/data/output/columnExpressions_output_dataDictionary.parquet')
	mathOperation_year_of_birth__output_dataDictionary_df=pd.read_parquet('/wf_validation_python/data/output/columnExpressions_output_dataDictionary.parquet')
	mathOperation_year_of_birth__input_dataDictionary_transformed=data_transformations.transform_math_operation(data_dictionary=mathOperation_year_of_birth__input_dataDictionary_transformed,
																math_op=MathOperator(1), field_out='year-of-birth',
																first_operand=1994, is_field_first=False,second_operand='age', is_field_second=True)
	
	mathOperation_year_of_birth__output_dataDictionary_df=mathOperation_year_of_birth__input_dataDictionary_transformed
	mathOperation_year_of_birth__output_dataDictionary_df.to_parquet('/wf_validation_python/data/output/columnExpressions_output_dataDictionary.parquet')
	mathOperation_year_of_birth__output_dataDictionary_df=pd.read_parquet('/wf_validation_python/data/output/columnExpressions_output_dataDictionary.parquet')
	



set_logger("transformations")
generateWorkflow()
