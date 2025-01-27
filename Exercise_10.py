import sys, glob, os

# Get the directory name
if sys.platform == 'win32':
    hdir = os.environ['HOMEPATH']
else:
    hdir = os.environ['HOME']
print(hdir)

# Construct a portable wildcard pattern
pattern = os.path.join(hdir,'*')
print(pattern)

# TODO: Use the glob.glob() function to obtain the list of filenames
list_fileName = glob.glob(pattern)
print(list_fileName)