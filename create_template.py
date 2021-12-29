import os
import shutil

cwd = os.getcwd()
code_dir = os.path.join(cwd, 'code')
template_dir = os.path.join(code_dir, 'Template.ipynb')

file_name = input('plz type the file name')

dst_dir = os.path.join(code_dir, file_name + '.ipynb')

# advanced copy to keep the meta information
shutil.copy2(template_dir, dst_dir)

# add escape character to whitespace
dst_dir = dst_dir.replace(' ', '\ ')

open_file_command = 'code ' + dst_dir

# open new file in a new vscode tab
# ref1: https://blog.csdn.net/Guo_ya_nan/article/details/103242652
# ref2: https://cloud.tencent.com/developer/article/1540943
os.system(open_file_command)