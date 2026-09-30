import utils.clients
import utils.http_session
import utils.transport
import utils.session
import pandas as pd

df = pd.read_csv("sample_applicants.csv")


print(df.head()) 
print(df.info())  
print(df.describe())   
