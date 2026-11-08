import pandas as pd
#Path files
my_path_file = "My_path_file"
# Import dataset
df = pd.read_csv(my_path_file+'bestsellersAmazon.csv')
# Get the first 5 rows of dataset
print(df.head())
# Drop duplicates
df.drop_duplicates(inplace=True)
# Renaming columns
df.rename(columns={"Name": "Title", "Year": "Publication Year", "User Rating": "Rating"}, inplace=True)
# New colum's name
print(df.columns)
# Converting data types
df["Price"] = df["Price"].astype(float)
# Author best seller list
author_counts = df["Author"].value_counts()
print(author_counts)
#Average rating by genre
avg_rating_by_genre = df.groupby("Genre")["Rating"].mean()
print(avg_rating_by_genre)
# Export top selling authors to a CSV file
author_counts.head(10).to_csv(my_path_file + "top_authors.csv")
# Export average rating by genre to a CSV file
avg_rating_by_genre.to_csv(my_path_file + "avg_rating_by_genre.csv")