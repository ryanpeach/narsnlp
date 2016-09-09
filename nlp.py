from tools.parsing import *
import narsese

TNAME       = '{{t_\"{}\"}}'
SNAME       = '{{s_\"{}\"}}'
CNAME       = 'c_\"{}\"'
TOKEN       = 'nlp_Token'
SAYS        = 'nlp_Says'
SENTENCE    = 'nlp_Sentence'
RELATES     = 'nlp_Relates'
CONCEPT     = 'nlp_Concept'
AUTHOR      = 'nlp_Author'
IN_SENTENCE = 'nlp_In_Sentence'
UNKNOWN     = '{nlp_UnknownAuthority}'

def sentence_to_narsese(sentence, authority = UNKNOWN):
    """ Returns a list of all rules applying to this sentence. """
    # Initialize output
    out = []
    
    # Tokenize
    tokens = tokenize(sentence)
    
    # Tokens have names 
    token_names = [TNAME.format(t) for t in tokens]
    
    # Tokens relate concepts
    concept_names = [CNAME.format(t) for t in tokens]
    relationships = ['<({},{}) --> {}>.'.format(t,c,RELATES) for t, c in zip(token_names, concept_names)]
    out += relationships
    
    # Tokens are tokens
    tokens_are_tokens = ['<{} --> {}>.'.format(t, TOKEN) for t in token_names]
    out += tokens_are_tokens
    
    # Concepts are concepts
    concepts_are_concepts = ['<{} --> {}>.'.format(c, CONCEPT) for c in concept_names]
    out += concepts_are_concepts

    # Authority is an authority
    author_is_authority = '<{} --> {}>.'.format(authority, AUTHOR)
    out += author_is_authority
    
    # Tokens are said in time by authority
    if authority == None:
        token_said = ['<({},{}) --> {}>'.format('#1', t, SAYS) for t in token_names]
        token_said.append('<#1 --> {}>'.format('#1', AUTHOR))
        token_said = [narsese.compound(token_said, '&&') + '.']
    else:
        token_said = ['<({},{}) --> {}>'.format(authority, t, SAYS) for t in token_names]
    token_said_now = ['{}. :|:'.format(t) for t in token_said_by]
    out += token_said_now
    
    # Sentences have names
    sentence_name = SNAME.format(sentence)
    
    # Sentences are Sentences
    sent_are_sent = '<{} --> {}>.'.format(sentence_name, SENTENCE)
    out.append(sent_are_sent)
    
    # Sentence names are equivalent to sequences of tokens said
    said_sequence       = narsese.compound(token_said, '&/')
    seq_equals_sentence = '<{} <-> {}>.'.format(said_sequence, sentence_name)
    out.append(seq_equals_sentence)
    
    # Tokens are in this sentence
    tokens_in_sentence = ['<({},{}) --> {}>.'.format(t,sentence_name,IN_SENTENCE) for t in token_names]
    out += tokens_in_sentence

    return sentence_name, out