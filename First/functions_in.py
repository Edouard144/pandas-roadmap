# Convert skills into list
df['skills'] = df['skills'].apply(lambda x: x.split() if isinstance(x,str) else [])

# Count number of skills per applicant
df['skill_count'] = df['skills'].apply(len)

# Example: uppercase all names
df['firstname'] = df['firstname'].str.upper()
