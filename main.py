import pandas as pd
class data:
    def __init__(self, csv):
        self.df = (pd.read_csv(csv))        
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
        self.sortType = "Name"
        self.sortAcending = False
        self.salesAsInt = False
        self.entriesPerPage = 50
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
        print("  4. View DataFrame")
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
                elif o == 4:
                    self.compileDF()
                else:
                    self.options()
            except:
                    pass
    def resetDf(self):
        self.filteredDF = self.df
        self.df.reset_index()
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
        self.sortType = "Name"
        self.sortBy = "Name"
        self.sortAcending = False
        self.salesAsInt = False
        self.getFloat()
    def sortMain(self):
        def getSalesText():
            saleslist = ["Global Sales", "NA Sales", "EU_Sales", "JP Sales", "Other Sales"]
            if self.sortType in saleslist:
                return(f"{blue}  1. Sales | {self.sortType} {white}")
            else:
                return("  1. Sales")
        def checkActive(n, x):
            if x == self.sortType:
                return(f"  {blue}{n}. {x}{white}")
            else:
                return(f"  {n}. {x}")
        blankspace()
        print("DataFrame Sorting Options") # How are we going to sort by multiple things wont the sorts override each other?
        print(getSalesText())
        print(checkActive(2, "Year"))
        print(checkActive(3, "Name"))
        print(f"{getBoolCode(self.sortAcending)}  4. Sort Ascending == {self.sortAcending}{white}")
        print("  5. Save and Return")
        print()
        print(f"Sorting by {blue}{self.sortType}{white} | {getBoolCode(self.sortAcending)}Ascending == {self.sortAcending}{white}")
        print()
        o = None
        while True:
            try:
                o = int(input("Enter the number of the option you want to select: "))
                if o == 1:    
                    self.sortSales()
                    break
                elif o == 2:
                    if self.sortType != "Year":
                        self.sortType = "Year"
                    else:
                        self.sortType = "Name"
                    self.sortMain()
                elif o == 3:
                    if self.sortType != "Name":
                        self.sortType = "Name"
                    else:
                        self.sortType = "Name"
                    self.sortMain()
                elif o == 4:
                    if self.sortAcending == True:
                       self.sortAcending = False
                       self.sortMain()
                       break
                    elif self.sortAcending == False:
                       self.sortAcending = True
                       self.sortMain()
                elif o == 5:
                    self.options()
                    break
                else:
                    self.sortMain()
            except:
                pass
    def sortSales(self):
        def checkActive(n, x):
            if x == self.sortType:
                return(f"  {blue}{n}. {x}{white}")
            else:
                return(f"  {n}. {x}")
        blankspace()
        print("DataFrame Sales Sorting Options")
        print(checkActive(1, "Global Sales"))
        print(checkActive(2, "NA Sales"))
        print(checkActive(3, "EU Sales"))
        print(checkActive(4, "JP Sales"))
        print(checkActive(5, "Other Sales"))
        print("  6. Return")
        print()
        print(f"Sorting by {blue}{self.sortType}{white} | {getBoolCode(self.sortAcending)}Ascending == {self.sortAcending}{white}")
        print()
        while True:
            try:
                o = int(input("Enter the number of the option you want to select: "))
                if o == 1:    
                    if self.sortType != "Global Sales":
                        self.sortType = "Global Sales"
                    else:
                        self.sortType = "Name"
                    self.sortMain()
                elif o == 2:
                    if self.sortType != "NA Sales":
                        self.sortType = "NA Sales"
                    else:
                        self.sortType = "Name"
                    self.sortMain()
                elif o == 3:
                    if self.sortType != "EU Sales":
                        self.sortType = "EU Sales"
                    else:
                        self.sortType = "Name"
                    self.sortMain()
                elif o == 4:
                    if self.sortType != "JP Sales":
                        self.sortType = "JP Sales"
                    else:
                        self.sortType = "Name"
                    self.sortMain()
                elif o == 5:
                    if self.sortType != "Other Sales":
                        self.sortType = "Other Sales"
                    else:
                        self.sortType = "Name"
                    self.sortMain()
                elif o == 6:
                    self.sortMain()
                else:
                    self.sortMain()
            except:
                pass
    def advancedMain(self):
        blankspace()
        print("Advanced DataFrame options")
        print(f"{getBoolCode(self.salesAsInt)}  1. Sales Displayed as Integers == {self.salesAsInt}{white}")
        print(f"  2. {blue}{self.entriesPerPage}{white} Entries Displayed Per Page")
        print(f"{getBoolCode(False)}  3. Reset DataFrame{white}")
        print("  4. Save and Return")
        while True:
            try:
                o = int(input("Enter the number of the option you want to select: "))
                if o == 1:
                    if self.salesAsInt == True:
                        self.salesAsInt = False
                        self.getFloat()
                        self.advancedMain()                    
                    if self.salesAsInt == False:
                        self.salesAsInt = True
                        self.getInt()
                        self.advancedMain()
                elif o == 2:
                    self.showXEntries()
                elif o == 3:
                    self.confirmReset()
                elif o == 4:
                    self.options()
            except:
                pass
    def showXEntries(self):
        blankspace()
        print(f"Current Entries Per Page: {blue}{self.entriesPerPage}{white}")
        print()
        while True:
            try:
                o = int(input("How many entries would you like to see per page: "))
                if o >= 10:    
                    self.entriesPerPage = o
                    self.advancedMain()
            except:
                pass
    def confirmReset(self):
        blankspace()
        print("DataFrame Reset Confirmation")
        print()
        o = str(input(f"Type 'YES' to confirm reset: "))
        if o == "YES":
            self.resetDf()
            self.options()
        else:
            self.advancedMain()
    def filterMain(self):
        def MainFilterDisplay(x):
            if x == True:
                return(f"{getBoolCode(x)}After{white}")
            else:
                return(f"{getBoolCode(x)}Before{white}")
        blankspace()
        print("DataFrame Filter Options:")
        print(f"  1. Sales | Select to View More")
        print(f"  2. Year  | {MainFilterDisplay(self.YFO_After)} {blue}{self.YFO_Threshold}{white}")
        print(f"  3. Genre | Select to View More")
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
        def SalesFilterDisplay(x):
            if x == True:
                return(f"{getBoolCode(x)}More Than{white}")
            else:
                return(f"{getBoolCode(x)}Less Than{white}")
        blankspace()
        print("DataFrame Sales Filter Options: ")
        print(f"  1. Global Sales | {SalesFilterDisplay(self.GSFO_Greater_Than)} {blue}{self.GSFO_Sales_Amount}{white}")
        print(f"  2. NA Sales     | {SalesFilterDisplay(self.NASFO_Greater_Than)} {blue}{self.NASFO_Sales_Amount}{white}")
        print(f"  3. EU Sales     | {SalesFilterDisplay(self.EUSFO_Greater_Than)} {blue}{self.EUSFO_Sales_Amount}{white}")
        print(f"  4. JP Sales     | {SalesFilterDisplay(self.JPSFO_Greater_Than)} {blue}{self.JPSFO_Sales_Amount}{white}")
        print(f"  5. Other Sales  | {SalesFilterDisplay(self.OSFO_Greater_Than)} {blue}{self.OSFO_Sales_Amount}{white}")
        print(f"  6. Save and return")
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
                return(f"{getBoolCode(self.GSFO_Greater_Than)}GREATER THAN {blue}{self.GSFO_Sales_Amount}{white}")
            else:
                return(f"{getBoolCode(self.GSFO_Greater_Than)}LESS THAN {blue}{self.GSFO_Sales_Amount}{white}")
        blankspace()
        print("DataFrame Global Sales Filter Options: ")
        print(f"{getBoolCode(self.GSFO_Greater_Than)}  1. Greater Than == {str(self.GSFO_Greater_Than)}{white}")
        print(f"  2. Threshold == {blue}{str(self.GSFO_Sales_Amount)}{white}")
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
        print(f"Current Global Sales Threshold: {blue}{self.GSFO_Sales_Amount}{white}")
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
                return(f"{getBoolCode(self.NASFO_Greater_Than)}GREATER THAN {blue}{self.NASFO_Sales_Amount}{white}")
            else:
                return(f"{getBoolCode(self.NASFO_Greater_Than)}LESS THAN {blue}{self.NASFO_Sales_Amount}{white}")
        blankspace()
        print("DataFrame NA Sales Filter Options: ")
        print(f"{getBoolCode(self.NASFO_Greater_Than)}  1. Greater Than == {str(self.NASFO_Greater_Than)}{white}")
        print(f"  2. Threshold == {blue}{str(self.NASFO_Sales_Amount)}{white}")
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
        print(f"Current NA Sales Threshold: {blue}{self.NASFO_Sales_Amount}{white}")
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
                return(f"{getBoolCode(self.EUSFO_Greater_Than)}GREATER THAN {blue}{self.EUSFO_Sales_Amount}{white}")
            else:
                return(f"{getBoolCode(self.EUSFO_Greater_Than)}LESS THAN {blue}{self.EUSFO_Sales_Amount}{white}")
        blankspace()
        print("DataFrame EU Sales Filter Options: ")
        print(f"{getBoolCode(self.EUSFO_Greater_Than)}  1. Greater Than == {str(self.EUSFO_Greater_Than)}{white}")
        print(f"  2. Threshold == {blue}{str(self.EUSFO_Sales_Amount)}{white}")
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
        print(f"Current EU Sales Threshold: {blue}{self.EUSFO_Sales_Amount}{white}")
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
                return(f"{getBoolCode(self.JPSFO_Greater_Than)}GREATER THAN {blue}{self.JPSFO_Sales_Amount}{white}")
            else:
                return(f"{getBoolCode(self.JPSFO_Greater_Than)}LESS THAN {blue}{self.JPSFO_Sales_Amount}{white}")
        blankspace()
        print("DataFrame JP Sales Filter Options: ")
        print(f"{getBoolCode(self.JPSFO_Greater_Than)}  1. Greater Than == {str(self.JPSFO_Greater_Than)}\x1b[0m")
        print(f"  2. Threshold == {blue}{str(self.JPSFO_Sales_Amount)}{white}")
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
        print(f"Current JP Sales Threshold: {blue}{self.JPSFO_Sales_Amount}{white}")
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
                return(f"{getBoolCode(self.OSFO_Greater_Than)}GREATER THAN {blue}{self.OSFO_Sales_Amount}{white}")
            else:
                return(f"{getBoolCode(self.OSFO_Greater_Than)}LESS THAN {blue}{self.OSFO_Sales_Amount}{white}")
        blankspace()
        print("DataFrame Other Sales Filter Options: ")
        print(f"{getBoolCode(self.OSFO_Greater_Than)}  1. Greater Than == {str(self.OSFO_Greater_Than)} \x1b[0m")
        print(f"  2. Threshold == {blue}{str(self.OSFO_Sales_Amount)}{white}")
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
        print(f"Current Other Sales Threshold: {blue}{self.JPSFO_Sales_Amount}{white}")
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
                return(f"{getBoolCode(self.YFO_After)}AFTER {blue}{self.YFO_Threshold}{white}")
            elif self.YFO_After == False:
                return(f"{getBoolCode(self.YFO_After)}BEFORE {blue}{self.YFO_Threshold}{white}")
        print("Data Frame Year Filtering Options")
        print(f"{getBoolCode(self.YFO_After)}  1. After == {self.YFO_After} \x1b[0m")
        print(f"  2. Threshold == {blue}{self.YFO_Threshold}{white}")
        print("  3. Save and Return")
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
        print(f"Current Year Threshold: {blue}{self.YFO_Threshold}{white}")
        print()
        while True:
            try:
                o = int(input("Enter the new Year Threshold: "))
                if o >= 1980:    
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
        def getItemColor(x):
            if x in self.GFO_List:
                return("\x1b[0;38;2;0;119;255;49m")
            else:
                return("\x1b[0m")
        print("DataFrame Main Genre Filtering Options")
        print()
        print(f"{getItemColor("Sports")}  1. Sports\x1b[0m")
        print(f"{getItemColor("Platform")}  2. Platforming\x1b[0m")
        print(f"{getItemColor("Racing")}  3. Racing\x1b[0m")
        print(f"{getItemColor("Role-Playing")}  4. Role-Playing\x1b[0m")
        print(f"{getItemColor("Puzzle")}  5. Puzzle\x1b[0m")
        print(f"{getItemColor("Shooter")}  6. Shooter\x1b[0m")
        print(f"{getItemColor("Simulation")}  7. Simulation\x1b[0m")
        print(f"{getItemColor("Action")}  8. Action\x1b[0m")
        print(f"{getItemColor("Fighting")}  9. Fighting\x1b[0m")
        print(f"{getItemColor("Adventure")}  10. Adventure\x1b[0m")
        print(f"{getItemColor("Strategy")}  11. Strategy\x1b[0m")
        print(f"{getItemColor("Misc")}  12. Misc\x1b[0m")
        print(f"{getBoolCode(self.GFO_Include)}  13. Include == {self.GFO_Include} \x1b[0m")
        print("  14. Save and Return")
        print()
        print(f"  The DataFrame Will {getBoolCode(self.GFO_Include)}{Genre_Filter_Include()}{white}The Following Genres:")
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
                pass          
    def compileDF(self):
        blankspace()
        def convertSortBy():
            if self.sortType == "Global Sales":
                self.sortBy = "Global_Sales"
            elif self.sortType == "NA Sales":
                self.sortBy = "NA_Sales"
            elif self.sortType == "EU Sales":
                self.sortBy = "EU_Sales"
            elif self.sortType == "JP Sales":
                self.sortBy = "JP_Sales"
            elif self.sortType == "Other Sales":
                self.sortBy = "Other_Sales"
            else:
                self.sortBy = self.sortType
        convertSortBy()
        print(self.entriesPerPage)
        print(self.sortBy)
        print(self.sortAcending)
        if self.GSFO_Greater_Than == True:    
            self.df = self.df.loc[df["Global_Sales"] > (self.GSFO_Sales_Amount)]
        elif self.GSFO_Greater_Than == False:    
            self.df = self.df.loc[df["Global_Sales"] < (self.GSFO_Sales_Amount)]
        if self.NASFO_Greater_Than == True:    
            self.df = self.df.loc[df["NA_Sales"] > (self.NASFO_Sales_Amount)]
        elif self.NASFO_Greater_Than == False:    
            self.df = self.df.loc[df["NA_Sales"] < (self.NASFO_Sales_Amount)]
        if self.EUSFO_Greater_Than == True:    
            self.df = self.df.loc[df["EU_Sales"] > (self.EUSFO_Sales_Amount)]
        elif self.EUSFO_Greater_Than == False:    
            self.df = self.df.loc[df["EU_Sales"] < (self.EUSFO_Sales_Amount)]
        if self.JPSFO_Greater_Than == True:    
            self.df = self.df.loc[df["JP_Sales"] > (self.JPSFO_Sales_Amount)]
        elif self.JPSFO_Greater_Than == False:    
            self.df = self.df.loc[df["JP_Sales"] < (self.JPSFO_Sales_Amount)]
        if self.OSFO_Greater_Than == True:    
            self.df = self.df.loc[df["Other_Sales"] > (self.OSFO_Sales_Amount)]
        elif self.OSFO_Greater_Than == False:    
            self.df = self.df.loc[df["Other_Sales"] < (self.OSFO_Sales_Amount)]        
        if self.YFO_After == True:    
            self.df = self.df.loc[df["Year"] > (self.YFO_Threshold)]
        elif self.YFO_After == False:    
            self.df = self.df.loc[df["Year"] < (self.YFO_Threshold)]
        print(self.df.sort_values(by=(self.sortBy), ascending=(self.sortAcending)).head(self.entriesPerPage))
df = data("/workspaces/Coding-2-PANDAS-Project/vgsales.csv")
blue = "\x1b[0;38;2;0;119;255;49m"
white = "\x1b[0m"
# print(df.df.sort_values(by="Year").head())
def blankspace():
    for i in range(50):
        print()
def getBoolCode(x):
    if x == True:
        return("\x1b[0;38;2;0;255;0;49m")
    else:
        return("\x1b[0;38;2;255;0;0;49m")
# print(df.df["Genre"].unique())
# sorted_df = df.df.sort_values(by="Global_Sales", ascending=True)
# print(sorted_df.head(10))
df.options() # This calls the first method so the program starts