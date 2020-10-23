import json
from pprint import pprint
from collections import Counter

def get_json_top(filename, char,rating):
  with open(filename, encoding='utf-8') as f:
    file = json.load(f)
    all_words = ''
    titles = file["rss"]["channel"]["items"]
    for title in titles:
      all_words = all_words + '' + title["description"]
      first = all_words.split()
      total_first = []
      for word in first:
        if len(word) >= char:
          total_first.append(word)
  cap_words = [word.upper() for word in total_first]
  word_counts = Counter(cap_words).most_common(rating)

  return word_counts

pprint(get_json_top("amp.json", 6 , 10))