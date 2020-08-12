from ncmdump import dump
import os,fnmatch

print("软件仅供学习交流，请勿用于商业及非法用途，如产生法律纠纷与本人无关。")
print("------")
print("请在下方输入网易云音乐下载路径，请确保输入正确，否则无法正常转换。")
print("如果您不知道路径在哪里，在网易云客户端中点击：设置 --> 下载设置，即可看到下载路径。")
print("如留空，默认: C:\\CloudMusic\\")
download_folder = input("下载路径：") or "C:\\CloudMusic\\"
os.system('cls')
waiting = True
print("当前下载路径：" + download_folder)
print("您现在可以在网易云音乐客户端中直接下载歌曲，本工具会自动将ncm转换成mp3格式。")
print("等待转换...")

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
    thefile=list(all_files(download_folder, '*.ncm'))
    for item in thefile:
        if(waiting == True):
            waiting = False
            os.system('cls')
        print (dump(item),"转换成功！")
        delete = os.remove(item)
