from .task import Tododata
from .task_storage import Filemanager
from dataclasses import asdict


class Taskoperation():
    def __init__(self):
        self.files = Filemanager()
    
    def getOrder(self):
            order = 0
            for i in self.files.loadFile():
                order += 1
            return order + 1
        

    def addTodo(self, content: Tododata):
        loadcontent = []
        for i in self.files.loadFile():
            loadcontent.append(i)
        loadcontent.append(content)
        self.files.saveFile(loadcontent)

    def removeTodo(self, number):
        try:
            loadcontent = []
            for i in self.files.loadFile():
                loadcontent.append(i)
            del loadcontent[number - 1]
            for i in loadcontent:
                if i["order"] > number:
                    i["order"] = int(i["order"]) - 1
            self.files.saveFile(loadcontent)
        except (TypeError, ValueError):
            print("you input invalid number/out of scope")

    def listTodo(self):
        return self.files.loadFile()


def main():
    testop = Taskoperation()
    testdict = Tododata(2, "Get fuzz asp ᓀᵥᓂ")
    testop.addTodo(asdict(testdict))
    print(testop.listTodo())
    testop.removeTodo(0)
    print(testop.listTodo())
    print(testop.getOrder())

if __name__ == "__main__":
    main()