import sys

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

path = 'checkPlagiarism'
myresult = [{"username":'student01',"code":'aaaaa'},{"username":'student02',"code":'bbbbb'},{"username":'student03',"code":'aaaaa'},]
def vectorize(Text): return TfidfVectorizer().fit_transform(Text).toarray()
def similarity(doc1, doc2): return cosine_similarity([doc1, doc2])

def checkPlagiarism(myresult,problem_id):
    plagiarism_results = set()
    Data = myresult
    allusernameC = []
    allcodeC = []
    allusernameCPP = []
    allcodeCPP = []
    allusernameJava = []
    allcodeJava = []
    allLang = []
    i = 0
    while i < len(Data):
        if Data[i][2] == "c":
            allusernameC.append(Data[i][0]) #พยายามแยก code กับชื่อ C
            allcodeC.append(Data[i][1])
        elif Data[i][2] == "cpp":
            allusernameCPP.append(Data[i][0]) #พยายามแยก code กับชื่อ CPP
            allcodeCPP.append(Data[i][1])
        elif Data[i][2] == "java":
            allusernameJava.append(Data[i][0]) #พยายามแยก code กับชื่อ JAVA
            allcodeJava.append(Data[i][1])
        allLang.append(Data[i][2]) #พยายามแยก ภาษา
        i += 1
    
    allLang = unique(allLang)

    for x in allLang:
        if x == "c":
            student_files = allusernameC
            student_notes = allcodeC
        elif x == "cpp":
            student_files = allusernameCPP
            student_notes = allcodeCPP
        elif x == "java":
            student_files = allusernameJava
            student_notes = allcodeJava
        try:
            vectors = vectorize(student_notes)
            s_vectors = list(zip(student_files, vectors))
        except:
            print("Something wrong in Plagiarism")
        else:
            for student_a, text_vector_a in s_vectors:
                new_vectors = s_vectors.copy()
                current_index = new_vectors.index((student_a, text_vector_a))
                del new_vectors[current_index]
                for student_b, text_vector_b in new_vectors:
                    sim_score = similarity(text_vector_a, text_vector_b)[0][1]
                    student_pair = sorted((student_a, student_b))
                    results = (student_pair[0],student_pair[1],float('{:.2f}'.format(sim_score*100)),int(problem_id))
                    plagiarism_results.add(results)
    plagiarism_results = list(plagiarism_results)
    return plagiarism_results

def unique(list1):
    unique_list = []
    for x in list1:
        if x not in unique_list:
            unique_list.append(x)
    return unique_list

if __name__ == '__main__':
    globals()[sys.argv[1]]()