history
ls
from pathlib import Path
pathname = "kitten_web"
path = Path(pathname)
path
path.resolve()
list(path.iterdir())
path.is_dir()
path.is_file()
def handle_directory(target):
    for p in target.iterdir():
        if p.is_dir(): handle_directory(p)
        if p.is_file(): print(p)
def handle_directory(target):
    for p in target.iterdir():
        if p.is_dir(): handle_directory(p)
        if p.is_file(): print(p.as_posix())
handle_directory(path)
path
pathname = "~/code/automating-aws-with-python/01-webotron/kitten_web/"
path = Path(pathname)
handle_directory(path.expanduser())
root = pathname
path
root
path.relative_to(root)
def handle_directory(target):
    for p in target.iterdir():
        if p.is_dir(): handle_directory(p)
        if p.is_file(): print("Path: {}\n Key: {}").format(p, p.relative_to(root))
root
root = "/Users/breihms1/code/automating-aws-with-python/01-webotron/kitten_web/"
root
handle_directory(Path(root))
def handle_directory(target):
    for p in target.iterdir():
        if p.is_dir(): handle_directory(p)
        if p.is_file(): print("Path: {}\n Key: {}".format(p, p.relative_to(root)))
handle_directory(Path(root))
%history
save pathliblab.py
save
help
help()
history -f pathlib.py
