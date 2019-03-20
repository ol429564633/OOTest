import os
from config import config
from myMatch import match
from generate import generator


# os.chdir(config.auto_dir)
# os.system("call {}".format(config.auto_cmd))
# input_line = open(config.input_file).readline()
# output_lines = {}
# output_lines.update({"CYX": open(config.output_file).readline()})
# if not match(output_lines, input_line):
#     print("Fail")

os.chdir(config.dir)
while True:
    pat_string = generator()
    open(config.input_file, "w").write(pat_string)
    os.system("call {}".format(config.auto_cmd))
    input_line = open(config.input_file).readline()
    output_lines = {}
    for string in config.output_files:
        output_lines.update({string: open(config.output_files[string]).readline()})
    match(output_lines, input_line)
