import pandas as pd

# Read the main restaurant database:
header_names = ['restaurant_name', 'Category', 'Address', 'Phone_number', 'rating', 'price', 'noise_level'] 
df_rest = pd.read_csv('restaurant_database.csv', names=header_names, header=1)

# Read the first distance CSV file
header_names = ['Name', 'Address', 'Zipcode', 'Distance_from_94114', 'lat', 'lng']
df_rest1 = pd.read_csv('restaurant_distances_94114.csv', names = header_names, header=1, usecols=(0,3))

# Merge the two: 
df_merge = df_rest.join(df_rest1)

df_merge.to_csv("test_super_DB.csv")