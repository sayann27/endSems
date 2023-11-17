with open('demo.txt', 'r') as file:
    lines = file.readlines()

    with open('new_file.txt', 'w+') as file1:
        file1.writelines(lines)
        file1.write("\nThis is the newline")


with open('demo.txt', 'a') as file:
    file.write("\nThis is written using append mode")