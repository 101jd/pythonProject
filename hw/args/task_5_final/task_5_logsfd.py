import logging as log
import pathlib as pl
import os

f = "logs/files.log"
d = "logs/dirs.log"

if not os.path.exists("logs/"):
    os.mkdir("logs")
if not os.path.exists(f):
    os.open(f, os.O_CREAT)
if not os.path.exists(d):
    os.open(d, os.O_CREAT)
path_files = pl.Path(f)
path_dirs = pl.Path(d)

formatt = '{levelname}: {msg}'
file_formatt = log.Formatter('%(levelname)s: %(msg)s')

log.basicConfig(level=log.INFO, format=formatt, style='{')

log_files = log.getLogger("files")
log_files_fh = log.FileHandler(path_files)
log_files_fh.setLevel(log.INFO)
log_files_fh.setFormatter(file_formatt)
log_files.addHandler(log_files_fh)


log_dirs = log.getLogger("dirs")
log_dirs_fh = log.FileHandler(path_dirs)
log_dirs_fh.setLevel(log.INFO)
log_dirs_fh.setFormatter(file_formatt)
log_dirs.addHandler(log_dirs_fh)