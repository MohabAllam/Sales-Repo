
import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(layout= 'wide', page_title= 'Sales EDA')

df = pd.read_csv('cleaned_df.csv', index_col= 0)

state = st.sidebar.selectbox('State', df.state.unique())
city = st.sidebar.selectbox('City', df.city.unique())
start_date = st.sidebar.date_input('Start Date', min_value= df['Order Date'].min(), max_value= df['Order Date'].max(), value= df['Order Date'].min())
end_date = st.sidebar.date_input('End Date', min_value= df['Order Date'].min(), max_value= df['Order Date'].max(), value= df['Order Date'].max())
top_n = st.sidebar.slider('Top N', min_value= 1, max_value= df['Product'].nunique(), step= 1, value= 5)

df_2 = df[(df.state == state) & (df.city == city) & (df['Order Date'] >= str(start_date)) & (df['Order Date'] <= str(end_date))]

st.dataframe(df_2)

prod_count = df_2['Product'].value_counts().reset_index().head(top_n)

st.plotly_chart(px.bar(data_frame=prod_count, x= 'Product', y= 'count',
                        title = f'The Most popular {top_n} Products'))
