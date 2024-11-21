#streamlit run D:/TT/streamlit/car_sales_dashboard/app.py
import pandas as pd
import plotly.express as px
import streamlit as st 
import plotly.graph_objects as go
from ipywidgets import interact, Checkbox

df= pd.read_csv('D:/TT/streamlit/car_sales_dashboard/vehicles_us.csv')
df= pd.read_csv('vehicles_us.csv')
st.write('# Car Sales Data Analysis Dashboard')
st.write('### Car sales dataset')
st.dataframe(df)
st.markdown("---")

st.write('# Most Popular Models')
models = df[['model', 'price']].groupby('model').agg({'model': 'count', 'price': 'mean'})
models.columns = ['Count', 'Average price ($)']
models = models.sort_values(by='Count', ascending=False)
top_10_models = models.head(10)
top_10_models['Average price ($)']= top_10_models['Average price ($)'].round(2)
st.table(top_10_models)
st.markdown("---")

#graphs
st.write('## Visualizing Car Sales Trends')
st.write('### Price vs Odometer')
fig = px.scatter(df, x='odometer', y='price', color='condition', animation_frame='model_year', hover_name='model', 
                 labels={'odometer': 'Odometer Reading (miles)', 'model_year': 'Year of Manufacture' })
st.plotly_chart(fig)
st.write('''The graph shows a clear trend: as mileage increases, prices go down. Cars in "like new" or "excellent" condition sell for higher prices even at moderate mileage. 
         However, cars in "salvage" or "fair" condition have much lower prices no matter the mileage. There are some cars marked as "like new" with low prices, which might be errors in the data.''')
st.markdown("---")

st.write('### Distribution of Car Prices')
# Define the function to filter and plot the chart
def filter_chart(exclude_expensive):
    filtered_df = df[df['price'] <= 50000] if exclude_expensive else df
    fig = px.histogram(filtered_df, x='price', nbins=100, labels={'price': 'Price ($)'})
    return fig
# Add the checkbox to interact with the function
exclude_expensive = st.checkbox('Exclude Vehicles > $50,000', value=False)
fig = filter_chart(exclude_expensive)
st.plotly_chart(fig)
st.write('''Most cars are priced below $20,000, with the highest number in the $5,000–$10,000 range. The few cars priced much higher seem to be luxury or rare models. 
         This means the analysis mostly reflects trends in affordable cars, with less focus on higher-end vehicles.''')
st.markdown("---")


st.write('### Car Prices by Model Year and Fuel Type')
fig = px.histogram(df, x='model_year', y='price', color='fuel', labels={'model_year': 'Year of Manufacture' })
st.plotly_chart(fig)
st.write('''Gas-powered cars make up most of the dataset across all years. Hybrid and electric cars are priced lower than expected, which might mean the dataset includes older or less popular models. 
         Diesel cars are the most expensive on average, likely due to their durability or niche uses. The presence of more alternative fuel cars in recent years shows a shift in the market.''')
st.markdown("---")

st.write('### Proportion of Car Types')
fig = px.pie(df, names='type')
st.plotly_chart(fig)
st.write('''SUVs and sedans are the most common types, matching their popularity in the market. Pickup trucks also have a good share, likely because of their versatility. 
         However, categories like convertibles and off-road vehicles are rare, which could be due to market trends or limited data collection.''')
st.markdown("---")

st.write('### Average Price Over Years')
df_grouped = df[['model_year', 'price']].groupby('model_year').mean().reset_index()
fig = px.line(df_grouped, x='model_year', y='price', labels={'model_year': 'Year of Manufacture' })
st.plotly_chart(fig)
st.write('''The graph shows that newer cars are more expensive, as expected. Prices level off for cars made between 2015 and 2019, which could mean demand slowed during this time. 
         Older cars (before 2000) have much lower prices, as they depreciate faster. These patterns might also reflect changes in the economy or customer preferences.''')


