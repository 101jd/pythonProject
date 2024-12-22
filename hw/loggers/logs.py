import logging as log
import pathlib

path_info = pathlib.Path("logs/debug_info.log")
path_warn = pathlib.Path("logs/warnings_errors.log")
formatt = '{levelname} {asctime} in module {name} line {lineno} function {funcName}(): {msg}'
file_formatt = log.Formatter('%(levelname)s %(asctime)s in module %(name)s line %(lineno)d function %(funcName)s(): %(msg)s')

log.basicConfig(level=log.DEBUG, format=formatt, style='{')

log_info = log.getLogger("info")
log_info_h = log.FileHandler(path_info)
log_info_h.setLevel(log.DEBUG)
log_info_h.setFormatter(file_formatt)
log_info.addHandler(log_info_h)


log_warns = log.getLogger("warns")
log_warns_h = log.FileHandler(path_warn)
log_warns_h.setLevel(log.WARNING)
log_warns_h.setFormatter(file_formatt)
log_warns.addHandler(log_warns_h)
