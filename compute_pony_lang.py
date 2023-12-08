import argparse
import json
from pathlib import Path
import math

parser = argparse.ArgumentParser()


parser.add_argument("-c","--input_file", required=True)
parser.add_argument("-n", "--num_words", required = True)

#tf = word_count[pony][word]/word_count[pony][All word, iteratively find, sum over values]

#idf =  log (6/number of ponies that have the word as key)

arg = parser.parse_args()

inputfile = Path(__file__).parent/arg.input_file

pony_word_scores = {}
pony_topwords = {}
# valid_names = ["twilight sparkle", "applejack", "rarity", "pinkie pie", "rainbow dash", "fluttershy"]
valid_names = ["twilight sparkle", "applejack", "rarity", "pinkie pie", "rainbow dash", "fluttershy"]

check = {}
final_output = {}
for name in valid_names:
    pony_word_scores[name] = {}
    pony_topwords[name] = {}
    check[name] = {}
    final_output[name] = {}


with open(inputfile) as file:
    #2D dictionary
    word_counts = json.load(file)
    for pony, inner_dict in word_counts.items():
        #we need a dictionary of word and word tf-idf score for each pony
        #compute tfidf for word and add to pony_word_scores
        #pony_word_scores[pony][word] = score
        total_words = sum(int(x) for x in inner_dict.values())
        #print("total words: ", total_words)
        for word in inner_dict:
            tf = word_counts[pony][word]/total_words
            counter = 0
            #word_counts.values() is a dictionary
            # in dictionary checks if in its keys
            for p in word_counts.values():
                #p is a list of words
                if word in p:
                    counter+=1
            #check[pony][word] = counter
            idf = math.log10(6/counter)
            check[pony][word] = idf

            tfidf = tf*idf
            pony_word_scores[pony][word] = tfidf

    #print(pony_word_scores)
    #print(check)
    #there are a lot of 6, especially for and
def get_top_n_key_value_pairs(input_dict, n):
    sorted_items = [key for key, value in sorted(input_dict.items(), key=lambda x: x[1], reverse=True)]
    return sorted_items[:n]





with open (Path(__file__).parent/"tfidf.json", 'w') as file:
    json.dump(pony_word_scores, file, indent = 4)

# now we iterate through pony_word_scores to find the n highest tfidf words for each pony

for pony, pony_tfidf in pony_word_scores.items():
    topn_pairs = get_top_n_key_value_pairs(pony_tfidf, int(arg.num_words))
    final_output[pony] = topn_pairs


with open (Path(__file__).parent/"Distinctive_pony_words.json", 'w') as file:
    json.dump(final_output, file, indent=4)
    
                
                