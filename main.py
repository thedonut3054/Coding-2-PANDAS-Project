import pandas as pd
class data:
    def __init__(self, csv):
        self.df = (pd.read_csv(csv))
        self.GSFO_Greater_Than = True
        self.GSFO_Sales_Amount = 0
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
                elif o == 2:
                    self.sortMain()
                # elif o == 2:
                #     self.sortMain() no need for two of these
                    break
            except:
                pass
    def filterMain(self):
        print("DataFrame Filter Options:")
        print("  1. Sales")
        print("  2. Genre")
        print("  3. Year")
        print("  4. Platform")
        print("  5. Save and return")
        print()
        o = None
        while True:
            try:
                o = int(input("Enter the number of the option you want to select: "))
                if o == 1:
                    self.filterSales()
                    break
            except:
                pass
    def sortMain(self):
        print("DataFrame Sorting Options") # How are we going to sort by multiple things wont the sorts override each other?
        print("DataFrame Sorting Options: ")
        print("DataFrame Sorting Options") # How are we going to sort by multiple things wont the sorts override each other?
        print("  1. Sales")
        print("  2. Year")
        print("  3. Title")
        print("  4. Save and return")
        print()
        o = None
        while True:
            try:
                o = int(input("Enter the number of the option you want to select: "))
                if o == 1:    
                    print("Sorted By Sales!") # Should sales take us to another menu for where sales are like NA or EU
                    # self.df.sort_values["Global_Sales"]
                    self.sortMain()
                    break
                elif o == 2:
                    print("Sorted By Genre!")
                    self.sortMain()
                    break
                elif o == 3:
                    print("Sorted By Year!")
                    self.sortMain()
                    break
                elif o == 4:
                    print("Sorted By Platform!")
                    self.sortMain()
                    break
                elif o == 5:
                    print("Saved Renturning To Home!")
                    self.options()
                    break
                else:
                    print("Invalid Input Try Again")
                    self.sortMain()
                    break
            except:
                pass
    def advancedMain(self):
        print("Advanced DataFrame options")
        print("Make Sales Integers")
        print("Make Sales Floats")
        print("other option idk")
    def filterSales(self): 
        print("DataFrame Sales Filter Options: ")
        print("  1. Global Sales")
        print("  2. NA Sales")
        print("  3. EU Sales")
        print("  4. JP Sales")
        print("  5. Other Sales")
        print("  6. Save and return")
        print()
        o = None
        while True:
            try:
                o = int(input("Enter the number of the option you want to select: "))
                if o == 1:
                    self.filterGlobalSales()
            except:
                pass        
    def filterGlobalSales(self):
        def GSFOptions():
            if self.GSFO_Greater_Than == True:
                return(f"GREATER THAN {self.GSFO_Sales_Amount}")
        print("DataFrame Global Sales Filter Options: ")
        print(f"  Only Show entries with {GSFOptions()} sales")
                    
    def advancedMain(self):
        print("Advanced DataFrame options")
        print("Make Sales Integers")
        print("Make Sales Floats")
        print("other option idk")
    # def filterSales(self): 
    #     pass
    # def sortMain():
    #     print("DataFrame Sorting Options")
    #     print("  1. Sales")
    #     print("  2. Genre")
    #     print("  3. Year")
    #     print("  4. Platform")
    #     print("  5. Save and return")
    #     print()
    #     o = None
    #     while True:
    #         try:
    #             o = int(input("Enter the number of the option you want to select: "))
    #         except:
    #             pass
# im pretty sure lines 66 through 81 should not be here? so ive comented them out for now

df = data("/workspaces/Coding-2-PANDAS-Project/vgsales.csv")
df.options() # what is this here for