# Drop duplicates
df = df.drop_duplicates()


# Fill missing values
df = df.fillna("Unknown")


# Rename columns
df = df.rename(columns={'firstName':'firstname', 'lastName':'lastname'})


# Strip whitespace
df['headline'] = df['headline'].str.strip()
