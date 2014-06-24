import pandas as pd
import numpy as np
filename = 'movie_database.csv'
header_names = ["Theatre", "Movie_name", "times_1", "times_2", "times_3", "times_4", "times_5", "times_6"]
df_theatres = pd.read_csv(filename, names = header_names, na_values = ["NaN"])
print df_theatres["Movie_name"].unique()