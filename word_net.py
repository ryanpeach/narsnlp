from nltk.corpus import wordnet as wn

properties = {}

properties['synonym_sets'] = {'Requires': '<{} --> TOKEN>',
                              'Output':   '<{} --> SYNSET>',
                              'Returns':  '<({},{}) --> SYNONYM>'}
def synonym_sets(w):
    S = [x.name() for x in wn.synsets(w)]
    out = [nal_output('synonym_sets',w,s) for s in S]
    return "(&/, {}) :|:".format(", ".join(out))

properties['lemmas'] = {'Requires': '<{} --> SYNSET>',
                        'Output':   '<{} --> LEMMA>',
                        'Returns':  '<({},{}) --> LEMMAS_OF>'}
def lemmas(s):
    S = wn.synset(s).name()
    out = [nal_output('lemmas',s,l) for l in S.lemmas()]
    return "(&/, {}) :|:".format(", ".join(out))
    
properties['antonyms'] = {'Requires': '<{} --> LEMMA>',
                          'Output':   '<{} --> LEMMA>',
                          'Returns':  '<({},{}) --> ANTONYMS>'}
def antonyms(l):
    L = wn.lemma(l)
    out = [nal_output('antonyms',l,a.name()) for a in L.antonyms()]
    return "(&/, {}) :|:".format(", ".join(out))


properties['hypernyms'] = {'Requires': '<{} --> SYNSET>',
                           'Output':   '<{} --> SYNSET>',
                           'Returns':  '<({},{}) --> HYPERNYM_OF>'}
def hypernyms(s):
    S = wn.synset(s)
    out = [nal_output('hypernyms',s,hs.name()) for hs in S.hypernyms()]
    return "(&/, {}) :|:".format(", ".join(out))


properties['hyponyms'] = {'Requires': '<{} --> SYNSET>',
                          'Output':   '<{} --> SYNSET>',
                          'Returns':  '<({},{}) --> HYPONYM_OF>'}
def hyponyms(s):
    S = wn.synset(s)
    out = [nal_output('hyponyms',s,hs.name()) for hs in S.hyponyms()]
    return "(&/, {}) :|:".format(", ".join(out))

properties['morphy'] = {'Requires': '<{} --> TOKEN>',
                        'Output':   '<{} --> TOKEN>',
                        'Returns':  '<({},{}) --> MORPHY_OF>'}
def morphy(w):
    return nal_output('morphy',w,wn.morphy(w)) + " :|:"

properties['definition'] = {'Requires': '<{} --> SYNSET>',
                            'Output':   '<{} --> PARAGRAPH>',
                            'Returns':  '<({},{}) --> DEFINITION_OF>'}
def definition(s):
    S = wn.synset(s)
    return nal_output('definition',s,S.definition()) + " :|:"

properties['name'] = {'Requires': '<{} --> LEMMA>',
                      'Output':   '<{} --> LEMMA>',
                      'Returns':  '<({},{}) --> NAME_OF>'}
def lemma_name(l):
    L = wn.lemma(l)
    return nal_output('lemma_name',l,L.name()) + " :|:"
    
properties['synset_pos'] = {'Requires': '<{} --> SYNSET>',
                            'Output':   '<{} --> POS>',
                            'Returns':  '<({},{}) --> POS_OF>'}
def synset_pos(s):
    S = wn.synset(s)
    return nal_output('synset_pos',s,S.pos()) + " :|:"

properties['lemma_pos'] = {'Requires': '<{} --> LEMMA>',
                           'Output':   '<{} --> POS>',
                           'Returns':  '<({},{}) --> POS_OF>'}

def nal_output(name,i1,o1):
    P = properties[name]
    req = P['Requires'].format(i1), P['Output'].format(o1)
    ret = P['Returns'].format(i1,o1)
    return '(&&,{},{},{})'.format(req[0],req[1],ret)
    
#def v_frames(s):
#    pass
#def morphonyms(s):
#    pass
#def similarity(x,y):
#    """Requires: (&&, <(*,$1,SYNSET) --> IS_A>, <(*,$2,SYNSET) --> IS_A>)
#       Output: None
#       Additional Properties:"""
#    w1 = wn.synset(x)
#    w2 = wn.synset(y)
#    f = w1.wup_similarity(w2)
#    return ["<{} <-> {}>. {};.9".format(x,y,f)]