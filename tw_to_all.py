import sys
import os
import shutil
targets = sys.argv[1:]
def copy_and_overwrite(from_path, to_path):
    if os.path.exists(to_path):
        shutil.rmtree(to_path)
    shutil.copytree(from_path, to_path)

for v in targets:
    shutil.copyfile(v, v.replace('zh-tw', 'zh-cn'))
    shutil.copyfile(v, v.replace('zh-tw', 'vi'))
    shutil.copyfile(v, v.replace('zh-tw', 'th-th'))