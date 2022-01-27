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

path = 'checkPlagiarism'
def deleteComment():
    for x in os.listdir(path):
        if x.endswith(".c") or x.endswith(".cpp") or x.endswith(".java"):
            # filename = x
            filename = f'{path}\\{x}'
            with open(filename) as f:
                uncmtFile = commentRemover(f.read())

            new_file = open(filename, "w+")
            new_file.write(uncmtFile)

    print('Comment has been deleted.')

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