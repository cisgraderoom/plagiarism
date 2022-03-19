import os,sys
import json

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

path = 'checkPlagiarism'

def vectorize(Text): return TfidfVectorizer().fit_transform(Text).toarray()
def similarity(doc1, doc2): return cosine_similarity([doc1, doc2])

def check_plagiarism():
    plagiarism_results = []
    student_files = [doc for doc in os.listdir(path) if doc.endswith('.c')] #username
    student_notes = [open(f'{path}\\{File}').read() for File in student_files] #code
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

def checkPlagiarism():
    json_string = json.dumps(check_plagiarism())
    with open('result.json', 'w') as outfile:
        outfile.write(json_string)

if __name__ == '__main__':
    globals()[sys.argv[1]]()