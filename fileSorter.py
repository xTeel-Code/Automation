from pathlib import Path
import os
import shutil
import keyboard


user_path_list = os.getcwd().split('\\')

downloads_path = str('C:\\Users\\'+ user_path_list[2] +'\\Downloads')
torrent_path = str('C:\\Users\\'+ user_path_list[2] +'\\Downloads\\torrents')
exe_path = str('C:\\Users\\'+ user_path_list[2] +'\\Downloads\\exes')
zip_path = str('C:\\Users\\'+ user_path_list[2] +'\\Downloads\\zipFiles')
word_path = str('C:\\Users\\'+ user_path_list[2] +'\\Downloads\\wordDocuments')
pdf_path = str('C:\\Users\\'+ user_path_list[2] +'\\Downloads\\PDFs')
pictures = str('C:\\Users\\'+ user_path_list[2] +'\\Pictures\\Saved Pictures\\')
isos = str('C:\\Users\\'+ user_path_list[2] +'\\Downloads\\iso')
paths = [torrent_path, exe_path, zip_path, word_path, pdf_path, pictures, isos] 

def ensure_dir(dir):
    try:
        os.makedirs(dir)
        print("Done")
    except:
        print("Folder "+ dir +" Exists")
for x in paths:
    ensure_dir(x)

for file in os.listdir(downloads_path):
    if file.endswith('.torrent'):
        shutil.move(downloads_path + '//' + file, torrent_path)
    if file.endswith('.zip') or file.endswith('.rar'):
        shutil.move(downloads_path + '//' + file, zip_path)
    if file.endswith('.exe') or file.endswith('.msi'):
        shutil.move(downloads_path + '//' + file, exe_path)
    if file.endswith('.docx') or file.endswith('.doc') or file.endswith('.odt'):
        shutil.move(downloads_path + '//' + file, word_path)
    if file.endswith('.iso'):
        shutil.move(downloads_path + '//' + file, isos)
    if file.endswith('.pdf'):
        shutil.move(downloads_path + '//' + file, pdf_path)
    if file.endswith('.jpg') or file.endswith('.jpeg') or file.endswith('.png'):
        shutil.move(downloads_path + '//' + file, pdf_path)
    print("Sorting Completed Successfully")
input("Press Enter to exit")
