import shutil

from datetime import date
from pathlib import Path
import os
from watchdog.events import FileSystemEventHandler
import time
from watchdog.observers import Observer

# for git

class Pc_Cleaner(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            i = 1
            if filename != 'Ashfak':
                new_name = filename
                extension = os.path.splitext(new_name)
                if extension[1] not in extension_path:
                    extension_noname = 'noname'
                    if not os.path.exists(folder_destination + '/' + extension_noname + dir_sort):
                        os.makedirs(folder_destination + '/' + extension_noname + dir_sort)

                    file_exists = os.path.isfile(folder_destination + '/' + extension_noname + dir_sort + new_name)
                    while file_exists:
                        i += 1
                        new_name = filename + str(i)
                        file_exists = os.path.isfile(folder_destination + extension_noname + dir_sort + new_name)

                    src = folder_to_track + '/' + filename
                    new_name = folder_destination + '/' + extension_path['noname'] + dir_sort + new_name
                    os.rename(src, new_name)
                    break

                else:
                    if not os.path.exists(folder_destination + '/' + extension_path[extension[1]] + dir_sort):
                        os.makedirs(folder_destination + '/' + extension_path[extension[1]] + dir_sort)

                    file_exists = os.path.isfile(folder_destination + '/' + extension_path[extension[1]] + dir_sort + new_name)
                    print(file_exists)
                    while file_exists:
                       i += 1
                       filename_2 = filename.split('.')
                       new_name = filename_2[0] + str(i) + '.' + filename_2[1]
                       file_exists = os.path.isfile(folder_destination + '/' + extension_path[extension[1]] + dir_sort + new_name)


                    src = folder_to_track + '/' + filename
                    new_name = folder_destination + '/' + extension_path[extension[1]] + dir_sort + new_name
                    os.rename(src, new_name)


folder_to_track = '/Users/ashfak.mohamed/Desktop'
folder_destination = '/Users/ashfak.mohamed/Desktop/Ashfak'
today = str(date.today())
year, month, date = today.split('-')
dir_sort = '{}/{}/'.format(year, month)



extension_path = {

    'noname': 'Others/',
    '.pub': 'Others/',
    '.vsdx': 'Others/',
    # text
    '.txt': 'Text/',
    '.odt ': 'Text/',
    '.log ': 'Text/',
    '.rtf': 'Text/',
    '.tex': 'Text/',
    '.wks ': 'Text/',
    '.wps': 'Text/',
    '.wpd': 'Text/',
    # video
    '.3g2': 'Videos/',
    '.3gp': 'Videos/',
    '.avi': 'Videos/',
    '.flv': 'Videos/',
    '.h264': 'Videos/',
    '.m4v': 'Videos/',
    '.mkv': 'Videos/',
    '.mov': 'Videos/',
    '.mp4': 'Videos/',
    '.mpg': 'Videos/',
    '.mpeg': 'Videos/',
    '.rm': 'Videos/',
    '.swf': 'Videos/',
    '.vob': 'Videos/',
    '.wmv': 'Videos/',
    '.wmz': 'Videos/',
    # audio
    '.wav': 'Audio',
    '.mp3': 'Audio',
    # images
    '.ai': 'Images/',
    '.bmp': 'Images/',
    '.gif': 'Images/',
    '.JPG': 'Images/',
    '.jpeg': 'Images/',
    '.png': 'Images/',
    '.ps': 'Images/',
    '.psd': 'Images/',
    '.svg': 'Images/',
    '.tif': 'Images/',
    '.tiff': 'Images/',
    '.cr2': 'Images/',
    # internet
    '.eml': 'Others/internet/',
    '.msg': 'Others/internet/',
    '.cer': 'Others/internet/',
    '.cfm': 'Others/internet/',
    '.cgi': 'Others/internet/',
    '.pl': 'Others/internet/',
    '.css': 'Others/internet/',
    '.htm': 'Others/internet/',
    '.js': 'Others/internet/',
    '.jsp': 'Others/internet/',
    '.part': 'Others/internet/',
    '.php': 'Others/internet/',
    '.rss': 'Others/internet/',
    '.xhtml': 'Others/internet/',
    '.html': 'Others/internet/',
    # compressed
    '.7z': 'Others/compressed',
    '.arj': 'Others/compressed',
    '.deb': 'Others/compressed',
    '.pkg': 'Others/compressed',
    '.rar': 'Others/compressed',
    '.rpm': 'Others/compressed',
    '.tar.gz': 'Others/compressed',
    '.z': 'Others/compressed',
    '.zip': 'Others/compressed',
    # doc
    '.doc': 'Word/',
    '.docx': 'Word/',
    # pdf
    '.pdf': 'PDF/',
    # executables
    '.msi': 'Others/executables',
    '.apk': 'Others/executables',
    '.bat': 'Others/executables',
    '.com': 'Others/executables',
    '.exe': 'Others/executables',
    '.gadget': 'Others/executables',
    '.jar': 'Others/executables',
    '.wsf': 'Others/executables',

    # presentations
    '.key': 'Others/presentations',
    '.odp': 'Others/presentations',
    '.pps': 'Others/presentations',
    '.ppt': 'Others/presentations',
    '.pptx': 'Others/presentations',
    '.ppsx': 'Others/presentations',
    # programming
    '.c': 'programming/c&c++',
    '.class': 'programming/java',
    '.java': 'programming/java',
    '.py': 'programming/python',
    '.ipynb': 'programming/python',
    '.sh': 'programming/shell',
    '.h': 'programming/c&c++',
    # spreadsheets
    '.ods': 'Excel/',
    '.xlr': 'Excel/',
    '.xls': 'Excel/',
    '.xlsx': 'Excel/',
    '.xlsb': 'Excel/',
    # CSV
    '.csv': 'Excel/CSV/'

}

""" # system
        '.bak':    'Others/system/',
        '.cab':    'Others/system/',
        '.cfg':    'Others/system/',
        '.cpl':    'Others/systems',
        '.cur':    'Others/systems',
        '.dll':    'Others/systems',
        '.dmp':    'Others/systems',
        '.drv':    'Others/systems',
        '.icns':   'Others/systems',
        '.ico':    'Others/systems',
        '.ini':    'Others/systems',
        '.lnk':    'Others/systems',
        '.msi':    'Others/systems',
        '.sys':    'Others/systems',
        '.tmp':    'Others/systems'
"""




event_handler = Pc_Cleaner()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(30)
except KeyboardInterrupt:
    observer.start()
observer.join()
