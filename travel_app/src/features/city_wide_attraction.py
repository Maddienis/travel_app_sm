import pandas as pd
import numpy as np
from pandas.io.json import json_normalize
import ast


def create_dummy(df):
	df['split_types'] = [ast.literal_eval(x) for x in df.types]
	df['split_types_str'] = [','.join(x) for x in df.split_types]
	dummies = df.split_types_str.str.get_dummies(sep=',')
	dummies['total'] = dummies.sum(axis=1)

	return dummies









