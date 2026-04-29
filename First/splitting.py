# Split availability into status and type
df[['availability_status','availability_type']] = df['availability'].str.split('|', expand=True)

# Split education into structured fields
df[['university','degree','major','start_year','end_year']] = df['education'].str.split('|', expand=True)

# Split experience
df[['company','role','exp_start_year','exp_end_year','focus']] = df['experience'].str.split('|', expand=True)
