#!/usr/bin/python3
#-*- coding: utf-8 -*-
#marshal py3

'''
PyMarshal - Compile Python Script
This project was created by Dfv47 with Black Coder Crush. 
Copyright 12 - 07 - 2k19 @m_d4fv
'''

try:
        import os,sys,time,marshal
except Exception as F:
        exit("[ModuleErr] %s"%(F))
        
if sys.version[0] in '2':
        exit("[sorry] use python version 3")

# Color
a='\033[1;30m'
r='\033[1;31m'
g='\033[32;1m' 
y='\033[1;33m'
c='\033[1;36m' 
w='\033[1;37m' 
n='\033[0;00m' 
br='\033[91;7m' 

bannerpy3 = """
         {}___ 
{} ___ _  |{}_  {}{}| {}Author  {}:{} Emprror
{}| . | | |{}_  {}{}| {}Code    {}:{} Python
{}|  _|_  |{}___{}{}| {}Version {}:{} v.5.0
{}|_| |___| {}*{} https://github.com/Emperror-12
""".format(r,y,br,n,y,w,r,w,y,br,n,y,w,r,w,y,br,n,y,w,r,w,y,r,a)

'''
Coded  : @m_d4fv
Author : Dfv47
Team   : Black Coder Crush
Phone  : 6282223108828
Email  : daffamfthhsn21@gmail.com
Thanks : ZoneExploiter & CytoXploit
'''

os.system('clear')
try:
    print(bannerpy3)
    print (y+' ['+w+'#'+y+'] '+w+'Contoh '+y+':'+w+' /sdcard/nama.py')
    file = input(y+' ['+w+'?'+y+'] '+w+'Masukan Nama File'+y+' :'+w+' ')
    o = file.replace('.py', '')
except KeyboardInterrupt:
    sys.exit()
else:
    try:
        strng = open(file, 'r').read()
    except IOError:
        print (r+'\n ['+w+'!'+r+'] '+r+'[ '+w+'Error '+r+'] '+w+'File tidak di Temukan '+r+': '+w+'"'+dfv+'"\n')
        sys.exit()
    try:
        code = compile(strng,'','exec')
        data = marshal.dumps(code)
    except TypeError:
        print (R + '   ['+W+'!'+R+'] '+R+'[ '+W+'File Sudah di kompilasi\n') 
        sys.exit()

fileout = open(o + 'enc.py', 'w')
fileout.write('#Facebook : X Branden\n')
fileout.write('#JANGN DI RECORD SC GUA\n')
fileout.write('#Compiled By Emperror-12\n')
fileout.write('#https://github.com/Emperror-12\n')
fileout.write('import marshal\n')
fileout.write('exec(marshal.loads(' + repr(data) + '))')
fileout.close()
time.sleep(3) 
print (y+'\n ['+w+'+'+y+'] '+w+'File sukses,   '+y+': ' + w + o + 'enc.py\n')
