import json


class Filemanager():
    def __init__(self):
        self.filePath = "task_manager/todolistdata.json"

    def saveFile(self, content):
        """
            open and write json file

        Args:
            content (self.filepath, w): dump all value to json file
        """
        try:
            with open(self.filePath, 'w') as json_file:
                json.dump(content, json_file, indent=4)
        except FileNotFoundError:
            print("Somthing wrong with the json file, cant be found")

    def loadFile(self):
        """open and read file

        Returns:
            list: json content
        """
        try:
            with open(self.filePath, 'r') as json_file:
                content = json.load(json_file)
                return content
        except FileNotFoundError:
            print("Somthing wrong with the json file, cant be found")

# def main():
#     files = Filemanager()
#     testsave = {
#         "order": 0,
#         "content": "ToDoList"
#     }

#     testload = {}

#     files.saveFile(testsave)
#     testload = files.loadFile()
#     print(testload)


if __name__ == "__main__":
    print("only for testing only")
