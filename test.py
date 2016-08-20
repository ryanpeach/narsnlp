import unittest
from word_net import *
import logger as logging
#from knowledgegraph import *
#from read import *

logger = logging.createLogger("test","./",out=True)

class TestWordNet(unittest.TestCase):
    def test_synonym_sets(self):
        print("\ntest_synonym_sets")
        out = synonym_sets('ball')
        logger.debug(out)
        self.assertTrue(out)
    def test_lemmas(self):
        print("\ntest_lemmas")
        out = lemmas('ball.n.01')
        logger.debug(out)
        self.assertTrue(out)
    def test_antonyms(self):
        print("\ntest_antonyms")
        out = antonyms('ball.n.01.ball')
        logger.debug(out)
        self.assertTrue(out)
    def test_hypernyms(self):
        print("\ntest_hypernyms")
        out = hypernyms('ball.n.01')
        logger.debug(out)
        self.assertTrue(out)
    def test_hyponyms(self):
        print("\ntest_hyponyms")
        out = hyponyms('ball.n.01')
        logger.debug(out)
        self.assertTrue(out)
    def test_morphy(self):
        print("\ntest_morphy")
        out = morphy('dogs')
        logger.debug(out)
        self.assertTrue(out)
    def test_definition(self):
        print("\ntest_definition")
        out = definition('ball.n.01')
        logger.debug(out)
        self.assertTrue(out)
    def test_synset_pos(self):
        print("\ntest_synset_pos")
        out = synset_pos('ball.n.01')
        logger.debug(out)
        self.assertTrue(out)
        
if __name__ == '__main__':
    unittest.main()