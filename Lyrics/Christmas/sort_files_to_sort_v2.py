import shutil
import os


def main():
    os.chdir("FilesToSort")
    print("working directory is ", os.getcwd())

    filenames = os.listdir(".")
    # print(filenames)

    for filename in filenames:
        if os.path.isdir(filename):
            continue
        # print(filename)
        file_type = filename.split(".")[-1]
        print(file_type)
        try:
            os.mkdir(file_type)  # makes directory only if one doesnt not already exist
        except FileExistsError:
            print("Already exists")
        shutil.move(filename, file_type)
        print("move {} to {}".format(filename, file_type))

        # directory_name = input("what would you like the {} in? ".format(file_type))
        # os.rename(file_type, directory_name)
        # print("rename {} to {}".format(file_type, directory_name))


main()