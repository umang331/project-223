import zipfile
import time

folderpath = input('Path to the file: ')
zipf = zipfile.ZipFile(folderpath)

global r
r = 0
global tried
tried = 0
c = 0

if not zipf:
    print('The zip file/folder is not password protected, you can open it')
else:
    starttime = time.time()
    wordListFile = open('wordlist.txt', 'r', errors='ignore')
    body = wordListFile.read().lower()
    words = body.split('\n')

    for i in range(len(words)):
        word = words[i]
        password = word.encode('utf8').strip()
        c = c + 1
        print(f'Trying to decode password by: {format(word)}')
        try:
            with zipfile.ZipFile(folderpath, 'r') as zf:
                zf.extractall(pwd=password)
                print(f'The password is: {word}')
                endtime = time.time()
                r = 1
            break
        except:
            pass

        duration = endtime - starttime
        if(r == 0):
            print(
                f'Sorry, password not found. A total of {str(c)} possible combinations tried in {str(duration)} seconds. Password is not of 4 characters.')
        else:
            print(
                f'Password found after trying {str(c)} combinations in {str(duration)} seconds')
