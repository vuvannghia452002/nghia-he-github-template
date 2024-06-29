# import os

# def CreateFile(name):
#     print(f"🚀 Tạo file {name}")
#     with open(f"{new_repo}/{name}", "w") as file:
#         file.write("")



#     CreateFile(f"{os.path.basename(new_repo)}.code-workspace")
#     CreateFile(".gitignore")

class NewRepo:
    def __init__(self, root_folder):
        self.root_folder = root_folder

    def start(self):
        print(f"Thư mục gốc: {self.root_folder}")
        
        CreateFile("README.md")

