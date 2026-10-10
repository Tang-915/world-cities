import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn-v0_8')

st.title('California Housing Data (1990) by Wanyu Tang')
df = pd.read_csv('housing.csv')

# create a slider to filter by median house value
value_filter = st.slider('Minimal Median House Value', 0, 500001, 200000)  # min, max, default

st.subheader('See more filters in the sidebar:')

# create a multi select to filter by location type
location_types = df.ocean_proximity.unique()
location_filter = st.sidebar.multiselect(
    'Choose the location type',
    location_types,  # options
    location_types)  # defaults

# create a radio button to filter by income level
income_level = st.sidebar.radio('Choose income level', ['Low', 'Medium', 'High'])

# filter by median house value
df = df[df.median_house_value >= value_filter]

# filter by ocean proximity
df = df[df.ocean_proximity.isin(location_filter)]

# filter by median income
if income_level == 'Low':
    df = df[df.median_income <= 2.5]
elif income_level == 'Medium':
    df = df[(df.median_income > 2.5) & (df.median_income < 4.5)]
else:
    df = df[df.median_income >= 4.5]

# show on map
st.map(df)

# show the histogram of median house value
fig, ax = plt.subplots(figsize=(20, 5))
ax.hist(df.median_house_value, bins=30)
st.pyplot(fig)
