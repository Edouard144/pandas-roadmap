# Count applicants per country
print(df['location'].value_counts())

# Group by availability type
print(df.groupby('availability_type')['firstname'].count())

# Average start year of education per country
print(df.groupby('location')['start_year'].mean())
