from modules.new_repo import NewRepo


if __name__ == "__main__":

    # root_folder = r"c:\Users\vvn20206205\Desktop\test_rr"
    root_folder = input(f"Nhập vị trí repo mới: ")

    new = NewRepo(root_folder)
    new.start()
