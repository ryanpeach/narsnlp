from nars import OnlineNARS
import nltk
from tools.user import *
from nlp import *

# Create a local connection to NARS
NARS = OnlineNARS()

def user_input(TEST = True):
    """ This asks a user for a sentence and a translation. """
    while True:
        # Get user text (must be a sentence)
        get_text = lambda: raw_input('Say (Type \"Quit.\" to exit): ')
        text_error = lambda x: print("{} is not a sentence.".format(x))
        text = do_check(get_text, is_sentence, text_error)
        if text == "Quit.":
            break
        
        # Get user translation (must be Narsese)
        get_trans = lambda: raw_input('Translation: ')
        text_error = lambda x: print("{} is not valid narsese.".format(x))
        trans = do_check(get_trans, NARS.valid_narsese, text_error)
        
        # Parse the Input
        name, out = sentence_to_narsese(text)
        
        # Sentence is the same as the translation
        sentence_translation = '<{} <-> {}>.'.format(name, trans)
        out.append(sentence_translation)
        
        # Print the final output and confirm correct
        for s in out: print(s)
        if not confirmYN("Is this correct?"): continue
        
        # Input the narsese
        conf = NARS.input_narsese(out)
        if not conf: raise Exception("Input did not work, check syntax in-code.")