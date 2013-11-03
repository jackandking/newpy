newpy.py
=====
Quick Python programming for experienced lazy developers on small utilities. It will enable your switch from other script languages to Python in short time without googling. If you believe that 20% of all Python grammar can support 80% of use as I do, then newpy.py is your good choice. Personally I will use it to recall key syntax when I have stopped using Python for a while. newpy.py will save 10 minutes each time we do language context switch.

Run Environment
---------------
Tested in Python 2.7 under Windows and Linux, Python 2.6 under Linux.

Python Installation
-----------------
Python is so famous that you can easily figure out how to download&install it via google. Otherwise just visit below link to save 10 seconds.
    http://www.python.org/getit/

Module Management
-----------------
Python is powerful only because there are lots of useful modules. They are free for you, so you must learn to download&install modules.

For our sake, Christoph Gohlke prepares Windows installers (.msi) for popular Python packages. He builds installers for Python 2.x and 3.x, 32 bit and 64 bit. You need to

Install setuptools: 
    curl https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py | python
For manual install inside setuptools:
    setup.py install
Install pip:
    easy_install pip
Install Module with pip: 
    pip install <module>

Install from Binary: http://www.lfd.uci.edu/~gohlke/pythonlibs/#setuptoo


Install newpy.py
----------------
Download newpy.py from GitHub to your local disk. Edit newpy.py with any text editor to overwrite below line with your email or other info as your author name.

    # Configuration Area Start for users of newpy.py
    _author_ ='Yingjie.Liu@thomsonreuters.com'
    # Configuration Area End

Usage
-----

    Python newpy.py -h

Use Cases
-------
generate test.py without samples.

    Python newpy.py test

list all existing samples

    Python newpy.py -l

generate test.py with sample 1 included only.

    Python newpy.py test -s1

generate test.py with sample 1 and 3 included as comment.

    Python newpy.py test -s13 -c

By defaule, newpy.py will submit statistical data to global database for new file generation. In such case, a global newpy.py ID will be assigned to your test.py. Your IP address, Author name and Sample Selection will be recorded. Those data will only be used to improve newpy.py. Use -n to disable it.

Support
-------
mailto: jackandking@gmail.com

