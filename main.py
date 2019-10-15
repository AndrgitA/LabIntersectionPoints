import os.path
from modules.intersection import IntersectionLines, IntersectionLinesWithDraw

filePath = "./src/lines"

def main():
    if (os.path.isfile(filePath)) :             # file exist
        f = open(filePath, 'r')
        print("lines format: ", f.readline())
        IntersectionLines(f)
        # IntersectionLinesWithDraw(f)
        f.close()
    else :                                      # file not exist
        exit(1)

    
if __name__ == "__main__":
    main()