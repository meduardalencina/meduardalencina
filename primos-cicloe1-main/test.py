"""
Nada para ver aqui. Siga em frente...
"""

import unittest


def compila_e_testa(file_name: str):
    import os
    import subprocess

    read_path = 'src'

    ext = '.exe' if os.name == 'nt' else ''

    output_file = os.path.join(read_path, file_name.replace('.c', ext))

    return_code = 0

    try:
        subprocess.run(['gcc', os.path.join(read_path, file_name), '-o', output_file], check=True)

        subprocess.run([output_file], check=True)
    except subprocess.CalledProcessError:
        return_code = 1
    finally:
        if os.path.exists(output_file):
            os.remove(output_file)
        return return_code


class TestaTudo(unittest.TestCase):
    def testa_primos(self):
        nome_tarefa = 'primes.c'
        self.assertEqual(0, compila_e_testa(nome_tarefa), 'A tarefa %s não foi resolvida corretamente' % nome_tarefa)

    def testa_gemeos(self):
        nome_tarefa = 'twins.c'
        self.assertEqual(0, compila_e_testa(nome_tarefa), 'A tarefa %s não foi resolvida corretamente' % nome_tarefa)


if __name__ == '__main__':
    unittest.main()
