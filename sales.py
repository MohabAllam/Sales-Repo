
import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(layout= 'wide', page_title= 'Sales EDA')

df = pd.read_csv('cleaned_df.csv', index_col= 0)

st.title('What is the percentage of each City in the Data ?')
st.plotly_chart(px.pie(df, names= 'city'))

st.title('What is the total number of order per State ?')
state_count = df.state.value_counts().reset_index()
st.plotly_chart(px.bar(state_count, x= 'state', y= 'count'))

st.title('What is the cumulative revenue from start date till end date ?')
df_sorted = df.sort_values(by= 'Order Date')
df_sorted['cum_rev'] = df_sorted['Price Each'].cumsum().round(2)
st.plotly_chart(px.line(data_frame= df_sorted, x= 'Order Date', y= 'cum_rev'))
