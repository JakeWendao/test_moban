# coding=utf-8
__author__ = '112'

#jake learn python from liaoxuefeng
#xuliehua_Serialization


# # more about JSON. Use 'class' instead of dict
# # first should make a funtion,which will trans class to dict
# def classtokdict(myclass):
#     return {
#         'name':myclass.name,
#         'age':myclass.age,
#         'score':myclass.score
#     }
#
# import json
# class Student(object):
#      def __init__(self,name,age,score):
#          self.name = name
#          self.age = age
#          self.score = score
# s = Student('jake',20,22)
# print json.dumps(s,default=classtokdict)


#learn JSON
# if we want to transform object between different programming language,must trans to some standard format,for example JSON.
# Moudle inclued in Python "json" provides very perfect transform from Python to JSON.

## third example
## function 'json.dumps'
# import json
# d = dict(name= 'bob',age = 20,score = 99)
# myjsond = json.dumps(d) # Equaly,if use 'dump()',it can put 'd' in a file-like object directly
# myfile = open('111.txt','wb')
# myfile.write(myjsond)
# myfile.close()

#-----------------------

# # fours example:function 'json.loads'
# import json
# json_str = '{"age": 20, "score": 99, "name": "bob"}'
# python_str = json.loads(json_str)
# print(python_str)

#------------------------

# #second example
# myfile = open('1234.txt','rb')
# mypickled = pickle.load(myfile)
# file.close
# print mypickled

#------------------------

# # try import cPickle ,because cPickle is made from c,it is faster.
# try:
# 	import cPickle as pickle
# except ImportError:
# 	import pickle

# # first example
# d = dict(name = 'Bob',age = 22,score = 88)
# f = open('1234.txt','wb')
# pickle.dump(d,f)
# f.close()