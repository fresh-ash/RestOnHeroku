import random
import os

path = os.getcwd() + "/Files/"

file_names = {'adverbs': path + "adverbs.txt", 'adjectives': path + "adjectives.txt",
              'nouns': path + "nouns.txt", 'verbs': path + "verbs.txt"}

conjunctions_list = [ "though", "although", "even though", "while",
                     "if", "only if", "unless", "until",
]

def read_f_as_lines(name):
  file = open(name)
  lines = []
  for line in file:
    lines.append(line[:-1])
  file.close()
  return lines


def get_words(list, count):
  words = random.choices(list, k = count)
  return words

def get_random_pair_of_words(x, y):
  result = {}
  for word in x:
    result[word] = y.pop()
  return result

def get_custom_pair(word, list, limit):
  rand_list = get_words(list, limit)
  result = {}
  for i in rand_list:
    result[i] = word
  return result