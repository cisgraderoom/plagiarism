import re
import os,sys

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

# path = 'checkPlagiarism'
def deleteComment(myresult):
    # for x in os.listdir(path):
    Data = myresult
    i = 0
    while i < len(Data):
        uncmtFile = commentRemover(Data[i][1])
        Data[i][1] = uncmtFile
        print(Data[i][1])
        i += 1
    # Data[0][1] = "1"
    # for i, element in enumerate(Data):
    #     uncmtFile = commentRemover(element[i][1])
    #     Data[i][1] = uncmtFile
    print(Data)
    # for x in Data:
    #     print(x[1])
    #     uncmtFile = commentRemover(x[1])
    #     print(uncmtFile)
        # x[1] = uncmtFile
        # if x.endswith(".c") or x.endswith(".cpp") or x.endswith(".java"):
        #     # filename = x
        #     filename = f'{path}\\{x}'
        #     with open(filename) as f:
        #         uncmtFile = commentRemover(f.read())
        #     new_file = open(filename, "w+")
        #     new_file.write(uncmtFile)
    # print(myresult[0][1])
    print('Comment has been deleted.')
    return Data

if __name__ == '__main__':
    globals()[sys.argv[1]]()

# for x in os.listdir():
#     if x.endswith(".c") or x.endswith(".cpp") or x.endswith(".java"):
#         filename = x
#         with open(filename) as f:
#           uncmtFile = commentRemover(f.read())

#         new_file = open(filename, "w+")
#         new_file.write(uncmtFile)

# print('Comment has been deleted.')