import sys
import os
import re
targets = sys.argv[1:]
p = re.compile(r'.*[a-zA-Z]+0*')
for v in targets:
    a = p.sub('', v)
    print(a)
    input()
    os.rename(v, a)    
input()