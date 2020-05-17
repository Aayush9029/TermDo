#!/usr/local/bin/python3
'''
Date Created: May 16, 2020
Creator: Aayush Pokharel
License Apache-2.0
'''

import json
from os import system, listdir
import re

class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Todo:

    def __init__(self):
        self.filename = "./todos.json"


    def readData(self):
        json_file =  open(self.filename, 'r')       
        json_object = json.load(json_file) 
        return json_object 
    

    def save(self, data):
        with open(self.filename, "w") as outfile: 
            json.dump(data, outfile, indent=1) 
    
    def addItem(self, item, priority=3):
        print(f"adding {item}")
        data = self.readData()
        
        dictionary = { 
            "priority" : priority,
            "item" : item
        } 
        
        data.append(dictionary)
        self.save(data)



    def deleteItem(self, index=None):
        if index == ' ' or index == '':
            index = '0'

        data = self.readData()
        
        if '-' in index:
            start, end = index.split("-")
            for _ in range((int(end) + 1)-int(start)):
                del data[int(start)]
                self.save(data)
        else:
            for i, _ in enumerate(data):
                if int(index) == i:
                    confirm = input(f"Are you sure you want to delete {data[i]['item']}? ").lower()
                    if confirm == "y" or confirm == 'yes':
                        print(f"Deleting.. => {data[i]['item']}")
                        del data[i]
                        self.save(data)

        self.showToDo()

    
    def showToDo(self):
        banner = f'''{colors.OKBLUE}
    Index       Prority     ToDo{colors.ENDC}  
        '''
        data = self.readData()
        print(banner)
        for index, d in enumerate(data):
            index = f"[{index}]"
            print(' '*2,'{} {:<10s} {} {:<10} {}{} {:<4s} {}'.format(colors.OKGREEN, str(index),colors.FAIL, "!" * d["priority"],colors.BOLD,colors.WARNING, d["item"], colors.ENDC))

 
def checkIndex(user_input):
    filterList = '^[0-9\-]*$'
    numList = '^[0-9]*$'

    if re.match(filterList, user_input):
        return True
    elif re.match(numList, user_input):
        return True
    else:
        print("wrong index")
        return False



Todo = Todo()

def checkFile():
    if "todos.json" in listdir():
        print("FOUND")
        pass
    else:
        print("Data file not found")
        ask = input("Would you like to make one?: ").lower()
        if ask == "yes" or ask == "y":
            with open("todos.json", "w") as f:
                f.write("[]")


def main():
    checkFile()
    system("clear")
    Todo.showToDo()
    
    ask = input("\nPress a to add data d to delete: ").lower()
    if ask == "a":
        item = input("Title: ")
        priority = input("priority (default 3): ")
        if len(priority) < 1:
            priority = 3
        Todo.addItem(item, int(priority))
    elif ask == "d":
        index = input("which index: ")
        if checkIndex(index):
            Todo.deleteItem(index)
    elif ask == 'q':
        exit("Bye")
    else:
        print("unknown command")

    main()

try:
    main()
except KeyboardInterrupt:
    exit("\nBye..")

