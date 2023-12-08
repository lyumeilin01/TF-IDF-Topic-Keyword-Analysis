

Python3 ./compile_word_counts.py -o pony_counts.json -d clean_dialog.csv


Python3 ./compile_word_counts.py -o topic_counts.json -d topics.csv

Python3 ./compute_pony_lang.py -c topic_counts.json -n 15   
