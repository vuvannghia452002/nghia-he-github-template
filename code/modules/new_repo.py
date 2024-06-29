import os
from modules.create_file import CreateFile


class NewRepo:
    def __init__(self, root_folder):
        self.root_folder = root_folder

    def start(self):
        print(f"Thư mục gốc: {self.root_folder}")

        CreateFile(f"{self.root_folder}/README.md")
        CreateFile(f"{self.root_folder}/.gitignore")
        contents = """

{
  "extensions": {
    "recommendations": []
  },
  "folders": [
    {
      "path": "."
    },
    {
      "path": "contents"
    }
  ],
  "settings": {}
}

  



"""
        CreateFile(f"{self.root_folder}/{os.path.basename(self.root_folder)}.code-workspace")
