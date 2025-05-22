import numpy as np #Linear Algebra
import pandas as pd  #Data Processing
import plotly.express as px #Data Visualization

#Load DataSet
df = pd.read_csv('Unemployment in India.csv') #DataSet

print(df.info())
print(df.describe()) 

#Data PreProcessing
df.dropna(axis=0, inplace=True)
print(df.head())
print(df.tail())
print(df.shape)

x = df['Region'] #plotting column 'Region' on x-axis
y = df[' Estimated Unemployment Rate (%)'] #plotting column 'Rate' on y-axis

dfz = df.iloc[:,3]
print(dfz)

#Analyzing Data By Graphs
rue = px.bar(df,x=x,y=y,color='Region',title='Unemployment Rate (Region Wise) by Bar Origin',template='plotly')
rue.update_layout(xaxis={'categoryorder':'total descending'})
rue.show()

fig = px.pie(df, values=y, names='Region', title='Unemployment Rate (Region Wise) by Pie Origin', template='plotly')
fig.update_layout(xaxis={'categoryorder':'total descending'})
fig.show()

ree = px.bar(df,x='Area',y=y,color='Area',title='Unemployment Rate (Area Wise) by Bar Origin',template='plotly')
ree.update_layout(xaxis={'categoryorder':'total descending'})
ree.show()

labour = px.bar(df,x='Region',y=' Estimated Labour Participation Rate (%)',color='Region',title='Labour Rate (Region Wise) by Bar Origin',template='plotly')
labour.update_layout(xaxis={'categoryorder':'total descending'})
labour.show()
