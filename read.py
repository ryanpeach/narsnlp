import nlp
from nars import *
from logger import *

from nlp import quote

# Create log for all user input
log = createLogger("NLPInput", "./nlpinput.txt")

def process_nlp_input(raw):
    out = []
    sentences = nlp.tokenize_sentences(raw)
    for s in sentences:
        out += process_nlp_sentence(s)
    return out
        
def process_nlp_sentence(s_in):
    out = []
    # Get tokenization
    tokens = nlp.tokenize(s_in)
    dependencies = dependency(s_in)
    
    # All tokens are TOKEN, tokens relate concepts
    for t in tokens:
        out.append("<\"{}\" --> TOKEN>.".format(t))
        out.append("<(*,\"{0}\",{0}) --> RELATES>.".format(t))
        
    # The tokens together are a sentence
    sent = "(*,\"{}\")".format("\", \"".join(tokens))
    out.append("<{} --> SENTENCE>.".format(sent))
    out.append("<{} --> (*,USER,SAYS)>. :|:".format(sent))
    out.append("<{} <-> {}>.".format(sent, quote(raw)))
    
    # Process dependencies
    for D in dependencies:                                  
        (t1, pos1), d, (t2, pos2) = D                       # Get all terms seperately
        i1 = "<(*,{},{}) --> INSIDE>".format(t1,sent)       # get term for t1 in sentence
        i2 = "<(*,{},{}) --> INSIDE>".format(t2,sent)       # get term for t2 in sentence
        p1 = "<{} --] {}>.".format(i1,pos1)                 # i1 has part of speech pos1
        p2 = "<{} --] {}>.".format(i2,pos2)                 # i2 has part of speech pos2
        d0 = "<(&&,{},{}) --> {}>.".format(i1,i2,d)         # p1 and p2 have dependency d
        out += [p1,p2,d0]                                   # output p1, p2, and d0
    
    return out

if __name__=="__main__":
    # Create NARS object
    NARS = Nars("../opennars2/", include=['./rules/ngram.nal'])
    NARS.process_nlp_input = process_nlp_input

    # Create input loop
    while True:
        try:
            # Get input
            raw = input("INPUT: ")
            if raw == "Quit":
                break
            log.info(raw)
            NARS.process(process_nlp_input(raw))
            
            # Get translation
            # The sentence is the same as it's translation
            trans = input("Translation: ")
            if trans != "":
                NARS.process("<{} <-> {}>.".format(sent, trans))
                log.info(trans)
                
        # Catch exceptions so that NARS can quit
        except Exception e:
            print(e)
            break

    NARS.quit()