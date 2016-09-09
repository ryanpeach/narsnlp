from nltk import *
from itertools import combinations

# Primitive classes
class Term():
    def __init__(self, x):
        self.X = str(x)
    def nal(self):
        return self.X
    def nlp(self):
        return self.X
    def __str__(self):
        return self.nal()
        
class Compound(Term):
    def __init__(self, copula, attributes):
        if isinstance(copula, str):
            copula = Term(copula)
        self.C, self.A = copula, attributes
    def nal(self):
        return "({},{})".format(self.C.nal(),", ".join([a.nal() for a in self.A]))
    def nlp(self):
        return "({},{})".format(self.C.nal(),", ".join([a.nal() for a in self.A]))

class Statement(Term):
    COPULAS = {'--]': 'property of', '-->': 'inherits', '<|>': 'is now', '<=>': 'equivalent to',
        '{-]': 'instance of property', '</>': 'will be', '=\\\\>': 'retrospective to', '==>':
        'implies', '=/>': 'predicts', '<->': 'same as', '{--': 'instance of', '=|>': 'concurrent with'}
    def __init__(self, x, copula, y):
        assert(isinstance(x, Term))
        assert(isinstance(y, Term))
        assert(copula in self.COPULAS)
        self.X, self.Y, self.C = x, y, copula
    def nal(self):
        return "<{} {} {}>".format(self.X.nal(),self.C,self.Y.nal())
    def nlp(self):
        return "\""+self.X.nlp()+" "+self.COPULAS[self.C]+" "+self.Y.nlp()+"\""
    def __iter__(self):
        return iter((self.X, self.C, self.Y))
    def __str__(self):
        return self.nal()
        
class NLPStatement(Statement):
    def __init__(self, x, rel, y):
        assert(isinstance(x, Term))
        assert(isinstance(y, Term))
        assert(isinstance(rel, Term))
        self.X, self.Y, self.REL = x, y, rel
    def nal(self):
        return "<(*,{},{})-->{}>".format(self.X.nal(), self.Y.nal(), str(self.REL))
    def nlp(self):
        return "\"{} {} {}\"".format(self.X.nlp(), str(self.REL), self.Y.nlp())
        
class Sentence(Statement):
    ends = (".","?","!","@")
    def __init__(self, state, end, tense, truth):
        assert(end in ends)
        self.S, self.E, self.F, self.C = state, end, tense, truth

def statement(x, rel, y):
    """ Chooses between NLPStatement and Statement"""
    if rel in Statement.COPULAS:
        return Statement(x, rel, y)
    else:
        return NLPStatement(x, str(rel), y)
        
# Shorthand
# Returns Sentences
def rename(properties, desc):
    """ Returns some x of description desc relating to the properties provided.
        EX: properties = [('is_a', 'man'), ('is_a', 'god')]
            desc = ('is_a', 'demigod')
            <(&&, <$1 is_a man>, <$1 is_a god>) ==> <$1 is_a demigod>>"""
    attributes = []
    for rel, y in properties:
        attributes.append(Statement("$1", rel, y))
    qualities = Compound("&&", attributes)
    out = (given("$1",qualities), "<->", sentence("$1", *desc))
    return sentence(*out)

# Returns Lists   
def all_inherit_type(X, rel, y):
    """ Given a list of input terms, and an output term, relates each input to output. """
    out = []
    for x in X:
        out.append(statement(x,rel,y))
    return out
    
def f_requires(f_op, in_number, req):
    """<(*,<(*,$f_op, $input) --> REQUIRES>, $req) --> WHERE>"""
    return '<(*,<(*,{},$i{}) --> REQUIRES>, {}) --> WHERE>'.format(f_op, in_number, req)