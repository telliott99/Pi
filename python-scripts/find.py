import sys, subprocess, re, os
import utils as ut

'''
take a directory on the command line
find all .md files
search for links within those .md files
check if the linked file exists
'''

try:
    d = sys.argv[1]
except IndexError:
    print("This program requires an input directory")
    print("-v flag requests verbose output")
    sys.exit()

try: 
    v = sys.argv[2] == '-v'
except:
    v = False

if v:  print('dir:  ' + d)
if v:  print("")

#-----------------------------------

# all .md files in the directory and sub-directories
out = subprocess.check_output(['find', d])

L = out.strip().split('\n')
L = [p for p in L if p.endswith('.md')]
# make the path shorter by removing the directory
L = [p.replace(d,"") for p in L]

# note:  file paths in L start with '/'

#-----------------------------------

def pp(fn,link,path):
    print('fn:   ' + fn) 
    print('link: ' + link)
    print('path: ' + path)
    print("")

# check if file exists for a given link
    
def check(fn,link,D):
    if 'http' in link:
        return
        
    # some files have expressions
    # that don't parse with our regexpr
    # temp fix:
    for term in ['via', 'clang', 'x + 26']:
	    if term in link:
	        return
            
    pL = fn[1:].split('/')
    if link.startswith('..'):
        parent = '/' + '/'.join(pL[:-2])
        link = link[2:]
    else:
        parent = '/' + '/'.join(pL[:-1])
        link = '/' + link
    
    path = d + parent + link
    short = path.replace(d, "")
    
    # there's an error in the logic
    # rarely, we get '//' in path
    # just fix it
  
    if '//' in path:
        path = path.replace('//','/')
        short = path.replace(d, "")
    
    if not os.path.exists(path):
        pp(fn,link,short)
        print('** error **\n' + short + '\ndoes not exist\n')
        print('-'*10)
        D[fn] = False
        
    else:
        if v:
            pp(fn,link,short)
            print("OK:  file exists\n")
            
        if v:  print('-'*10)

#-----------------------------------
# do the search

def run(D):
	for fn in L:
	    OK_files[fn] = True
	
	    with open(d+fn,'r') as fh:
	        data = fh.read()
	        sL = data.strip().split('\n')
	        for line in sL:
	            link = ut.extract_link(line)
	            if link:
	                check(fn, link, OK_files)
	

OK_files = dict()
run(OK_files)
D = OK_files
good = sum( [1 for k in D.keys() if D[k]] )
t = (len(D.keys()), good)
print('%d files searched: %d OK' % t) 

