#! python3
#windows file creator
import sys,os

if len(sys.argv) < 2:
    print("Enter 'FileCreator.py' and file name to add DO NOT ADD THE FILE EXT.")

with open(sys.argv[1]+".py","x") as new_file:
    create_py_file = new_file.write("#! python3")

with open(sys.argv[1] + ".bat","x") as new_bat:
    create_bat_file = new_bat.write('@py.exe ' + "\"" +
        os.path.join(os.getcwd(),sys.argv[1])+".py"+ "\"" + "\n" + "@pause")
print(new_file.closed)
