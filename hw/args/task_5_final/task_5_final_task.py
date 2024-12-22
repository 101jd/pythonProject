import pathlib
import task_5_logsfd
import argparse
import collections as col

parser = argparse.ArgumentParser(description='Input path')

parser.add_argument("path", type=str)

args = parser.parse_args()

path = pathlib.Path(args.path)

lst = []
files = col.namedtuple('Files', 'Names')
dirs = col.namedtuple('Dirs', "Names")


for dir in path.iterdir():
    if pathlib.Path(dir).is_dir():
        lst.append(dirs(dir.name))
        logsfd.log_dirs.info(f'Directory {dir.name}')
    if pathlib.Path(dir).is_file():
        lst.append(files((dir.name[:dir.name.index('.')], dir.suffix)))
        logsfd.log_files.info(f'File {dir.name}')

print(lst)


