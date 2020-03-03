import pandas as pd

map  = [{ 'Name':'James','Math': 85,'Chemistry': 90,'Chinese': 40,'physics':40,'English': 60},
        { 'Name':'Davis','Math': 90,'Chemistry': 70,'Chinese': 45,'physics': 30, 'English': 70},
        { 'Name':'Green','Math': 80,'Chemistry': 50,'Chinese': 40,'physics': 80, 'English': 50},
       ]
  
df = pd.DataFrame(map,columns = ['Name','Math','Chemistry','Chinese','physics','English'])





print ("df.shape")
print (df.shape)
print("----------") 
print ("df.describe()")
print (df.describe())
print("----------") 
print ("df.head()")
print (df.head())
print("----------") 
print ("df.columns")
print (df.columns)
print("----------") 
