
# coding: utf-8

# # Assignment 0
# 
# This notebook will help verify that you're all set up with the Python packages we'll be using this semester.
# 
# **Your task:** just run the cells below, and verify that the output is as expected. If anything looks wrong, weird, or crashes, update your Python installation or contact the course staff. We don't want library issues to get in the way of the real coursework!

# In[1]:


# Version checks
import importlib
def version_greater_equal(v1, v2):
    for x, y in zip(v1.split('.'), v2.split('.')):
        if int(x) != int(y):
            return int(x) > int(y)
    return True
    
assert version_greater_equal('1.2.3', '0.1.1')
assert version_greater_equal('1.2.3', '0.5.1')
assert version_greater_equal('1.2.3', '1.2.3')
assert version_greater_equal('0.22.0', '0.20.3')
assert not version_greater_equal('1.1.1', '1.2.3')
assert not version_greater_equal('0.5.1', '1.2.3')
assert not version_greater_equal('0.20.3', '0.22.0')

def version_check(libname, min_version):
    m = importlib.import_module(libname)
    print ("%s version %s is " % (libname, m.__version__))
    print ("OK"
           if version_greater_equal(m.__version__, min_version) 
           else "out-of-date. Please upgrade!")
    
version_check("numpy", "1.13.3")
version_check("matplotlib", "2.1")
version_check("pandas", "0.22")
version_check("nltk", "3.2.5")
version_check("tensorflow", "1.8")


# ## TensorFlow
# 
# We'll be using [TensorFlow](tensorflow.org) to build deep learning models this semester. TensorFlow is a whole programming system in itself, based around the idea of a computation graph and deferred execution. We'll be talking a lot more about it in Assignment 1, but for now you should just test that it loads on your system.
# 
# Run the cell below; you should see:
# ```
# Hello, TensorFlow!
# 42
# ```

# In[2]:


import tensorflow as tf

hello = tf.constant("Hello, TensorFlow!")
sess = tf.Session()
print(sess.run(hello))

a = tf.constant(10)
b = tf.constant(32)
print(sess.run(a+b))


# ## NLTK
# 
# [NLTK](http://www.nltk.org/) is a large compilation of Python NLP packages. It includes implementations of a number of classic NLP models, as well as utilities for working with linguistic data structures, preprocessing text, and managing corpora.
# 
# NLTK is included with Anaconda, but the corpora need to be downloaded separately. Be warned that this will take up around 3.2 GB of disk space if you download everything! If this is too much, you can download individual corpora as you need them through the same interface.
# 
# Type the following into a Python shell on the command line. It'll open a pop-up UI with the downloader:
# 
# ```
# import nltk
# nltk.download()
# ```
# 
# Alternatively, you can download individual corpora by name. The cell below will download the famous [Brown corpus](http://www.essex.ac.uk/linguistics/external/clmt/w3c/corpus_ling/content/corpora/list/private/brown/brown.html):

# In[3]:


import nltk
assert(nltk.download("brown"))  # should return True if successful, or already installed


# Now we can look at a few sentences. Expect to see:
# ```
# The Fulton County Grand Jury said Friday an investigation of Atlanta's recent primary election produced `` no evidence '' that any irregularities took place .
# 
# The jury further said in term-end presentments that the City Executive Committee , which had over-all charge of the election , `` deserves the praise and thanks of the City of Atlanta '' for the manner in which the election was conducted .
# ```

# In[4]:


from nltk.corpus import brown
# Look at the first two sentences
for s in brown.sents()[:2]:
    print(" ".join(s))
    print("")


# NLTK also includes a sample of the [Penn treebank](https://www.cis.upenn.edu/~treebank/), which we'll be using later in the course for parsing and part-of-speech tagging. Here's a sample of sentences, and an example tree. Expect to see:
# ```
# The top money funds are currently yielding well over 9 % .
# 
# (S
#   (NP-SBJ (DT The) (JJ top) (NN money) (NNS funds))
#   (VP
#     (VBP are)
#     (ADVP-TMP (RB currently))
#     (VP (VBG yielding) (NP (QP (RB well) (IN over) (CD 9)) (NN %))))
#   (. .))
# ```

# In[5]:


assert(nltk.download("treebank"))  # should return True if successful, or already installed
print("")
from nltk.corpus import treebank
# Look at the parse of a sentence.
# Don't worry about what this means yet!
idx = 45
print(" ".join(treebank.sents()[idx]))
print("")
print(treebank.parsed_sents()[idx])


# We can also look at the [Europarl corpus](http://www.statmt.org/europarl/), which consists of *parallel* text - a sentence and its translations to multiple languages. You should see:
# ```
# ENGLISH: Resumption of the session I declare resumed the session of the European Parliament adjourned on Friday 17 December 1999 , and I would like once again to wish you a happy new year in the hope that you enjoyed a pleasant festive period .
# ```
# and its translation into French and Spanish.

# In[6]:


assert(nltk.download("europarl_raw"))  # should return True if successful, or already installed
print("")
from nltk.corpus import europarl_raw

idx = 0

print("ENGLISH: " + " ".join(europarl_raw.english.sents()[idx]))
print("")
print("FRENCH: " + " ".join(europarl_raw.french.sents()[idx]))
print("")
print("SPANISH: " + " ".join(europarl_raw.spanish.sents()[idx]))

