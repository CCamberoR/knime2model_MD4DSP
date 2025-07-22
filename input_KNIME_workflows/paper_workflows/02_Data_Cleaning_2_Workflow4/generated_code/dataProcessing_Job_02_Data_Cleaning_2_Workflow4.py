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
	mathOperation_Change__input_dataDictionary_df=pd.read_parquet('/wf_validation_python/data/output/mathOperation1_input_dataDictionary.parquet')

	
	common_invalid_list=['inf', '-inf', 'nan']
	common_missing_list=['', '?', '.','null','none','na']
	
	
	data_smells.check_missing_invalid_value_consistency(data_dictionary=mathOperation_Change__input_dataDictionary_df, 
														missing_invalid_list=[], common_missing_invalid_list=common_missing_list, field='Latitude', origin_function="Math Formula")
	
	data_smells.check_missing_invalid_value_consistency(data_dictionary=mathOperation_Change__input_dataDictionary_df, 
														missing_invalid_list=[], common_missing_invalid_list=common_missing_list, field='Longitude', origin_function="Math Formula")
	
	data_smells.check_integer_as_floating_point(data_dictionary=mathOperation_Change__input_dataDictionary_df, field='Latitude', origin_function="Math Formula")
	data_smells.check_types_as_string(data_dictionary=mathOperation_Change__input_dataDictionary_df, field='Latitude', expected_type=DataType.DOUBLE, origin_function="Math Formula")
	data_smells.check_suspect_precision(data_dictionary=mathOperation_Change__input_dataDictionary_df, field='Latitude', origin_function="Math Formula")
	data_smells.check_date_as_datetime(data_dictionary=mathOperation_Change__input_dataDictionary_df, field='Latitude', origin_function="Math Formula")
	data_smells.check_ambiguous_datetime_format(data_dictionary=mathOperation_Change__input_dataDictionary_df, field='Latitude', origin_function="Math Formula")
	data_smells.check_suspect_distribution(data_dictionary=mathOperation_Change__input_dataDictionary_df, min_value=440.0, max_value=1600.0, field='Latitude', origin_function="Math Formula")
	data_smells.check_intermingled_data_type(data_dictionary=mathOperation_Change__input_dataDictionary_df, field='Latitude', origin_function="Math Formula")
	data_smells.check_separating_consistency(data_dictionary=mathOperation_Change__input_dataDictionary_df, decimal_sep='.',  field='Latitude', origin_function="Math Formula")
			
	data_smells.check_integer_as_floating_point(data_dictionary=mathOperation_Change__input_dataDictionary_df, field='Longitude', origin_function="Math Formula")
	data_smells.check_types_as_string(data_dictionary=mathOperation_Change__input_dataDictionary_df, field='Longitude', expected_type=DataType.DOUBLE, origin_function="Math Formula")
	data_smells.check_suspect_precision(data_dictionary=mathOperation_Change__input_dataDictionary_df, field='Longitude', origin_function="Math Formula")
	data_smells.check_date_as_datetime(data_dictionary=mathOperation_Change__input_dataDictionary_df, field='Longitude', origin_function="Math Formula")
	data_smells.check_ambiguous_datetime_format(data_dictionary=mathOperation_Change__input_dataDictionary_df, field='Longitude', origin_function="Math Formula")
	data_smells.check_suspect_distribution(data_dictionary=mathOperation_Change__input_dataDictionary_df, min_value=440.0, max_value=1600.0, field='Longitude', origin_function="Math Formula")
	data_smells.check_intermingled_data_type(data_dictionary=mathOperation_Change__input_dataDictionary_df, field='Longitude', origin_function="Math Formula")
	data_smells.check_separating_consistency(data_dictionary=mathOperation_Change__input_dataDictionary_df, decimal_sep='.',  field='Longitude', origin_function="Math Formula")
			
	
	missing_values_mathOperation_PRE_valueRange=[]
	if contract_pre_post.check_missing_range(belong_op=Belong(0), data_dictionary=mathOperation_Change__input_dataDictionary_df, field='Latitude', 
									missing_values=missing_values_mathOperation_PRE_valueRange,
									quant_abs=None, quant_rel=None, quant_op=None, origin_function="Math Formula"):
		print('PRECONDITION Math Formula(Latitude) MissingValues:[] VALIDATED')
	else:
		print('PRECONDITION Math Formula(Latitude) MissingValues:[] NOT VALIDATED')
	missing_values_mathOperation_PRE_valueRange=[]
	if contract_pre_post.check_missing_range(belong_op=Belong(0), data_dictionary=mathOperation_Change__input_dataDictionary_df, field='Longitude', 
									missing_values=missing_values_mathOperation_PRE_valueRange,
									quant_abs=None, quant_rel=None, quant_op=None, origin_function="Math Formula"):
		print('PRECONDITION Math Formula(Longitude) MissingValues:[] VALIDATED')
	else:
		print('PRECONDITION Math Formula(Longitude) MissingValues:[] NOT VALIDATED')
	
	mathOperation_Change__input_dataDictionary_transformed=mathOperation_Change__input_dataDictionary_df.copy()
	mathOperation_Change__input_dataDictionary_transformed=data_transformations.transform_derived_field(data_dictionary=mathOperation_Change__input_dataDictionary_transformed,
																  data_type_output = DataType(5),
																  field_in = 'Latitude', field_out = 'Change')
	
	mathOperation_Change__output_dataDictionary_df=mathOperation_Change__input_dataDictionary_transformed
	mathOperation_Change__output_dataDictionary_df.to_parquet('/wf_validation_python/data/output/mathOperation1_output_dataDictionary.parquet')
	mathOperation_Change__output_dataDictionary_df=pd.read_parquet('/wf_validation_python/data/output/mathOperation1_output_dataDictionary.parquet')
	mathOperation_Change__input_dataDictionary_transformed=data_transformations.transform_math_operation(data_dictionary=mathOperation_Change__input_dataDictionary_transformed,
																math_op=MathOperator(1), field_out='Change',
																first_operand='Latitude', is_field_first=True,second_operand='Longitude', is_field_second=True)
	
	mathOperation_Change__output_dataDictionary_df=mathOperation_Change__input_dataDictionary_transformed
	mathOperation_Change__output_dataDictionary_df.to_parquet('/wf_validation_python/data/output/mathOperation1_output_dataDictionary.parquet')
	mathOperation_Change__output_dataDictionary_df=pd.read_parquet('/wf_validation_python/data/output/mathOperation1_output_dataDictionary.parquet')
	
	missing_values_mathOperation_POST_valueRange=[]
	if contract_pre_post.check_missing_range(belong_op=Belong(1), data_dictionary=mathOperation_Change__output_dataDictionary_df, field='Change', 
									missing_values=missing_values_mathOperation_POST_valueRange,
									quant_abs=None, quant_rel=None, quant_op=None, origin_function="Math Formula"):
		print('POSTCONDITION Math Formula(Change) MissingValues:[] VALIDATED')
	else:
		print('POSTCONDITION Math Formula(Change) MissingValues:[] NOT VALIDATED')
	
	if contract_invariants.check_inv_math_operation(data_dictionary_in=mathOperation_Change__input_dataDictionary_df,
											data_dictionary_out=mathOperation_Change__output_dataDictionary_df,
											math_op=MathOperator(1),
											first_operand='Latitude', is_field_first=True, second_operand='Longitude', is_field_second=True, 
											belong_op_out=Belong(0), field_in='Latitude', field_out='Change', origin_function="Math Formula"):
		print('INVARIANT Math Formula(Change) substract(Latitude, Longitude, ) VALIDATED')
	else:
		print('INVARIANT Math FormulaChange substract(Latitude, Longitude, ) NOT VALIDATED')
	
	
	
	
	
	
	
	#-----------------New DataProcessing-----------------
	mathOperation_Percentage__input_dataDictionary_df=pd.read_parquet('/wf_validation_python/data/output/mathOperation1_output_dataDictionary.parquet')

	
	common_invalid_list=['inf', '-inf', 'nan']
	common_missing_list=['', '?', '.','null','none','na']
	
	
	data_smells.check_missing_invalid_value_consistency(data_dictionary=mathOperation_Percentage__input_dataDictionary_df, 
														missing_invalid_list=[], common_missing_invalid_list=common_missing_list, field='Change', origin_function="Math Formula")
	
	data_smells.check_missing_invalid_value_consistency(data_dictionary=mathOperation_Percentage__input_dataDictionary_df, 
														missing_invalid_list=[], common_missing_invalid_list=common_missing_list, field='Latitude', origin_function="Math Formula")
	
	data_smells.check_integer_as_floating_point(data_dictionary=mathOperation_Percentage__input_dataDictionary_df, field='Change', origin_function="Math Formula")
	data_smells.check_types_as_string(data_dictionary=mathOperation_Percentage__input_dataDictionary_df, field='Change', expected_type=DataType.DOUBLE, origin_function="Math Formula")
	data_smells.check_suspect_precision(data_dictionary=mathOperation_Percentage__input_dataDictionary_df, field='Change', origin_function="Math Formula")
	data_smells.check_date_as_datetime(data_dictionary=mathOperation_Percentage__input_dataDictionary_df, field='Change', origin_function="Math Formula")
	data_smells.check_ambiguous_datetime_format(data_dictionary=mathOperation_Percentage__input_dataDictionary_df, field='Change', origin_function="Math Formula")
	data_smells.check_suspect_distribution(data_dictionary=mathOperation_Percentage__input_dataDictionary_df, min_value=440.0, max_value=1600.0, field='Change', origin_function="Math Formula")
	data_smells.check_intermingled_data_type(data_dictionary=mathOperation_Percentage__input_dataDictionary_df, field='Change', origin_function="Math Formula")
	data_smells.check_separating_consistency(data_dictionary=mathOperation_Percentage__input_dataDictionary_df, decimal_sep='.',  field='Change', origin_function="Math Formula")
			
	data_smells.check_integer_as_floating_point(data_dictionary=mathOperation_Percentage__input_dataDictionary_df, field='Latitude', origin_function="Math Formula")
	data_smells.check_types_as_string(data_dictionary=mathOperation_Percentage__input_dataDictionary_df, field='Latitude', expected_type=DataType.DOUBLE, origin_function="Math Formula")
	data_smells.check_suspect_precision(data_dictionary=mathOperation_Percentage__input_dataDictionary_df, field='Latitude', origin_function="Math Formula")
	data_smells.check_date_as_datetime(data_dictionary=mathOperation_Percentage__input_dataDictionary_df, field='Latitude', origin_function="Math Formula")
	data_smells.check_ambiguous_datetime_format(data_dictionary=mathOperation_Percentage__input_dataDictionary_df, field='Latitude', origin_function="Math Formula")
	data_smells.check_suspect_distribution(data_dictionary=mathOperation_Percentage__input_dataDictionary_df, min_value=440.0, max_value=1600.0, field='Latitude', origin_function="Math Formula")
	data_smells.check_intermingled_data_type(data_dictionary=mathOperation_Percentage__input_dataDictionary_df, field='Latitude', origin_function="Math Formula")
	data_smells.check_separating_consistency(data_dictionary=mathOperation_Percentage__input_dataDictionary_df, decimal_sep='.',  field='Latitude', origin_function="Math Formula")
			
	
	missing_values_mathOperation_PRE_valueRange=[]
	if contract_pre_post.check_missing_range(belong_op=Belong(0), data_dictionary=mathOperation_Percentage__input_dataDictionary_df, field='Change', 
									missing_values=missing_values_mathOperation_PRE_valueRange,
									quant_abs=None, quant_rel=None, quant_op=None, origin_function="Math Formula"):
		print('PRECONDITION Math Formula(Change) MissingValues:[] VALIDATED')
	else:
		print('PRECONDITION Math Formula(Change) MissingValues:[] NOT VALIDATED')
	missing_values_mathOperation_PRE_valueRange=[]
	if contract_pre_post.check_missing_range(belong_op=Belong(0), data_dictionary=mathOperation_Percentage__input_dataDictionary_df, field='Latitude', 
									missing_values=missing_values_mathOperation_PRE_valueRange,
									quant_abs=None, quant_rel=None, quant_op=None, origin_function="Math Formula"):
		print('PRECONDITION Math Formula(Latitude) MissingValues:[] VALIDATED')
	else:
		print('PRECONDITION Math Formula(Latitude) MissingValues:[] NOT VALIDATED')
	
	if contract_pre_post.check_fix_value_range(value=0, is_substring=False, data_dictionary=mathOperation_Percentage__input_dataDictionary_df, belong_op=Belong(1), field='Latitude',
									quant_abs=None, quant_rel=None, quant_op=None, origin_function="Math Formula"):
		print('PRECONDITION Math Formula(Latitude) FixValue:0 VALIDATED')
	else:
		print('PRECONDITION Math Formula(Latitude) FixValue:0 NOT VALIDATED')
	
	mathOperation_Percentage__input_dataDictionary_transformed=mathOperation_Percentage__input_dataDictionary_df.copy()
	mathOperation_Percentage__input_dataDictionary_transformed=data_transformations.transform_derived_field(data_dictionary=mathOperation_Percentage__input_dataDictionary_transformed,
																  data_type_output = DataType(5),
																  field_in = 'Change', field_out = 'Percentage')
	
	mathOperation_Percentage__output_dataDictionary_df=mathOperation_Percentage__input_dataDictionary_transformed
	mathOperation_Percentage__output_dataDictionary_df.to_parquet('/wf_validation_python/data/output/mathOperation2_output_dataDictionary.parquet')
	mathOperation_Percentage__output_dataDictionary_df=pd.read_parquet('/wf_validation_python/data/output/mathOperation2_output_dataDictionary.parquet')
	mathOperation_Percentage__input_dataDictionary_transformed=data_transformations.transform_math_operation(data_dictionary=mathOperation_Percentage__input_dataDictionary_transformed,
																math_op=MathOperator(3), field_out='Percentage',
																first_operand='Change', is_field_first=True,second_operand='Latitude', is_field_second=True)
	
	mathOperation_Percentage__output_dataDictionary_df=mathOperation_Percentage__input_dataDictionary_transformed
	mathOperation_Percentage__output_dataDictionary_df.to_parquet('/wf_validation_python/data/output/mathOperation2_output_dataDictionary.parquet')
	mathOperation_Percentage__output_dataDictionary_df=pd.read_parquet('/wf_validation_python/data/output/mathOperation2_output_dataDictionary.parquet')
	
	missing_values_mathOperation_POST_valueRange=[]
	if contract_pre_post.check_missing_range(belong_op=Belong(1), data_dictionary=mathOperation_Percentage__output_dataDictionary_df, field='Percentage', 
									missing_values=missing_values_mathOperation_POST_valueRange,
									quant_abs=None, quant_rel=None, quant_op=None, origin_function="Math Formula"):
		print('POSTCONDITION Math Formula(Percentage) MissingValues:[] VALIDATED')
	else:
		print('POSTCONDITION Math Formula(Percentage) MissingValues:[] NOT VALIDATED')
	
	if contract_invariants.check_inv_math_operation(data_dictionary_in=mathOperation_Percentage__input_dataDictionary_df,
											data_dictionary_out=mathOperation_Percentage__output_dataDictionary_df,
											math_op=MathOperator(3),
											first_operand='Change', is_field_first=True, second_operand='Latitude', is_field_second=True, 
											belong_op_out=Belong(0), field_in='Change', field_out='Percentage', origin_function="Math Formula"):
		print('INVARIANT Math Formula(Percentage) divide(Change, Latitude, ) VALIDATED')
	else:
		print('INVARIANT Math FormulaPercentage divide(Change, Latitude, ) NOT VALIDATED')
	
	
	
	
	
	
	
	#-----------------New DataProcessing-----------------
	binner_Change__input_dataDictionary_df=pd.read_parquet('/wf_validation_python/data/output/mathOperation2_output_dataDictionary.parquet')

	
	common_invalid_list=['inf', '-inf', 'nan']
	common_missing_list=['', '?', '.','null','none','na']
	
	
	data_smells.check_missing_invalid_value_consistency(data_dictionary=binner_Change__input_dataDictionary_df, 
														missing_invalid_list=[], common_missing_invalid_list=common_missing_list, field='Change', origin_function="Rule Engine")
	
	data_smells.check_integer_as_floating_point(data_dictionary=binner_Change__input_dataDictionary_df, field='Change', origin_function="Rule Engine")
	data_smells.check_types_as_string(data_dictionary=binner_Change__input_dataDictionary_df, field='Change', expected_type=DataType.INTEGER, origin_function="Rule Engine")
	data_smells.check_suspect_precision(data_dictionary=binner_Change__input_dataDictionary_df, field='Change', origin_function="Rule Engine")
	data_smells.check_date_as_datetime(data_dictionary=binner_Change__input_dataDictionary_df, field='Change', origin_function="Rule Engine")
	data_smells.check_ambiguous_datetime_format(data_dictionary=binner_Change__input_dataDictionary_df, field='Change', origin_function="Rule Engine")
	data_smells.check_suspect_distribution(data_dictionary=binner_Change__input_dataDictionary_df, min_value=0.0, max_value=8.0, field='Change', origin_function="Rule Engine")
	data_smells.check_intermingled_data_type(data_dictionary=binner_Change__input_dataDictionary_df, field='Change', origin_function="Rule Engine")
	data_smells.check_separating_consistency(data_dictionary=binner_Change__input_dataDictionary_df, decimal_sep='.',  field='Change', origin_function="Rule Engine")
			
	
	if contract_pre_post.check_interval_range(left_margin=0.0, right_margin=1000.0, data_dictionary=binner_Change__input_dataDictionary_df,
	                                	closure_type=Closure(3), belong_op=Belong(0), field='Change', origin_function="Rule Engine"):
		print('PRECONDITION Rule Engine(Change) Interval:[0.0, 1000.0] VALIDATED')
	else:
		print('PRECONDITION Rule Engine(Change) Interval:[0.0, 1000.0] NOT VALIDATED')
	
	binner_Change__input_dataDictionary_transformed=binner_Change__input_dataDictionary_df.copy()
	binner_Change__input_dataDictionary_transformed=data_transformations.transform_derived_field(data_dictionary=binner_Change__input_dataDictionary_transformed,
																  data_type_output = DataType(0),
																  field_in = 'Change', field_out = 'Increase/Decrease')
	
	binner_Change__output_dataDictionary_df=binner_Change__input_dataDictionary_transformed
	binner_Change__output_dataDictionary_df.to_parquet('/wf_validation_python/data/output/binner_output_dataDictionary.parquet')
	binner_Change__output_dataDictionary_df=pd.read_parquet('/wf_validation_python/data/output/binner_output_dataDictionary.parquet')
	binner_Change__input_dataDictionary_transformed=data_transformations.transform_interval_fix_value(data_dictionary=binner_Change__input_dataDictionary_transformed,
																  left_margin=-1.0E9, right_margin=0.0,
																  closure_type=Closure(0),
																  fix_value_output='Decrease',
							                                      data_type_output = DataType(0),
																  field_in = 'Change',
																  field_out = 'Increase/Decrease')
	
	binner_Change__output_dataDictionary_df=binner_Change__input_dataDictionary_transformed
	binner_Change__output_dataDictionary_df.to_parquet('/wf_validation_python/data/output/binner_output_dataDictionary.parquet')
	binner_Change__output_dataDictionary_df=pd.read_parquet('/wf_validation_python/data/output/binner_output_dataDictionary.parquet')
	binner_Change__input_dataDictionary_transformed=data_transformations.transform_interval_fix_value(data_dictionary=binner_Change__input_dataDictionary_transformed,
																  left_margin=0.0, right_margin=1.0E9,
																  closure_type=Closure(0),
																  fix_value_output='Increase',
							                                      data_type_output = DataType(0),
																  field_in = 'Change',
																  field_out = 'Increase/Decrease')
	
	binner_Change__output_dataDictionary_df=binner_Change__input_dataDictionary_transformed
	binner_Change__output_dataDictionary_df.to_parquet('/wf_validation_python/data/output/binner_output_dataDictionary.parquet')
	binner_Change__output_dataDictionary_df=pd.read_parquet('/wf_validation_python/data/output/binner_output_dataDictionary.parquet')
	
	if contract_pre_post.check_interval_range(left_margin=0.0, right_margin=1000.0, data_dictionary=binner_Change__output_dataDictionary_df,
	                                	closure_type=Closure(0), belong_op=Belong(1), field='Increase/Decrease', origin_function="Rule Engine"):
		print('POSTCONDITION Rule Engine(Increase/Decrease) Interval:(0.0, 1000.0) VALIDATED')
	else:
		print('POSTCONDITION Rule Engine(Increase/Decrease) Interval:(0.0, 1000.0) NOT VALIDATED')
	
	if contract_invariants.check_inv_interval_fix_value(data_dictionary_in=binner_Change__input_dataDictionary_df,
											data_dictionary_out=binner_Change__output_dataDictionary_df,
											left_margin=-1.0E9, right_margin=0.0,
											closure_type=Closure(0),
											fix_value_output='Decrease',
											belong_op_in=Belong(0), belong_op_out=Belong(0),
											data_type_output=DataType(0),
											field_in='Change', field_out='Increase/Decrease', origin_function="Rule Engine"):
		print('INVARIANT Rule Engine(Change) Interval:(-1.0E9, 0.0) FixValue:Decrease VALIDATED')
	else:
		print('INVARIANT Rule Engine(Change) Interval:(-1.0E9, 0.0) FixValue:Decrease NOT VALIDATED')
	
	if contract_invariants.check_inv_interval_fix_value(data_dictionary_in=binner_Change__input_dataDictionary_df,
											data_dictionary_out=binner_Change__output_dataDictionary_df,
											left_margin=0.0, right_margin=1.0E9,
											closure_type=Closure(0),
											fix_value_output='Increase',
											belong_op_in=Belong(0), belong_op_out=Belong(0),
											data_type_output=DataType(0),
											field_in='Change', field_out='Increase/Decrease', origin_function="Rule Engine"):
		print('INVARIANT Rule Engine(Change) Interval:(0.0, 1.0E9) FixValue:Increase VALIDATED')
	else:
		print('INVARIANT Rule Engine(Change) Interval:(0.0, 1.0E9) FixValue:Increase NOT VALIDATED')
	
	
	
	
	



set_logger("dataProcessing")
generateWorkflow()
