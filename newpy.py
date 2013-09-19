# -*- coding: utf-8 -*-
# Author: jackandking@gmail.com
# DateTime: 2013-07-07 16:54:15
# HomePage: https://github.com/jackandking/newpy

__version__='0.9'

'''Contributors:
    Yingjie.Liu@thomsonreuters.com
'''

# Configuration Area Start for users of newpy
_author_ = 'Yingjie.Liu@thomsonreuters.com'
# Configuration Area End

_newpy_server_='newxx.sinaapp.com'
#_newpy_server_='localhost:8080'

from datetime import datetime
from optparse import OptionParser
import sys,os
import urllib,urllib2
import re
import socket
socket.setdefaulttimeout(3)

header='''# -*- coding: utf-8 -*-
# Author: %s
# DateTime: %s
# Generator: https://github.com/jackandking/newpy
# Newpy Version: %s
# Newpy ID: %s
# Description: I'm a lazy person, so you have to figure out the function of this script by yourself.
'''

sample_blocks = dict([

    ('0' , 
['Hello World',
'''
world=raw_input("Hello:")
World='python is case sensitive'
print "Hello",world + "!"
''']),

    ('1' , 
['''If-Else inside While''',
'''
from time import time
while not None:
    if int(time()) % 2:
            print "True"
            continue
    else:
            break
''']),

    ('2' , 
['''List and Dict''',
'''
list=[1,3,2]; print list
list.append(4); print list
list.pop(); print list
list_of_list=[1,2,[3,4]]; print list_of_list
list_of_dict=[{"name":"jack", "sex":"M"},{"name":"king","sex":"M"}]; print list_of_dict
dict={'yi':'one','san':'three','er':'two','array':['four','five']}; print dict
for i in dict.keys(): print dict[i]
for i in sorted(dict.keys()): print dict[i]
print len(dict.keys())
''']),

    ('3' , 
['''File Read and Write''',
'''
file=open("test.txt","w")
file.write("line1")
file.close
file=open("test.txt","r")
line=file.readline()
while line:
    print line
    line=file.readline()
file.close
''']),

    ('4' , 
['''Regular Expression''',
'''
import re
line='abc123abc'
m=re.search('(\d+)',line)
if m: print m.group(1)
''']),

    ('7' , 
['''URLFetch and Exception Handling''',
'''
import urllib2,sys
from urllib2 import URLError, HTTPError
try:
    response=urllib2.urlopen("www.google.com")
    response=urllib2.urlopen("http://www.google.com")
    print response.read(); 
    raise Exception("I know python!")
except HTTPError, e:
    print 'The server could not fulfill the request.'
    print 'Error code: ', e.code
except URLError, e:
    print 'We failed to reach a server.'
    print 'Reason: ', e.reason
except:
    print "Unexpected error:", sys.exc_info()[0]
''']),

    ('6' , 
['System Call',
'''
import subprocess
#only care about return value
print subprocess.call("dir abc.txt", shell=True)
#Care about output
print subprocess.check_output("hostname", shell=True)
''']),

    ('5' , 
['String Operation',
'''
s='abc'+'de'+str(1)
print len(s)
print s[0],s[-1]
print s[:3] #first 3
print s[-3:] #last 3
''']),

    ('8' , 
['eval and exec',
'''
a=eval('1+1')
exec('b=1+1')
print a,b
''']),

    ('9' , 
['Unit Test',
'''
import unittest

# Here's our "unit".
def IsOdd(n):
    return n % 2 == 1

# Here's our "unit tests".
class IsOddTests(unittest.TestCase):

    def testOne(self):
        self.failUnless(IsOdd(1))

    def testTwo(self):
        self.failIf(IsOdd(2))

def main():
    unittest.main()

if __name__ == '__main__':
    main()
''']),

    ('a' , 
['CSV read and write',
r'''
# http://www.pythonforbeginners.com/systems-programming/using-the-csv-module-in-python/

#read
import csv
 
file=open("test.csv","w")
file.write("a,b,c\n")
file.write("1,2,3\n")
file.write("11,12,13")
file.close()

ifile  = open('test.csv', "rb")
reader = csv.reader(ifile)
 
rownum = 0
for row in reader:
    # Save header row.
    if rownum == 0:
        header = row
    else:
        colnum = 0
        for col in row:
            print '%-8s: %s' % (header[colnum], col)
            colnum += 1
             
    rownum += 1
 
ifile.close()

# write
ifile  = open('test.csv', "rb")
reader = csv.reader(ifile)
ofile  = open('ttest.csv', "wb")
writer = csv.writer(ofile, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
 
for row in reader:
    writer.writerow(row)
 
ifile.close()
ofile.close()
''']),

    ('b' , 
['Bottle: Python Web Framework',
'''
from bottle import route, run, template

@route('/hello/<name>')
def index(name='World'):
    return template('<b>Hello {{name}}</b>!', name=name)

run(host='localhost', port=8080)
''']),

    ('c' , 
['Class and SubClass',
'''
class Parent:        # define parent class
   data = 100
   def __init__(self): print "Calling parent constructor"
   def __del__(self): print "Parent D'tor: ",self.data,Parent.data

class Child(Parent): # define child class
   def __init__(self): self.data=2; print "Calling child constructor"

print Child()
''']),

    ('d' , 
['Dict Deep Copy',
'''
import copy
my_dict = {'a': [1, 2, 3], 'b': [4, 5, 6]}
my_copy = copy.deepcopy(my_dict)
my_dict['a'][2] = 7
print my_copy['a'][2]
''']),

    ('e' , 
['Inspect, print function parameter',
'http://newxx.sinaapp.com/newpy/129']),

    ('f' , 
['Function and DataTime',
'''
from datetime import date
def isleap(year):
    """Return True for leap years, False for non-leap years."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
thisyear=date.today().year
print isleap.__doc__
print "this year is leap year:",isleap(thisyear)
''']),

    ('i' , 
['Runtime Import',
'''
libname='time'
globals()[libname] = __import__(libname)
mod=globals()[libname]
if hasattr(mod,'sleep'):
    mod.sleep(1)
''']),

    ('l' , 
['Logging, logger',
'''
#refer to http://docs.python.org/2/howto/logging.html

import logging

# create logger
logger = logging.getLogger('simple_example')
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warn('warn message')
logger.error('error message')
logger.critical('critical message')
''']),

    ('m' , 
['MongoDB - NoSQL',
'''
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.test_database
collection = db.test_collection
post = {"author": "Mike","text": "My first blog post!"}
posts = db.posts
post_id = posts.insert(post)
posts.find_one({"author": "Mike"})
for post in posts.find():
    post
''']),

    ('D' , 
['PDB: python debug',
'''
# python -m pdb myscript.py
import pdb
i=1
pdb.set_trace()
print i
''']),

])

def get_file_content(a_url):
    response=urllib2.urlopen(a_url)
    return response.read()[11:][:-13] 

def write_sample_to_file(newpy_id=0,
                         id_list=None,
                         filename=None,
                         comment=None):
    if id_list is None: id_list=sample_blocks.iterkeys()
    if filename is None: file=sys.stdout
    else: file=open(filename,'w')
    print >> file, header%(_author_, datetime.now(), __version__, newpy_id)
    for i in id_list:
        if i not in sample_blocks.iterkeys(): print "invalid sample ID, ignore",i; continue
        print >> file, ""
        if comment: print >> file, "'''"
        print >> file, '##',sample_blocks[i][0]
        if sample_blocks[i][1][:5] == "http:":
          print >> file, ""
          print >> file, get_file_content(sample_blocks[i][1])
        else:
          print >> file, sample_blocks[i][1]
        if comment: print >> file, "'''"
        print >> file, ""
    if file != sys.stdout: file.close()

def list_sample(option, opt_str, value, parser):
    print "Here are the available samples:"
    print "---------------------------------------"
    for i in sorted(sample_blocks.iterkeys()):
        print i,"=>",sample_blocks[i][0]
    print "---------------------------------------"
    sys.exit()

def submit_record(what,verbose):
    params = urllib.urlencode({'which': __version__, 'who': _author_, 'what': what})
    if verbose: sys.stdout.write("apply for newpy ID...")
    newpyid=0
    try:
        f = urllib2.urlopen("http://"+_newpy_server_+"/newpy", params)
        newpyid=f.read()
        if verbose: print "ok, got",newpyid
    #except urllib2.HTTPError, e:
        #print e.reason
    except:
        #print "Unexpected error:", sys.exc_info()[0]
        if verbose: print "ko, use 0"

    return newpyid
 
def upload_file(option, opt_str, value, parser):
    filename=value
    if not os.path.isfile(filename): sys.exit("error: "+filename+" does not exist!")
    file=open(filename,"r")
    line=file.readline()
    newpyid=0
    while line:
        line=file.readline()
        m=re.search('# Newpy ID: (\d+)',line)
        if m: 
            newpyid=int(m.group(1))
            break
    file.close
    if newpyid == 0: sys.exit("error: no valid newpy ID found for "+filename)
    sys.stdout.write("uploading "+filename+"(newpyid="+str(newpyid)+")...")
    params = urllib.urlencode({'filename': filename, 'content': open(filename,'rb').read()})
    try:
        f = urllib2.urlopen("http://"+_newpy_server_+"/newpy/upload", params)
        print f.read()
        print "weblink: http://"+_newpy_server_+"/newpy/"+str(newpyid)
    except:
        print "Unexpected error:", sys.exc_info()[0]
    sys.exit()

def main():
    usage = "usage: %prog [options] filename"
    parser = OptionParser(usage)
    parser.add_option("-s", "--samples", type="string", dest="sample_list", metavar="sample-id-list",
                      help='''select samples to include in the new file,
                      e.g. -s 123, check -l for all ids''',default="")
    parser.add_option("-l", "--list", help="list all the available samples.", action="callback", callback=list_sample)
    parser.add_option("-u", "--upload", type="string", dest="filename",
                      help='''upload file to newpy server as sample to others. the file must have a valid newpy ID.''',
                      action="callback", callback=upload_file)
    parser.add_option("-c", "--comment", dest="comment",
                      action="store_true", help="add samples with prefix '#'" )
    parser.add_option("-q", "--quiet", help="run in silent mode",
                      action="store_false", dest="verbose", default=True)
    parser.add_option("-o", "--overwrite", help="overwrite existing file",
                      action="store_true", dest="overwrite")
    parser.add_option("-t", "--test", help="run in test mode, no file generation, only print result to screen.",
                      action="store_true", dest="test")
    parser.add_option("-r", "--record", help="submit record to improve newpy (obsolete, refer to -n)",
                      action="store_true", dest="record")
    parser.add_option("-n", "--norecord", help="don't submit record to improve newpy",
                      action="store_false", dest="record", default=True)
    (options, args) = parser.parse_args()
    verbose=options.verbose
    sample_list=options.sample_list

    if options.test is None:
        if len(args) != 1:
            parser.error("incorrect number of arguments, try -h")

        filename=args[0]+'.py'
        if options.overwrite is None and os.path.isfile(filename): sys.exit("error: "+filename+" already exist!")

        if options.record: newpy_id=submit_record(sample_list,verbose)
        else: newpy_id=0
    else:
        newpy_id=0
        filename=None

    write_sample_to_file(newpy_id=newpy_id,
                         id_list= sample_list,
                         filename=filename,
                         comment=options.comment)
    if verbose and filename: print "generate",filename,"successfully."

if __name__ == '__main__':
    main()

