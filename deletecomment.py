import re
import sys

def commentRemover(text):
    def replacer(match):
        s = match.group(0)
        if s.startswith('/'):
            return ""
        else:
            return s
    pattern = re.compile(
        r'//.*?$|/\*.*?\*/|\'(?:\\.|[^\\\'])*\'|"(?:\\.|[^\\"])*"',
        re.DOTALL | re.MULTILINE
    )
    return re.sub(pattern, replacer, text)

def deleteComment(myresult):
    Data = myresult
    i = 0
    while i < len(Data):
        uncmtFile = commentRemover(Data[i][1])
        Data[i][1] = uncmtFile
        i += 1
    return Data

if __name__ == '__main__':
    globals()[sys.argv[1]]()