import os,sys
# import json

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

path = 'checkPlagiarism'
myresult = [{"username":'student01',"code":'aaaaa'},{"username":'student02',"code":'bbbbb'},{"username":'student03',"code":'aaaaa'},]
def vectorize(Text): return TfidfVectorizer().fit_transform(Text).toarray()
def similarity(doc1, doc2): return cosine_similarity([doc1, doc2])

def checkPlagiarism(myresult):
    plagiarism_results = []
    Data = myresult
    allusername = []
    allcode = []
    print(Data)
    i = 0
    while i < len(Data):
        allusername.append(Data[i][0])
        allcode.append(Data[i][1]) #พยายามแยก code กับชื่อ
        i += 1
    # for x in myresult:
        # allusername.append(myresult[x].username)
        # allcode.append(myresult[x].code) #พยายามแยก code กับชื่อ
    student_files = allusername #username ต้อง add เป็น array ก่อน
    # student_files = [doc for doc in os.listdir(path) if doc.endswith('.c')]
    student_notes = allcode #code ต้อง add เป็น array ก่อน
    # student_notes = [open(f'{path}\\{File}').read() for File in student_files]
    vectors = vectorize(student_notes)
    s_vectors = list(zip(student_files, vectors))

    print(student_files)
    for student_a, text_vector_a in s_vectors:
        new_vectors = s_vectors.copy()
        current_index = new_vectors.index((student_a, text_vector_a))
        del new_vectors[current_index]
        for student_b, text_vector_b in new_vectors:
            sim_score = similarity(text_vector_a, text_vector_b)[0][1]
            student_pair = sorted((student_a, student_b))
            results = {'username1': student_pair[0],'username2': student_pair[1],'score': sim_score}
            plagiarism_results.append(results)
    return plagiarism_results

# def check_Plagiarism():
#     json_string = json.dumps(checkPlagiarism())
#     with open('result.json', 'w') as outfile:
#         outfile.write(json_string)

if __name__ == '__main__':
    globals()[sys.argv[1]]()