import pandas as pd
class data:
    def __init__(self, csv):
        self.df = (pd.read_csv(csv))
    def getInt(self):
        self.df[["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales", "Global_Sales"]] = self.df[["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales", "Global_Sales"]].apply(lambda y: y*1000000)
        self.df[["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales", "Global_Sales"]] = self.df[["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales", "Global_Sales"]].astype(int)
    def getFloat(self):
        self.df[["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales", "Global_Sales"]] = self.df[["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales", "Global_Sales"]].astype(float)
        self.df[["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales", "Global_Sales"]] = self.df[["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales", "Global_Sales"]].apply(lambda y: round(y/1000000, 2))
    def options(self):
        print("DataFrame View Options:")
        print("  1. Filter")
        print("  2. Sort")
        print("  3. Advanced")
        print("  4. Reset")
        print("  5. View DataFrame")
        print()
        o = None
        while True:
            try:
                o = int(input("Enter the number of the option you want to select: "))
                if o == 1:
                    self.filterMain()
            except:
                pass
    def filterMain(self):
        print("DataFrame Filter Options:")
        print("  1. Sales")
        print("  2. Genre")
        print("  3. Year")
        print("  4. Platform")
        print("  5. Save and return")
df = data("/workspaces/Coding-2-PANDAS-Project/vgsales.csv")
df.options()