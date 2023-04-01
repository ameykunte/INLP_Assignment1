from smoothing import witten_bell_smoothing, kneser_ney_smoothing
import sys

def take_input():
    smoothing_alg = sys.argv[1]
    corpus_path = sys.argv[2]
    sentence = input('input sentence: ')
    return  smoothing_alg, corpus_path, sentence

def calculate_probability(smoothing_alg, corpus_path, sentence):
    if smoothing_alg == 'k':
        model = kneser_ney_smoothing(open(corpus_path).read(),sentence)
        print(model)
    elif smoothing_alg == 'w':
        model = witten_bell_smoothing(open(corpus_path).read(),sentence)
        print(model)
    return 
    
if __name__ == "__main__":
   smoothing_alg, corpus_path, sentence = take_input()
   calculate_probability(smoothing_alg, corpus_path, sentence)
