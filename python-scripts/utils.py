import re
v = False

# image style 1:  ![](link)
img1 = re.compile(r'!\[\]\(.+\)')

# image style 2:
# <img src="../super/fn.png" ... />
img2 = re.compile('<img.+\/>')

# link containing standard file path:
link = re.compile(r'\[.+\](.+)')
path = re.compile(r'(.+)')

#-------------------------------

def f(s):
    if v:  print("found image path type 1\n" + s)
    # remove '![[(' and ')'
    ret = s[4:-1]
    if v:  print(ret + '\n')
    return ret
    
def g(s):
    if v:  print("found image path type 2\n" + s)
    # find file path in:
    # <img src="../super/fn.png" ... />
    i = s.find('"')
    assert i != -1
    j = s.find('"',i+1)
    ret = s[i+1:j]
    if v:  print(ret + '\n')
    return ret
    
def h(s):
    if v:  print("found file path\n" + s)
    m = path.match(s)
    if m:
        i = s.find('(')
        if i == -1:
            return
        j = s.find(')',i+1)
        ret = s[i+1:j]
        if v:  print(ret + '\n')
        return ret
    if v:  print("no match")

#------------------------------------

def extract_link(s):
    L1 = [img1, img2, link]
    L2 = [f,g,h]
    for regexpr, handler in zip(L1,L2):
        m = regexpr.match(s)
        if m:
            result = m.group(0)
            return handler(result)
        
if __name__ == "__main__":
    v = True
    L = ['![](path)',
         '<img src="../super/fn.png" ... />',
         '[app.py](app.py)',
         '[name](../path/to/file.md)'
         ]
         
    for s in L:
        print("main: " + s)
        extract_link(s)