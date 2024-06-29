from modules.new_repo import NewRepo


if __name__ == "__main__":

    # root_folder = input(f"Nhập vị trí repo mới: ")
    root_folder = r"c:\Users\vvn20206205\Desktop\test_rr"

    new = NewRepo(root_folder)
    new.start()
