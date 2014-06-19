import pandas as pd

# Read the main restaurant database:
header_names = ['restaurant_name', 'Category', 'Address', 'Phone_number', 'rating', 'price', 'noise_level'] 
df_rest = pd.read_csv('restaurant_database.csv', names=header_names, header=1)

# Read the first distance CSV file
header_names = ['Name', 'Address', 'Zipcode', 'Distance_from_94114', 'lat', 'lng']
df_rest1 = pd.read_csv('restaurant_distances_94114.csv', names = header_names, header=1, usecols=(0,3))

# Read the second distance CSV file
header_names = ['Name', 'Address', 'Zipcode', 'Distance_from_94501', 'lat', 'lng']
df_rest2 = pd.read_csv('restaurant_distances_94501.csv', names = header_names, header=1, usecols=(0,3))

# Read the third distance CSV file
header_names = ['Name', 'Address', 'Zipcode', 'Distance_from_94607', 'lat', 'lng']
df_rest3 = pd.read_csv('restaurant_distances_94607.csv', names = header_names, header=1, usecols=(0,3))

# Read the fourth distance CSV file
header_names = ['Name', 'Address', 'Zipcode', 'Distance_from_94707', 'lat', 'lng']
df_rest4 = pd.read_csv('restaurant_distances_94707.csv', names = header_names, header=1, usecols=(0,3))


df_merge1 = df_rest.join(df_rest1["Distance_from_94114"])
df_merge2 = df_merge1.join(df_rest2["Distance_from_94501"])
df_merge3 = df_merge2.join(df_rest3["Distance_from_94607"])
df_merge4 = df_merge3.join(df_rest4["Distance_from_94707"])

print df_merge4.head()

df_merge4.to_csv("restaurant_database_distances.csv")