with open("newfile.txt","r") as file:

    content = file.read()
    print(content)
    file.seek(0)
    print(file.tell())
    content2 = file.read()
    print(content2)
