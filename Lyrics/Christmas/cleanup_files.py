"""
CP1404/CP5632 Practical
Demos of various os module examples
"""
import os


def main():
    """Clean up inconsistent song lyric file names"""
    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):
        print("Directory:", directory_name)
        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))

        for filename in filenames:
            full_name = os.path.join(directory_name, filename)
            new_name = os.path.join(directory_name, get_fixed_filename(filename))
            print("From {} to {}".format(full_name, new_name))
            # os.rename(full_name, new_name)


def get_fixed_filename(filename):  # does not work as intended
    """Return a 'fixed' version of filename."""
    char_list = []
    underscore_list = []
    for i, char in enumerate(filename):
        char_list.append(char)
        # print(char_list)
        try:
            if char.isupper() and char_list[-2].islower():
                print(char, i)
                # char_list.insert(i, "_")
                underscore_list.append(i)
        except IndexError:
            continue

    for i in underscore_list:
        char_list.insert(i, "_")

    print(char_list)
    print(underscore_list)
    new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
    print(new_name)
    return new_name


main()