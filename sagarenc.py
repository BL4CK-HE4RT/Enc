#!/data/data/com.termux/files/usr/bin/python
import platform,os,sys
bit = platform.architecture()[0]
if bit == '64bit':
    print(" [///] You Are 64 BIT USER")
    import encrypt_enc

elif bit == '32bit':
    print(" [///] sorry bit is not frequent")
