import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Read the data
car_crash_df = pd.read_csv("car-crashes.csv", skiprows=1)

northEast = ["New Jersey", "New York", "Pennsylvania", "Connecticut", "Maine", "Massachusetts", "New Hampshire", "Rhode Island", "Vermont"]
midwest = ["Illinois", "Indiana", "Michigan", "Ohio", "Wisconsin", "Iowa", "Kansas", "Minnesota", "Missouri", "Nebraska", "North Dakota", "South Dakota"]
south = ["Delaware", "Florida", "Georgia", "Maryland", "North Carolina", "South Carolina", "Virginia", "Washington", "District of Columbia", "West Virginia", "Alabama", "Kentucky", "Mississippi", "Tennessee", "Arkansas", "Louisiana", "Oklahoma", "Texas"]
west = ["Arizona", "Colorado", "Idaho", "Montana", "Nevada", "New Mexico", "Utah", "Wyoming", "Alaska", "California", "Hawaii", "Oregon", "Washington"]

# Display the column names to verify correct case sensitivity
st.write("Column names:", car_crash_df.columns)

# Define regions
# ... (rest of your code)

# Add a new column for the region
if 'State' in car_crash_df.columns:  # Check if 'State' column exists
    car_crash_df['Region'] = car_crash_df['State'].apply(lambda state: 'North East' if state in northEast
                                                           else ('Midwest' if state in midwest
                                                                 else ('South' if state in south
                                                                       else ('West' if state in west
                                                                             else 'National Average'))))
else:
    st.error("Column 'State' not found in the DataFrame. Please check your column names.")

# Calculate the average deaths per 100,000 population for each region
if 'Deaths per 100,000 population' in car_crash_df.columns:  # Check if the target column exists
    average_deaths_by_region = car_crash_df.groupby('Region')['Deaths per 100,000 population'].mean()
    std_dev_by_region = car_crash_df.groupby('Region')['Deaths per 100,000 population'].std()

    # Create a bar plot with Seaborn
    plt.figure(figsize=(10, 6))
    sns.barplot(x=average_deaths_by_region.index, y=average_deaths_by_region.values, ci=None)
    plt.errorbar(x=average_deaths_by_region.index, y=average_deaths_by_region.values,
             yerr=2 * std_dev_by_region.values, fmt='none', color='black', capsize=5, label='2x SD')
    plt.title('Average Car Crash Deaths per 100,000 Population by Region')
    plt.xlabel('Region')
    plt.ylabel('Average Deaths per 100,000 Population')

    # Display the plot in Streamlit
    st.pyplot(plt)
else:
    st.error("Column 'Deaths per 100,000 population' not found in the DataFrame. Please check your column names.")
