import sys, subprocess, re, os
import utils as ut

'''
input a directory on the command line
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

# check if file exists for a given link
    
def check(fn,link,D):
    # don't check external links
    if 'http' in link:
        return
        
    # weird pattern that matches our regex
    # [ ok ] Starting nginx (via systemctl)
    if link == "via systemctl":
        return
    	
	# file names result from removing the directory d
	# so they always start with '/' 
    assert fn[0] == '/'
    fnL = fn[1:].split('/')
    
    # remove the file name containing the link
    fnL.pop()
    
    # links either start with '../' or '../..'
    # or they're relative to the current directory
    linkL = link.split('/')
    
    while linkL[0] == '..':
        linkL.pop(0)
        fnL.pop()
    
    short = '/'.join(fnL + linkL)
    path = d + '/' + short
    
    if not os.path.exists(path):
        pp(fn,link,short)
        print('** error **\n' + short + '\ndoes not exist\n')
        print('-'*10)
        D[fn] = False
        
    else:
        if v:
            pp(fn,link,short)
            print("OK:  file exists")
            
    if v:  print('-'*10)

#-----------------------------------
# do the search

def run(D):
    active = True
    for fn in L:
        D[fn] = True

        with open(d+fn,'r') as fh:
            data = fh.read()
            sL = data.strip().split('\n')
            for line in sL:
            
                # don't read quoted blocks
                if line.strip() == '```':
                    active = not(active)
                if not active:
                    continue
            
                link = ut.extract_link(line)
                if link:
                    check(fn, link, D)

OK_files = dict()
run(OK_files)
D = OK_files
good = sum( [1 for k in D.keys() if D[k]] )
t = (len(D.keys()), good)
print('%d files searched: %d OK' % t) 

