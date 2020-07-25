from ncmdump import dump
import os,fnmatch

def all_files(root, patterns='*', single_level=False, yield_folder=False):
    patterns = patterns.split(';')
    for path, subdirs, files in os.walk(root):
        if yield_folder:
            files.extend(subdirs)
        files.sort()
        for fname in files:
            for pt in patterns:
                if fnmatch.fnmatch(fname, pt):
                    yield os.path.join(path, fname)
                    break
        if single_level:
            break
while 1:
    thefile=list(all_files('C:\\CloudMusic\\', '*.ncm'))
    for item in thefile:
        print (dump(item),"转换成功！")
        delete = os.remove(item)
