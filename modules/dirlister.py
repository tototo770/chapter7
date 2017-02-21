# -*- coding: utf-8 -*-

import os

def run(**kwargs):

    print("[*] In dirlister module.")
    files = os.listdir(".")

    return str(files)