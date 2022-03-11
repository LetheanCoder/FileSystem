#!/usr/bin/python3

# imports tempfile module
import tempfile

# creates temporary file & writes data to object
fp = tempfile.TemporaryFile()
fp.write(b'This is some sample text.')

# reads data from created temporary file
fp.seek(0)
fp.read()

# closes file, removing it
fp.close()

# creates temporary file w/context manager
with tempfile.TemporaryFile() as fp:
    fp.write(b'This is some sample text')
    fp.seek(0)
    fp.read()

#file should now be closed and removed

# creates temporary directory w/context manager
with tempfile.TemporaryDirectory() as tmpdirname:
    print('created temporary directory', tmpdirname)

# directory and contents should be removed