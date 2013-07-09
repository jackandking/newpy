newpy
=====

Quickly python programming for small utilities. It will also enable experieced developers of other script languages to start pythoning in short time without googling. Personally I will use it recall python key syntax when I have stopped pythoning for a while.

Run Environment
---------------
Only tested in Python 2.7 under Windows and Linux.

Install
-------
Download newpy.py from GitHub to your local disk. Edit newpy.py with any text editor to overwrite below line with your email or other info as your author name.

    # Configuration Area Start for users of newpy
    _author_ = 'Yingjie.Liu@thomsonreuters.com'
    # Configuration Area End

Usage
-----
    python newpy.py -h

Samples
-------
generate test.py without samples.

    python newpy.py test

list all existing samples

    python newpy.py -l

generate test.py with sample 1 included only.

    python newpy.py test -s1

generate test.py with sample 1 and 3 included as comment.

    python newpy.py test -s13 -c

generate test.py and submit statistical data to newpy database. A global newpy ID will be assigned to your test.py. Your IP address, Author name and Sample Selection will be recorded with -r. Those data will only be used to improve newpy.

    python newpy.py test -r

Support
-------
Email: jackandking@gmail.com
