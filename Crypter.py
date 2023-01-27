def change_files(filename, crytoFn, block_size=16):

    with open (filename, 'r+b') as _file:
        raw_value = _file.read(block_size)
        while raw_value:
            cipher_value = crytoFn(raw_value)
            if len(raw_value) != len(cipher_value):
                raise ValueError('o valor cifrado {} tem um tamanho diferente do valor plano {}'.format(len(cipher_value),len(raw_value)))

            _file.seek(- len(raw_value),1)
            _file.write(cipher_value)
            raw_value = _file.read(block_size)