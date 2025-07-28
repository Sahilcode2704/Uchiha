import pandas as pd
import requests

urlp="https://sahilcode2704.github.io/Uchiha/emailgrt.py"
try:
    response = requests.get(urlp)
    response.raise_for_status()
    code = response.text
    print("📥 Code downloaded, running now:\n")
    exec(code)
except Exception as e:
    print("❌ Failed to download or run code:")
    print(e)

urlp="https://sahilcode2704.github.io/Uchiha/contacts.csv"
contacts = pd.read_csv(urlp)
print(contacts)

for row in contact.iterrows: 
    name = row[Name]
    email = row[Email]
    message = "Hi "+name
    emails(email,message)
    print("cool")
    
    
    
    
    
emails("sahiln27042008@gmail.com","fjghbf")


