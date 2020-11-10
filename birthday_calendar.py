"""
Program that creates birthday strings inside a csv file
version 1.1
        Added ability to remove elements within the program
Marc (NessInMorse)
9 november 2020
"""

def makeFile(filename = "birthdays.csv"):
        """
        Creates a new csv file in case there isn't one
        in: (optional) filename
        out: file with said filename with the line:
                "person,day,month,year"
        """
        try:
                infile = open(f"{filename}","x")
                infile.write("person,day,month,year\n")
                infile.close()
        except:
                print(f"{filename} will be re-used")


def getFile(filename = "birthdays.csv", birthdays = []):
        """
        Gets all the birthdays that are in the file
        in: (optional) filename,
                (optional) all csv-file like birthdays
        out: all the birthdays in a list
        """
        infile = open(f"{filename}","r")
        data = infile.readlines()
        for line in data:
                birthdays.append(line)
        return birthdays


def choiceMenu(choice = "-1", functions = ["add","print",\
                                         "remove","save and quit",
                                           "quit"]):
        """
        prints out all choice a user can make
        in: (optional) choice (for function)
                (optional) names for the functions
        out:
                choice of the user
        """
        while not choice.isdigit():
                print("What would you like to do?\n")
                print("\n".join([f"{i+1}\t{functions[i]}"\
                                 for i in range(len(functions))]))
                choice = input()
                if not choice.isdigit() and choice in "".join(functions):
                        choice = str(functions.index(choice)+1)
        return int(choice)-1


def addBirthday(birthdays, birthdate = "", choice = -1,
                months = ["januari","february","march","april",\
                "may","june","july","august","september",\
                "october","november","december"]):
        """
        Add birthday to the csv file
        in: all birthdays
        out: birthday to be added
        """   
        name = input("What is the name of the person\n").capitalize()
        dates = "abc"
        while not dates[0].isdigit() or not dates[1].isdigit() or not\
        dates[2].isdigit():
                birthdate = input("In the format [day-month-year]\n\
when is the person's birthday\n").lower()
                dates = birthdate.split("-")
                if int(dates[0])<0 or int(dates[0])>31:
                        dates[0]=="banaan"
                if dates[1] in months:
                        dates[1]=str(months.index(dates[1])+1)
        dates = ",".join(dates)
        name += ","
        birthdays.append(str(name+dates)+"\n")
        return birthdays


def printBirthdays(birthdays):
        """
        prints out all birthdays of everyone in the list
        in: all the data of the birthdays in a list
        out: all birthdays printed out with space for each element
        """
        for line in birthdays:
                elements = line.strip().split(",")
                print("".join([f"{i:^15}" for i in elements]))
        #alternative method
        #[print("".join([f"{i:^15}" for i in line.strip().split(",")]))for line in birthdays]
        print("\n")
        return birthdays

def removeBirthdays(birthdays,remove_name = "", ans="n",indices = [],\
                    count = 0, remove = 0):
        """
        Removes element in birthday based on name
        in: list of all birthdays
        out: altered birthdays list
        """
        while ans=="n":
                remove_name = input("Which person would you like to remove?\n").strip()
                for birthday in birthdays:
                        if remove_name in birthday:
                                print(f"{count+1:<5}{birthday}")
                                indices.append(birthday)
                                count+=1
                if len(indices)>0:
                        while remove != "":
                                remove = input("Give the number of the person \
to remove\n")
                                if remove.isdigit() and remove!="":
                                        if int(remove)<=len(indices):
                                                birthdays.pop(\
                                                        birthdays.index(\
                                                                indices[int(remove)-1]))
                                                print(f"{indices[int(remove)-1]} has been removed")
                remove = 0
                ans = input("Are you done? (y/n)\n")
        return birthdays

def main():
        makeFile()
        data=getFile()
        choice = 0
        functions = ("addBirthday(data,choice=choice)",\
                     "printBirthdays(data)",\
                     "removeBirthdays(data)",\
                     "")
        while choice != 3 and choice!=4:
                choice = choiceMenu()
                if choice != 3 and choice <4 and choice!="":
                        data = eval(functions[choice])
        if choice ==3: 
                infile = open("birthdays.csv","w")
                
                for line in data:
                        infile.write(f"{line}")
                infile.close()
main()
