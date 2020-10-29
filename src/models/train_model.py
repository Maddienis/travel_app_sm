import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import src.features.main as main
import src.visualization.flask as flask



# Is this correctly setting the index?
def cleanDf(df):

    df.reset_index(inplace=True)
    test_user = df[df['user'] == 50].copy()
    ready = df.drop(df[df.user == 50].index)
    ready.set_index(['user', 'city_id'])
    y_data = ready['rank']
    x_data = ready.drop(columns=['city', 'continent_city', 'rank'])

    return (x_data, y_data)



#df = main.startToEnd()
#x, y = cleanDf(df)
#print(x)
#rint(y)

print(req)

clf = RandomForestClassifier(random_state=12, max_depth=25)
clf.fit(x, y)
pickle.dump(clf, open('model_test2.pkl','wb'))

