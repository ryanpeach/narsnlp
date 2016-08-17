import nltk
from nltk.parse.stanford import StanfordDependencyParser
path_to_jar = '../stanford-parser-full-2015-12-09/stanford-parser.jar'
path_to_models_jar = '../stanford-parser-full-2015-12-09/stanford-parser-3.6.0-models.jar'
    
def dependency(x = 'I shot an elephant in my sleep.'):
    """http://stackoverflow.com/questions/7443330/how-do-i-do-dependency-parsing-in-nltk"""
    dependency_parser = StanfordDependencyParser(path_to_jar=path_to_jar, path_to_models_jar=path_to_models_jar)
    result = dependency_parser.raw_parse(x)
    dep = result.next()
    return list(dep.triples())

def tokenize(x):
    return nltk.word_tokenize(x)
    
def tokenize_sentences(x):
    return nltk.sent_tokenize(x)
    
def tag_pos(x):
    return nltk.pos_tag(x)
    
def quote(x):
    return "\"{}\"".format(str(x))

def is_token(x):
    return str(tokenize(x)[0]) == x

def is_sentence(x):
    return str(tokenize_sentences(x)[0]) == x
    
def is_url(x):
    pass

if __name__=="__main__":
    x = input("Input sentence: ")
    print(tokenize(x))
    print(tag_pos(tokenize(x)))
    print(dependency(x))