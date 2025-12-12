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
        self.OSFO_Greater_Than = True
        self.OSFO_Sales_Amount = 0
        self.YFO_Threshold = 1980
        self.YFO_After = True
        self.GFO_Include = False
        self.GFO_List = []
        self.sortType = "None"
        self.sortAcending = True
        self.topEntries = None
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
                    break
                elif o == 2:
                    self.sortMain()
                    break
                elif o == 3:
                    self.advancedMain()
                    break
                elif o == 4:
                    self.resetDf()
                    print("DataFrame Reset")
                    self.options()
                    break
                elif o == 5:
                    blankspace()
                    if self.topEntries == None:
                        print(self.df)
                    else:
                        print(self.df.head(self.topEntries))
                else:
                    print("Invalid Input Let's Try Agian")
                    self.options()
                    break
            except:
                    pass
    def resetDf(self):
        self.df.reset_index
    def sortMain(self):
        blankspace()
        print("DataFrame Sorting Options") # How are we going to sort by multiple things wont the sorts override each other?
        print("  1. Sales")
        print("  2. Year")
        print("  3. Title")
        print("  4. Reset DataFrame")
        print("  5. Save and Return")
        print()
        print(f"Sorting by {self.sortType} | Acending == {self.sortAcending}")
        o = None
        while True:
            try:
                o = int(input("Enter the number of the option you want to select: "))
                if o == 1:    
                    self.sortSales()
                    break
                elif o == 2:
                    self.sortYear()
                    break
                elif o == 3:
                    self.sortTitle()
                    break
                elif o == 4:
                    self.df.reset_index
                    self.sortMain()
                    break
                elif o == 5:
                    print("saved")
                    self.options()
                    break
                else:
                    print("Invaild Input")
                    self.sortMain()
            except:
                pass
    def sortYear(self):
        blankspace()
        self.df.sort_values(by="Year", ascending = self.sortAcending)
        print("DataFrame Year Sorting Options")
        print(f" 1. Acending | {self.sortAcending}")
        print("  2. Save and Return")
        o = None
        while True:
            o = int(input("Enter the number of the option you want to select:" ))
            if o == 1:
                if self.sortAcending == True:
                    self.sortAcending = False
                    self.sortYear()
                    break
                elif self.sortAcending == False:
                    self.sortAcending = True
                    self.sortYear()
                    break
            elif o == 2:
                self.sortMain()
                break
            else:
                print("Invaild Input")
                self.sortYear()
    def sortTitle(self):
        blankspace()
        self.df.sort_values("Name",ascending= self.sortAcending)
        print("DataFrame Title Sorting Options")
        print(f" 1. Acending | {self.sortAcending}")
        print("  2. Save and Return")
        o = None
        while True:
            o = int(input("Enter the number of the option you want to select:" ))
            if o == 1:
                if self.sortAcending == True:
                    self.sortAcending = False
                    self.sortTitle()
                    break
                elif self.sortAcending == False:
                    self.sortAcending = True
                    self.sortTitle()
                    break
            elif o == 2:
                self.sortMain()
                break
            else:
                print("Invaild Input")
                self.sortTitle()
    def sortSales(self):
        blankspace()
        print("DataFrame Sales Sorting Options")
        print("  1. Global Sales")
        print("  2. NA Sales")
        print("  3. EU Sales")
        print("  4. JP Sales")
        print("  5. Other Sales")
        print("  6. Reset Sales Sorting")
        print("  7. Return")
        while True:
            try:
                o = int(input("Enter the number of the option you want to select: "))
                if o == 1:    
                    self.sortGlobalsales()
                    break
                elif o == 2:
                    self.sortNAsales()
                    break
                elif o == 3:
                    self.sortEUsales()
                    break
                elif o == 4:
                    self.sortJPsales()
                    break
                elif o == 5:
                    self.sortOthersales()
                    break
                elif o == 6:
                    print("Reseting Sales Sorting Options")
                    self.df.reset_index()
                    self.sortSales()
                    break
                elif o == 7:
                    self.sortMain()
                    break
                else:
                    print("Invaild Input")
                    self.sortMain()
            except:
                pass
    def sortGlobalsales(self):
        blankspace()
        self.df.sort_values(by="Global_Sales", ascending = self.sortAcending)
        self.sortType = "Global Sales"
        print("Sorting by global sales")
        print(f"     1. Acending | {self.sortAcending}")
        print("     2. Save and Return")
        o = None
        while True:
            try:
                o = int(input("Which option do you want: "))
                if o == 1:
                    if self.sortAcending == True:
                       self.sortAcending = False
                       self.sortGlobalsales()
                       break
                    elif self.sortAcending == False:
                       self.sortAcending = True
                       self.sortGlobalsales()
                       break
                elif o == 2:
                    print("Saving choices")
                    self.sortSales()
                    break
                else:
                    print("Invaild Input")
                    self.sortGlobalsales()
            except:
                pass
    def sortNAsales(self):
        self.df.sort_values(by="NA_Sales", ascending = self.sortAcending)
        blankspace()
        self.sortType = "NA Sales"
        print("Sorting by NA sales")
        print(f"     1. Acending | {self.sortAcending}")
        print("     2. Save and Return")
        o = None
        while True:
            try:
                o = int(input("Which option do you want: "))
                if o == 1:
                    if self.sortAcending == True:
                       self.sortAcending = False
                       self.sortNAsales()
                       break
                    elif self.sortAcending == False:
                       self.sortAcending = True
                       self.sortNAsales()
                       break
                elif o == 2:
                    print("Saving choices")
                    self.sortSales()
                    break
                else:
                    print("Invaild Input")
                    self.sortNAsales()
            except:
                pass
    def sortJPsales(self):
        blankspace()
        self.df.sort_values(by="JP_Sales", ascending = self.sortAcending)
        self.sortType = "JP Sales"
        print("      Sorting by JP sales")
        print(f"     1. Acending | {self.sortAcending}")
        print("      2. Save and Return")
        o = None
        while True:
            try:
                o = int(input("Which option do you want: "))
                if o == 1:
                    if self.sortAcending == True:
                       self.sortAcending = False
                       self.sortJPsales()
                       break
                    elif self.sortAcending == False:
                       self.sortAcending = True
                       self.sortJPsales()
                       break
                elif o == 2:
                    print("Saving choices")
                    self.sortSales()
                    break
                else:
                    print("Invaild Input")
                    self.sortOthersales()
            except:
                pass
    def sortEUsales(self):
        blankspace()
        self.df.sort_values(by="EU_Sales", ascending = self.sortAcending)
        self.sortType = "EU Sales"
        print("      Sorting by EU sales")
        print(f"    1. Acending | {self.sortAcending}")
        print("     2. Save and Return")
        o = None
        while True:
            try:
                o = int(input("Which option do you want: "))
                if o == 1:
                    if self.sortAcending == True:
                       self.sortAcending = False
                       self.sortEUsales()
                       break
                    elif self.sortAcending == False:
                       self.sortAcending = True
                       self.sortEUsales()
                       break
                elif o == 2:
                    print("Saving choices")
                    self.sortSales()
                    break
                else:
                    print("Invaild Input")
                    self.sortEUsales()
            except:
                pass
    def sortOthersales(self):
        blankspace()
        self.df.sort_values(by="Other_Sales", ascending = self.sortAcending)
        self.sortType = "Other Sales"
        print("Sorting by Other sales")
        print(f"    1. Acending | {self.sortAcending}")
        print("     2. Save and Return")
        o = None
        while True:
            try:
                o = int(input("Which option do you want: "))
                if o == 1:
                    if self.sortAcending == True:
                       self.sortAcending = False
                       self.sortOthersales()
                       break
                    elif self.sortAcending == False:
                       self.sortAcending = True
                       self.sortOthersales()
                       break
                elif o == 2:
                    print("Saving choices")
                    self.sortSales()
                    break
                else:
                    print("Invaild Input")
                    self.sortOthersales()
            except:
                pass    
    def advancedMain(self):
        blankspace()
        print("Advanced DataFrame options")
        print("  1. Make Sales Integers")
        print("  2. Make Sales Floats")
        print("  3. Show X Amount of Entries")
        print("  4. Save and Return")
        while True:
            try:
                o = int(input("Enter the number of the option you want to select: "))
                if o == 1:
                    self.getInt()
                    print("Sales Converted to Integers")
                    self.advancedMain()
                    break
                elif o == 2:
                    self.getFloat()
                    print("Sales Converted to Floats")
                    self.advancedMain()
                    break
                elif o == 3:
                    self.showXEntries()
                    break
                elif o == 4:
                    self.options()
            except:
                pass
    def showXEntries(self):
        blankspace()
        print("Show X Amount of Entries")
        print()
        while True:
            try:
                o = int(input("Enter the amount of entries you want to view: "))
                blankspace()
                self.topEntries = o
                self.advancedMain()
                break
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
                elif o == 2:
                    self.filterYear()
                elif o == 3:
                    self.filterGenre()
                elif o == 4:
                    self.options()
            except:
                pass    
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
        x = True
        while x:
            try:
                o = int(input("Enter the number of the option you want to select: "))
                if o == 1:
                    self.filterGlobalSales()
                    x = False
                elif o == 2:
                    self.filterNASales()
                    x = False
                elif o == 3:
                    self.filterEUSales()
                    x = False
                elif o == 4:
                    self.filterJPSales()
                    x = False
                elif o == 5:
                    self.filterOtherSales()
                elif o == 6:
                    self.filterMain()
                    x = False
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
            if self.NASFO_Greater_Than == True:
                return(f"GREATER THAN {self.NASFO_Sales_Amount}")
            else:
                return(f"LESS THAN {self.NASFO_Sales_Amount}")
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
                return(f"GREATER THAN {self.JPSFO_Sales_Amount}")
            else:
                return(f"LESS THAN {self.JPSFO_Sales_Amount}")
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
    def filterOtherSales(self):
        def OSFOptions():
            if self.OSFO_Greater_Than == True:
                return(f"GREATER THAN {self.OSFO_Sales_Amount}")
            else:
                return(f"LESS THAN {self.OSFO_Sales_Amount}")
        blankspace()
        print("DataFrame Other Sales Filter Options: ")
        print(f"{getBoolCode(self.OSFO_Greater_Than)}  1. Greater Than == {str(self.OSFO_Greater_Than)} \x1b[0m")
        print(f"  2. Threshold == {str(self.OSFO_Sales_Amount)}")
        print(f"  3. Save and Return")
        print()
        print(f"  Only Show entries with {OSFOptions()} Other sales")
        print()
        o = None
        while True:
            try:
                o = int(input("Enter the number of the option you want to select: "))
                if o == 1:
                    if self.OSFO_Greater_Than == True:
                        self.OSFO_Greater_Than = False
                        self.filterOtherSales()
                    elif self.OSFO_Greater_Than == False:
                        self.OSFO_Greater_Than = True
                        self.filterOtherSales()
                elif o == 2:
                    self.filterOtherSalesThreshold()
                elif o == 3:
                    self.filterSales()
            except:
                pass  
    def filterOtherSalesThreshold(self):
        blankspace()
        print(f"Current Other Sales Threshold: {self.JPSFO_Sales_Amount}")
        print()
        while True:
            try:
                o = int(input("Enter the new Other Sales Threshold: "))
                self.OSFO_Sales_Amount = o
                self.filterOtherSales()
            except:
                pass  
    def filterYear(self):
        blankspace()
        def YearFilterOptions():
            if self.YFO_After == True:
                return(f"AFTER {self.YFO_Threshold}")
            elif self.YFO_After == False:
                return(f"BEFORE {self.YFO_Threshold}")
        print("Data Frame Year Filtering Options")
        print(f"{getBoolCode(self.YFO_After)}  1. After == {self.YFO_After} \x1b[0m")
        print(f"  2. Threshold == {self.YFO_Threshold}")
        print()
        print(f"  Only show entries released {YearFilterOptions()}")
        print()
        o = None
        while True:
            try:
                o = int(input("Enter the number of the option you want to select: "))
                if o == 1:
                    if self.YFO_After == True:
                        self.YFO_After = False
                        self.filterYear()
                    elif self.YFO_After == False:
                        self.YFO_After = True
                        self.filterYear()
                elif o == 2:
                    self.filterYearThreshold()
                elif o == 3:
                    self.filterMain()
            except:
                pass  
    def filterYearThreshold(self):
        blankspace()
        print(f"Current Year Threshold: {self.YFO_Threshold}")
        print()
        while True:
            try:
                o = int(input("Enter the new Year Threshold: "))
                self.YFO_Threshold = o
                self.filterYear()
            except:
                pass  
    def filterGenre(self):
        blankspace()
        def Genre_Filter_Include():
            if self.GFO_Include == True:
                return("INCLUDE")
            if self.GFO_Include == False:
                return("EXCLUDE")
        def Genre_Filter_List():
            if len(self.GFO_List) == 0:
                print("  None")
            else:
                for item in self.GFO_List:
                    print(f"  {item}")
        print("DataFrame Main Platform Filtering Options")
        print()
        print("  1. Sports")
        print("  2. Platform")
        print("  3. Racing")
        print("  4. Role-Playing")
        print("  5. Puzzle")
        print("  6. Shooter")
        print("  7. Simulation")
        print("  8. Action")
        print("  9. Fighting")
        print("  10. Adventure")
        print("  11. Strategy")
        print("  12. Misc")
        print(f"{getBoolCode(self.GFO_Include)}  13. Include == {self.GFO_Include} \x1b[0m")
        print("  14. Save and Return")
        print()
        print(f"  The DataFrame Will {Genre_Filter_Include()} The Following Genres:")
        Genre_Filter_List()
        print()
        o = None
        while True:
            try:
                o = int(input("Enter the number of the option you want to select: "))
                if o > 0 and o < 13:
                    GList = ['Sports', 'Platform', 'Racing', 'Role-Playing', 'Puzzle', 'Shooter', 'Simulation', 'Action', 'Fighting', 'Adventure', 'Strategy', 'Misc']
                    if GList[o-1] not in self.GFO_List:
                        self.GFO_List.append(GList[o-1])
                    else:
                        self.GFO_List.remove(GList[o-1])
                    self.filterGenre()
                elif o == 13:
                    if self.GFO_Include == True:
                        self.GFO_Include = False
                        self.filterGenre()
                    elif self.GFO_Include == False:
                        self.GFO_Include = True
                        self.filterGenre()
                elif o == 14:
                    self.filterMain()
            except:
                print("Test")
                pass          
df = data("/workspaces/Coding-2-PANDAS-Project/vgsales.csv")
print(df.df.sort_values(by="Year").head())
def blankspace():
    for i in range(50):
        print()
def getBoolCode(x):
    if x == True:
        return("\x1b[32m")
    else:
        return("\x1b[31m")
print(df.df["Genre"].unique())
df.options() # This calls the first method so the program starts