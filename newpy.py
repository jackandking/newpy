# -*- coding: utf-8 -*-
# Author: jackandking@gmail.com
# DateTime: 2013-07-07 16:54:15
# HomePage: https://github.com/jackandking/newpy

__version__='0.1'

'''Contributors:
    Yingjie.Liu@thonsomreuters.com
'''

# Configuration Area Start for users of newpy
_author_ = 'Yingjie.Liu@thonsomreuters.com'
# Configuration Area End

from collections import OrderedDict
from datetime import datetime
from optparse import OptionParser
import sys,os

header='''# -*- coding: utf-8 -*-
# Author: %s
# DateTime: %s
# Generator: https://github.com/jackandking/newpy
# Generator Version: %s
'''

sample_blocks = OrderedDict(sorted([

    ('0' , 
['Hello World',
'''
print "Hello World!"
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
dict={'yi':'one','san':'three','er':'two'}
print dict
for i in dict.keys(): print dict[i]
for i in sorted(dict.keys()): print dict[i]
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

    ('9' , 
['Unit Test',
'''
if __name__ == '__main__':
    print "hello world!"
''']),

]))

def write_sample_to_file(id_list=None,
                         filename=None,
                         comment=None):
    if id_list is None: id_list=sample_blocks.iterkeys()
    if filename is None: file=sys.stdout
    else: file=open(filename,'w')
    print >> file, header%(_author_, datetime.now(), __version__)
    for i in id_list:
        print >> file, ""
        if comment: print >> file, "'''"
        print >> file, '#',sample_blocks[i][0]
        print >> file, sample_blocks[i][1]
        if comment: print >> file, "'''"
        print >> file, ""
    if file != sys.stdout: file.close()

def list_sample(option, opt_str, value, parser):
    print "Here are the available samples:"
    for i in sample_blocks.iterkeys():
        print i,"=>",sample_blocks[i][0]
    sys.exit()
        
def main():
    usage = "usage: %prog [options] filename"
    parser = OptionParser(usage)
    parser.add_option("-s", "--samples", type="string", dest="sample_list", metavar="sample-id-list",
                      help='''select samples to include in the new file,
                      e.g. -s 123, check -l for all ids''')
    parser.add_option("-l", "--list_sample_id", action="callback", callback=list_sample)
    parser.add_option("-c", "--comment", dest="comment",
                      action="store_true", help="add samples with prefix '#'" )
    parser.add_option("-q", "--quiet", help="run in silent mode",
                      action="store_false", dest="verbose", default=True)
    parser.add_option("-o", "--overwrite", help="overwrite existing file",
                      action="store_true", dest="overwrite")
    parser.add_option("-t", "--test", help="run in test mode",
                      action="store_true", dest="test")
    (options, args) = parser.parse_args()
    if len(args) != 1:
        parser.error("incorrect number of arguments, try -h")

    filename=args[0]+'.py'
    if options.overwrite is None and os.path.isfile(filename): sys.exit("error: "+filename+" already exist!")
    verbose=options.verbose
    write_sample_to_file(id_list= options.sample_list,
                         filename= None if options.test else filename,
                         comment=options.comment)
    if verbose: print "generate",filename,"successfully."

if __name__ == '__main__':
    main()

