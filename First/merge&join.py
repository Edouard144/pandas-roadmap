# Suppose you have another dataset with certifications
certs = pd.DataFrame({
    'email': ['user1@example.com','user2@example.com'],
    'extra_cert': ['AWS Advanced','React Pro']
})

# Merge on email
merged = pd.merge(df, certs, on='email', how='left')
print(merged.head())
