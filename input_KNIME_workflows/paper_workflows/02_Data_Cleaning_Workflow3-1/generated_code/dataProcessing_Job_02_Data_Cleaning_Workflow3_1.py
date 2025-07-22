import pandas as pd
import numpy as np
import functions.contract_invariants as contract_invariants
import functions.contract_pre_post as contract_pre_post
import functions.data_transformations as data_transformations
import functions.data_smells as data_smells
from helpers.enumerations import Belong, Operator, Operation, SpecialType, DataType, DerivedType, Closure, FilterType, MapOperation, MathOperator
from helpers.logger import set_logger
import pyarrow
from functions.PMML import PMMLModel

def generateWorkflow():
	#-----------------New DataProcessing-----------------
	mapping_Country__input_dataDictionary_df=pd.read_parquet('/wf_validation_python/data/output/mapping_input_dataDictionary.parquet')

	
	common_invalid_list=['inf', '-inf', 'nan']
	common_missing_list=['', '?', '.','null','none','na']
	
	
	data_smells.check_missing_invalid_value_consistency(data_dictionary=mapping_Country__input_dataDictionary_df, 
														missing_invalid_list=[], common_missing_invalid_list=common_missing_list, field='Country', origin_function="String Manipulation")
	
	data_smells.check_integer_as_floating_point(data_dictionary=mapping_Country__input_dataDictionary_df, field='Country', origin_function="String Manipulation")
	data_smells.check_types_as_string(data_dictionary=mapping_Country__input_dataDictionary_df, field='Country', expected_type=DataType.STRING, origin_function="String Manipulation")
	data_smells.check_suspect_precision(data_dictionary=mapping_Country__input_dataDictionary_df, field='Country', origin_function="String Manipulation")
	data_smells.check_date_as_datetime(data_dictionary=mapping_Country__input_dataDictionary_df, field='Country', origin_function="String Manipulation")
	data_smells.check_ambiguous_datetime_format(data_dictionary=mapping_Country__input_dataDictionary_df, field='Country', origin_function="String Manipulation")
	data_smells.check_number_string_size(data_dictionary=mapping_Country__input_dataDictionary_df, field='Country', origin_function="String Manipulation")
	data_smells.check_special_character_spacing(data_dictionary=mapping_Country__input_dataDictionary_df, field='Country', origin_function="String Manipulation")
	data_smells.check_string_casing(data_dictionary=mapping_Country__input_dataDictionary_df, field='Country', origin_function="String Manipulation")
	data_smells.check_intermingled_data_type(data_dictionary=mapping_Country__input_dataDictionary_df, field='Country', origin_function="String Manipulation")
	data_smells.check_contracted_text(data_dictionary=mapping_Country__input_dataDictionary_df, field='Country', origin_function="String Manipulation")
	data_smells.check_abbreviation_consistency(data_dictionary=mapping_Country__input_dataDictionary_df, field='Country', origin_function="String Manipulation")
	data_smells.check_syntactic_synonym(data_dictionary=mapping_Country__input_dataDictionary_df, field='Country', origin_function="String Manipulation")
	data_smells.check_ambiguous_value(data_dictionary=mapping_Country__input_dataDictionary_df, field='Country', origin_function="String Manipulation")
	data_smells.check_separating_consistency(data_dictionary=mapping_Country__input_dataDictionary_df, decimal_sep='.',  field='Country', origin_function="String Manipulation")
			
	
	if contract_pre_post.check_fix_value_range(value='United States', is_substring=False, data_dictionary=mapping_Country__input_dataDictionary_df, belong_op=Belong(0), field='Country',
									quant_abs=None, quant_rel=None, quant_op=None, origin_function="String Manipulation"):
		print('PRECONDITION String Manipulation(Country) FixValue:United States VALIDATED')
	else:
		print('PRECONDITION String Manipulation(Country) FixValue:United States NOT VALIDATED')
	
	input_values_list=['United States']
	output_values_list=['USA']
	data_type_input_list=[DataType(0)]
	data_type_output_list=[DataType(0)]
	map_operation_list=[MapOperation(0)]
	mapping_Country__output_dataDictionary_df=data_transformations.transform_fix_value_fix_value(data_dictionary=mapping_Country__input_dataDictionary_df, input_values_list=input_values_list,
																  output_values_list=output_values_list,
							                                      data_type_input_list = data_type_input_list,
							                                      data_type_output_list = data_type_output_list,
																  map_operation_list = map_operation_list,
																  field_in = 'Country', field_out = 'Country')
	
	mapping_Country__output_dataDictionary_df.to_parquet('/wf_validation_python/data/output/mapping_output_dataDictionary.parquet')
	mapping_Country__output_dataDictionary_df=pd.read_parquet('/wf_validation_python/data/output/mapping_output_dataDictionary.parquet')
	
	if contract_pre_post.check_fix_value_range(value='United States', is_substring=False, data_dictionary=mapping_Country__output_dataDictionary_df, belong_op=Belong(1), field='Country',
									quant_abs=None, quant_rel=None, quant_op=None, origin_function="String Manipulation"):
		print('POSTCONDITION String Manipulation(Country) FixValue:United States VALIDATED')
	else:
		print('POSTCONDITION String Manipulation(Country) FixValue:United States NOT VALIDATED')
	
	
	input_values_list_mapping_INV_condition=['United States']
	output_values_list_mapping_INV_condition=['USA']
	
	data_type_input_list_mapping_INV_condition=[DataType(0)]
	data_type_output_list_mapping_INV_condition=[DataType(0)]
	
	is_substring_list_mapping_INV_condition=[False]
	
	if contract_invariants.check_inv_fix_value_fix_value(data_dictionary_in=mapping_Country__input_dataDictionary_df,
											data_dictionary_out=mapping_Country__output_dataDictionary_df,
											input_values_list=input_values_list_mapping_INV_condition, 
											output_values_list=output_values_list_mapping_INV_condition,
											is_substring_list=is_substring_list_mapping_INV_condition,
											belong_op_in=Belong(0),
											belong_op_out=Belong(0),
											data_type_input_list=data_type_input_list_mapping_INV_condition,
											data_type_output_list=data_type_output_list_mapping_INV_condition,
											field_in='Country', field_out='Country', origin_function="String Manipulation"):
		print('INVARIANT String Manipulation(Country) InputMapValues:United States OutputMapValues:USA VALIDATED')
	else:
		print('INVARIANT String Manipulation(Country) InputMapValues:United States OutputMapValues:USA NOT VALIDATED')
	
	
	
	

set_logger("dataProcessing")
generateWorkflow()
