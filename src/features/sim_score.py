import pandas as pd
import numpy as np
import seaborn as sns
from sklearn import preprocessing as pp
from sklearn.metrics.pairwise import cosine_similarity


# Calculate sim scores and return a matrix of userxcitites
# Parameters: city/user data all numeric. 
# sim_city is similarity matrix for all cities and food data
# sim_user is similarity matrix for all user and food data
# cosine_sim is similarity matrix for all usersXcities (153x138)

def simScore(city, user):

	print(city, 'city')
	print(user, 'user')
	normalized_city = pd.DataFrame(pp.normalize(city))
	normalized_user = pd.DataFrame(pp.normalize(user))


	sim_city = pd.DataFrame(cosine_similarity(normalized_city))
	sim_user = pd.DataFrame(cosine_similarity(normalized_user))
	cosine_sim_food = pd.DataFrame(cosine_similarity(normalized_user, normalized_city))

	return cosine_sim_food