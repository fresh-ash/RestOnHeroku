from fastapi import FastAPI
from Model.engine import *

adjectives = read_f_as_lines(file_names.get("adjectives"))
adverbs = read_f_as_lines(file_names.get("adverbs"))
nouns = read_f_as_lines(file_names.get("nouns"))
verbs = read_f_as_lines(file_names.get("verbs"))




app = FastAPI()

@app.get("/")
async def root():
  return {"message" : "That's root!"}

@app.get("/gameofwords/adj&noun/")
def adj_with_noun(noun: str = None, limit: int = 20):
  result = get_random_pair_of_words(get_words(adjectives, limit),
                                    get_words(nouns, limit))
  if noun:
    result = get_custom_pair(noun, adjectives, limit)
  return result

@app.get("/gameofwords/verb&noun/")
async def verb_with_noun(noun: str = None, verb: str = None, limit: int = 20):
  result = get_random_pair_of_words(get_words(verbs, limit),
                                    get_words(nouns, limit))
  if noun:
    result = get_custom_pair(noun, verbs, limit)
  if verb:
    result = get_custom_pair(verb, nouns, limit)
  return result

@app.get("/gameofwords/noun&noun/{noun}")
async def noun_with_noun(noun: str, limit: int):
  return {noun : limit}

@app.get("/gameofwords/verb&adverb/")
async def noun_with_noun(verb: str = None, limit: int = 20):
  result = get_random_pair_of_words(get_words(verbs, limit),
                                    get_words(adverbs, limit))
  if verb:
    result = get_custom_pair(verb, adverbs, limit)
  return result


