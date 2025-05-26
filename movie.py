import pandas as pd
import platform as plt
import matplotlib.pyplot as pt
import os
import sys

while True:
    uname=input('Enter your Username:')
    if uname=='Mridul':
        print()
        pwd=input('Enter your password:')
        if pwd=='100':
            print('ACCESS GRANTED')
            break
        else:
            print('ACCESS DENIED')
    else:
        print('INCORRECT USERNAME')
        
df=pd.read_csv("M:\Desktop\pythonMridul\Movie.csv",index_col='Movie_Name')
print(df)
    

def addmoviedetail(df):
    Movie_Name=input('Enter Movie Name:')
    Release_Date=(input('Enter Release Date:'))
    IMDB_Rating=float(input('Enter IMDB Rating:'))
    Box_Office_collection_in_crore=int(input('Enter Box Office Collection:'))
    Buget_in_crore=int(input('Enter NetBuget:'))
    Estimated_profit_in_crore=(Box_Office_collection_in_crore-Buget_in_crore)
    df.loc[Movie_Name,:]=[Release_Date,IMDB_Rating,Box_Office_collection_in_crore,Buget_in_crore,Estimated_profit_in_crore]
    df.to_csv("M:\Desktop\pythonMridul\Movie.csv")

def updatedetail(df):
    Movie_Name=input('Enter Movie name to be updated :')
    Release_Date=(input('Enter New Release Date:'))
    IMDB_Rating=(input('Enter New IMDB Rating:'))
    Box_Office_collection_in_crore=int(input('Enter New Box Office Collection:'))
    Buget_in_crore=int(input('Enter New NetBuget:'))
    Estimated_profit_in_crore=(Box_Office_collection_in_crore-Buget_in_crore)
    df.loc[Movie_Name,:]=[Release_Date,IMDB_Rating,Box_Office_collection_in_crore,Buget_in_crore,Estimated_profit_in_crore]
    df.to_csv('"M:\Desktop\pythonMridul\Movie.csv"')

    
def removedetails(df):
    Movie_Name=input('Enter the Movie Name which you want to drop:')
    df=df.drop([Movie_Name],axis=0)
    df.to_csv('"M:\Desktop\pythonMridul\Movie.csv"')


    
def readCSV():
    print('Reading complete csv file')
    df=pd.read_csv('"M:\Desktop\pythonMridul\Movie.csv"',index_col='Movie_Name')
    print(df)

def sortingdetails():
    df=pd.read_csv('"M:\Desktop\pythonMridul\Movie.csv"')
    print('1 - Arrange the  details as per Name')
    print('2 - Arrange the details as per Rating')
    print("3 - Arrange the details as per Buget")
    print('4 - Arrange the details as per Total Collection')
    print('5 - Arrange the details as per Profit')
    ch=int(input('Enter your choice:'))
    if ch==1:
        df.sort_values(['Movie_Name'],inplace=True)
        print(df)
    elif ch==2:
        df.sort_values(['IMDB_Rating'],inplace=True)
        print(df)
    elif ch==3:
        df.sort_values(['Buget_in_crore'],inplace=True)
        print(df)
    elif ch==4:
        df.sort_values(['Total_Collection_in_crore'],inplace=True)
        print(df)
    elif ch==5:
        df.sort_values(['Profit_in_crore'],inplace=True)
        print(df)
    else:
        print('Enter a valid input')


def TopandBottom():
    df=pd.read_csv('"M:\Desktop\pythonMridul\Movie.csv"',index_col=0)
    A=int(input('Enter number of record to be  displayed from the top:'))
    if A>20:
        print('Values out of record Range')
    else:
        print('First',A,'record are')
        print(df.head(A))
    B=int(input('Enter number of record to be  displayed from the bottom:'))
    if B>20:
        print('Values out of record Range')
    else:
        print('Last',B,'record are')
        print(df.tail(B))

def GarphicalRepresentation():
    df=pd.read_csv('"M:\Desktop\pythonMridul\Movie.csv"')
    print('1 - Graphical representation of Movie vs IMDB Ratings')
    print('2 - Graphical representation of Movie vs Collection')
    print('3 - Graphical representation of Movie vs Buget')
    print('4 - Graphical representation of Movie vs Profit') 
    Name=df['Movie_Name']
    Rating=df['IMDB_Rating']
    Collection=df['Total_Collection_in_crore']
    Buget=df['Buget_in_crore']
    Profit=df['Profit_in_crore']
    ch=int(input('Enter Your Choice:'))
    if ch==1:
        pt.xlabel('Movie')
        pt.ylabel('IMDB Ratings')
        pt.barh(Name,Rating)
        pt.show()
    elif ch==2:
        pt.xlabel('Movie')
        pt.ylabel('Point')
        pt.barh(Name,Collection)
        pt.show()
    elif ch==3:
        pt.xlabel('Movie')
        pt.ylabel('Ranking')
        pt.barh(Name,Buget)
        pt.show()
    elif ch==4:
        pt.xlabel('Movie')
        pt.ylabel('Profit')
        pt.barh(Name,Profit)
        pt.show()
        
    else:
        print('Enter a valid input')

def menu():
    print("************ Welcome To Movie Analysis Program***********")
    print('Enter 1 - Adding Movie Details')
    print('Enter 2 - Updating Movie Details')
    print('Enter 3 - Deleting Movie Details')
    print('Enter 4 - Sorting Details')
    print('Enter 5 - Top And Bottom Details')
    print('Enter 6 - Representing Details Graphically')
    print('Enter 7 - Show Full Data')
    ch=int(input('Enter your choice:'))
    if ch==1:
        addmoviedetail(df)
    elif ch==2:
        updatedetail(df)
    elif ch==3:
        removedetails(df)
    elif ch==4:
        sortingdetails()
    elif ch==5:
        TopandBottom()
    elif ch==6:
        GarphicalRepresentation()
    elif ch==7:
        readCSV()
    else:
        print('Enter valid choice')    
    
menu()

def runagain():
    A=input("Do you want to continue Y/N:")
    while(A.lower()=='y'):
        if (plt.system()=='Windows'):
            print (os.system('cls'))
        else:
            print(os.system('clear'))
        menu()
        A=input("Do you want to continue Y/N:")
runagain()        

