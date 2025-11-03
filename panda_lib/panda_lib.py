import pandas as pd


# ---Reading Data from files---


# df=pd.read_csv("E:\python_lib\panda_lib\\batting_stats.csv" , encoding="utf-8")
#for excel :- read_excel
#for json :- read_json
# print(df)


# ---Saving Data on files---

# data={
#     "Name":["Yukti", "Kashvi " , "Paridhi"],
#     "Age":[19 , 14, 12],
#     "City":["America" , "Mumbai" , "Bangalore"]
# }

# df=pd.DataFrame(data)
# print(df)

# df.to_csv("Output.csv" , index=False)

# df.to_excel("Output.xlsx" , index=False , engine="openpyxl")



# ---Understanding Dataset---
df=pd.read_csv("E:\python_lib\panda_lib\\batting_stats.csv"  ,  encoding="latin1")

print("Displaying First 5 Data")
print(df.head())

print("Displaying Last 5 Data")
print(df.tail())



