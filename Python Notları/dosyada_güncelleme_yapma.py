"""
with open("newfile.txt","r+") as file:
    file.seek(20)
    file.write("adam")

with open("newfile.txt","r+") as file:
    print(file.read())
"""
# sayfa sonunda güncelleme
'''
with open("newfile.txt","a") as file:
    file.write("\n Emel")
with open("newfile.txt","r") as file:
    print(file.read())    
'''
# sayfa başında güncelleme
"""
with open("newfile.txt","r+") as file:
    content = file.read()
    content = "hüseyin kızılay\n" + content
    file.seek(0)
    file.write(content)
    print(content)
"""
#sayfa ortasında güncelleme

with open("newfile.txt","r+") as file:
    list = file.readlines()
    list.insert(1, "emine kızılay\n")
    print(list)
    file.seek(0)
    file.writelines(list)
with open("newfile.txt","r") as file:
    print(file.read())