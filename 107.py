import pandas as pd
import plotly.graph_objects as go
import csv

df=pd.read_csv('data.csv')
studentdf=df.loc[df['student_id']=='TRL_xsl']
print (studentdf.groupby('level')['attempt'].mean())
fig=go.Figure(go.Bar(
    y=studentdf.groupby('level')['attempt'].mean(),
    x=['level 1','level 2','level 3','level 4'],
    orientation='v'
))
fig.show()