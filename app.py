import pandas as pd
import plotly.express as px
import streamlit as st 
import plotly.graph_objects as go

df= pd.read_csv('D:/TT/streamlit/project/vehicles_us.csv')
st.write('# Car Sales Data Analysis Dashboard')
st.write('### Car sales dataset')
st.dataframe(df)
#graphs
st.write('## Visualizing Car Sales Trends')
st.write('### Price vs Odometer')
fig = px.scatter(df, x='odometer', y='price', color='condition', animation_frame='model_year', hover_name='model')
st.plotly_chart(fig)
st.write('### Distribution of Car Prices')
fig = px.histogram(df, x='price', nbins=100)
st.plotly_chart(fig)
st.write('### Car Prices by Model Year and Fuel Type')
fig = px.histogram(df, x='model_year', y='price', color='fuel')
st.plotly_chart(fig)
st.write('### Proportion of Car Types')
fig = px.pie(df, names='type')
st.plotly_chart(fig)
st.write('### Average Price Over Years')
df_grouped = df[['model_year', 'price']].groupby('model_year').mean().reset_index()
fig = px.line(df_grouped, x='model_year', y='price')
st.plotly_chart(fig)

