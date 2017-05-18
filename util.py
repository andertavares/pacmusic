import os
import subprocess

def translate(string):

    eng = ['up', 'down', 'left', 'right']
    pt = ['acima', 'abaixo', 'esquerda', 'direita']

    for idx, word in enumerate(eng):
        string = string.replace(word, pt[idx])

    return string


def compile():
    if os.path.exists('compila.sh'):
        print 'Running compila.sh...'
        subprocess.call('chmod +x compila.sh', shell=True)
        subprocess.call('sh compila.sh > compile.log', shell=True)
        print 'Compilation complete!'
