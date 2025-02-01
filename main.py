from task_manager.task import Tododata
from task_manager.task_operations import Taskoperation
from task_manager.task_storage import Filemanager
from dataclasses import asdict
import sys


def addL():
    """
        get user input then put it in a data format
        then add to json file
    """
    file = Taskoperation()
    order = file.getOrder()
    try:
        content = str(input("input what cha wanna add: "))
        inputvalue = Tododata(order, content)
    except (TypeError, ValueError):
        print("wrong input/out of scope")
    file.addTodo(asdict(inputvalue))

def removeL():
    """
        get index, the remove value using said index
    """
    file = Taskoperation()
    try:
        number = int(input("input what cha wanna remove (number of the order): "))
    except (TypeError, ValueError):
        print("wrong input/out of scope")
    file.removeTodo(number)

def viewList():
    """
        print json file content
    """
    file = Taskoperation()
    print(file.listTodo())

def userChoiceMenu():
    """
        ask user for number input, limit to 0-3
    Returns:
        int: return user input
    """
    while True:
        try:
            userinput = int(input())
        except (TypeError, ValueError):
            print("wrong input/out of scope")
        if userinput >= 0 and userinput < 4:
            return userinput
        else:
            print("1-3 please")

def menu():
    """
        simple ui
    """
    print("Welcome todolist")
    print("1. Add")
    print("2. Remove")
    print("3. ViewList")
    print("0. exit")

def main():
    """
        get user choice then match with diffent case
        then do different thing accoring to user input
    """ 
    while True:
        menu()
        userChoice = userChoiceMenu()
        match userChoice:
            case 1:
                addL()
            case 2:
                removeL()
            case 3:
                viewList()
            case 0:
                sys.exit(0)
            case _:
                print("huh?")
    

if __name__ == "__main__":
    main()