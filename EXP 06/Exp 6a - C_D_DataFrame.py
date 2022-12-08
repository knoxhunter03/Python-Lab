import pandas as pd
import numpy as pn
exam_data = {'name':['Kelivn','Ram','Shyam','Peter','Kaveri','Rosy'],
             'score':[15,2,pn.nan,7,8,pn.nan],
             'attempts':[2,1,1,3,2,5],
             'qualify':['yes', 'no', 'yes', 'no', 'no', 'yes']
            }
indexs=['a','b','c','d','e','f']
df = pd.DataFrame(exam_data,index=indexs)
print(df)
