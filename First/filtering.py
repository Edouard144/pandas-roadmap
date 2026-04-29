# Select one column
print(df['firstName'])




# Select multiple columns
print(df[['firstName', 'lastName', 'location']])



# Filter rows (all applicants from Rwanda)
rwanda = df[df['location'].str.contains("Rwanda")]
print(rwanda)



# Filter by skill (React developers)
react_devs = df[df['skills'].str.contains("React")]
print(react_devs[['firstName','skills']])
