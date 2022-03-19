import os,sys
import json

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

path = 'checkPlagiarism'

# student_files = [doc for doc in os.listdir() if doc.endswith('.c')]
# student_notes = [open(File).read() for File in student_files]

def vectorize(Text): return TfidfVectorizer().fit_transform(Text).toarray()
def similarity(doc1, doc2): return cosine_similarity([doc1, doc2])

# vectors = vectorize(student_notes)
# s_vectors = list(zip(student_files, vectors))

def check_plagiarism():
    # plagiarism_results = set()
    plagiarism_results = []
    student_files = [doc for doc in os.listdir(path) if doc.endswith('.c')]
    student_notes = [open(f'{path}\\{File}').read() for File in student_files]
    vectors = vectorize(student_notes)
    s_vectors = list(zip(student_files, vectors))
    # global s_vectors
    for student_a, text_vector_a in s_vectors:
        new_vectors = s_vectors.copy()
        current_index = new_vectors.index((student_a, text_vector_a))
        del new_vectors[current_index]
        for student_b, text_vector_b in new_vectors:
            sim_score = similarity(text_vector_a, text_vector_b)[0][1]
            student_pair = sorted((student_a, student_b))
            results = {'name1': student_pair[0],'name2': student_pair[1],'score': sim_score}
            # score = set({student_pair[0],student_pair[1],sim_score})
            # print(score)
            plagiarism_results.append(results)
            # plagiarism_results.add(score)
    return plagiarism_results

def checkPlagiarism():
    # alldata = set()
    # print(check_plagiarism())
    json_string = json.dumps(check_plagiarism())
    print(json_string)
    with open('result.json', 'w') as outfile:
        outfile.write(json_string)
    # for data in check_plagiarism():
    #     # alldata.add(data)
    #     print(data)
    # # print(alldata)

if __name__ == '__main__':
    globals()[sys.argv[1]]()