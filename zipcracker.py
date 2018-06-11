from zipfile import ZipFile
import zipfile
from threading import *
import optparse
import sys
import time



def display():
    print("                                                                       ")
    print('            ******************welcome to ZipCracker********************')
    print('            ****Author : AMAN DUBEY                                ****')
    print("                                                                       ")


def extract(file, password):
        try:

             f = ZipFile(file)

             password_f = bytes(password.encode('utf-8'))

             f.extractall(pwd=password_f)

             print(">>>>> PASSWORD FOUND: " + password + '\n')


             sys.exit()

        except :
            exit(0)



def main():
    parser = optparse.OptionParser(description=" This is a simple zip password cracker program works on dictionary"
                                               " attack. \n", usage="  help: ----\n  USAGE:" + \
                                         "python3 zipcracker.py -f <zipfile> -d <dictionary>\n  -f --- for file (in zip format)"
                                         "\n  -d --- for dictionary name")

    parser.add_option('-f', dest='zfile', type='string', help='mention zip file name in format: name.zip')
    parser.add_option('-d', dest='dfile', type='string', help='mention dictionary file name in format: name.txt')

    (options, args) = parser.parse_args()

    if (options.zfile == None) | (options.dfile == None):
        print(parser.description)
        print(parser.usage)
        exit(0)
    else:
        zfile = options.zfile
        dfile = options.dfile

    if not zipfile.is_zipfile(zfile):
        print(' ERROR: plese enter correct zip file')

    try:

        passFile = open(dfile)
    except:
         print(" ERROR:dictionary not found/cannot crack")
         exit(0)


    for line in passFile.readlines():
        password = line.strip('\n')
        t = Thread(target=extract, args=(zfile, password))
        t.start()



if __name__ == '__main__':
 start_time = time.time()
 display()
 try:
    main()

 except KeyboardInterrupt:
     sys.exit()
 except IOError:
     sys.exit()
 except FileNotFoundError:
     print('file not found')
     sys.exit()
 print("----> EXECUTION TIME:  %s seconds --" % (time.time() - start_time))