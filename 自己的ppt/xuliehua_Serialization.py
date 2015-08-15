#jake learn python from liaoxuefeng
#xuliehua_Serialization

# try import cPickle ,because cPickle is made from c,it is faster.
try:
	import cPickle as pickle
except ImportError:
	import pickle

# first example
d = dict(name = 'Bob',age = 22,score = 88)
mypickled = pickle.dumps(d)
print mypickled