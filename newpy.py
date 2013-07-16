# -*- coding: utf-8 -*-
# Author: jackandking@gmail.com
# DateTime: 2013-07-07 16:54:15
# HomePage: https://github.com/jackandking/newpy

__version__='0.4'

'''Contributors:
    Yingjie.Liu@thomsonreuters.com
'''

# Configuration Area Start for users of newpy
_author_ = 'Yingjie.Liu@thomsonreuters.com'
# Configuration Area End

#from collections import OrderedDict
from datetime import datetime
from optparse import OptionParser
import sys,os
import socket

if os.name != "nt":
    import fcntl
    import struct

    def get_interface_ip(ifname):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        return socket.inet_ntoa(fcntl.ioctl(s.fileno(), 0x8915, struct.pack('256s',
                                ifname[:15]))[20:24])

def get_lan_ip():
    ip = socket.gethostbyname(socket.gethostname())
    if ip.startswith("127.") and os.name != "nt":
        interfaces = [
            "eth0",
            "eth1",
            "eth2",
            "wlan0",
            "wlan1",
            "wifi0",
            "ath0",
            "ath1",
            "ppp0",
            ]
        for ifname in interfaces:
            try:
                ip = get_interface_ip(ifname)
                break
            except IOError:
                pass
    return ip

header='''# -*- coding: utf-8 -*-
# Author: %s
# DateTime: %s
# Generator: https://github.com/jackandking/newpy
# Newpy Version: %s
# Newpy ID: %s
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
list=[1,3,2]
print list
dict={'yi':'one','san':'three','er':'two','array':['four','five']}
print dict
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

    ('5' , 
['''URLFetch and Exception Handling''',
'''
import urllib2,sys
try:
    response=urllib2.urlopen("www.baidu.com")
    response=urllib2.urlopen("http://www.baidu.com")
    print response.read(); 
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

    ('7' , 
['String Operation',
'''
s='abc'+'de'
print len(s)
print s[0],s[-1]
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
if __name__ == '__main__':
    print "hello world!"
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

])

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
        print >> file, '#',sample_blocks[i][0]
        print >> file, sample_blocks[i][1]
        if comment: print >> file, "'''"
        print >> file, ""
    if file != sys.stdout: file.close()

def list_sample(option, opt_str, value, parser):
    print "Here are the available samples:"
    for i in sorted(sample_blocks.iterkeys()):
        print i,"=>",sample_blocks[i][0]
    sys.exit()

def submit_record(what,verbose):
    import urllib,urllib2
    params = urllib.urlencode({'which': __version__, 'where': get_lan_ip(), 'who': _author_, 'what': what})
    if verbose: sys.stdout.write("apply for newpy ID...")
    newpyid=0
    try:
        f = urllib2.urlopen("http://newxx.sinaapp.com/newpy", params,timeout=1)
        newpyid=f.read().split(None,1)[0]
        if verbose: print "ok, got",newpyid
    except:
        if verbose: print "ko, use 0"

    return newpyid
        
def main():
    usage = "usage: %prog [options] filename"
    parser = OptionParser(usage)
    parser.add_option("-s", "--samples", type="string", dest="sample_list", metavar="sample-id-list",
                      help='''select samples to include in the new file,
                      e.g. -s 123, check -l for all ids''',default="")
    parser.add_option("-l", "--list_sample_id", action="callback", callback=list_sample)
    parser.add_option("-c", "--comment", dest="comment",
                      action="store_true", help="add samples with prefix '#'" )
    parser.add_option("-q", "--quiet", help="run in silent mode",
                      action="store_false", dest="verbose", default=True)
    parser.add_option("-o", "--overwrite", help="overwrite existing file",
                      action="store_true", dest="overwrite")
    parser.add_option("-t", "--test", help="run in test mode",
                      action="store_true", dest="test")
    parser.add_option("-r", "--record", help="submit record to improve newpy (obsolete, refer to -n)",
                      action="store_true", dest="record")
    parser.add_option("-n", "--norecord", help="don't submit record to improve newpy",
                      action="store_false", dest="record", default=True)
    (options, args) = parser.parse_args()
    if len(args) != 1:
        parser.error("incorrect number of arguments, try -h")

    filename=args[0]+'.py'
    if options.overwrite is None and os.path.isfile(filename): sys.exit("error: "+filename+" already exist!")

    verbose=options.verbose
    sample_list=options.sample_list

    if options.record: newpy_id=submit_record(sample_list,verbose)
    else: newpy_id=0

    write_sample_to_file(newpy_id=newpy_id,
                         id_list= sample_list,
                         filename= None if options.test else filename,
                         comment=options.comment)
    if verbose: print "generate",filename,"successfully."

if __name__ == '__main__':
    main()

