import os
import shutil

def list_path(p):
    d = [x for x in os.listdir(p) if os.path.isdir(os.path.join(p, x))]
    f = [x for x in os.listdir(p) if os.path.isfile(os.path.join(p, x))]
    print("Dirs:", d)
    print("Files:", f)
    print("All:", os.listdir(p))

def check_access(p):
    print("Exists:", os.path.exists(p))
    print("Readable:", os.access(p, os.R_OK))
    print("Writable:", os.access(p, os.W_OK))
    print("Executable:", os.access(p, os.X_OK))

def test_path(p):
    if os.path.exists(p):
        print("Path exists")
        print("Filename:", os.path.basename(p))
        print("Directory:", os.path.dirname(p))
    else:
        print("Path does not exist")

def count_lines(f):
    try:
        with open(f, "r") as r:
            print("Line count:", sum(1 for _ in r))
    except:
        print("Cannot read file")

def create_files():
    for i in range(65, 91):
        with open(chr(i) + ".txt", "w") as w:
            w.write("Created file " + chr(i))

def copy_file(src, dst):
    try:
        shutil.copy(src, dst)
        print("Copied")
    except:
        print("Cannot copy")

def del_file(f):
    if os.path.exists(f) and os.access(f, os.W_OK):
        os.remove(f)
        print("Deleted")
    else:
        print("Cannot delete")

# ֲûחמגû
# list_path(".")
# check_access("some_path")
# test_path("some_path")
# count_lines("test.txt")
# create_files()
# copy_file("A.txt", "B.txt")
# del_file("B.txt")
