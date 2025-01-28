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

# TODO: use os.path.getsize to find each file's size
for file in file_names:
    # Look for size
    size = os.path.getsize(file)
#     Print result
print(file, size, bytes)

# TODO: Add a test to only display files that are not zero length - this task is doing what the above task should do
for file in file_names:
 # condition for file lengths greater than 0
 if size > 0:
     print(file, size, 'bytes')