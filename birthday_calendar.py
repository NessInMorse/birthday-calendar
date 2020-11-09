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


def getFile(filename = "birthdays.csv",birthdays = []):
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


def choiceMenu(choice = "-1", functions = ["ADD","PRINT",\
                                         "REMOVE","SAVE AND QUIT",
                                           "QUIT"]):
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
                        choice = str(functions.index(choice))
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
        prints all birthdays of everyone in the list
        in: all the data of the birthdays in a list
        out: all birthdays printed out
        """
        for line in birthdays:
                elements = line.strip().split(",")
                for i in range(len(elements)):
                        print(f"{elements[i]:^15}",end =\
                              ("" if i!=len(elements)-1\
                               else "\n"))
        print("")
        return birthdays
        

def main():
        makeFile()
        data=getFile()
        choice = 0
        functions = ("addBirthday(data,choice=choice)","printBirthdays(data)","0","")
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