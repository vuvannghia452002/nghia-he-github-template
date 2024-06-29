def CreateFile(file, contents=""):
    print(f"🚀 Tạo file: {file}")
    with open(f"{file}", "w") as file:
        file.write(contents)
