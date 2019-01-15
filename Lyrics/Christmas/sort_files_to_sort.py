import shutil
import os


def main():
    os.chdir("FilesToSort")
    print("working directory is ", os.getcwd())

    filenames = os.listdir(".")
    print(filenames)

    for filename in filenames:
        print(filename)
        file_type = filename[filename.find(".")+1:]
        print(file_type)
        try:
            os.mkdir(file_type)  # makes directory only if one doesnt not already exist
        except FileExistsError:
            print("Already exists")
        shutil.move(filename, file_type)

# try:
#     print("make a new directory")
#     os.mkdir('temp')
# except FileExistsError:
#     print("File exists; pass")


main()