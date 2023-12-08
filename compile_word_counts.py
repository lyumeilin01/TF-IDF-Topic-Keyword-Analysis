
import argparse
from pathlib import Path
import csv
import json



parser = argparse.ArgumentParser()

parser.add_argument("-o", "--output_file", required = True)
parser.add_argument("-d", "--data", required = True)


arg = parser.parse_args()

valid_names = ["dating", "concert", "celeb", "brazil incident", "career", "politics", "lifestyle", "fan"]

word_counts = {}

for name in valid_names:
   word_counts[name] = {}


with open(arg.data) as file:
    csv_reader = csv.reader(file, delimiter = ',')
    #skip headers
    next(csv_reader, None)

    for row in csv_reader:
      #topics/pony names
      row[0] = row[0].lower()

      if row[0] not in valid_names:
         continue
      # content/title 
      row[1] = row[1].lower()

      for word in row[1].split():
        word = word.strip(",.?!-\"\'1234567890")
        # cleanup word
        
        if word in "taylor swift":
           continue

         #check if word is in word_counts[row[2]]
         #if not, add
        if word not in word_counts[row[0]]:
            word_counts[row[0]][word] = 1
        else:
           word_counts[row[0]][word]+=1
         #if is, value++
         
      
    print(word_counts)

    with open (arg.output_file,'w') as file:
       json.dump(word_counts, file, indent= 4)
         


         
         
         

      #print(row[2].lower())


    

    
    


