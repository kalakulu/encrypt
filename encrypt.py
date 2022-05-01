############ > Module < #########
import os,sys,marshal,zlib,base64
#################################

def help():  ########## > Help < ##########
    print ('''\n
  ╭━━╮╭━━╮
  ┃╭╮┗┻━━┻━╮    [•] Author  : kalakulu
  ┃╰┓╭━╮╭━╮┃    [•] Program : Python
  ╰━┓┃▇┃┃▇┃┃    [•] github  : https://github.com/kalakulu/encrypt
    ┃╱▔▔▔▔▔▔▔▇  [•] Version : 1.0
    ┃▏┏┳┳┳┳┳━┛
    ┃╲╰┻┻┻┻┻┓
    ▔▔▔▔▔▔▔▔▔
   [*] Usage   : python encrypt.py [command] [Mode] [File] [File-Output]
   [*] Mode    :
          -m    : encrypt marshal
          -z    : encrypt zlib
          -b85  : encrypt base85
          -b64  : encrypt base64
          -b32  : encrypt base32
          -b16  : encrypt base16
          -c    : encrypt marshal/zlib/base64
   [*] Command :
          -enc  : encrypt File
          -dec  : decrypt File  [Comming Soon]
''')

def more(command, mode, file, fileoutput): ########## > More < ##########
  ##########################################################################
  #                                 encrypt                                #
  ##########################################################################

    if (command) == "-enc" and (mode) == "-m": ##### Marshal #####
        try:                            #################
           see = open((file),'r').read()                #
        except FileNotFoundError:                       # > Checking File
           print ("[!]File not found")                  #
           sys.exit()                   #################
        comp = compile(see,"","exec")
        mars = marshal.dumps(comp)      ################# > Encrypt File
        wrte = open((fileoutput),'w')
        wrte.write("import marshal\n")  ##########################
        wrte.write(f"exec(marshal.loads({mars}))")               # > Write To File Output
        print (f"File Succes encrypt | Save to > {fileoutput}") ##
        sys.exit()

    elif (command) == "-enc" and (mode) == "-z": ##### Zlib #####
        try:                            #################
           see = open((file),'r').read()                #
        except FileNotFoundError:                       # > Checking File
           print ("[!]File not found")                  #
           sys.exit()                   #################
        byts = bytes(see,'ascii')
        zlip = zlib.compress(byts)      ################# > Encrypt File
        wrte = open((fileoutput),'w')
        wrte.write("import zlib\n")     ##########################
        wrte.write(f"exec(zlib.decompress({zlip}))")             # > Write To File Output
        print (f"File Succes encrypt | Save to > {fileoutput}")
        sys.exit()

    elif (command) == "-enc" and (mode) == "-b85": ##### Base 85 #####
        try:                            #################
           see = open((file),'r').read()                #
        except FileNotFoundError:                       # > Checking File
           print ("[!]File not found")                  #
           sys.exit()                   #################
        byts = bytes(see,'ascii')
        base = base64.b85encode(byts)   ################# > Encrypt File
        wrte = open((fileoutput),'w')
        wrte.write("import base64\n")   ##########################
        wrte.write(f"exec(base64.b85decode({base}))")            # > Write To File Output
        print (f"File Succes encrypt | Save to > {fileoutput}")
        sys.exit()

    elif (command) == "-enc" and (mode) == "-b64": ##### Base 64 #####
        try:                            #################
           see = open((file),'r').read()                #
        except FileNotFoundError:                       # > Checking File
           print ("[!]File not found")                  #
           sys.exit()()                 #################
        byts = bytes(see,'ascii')
        base = base64.b64encode(byts)   ################# > Encrypt File
        wrte = open((fileoutput),'w')
        wrte.write("import base64\n")   ##########################
        wrte.write(f"exec(base64.b64decode({base}))")            # > Write To File Output
        print (f"File Succes encrypt | Save to > {fileoutput}")
        sys.exit()

    elif (command) == "-enc" and (mode) == "-b32": ##### Base 32 #####
        try:                            #################
           see = open((file),'r').read()                #
        except FileNotFoundError:                       # > Checking File
           print ("[!]File not found")                  #
           sys.exit()()                 #################
        byts = bytes(see,'ascii')
        base = base64.b32encode(byts)   ################# > Encrypt File
        wrte = open((fileoutput),'w')
        wrte.write("import base64\n")   ##########################
        wrte.write(f"exec(base64.b32decode({base}))")            # > Write To File Output
        print (f"File Succes encrypt | Save to > {fileoutput}")
        sys.exit()

    elif (command) == "-enc" and (mode) == "-b16": ##### Base 16 #####
        try:                            #################
           see = open((file),'r').read()                #
        except FileNotFoundError:                       # > Checking File
           print ("[!]File not found")                  #
           sys.exit()()                 #################
        byts = bytes(see,'ascii')
        base = base64.b16encode(byts)   ################# > Encrypt File
        wrte = open((fileoutput),'w')
        wrte.write("import base64\n")   ##########################
        wrte.write(f"exec(base64.b16decode({base}))")            # > Write To File Output
        print (f"File Succes encrypt | Save to > {fileoutput}")
        sys.exit()

    elif (command) == "-enc" and (mode) == "-c": ##### Marshal , Zlib , Base64 #####
        try:                            #################
           see = open((file),'r').read()                #
        except FileNotFoundError:                       # > Checking File
           print ("[!]File not found")                  #
           sys.exit()                   #################
        comp = compile(see,"","exec")
        mars = marshal.dumps(comp)      #################
        zlip = zlib.compress(mars)                      # > Encrypt File
        base = base64.b64encode(zlip)   #################
        wrte = open(fileoutput,'w')
        wrte.write("import marshal,zlib,base64\n") #####################################
        wrte.write(f"exec(marshal.loads(zlib.decompress(base64.b64decode({base}))))") ## > Write To File Output
        print (f"File Succes encrypt | Save to > {fileoutput}")
        sys.exit()

  ##########################################################################
  #                                 decrypt                                #
  #                              --------------                            #
  #                               Comming Soon                             #
  ##########################################################################

    else:
        help()


def main(): ########## > main < ##########
    if len(sys.argv) != 5:
        help()
    else:
         more(sys.argv[1], (sys.argv[2]), (sys.argv[3]), (sys.argv[4]))


if __name__ == '__main__':
    main()
