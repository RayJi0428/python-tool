import sys
import os
from shutil import copyfile
targets = sys.argv[1:]
for v in targets:
    copyfile(v, v.replace('zh-tw', 'zh-cn'))
    copyfile(v, v.replace('zh-tw', 'vi'))
    copyfile(v, v.replace('zh-tw', 'th-th'))
