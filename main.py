import pandas as pd
class data:
    def __init__(self, csv):
        self.df = pd.read_csv(csv)
df = data("/workspaces/Coding-2-PANDAS-Project/vgsales.csv")
print(df.df.head(50))