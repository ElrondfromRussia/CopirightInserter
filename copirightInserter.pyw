import sys
import os

COSN_COPYSTRING = "// Copyright 2020 Company name\n//\n"
PY_COPYSTRING = "# Copyright 2020 Company name\n#\n"
WFILE = ".go"


################################################################
################################################################
################################################################
def insert_everywhere(dir_name):
    if dir_name == "":
        raise Exception("empty path")
    for root, dirs, files in os.walk(dir_name):
        for file in files:
            if file.endswith(WFILE):
                with open(os.path.join(root, file), 'r+') as f:
                    lines = f.readlines()
                    f.seek(0)
                    if WFILE in [".go", ".c", ".cpp", ".js"]:
                        f.write(COSN_COPYSTRING)
                    elif WFILE in [".py", ".pyw"]:
                        f.write(PY_COPYSTRING)
                    for line in lines:
                        f.write(line)


################################################################
################################################################
################################################################
def main():
    global WFILE
    path = ""
    if len(sys.argv) > 2:
        path = sys.argv[1]
        WFILE = "." + sys.argv[2]
    print(path, WFILE)
    try:
        print("START")
        insert_everywhere(path)
    except BaseException as ex:
        print("ERROR: ", ex)
    finally:
        print("END")


################################################################
################################################################
################################################################


main()
