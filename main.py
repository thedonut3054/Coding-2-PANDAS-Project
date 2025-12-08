import pandas as pd
class data:
    def __init__(self, csv):
        self.df = (pd.read_csv(csv))
        self.GSFO_Greater_Than = True
        self.GSFO_Sales_Amount = 0
        self.NASFO_Greater_Than = True
        self.NASFO_Sales_Amount = 0
        self.EUSFO_Greater_Than = True
        self.EUSFO_Sales_Amount = 0
        self.JPSFO_Greater_Than = True
        self.JPSFO_Sales_Amount = 0
    def getInt(self):
        self.df[["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales", "Global_Sales"]] = self.df[["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales", "Global_Sales"]].apply(lambda y: y*1000000)
        self.df[["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales", "Global_Sales"]] = self.df[["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales", "Global_Sales"]].astype(int)
    def getFloat(self):
        self.df[["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales", "Global_Sales"]] = self.df[["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales", "Global_Sales"]].astype(float)
        self.df[["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales", "Global_Sales"]] = self.df[["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales", "Global_Sales"]].apply(lambda y: round(y/1000000, 2))
    def options(self):
        blankspace()
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
                elif o == 3:
                    self.advancedMain()
                else:
                    print("Invalid Input Let's Try Agian")
                    self.options()
            except:
                    pass
    def filterMain(self):
        blankspace()
        print("DataFrame Filter Options:")
        print("  1. Sales")
        print("  2. Year")
        print("  3. Platform")
        print("  4. Save and return")
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
        blankspace()
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
                    self.filterSales()
                    break
                elif o == 2:
                    print("Sorted By Year!")
                    self.sortMain()
                    break
                elif o == 3:
                    print("Sorted By Platform!")
                    self.sortMain()
                    break
                elif o == 4:
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
        blankspace()
        print("Advanced DataFrame options")
        print("  1. Make Sales Integers")
        print("  2. Make Sales Floats")
        print("  3. other option idk")
    def filterSales(self): 
        blankspace()
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
                    break
                elif o == 2:
                    self.filterNASales()
                    break
                elif o == 3:
                    self.filterEUSales()
                    break
                elif o == 4:
                    self.filterJPSales()
                    break
                elif o == 5:
                    break
                elif o == 6:
                    self.filterMain()
                    break
            except:
                pass        
    def filterGlobalSales(self):
        def GSFOptions():
            if self.GSFO_Greater_Than == True:
                return(f"GREATER THAN {self.GSFO_Sales_Amount}")
            else:
                return(f"LESS THAN {self.GSFO_Sales_Amount}")
        blankspace()
        print("DataFrame Global Sales Filter Options: ")
        print(f"  1. Greater Than == {str(self.GSFO_Greater_Than)}")
        print(f"  2. Threshold == {str(self.GSFO_Sales_Amount)}")
        print(f"  3. Save and Return")
        print()
        print(f"  Only Show entries with {GSFOptions()} Global sales")
        print()
        o = None
        while True:
            try:
                o = int(input("Enter the number of the option you want to select: "))
                if o == 1:
                    if self.GSFO_Greater_Than == True:
                        self.GSFO_Greater_Than = False
                        self.filterGlobalSales()
                    elif self.GSFO_Greater_Than == False:
                        self.GSFO_Greater_Than = True
                        self.filterGlobalSales()
                elif o == 2:
                    self.filterGlobalSalesThreshold()
                elif o == 3:
                    self.filterSales()
            except:
                pass  
    def filterGlobalSalesThreshold(self):
        blankspace()
        print(f"Current Global Sales Threshold: {self.GSFO_Sales_Amount}")
        print()
        while True:
            try:
                o = int(input("Enter the new Global Sales Threshold: "))
                self.GSFO_Sales_Amount = o
                self.filterGlobalSales()
            except:
                pass  
    def filterNASales(self):
        def NASFOptions():
            if self.NA_Greater_Than == True:
                return(f"GREATER THAN {self.NA_Sales_Amount}")
            else:
                return(f"LESS THAN {self.NA_Sales_Amount}")
        blankspace()
        print("DataFrame NA Sales Filter Options: ")
        print(f"  1. Greater Than == {str(self.NASFO_Greater_Than)}")
        print(f"  2. Threshold == {str(self.NASFO_Sales_Amount)}")
        print(f"  3. Save and Return")
        print()
        print(f"  Only Show entries with {NASFOptions()} NA sales")
        print()
        o = None
        while True:
            try:
                o = int(input("Enter the number of the option you want to select: "))
                if o == 1:
                    if self.NASFO_Greater_Than == True:
                        self.NASFO_Greater_Than = False
                        self.filterNASales()
                    elif self.NASFO_Greater_Than == False:
                        self.NASFO_Greater_Than = True
                        self.filterNASales()
                elif o == 2:
                    self.filterNASalesThreshold()
                elif o == 3:
                    self.filterSales()
            except:
                pass        
    def filterNASalesThreshold(self):
        blankspace()
        print(f"Current NA Sales Threshold: {self.NASFO_Sales_Amount}")
        print()
        while True:
            try:
                o = int(input("Enter the new NA Sales Threshold: "))
                self.NASFO_Sales_Amount = o
                self.filterNASales()
            except:
                pass
    def filterEUSales(self):
        def EUSFOptions():
            if self.EUSFO_Greater_Than == True:
                return(f"GREATER THAN {self.EUSFO_Sales_Amount}")
            else:
                return(f"LESS THAN {self.EUSFO_Sales_Amount}")
        blankspace()
        print("DataFrame EU Sales Filter Options: ")
        print(f"  1. Greater Than == {str(self.EUSFO_Greater_Than)}")
        print(f"  2. Threshold == {str(self.EUSFO_Sales_Amount)}")
        print(f"  3. Save and Return")
        print()
        print(f"  Only Show entries with {EUSFOptions()} EU sales")
        print()
        o = None
        while True:
            try:
                o = int(input("Enter the number of the option you want to select: "))
                if o == 1:
                    if self.EUSFO_Greater_Than == True:
                        self.EUSFO_Greater_Than = False
                        self.filterEUSales()
                    elif self.EUSFO_Greater_Than == False:
                        self.EUSFO_Greater_Than = True
                        self.filterEUSales()
                elif o == 2:
                    self.filterEUSalesThreshold()
                elif o == 3:
                    self.filterSales()
            except:
                pass  
    def filterEUSalesThreshold(self):
        blankspace()
        print(f"Current EU Sales Threshold: {self.EUSFO_Sales_Amount}")
        print()
        while True:
            try:
                o = int(input("Enter the new EU Sales Threshold: "))
                self.EUSFO_Sales_Amount = o
                self.filterEUSales()
            except:
                pass  
    def filterJPSales(self):
        def JPSFOptions():
            if self.JPSFO_Greater_Than == True:
                return(f"GREATER THAN {self.JP_Sales_Amount}")
            else:
                return(f"LESS THAN {self.JP_Sales_Amount}")
        blankspace()
        print("DataFrame JP Sales Filter Options: ")
        print(f"  1. Greater Than == {str(self.JPSFO_Greater_Than)}")
        print(f"  2. Threshold == {str(self.JPSFO_Sales_Amount)}")
        print(f"  3. Save and Return")
        print()
        print(f"  Only Show entries with {JPSFOptions()} JP sales")
        print()
        o = None
        while True:
            try:
                o = int(input("Enter the number of the option you want to select: "))
                if o == 1:
                    if self.JPSFO_Greater_Than == True:
                        self.JPSFO_Greater_Than = False
                        self.filterJPSales()
                    elif self.JPSFO_Greater_Than == False:
                        self.JPSFO_Greater_Than = True
                        self.filterJPSales()
                elif o == 2:
                    self.filterJPSalesThreshold()
                elif o == 3:
                    self.filterSales()
            except:
                pass        
    def filterJPSalesThreshold(self):
        blankspace()
        print(f"Current JP Sales Threshold: {self.JPSFO_Sales_Amount}")
        print()
        while True:
            try:
                o = int(input("Enter the new JP Sales Threshold: "))
                self.JPSFO_Sales_Amount = o
                self.filterJPSales()
            except:
                pass
    def advancedMain(self):
        print("Advanced DataFrame options")
        print("Make Sales Integers")
        print("Make Sales Floats")
        print("other option idk")
        o = None
        while True:
            o = int(input("Enter the number of the option you want to select: "))
            if o == 1:
                pass
            elif o == 2 :
                pass
            elif o == 3:
                pass
  
df = data("/workspaces/Coding-2-PANDAS-Project/vgsales.csv")
def blankspace():
    for i in range(0, 50):
        print()
df.options() # This calls the first method so the program starts