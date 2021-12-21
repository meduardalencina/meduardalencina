import os
import sqlite3


class SQLite(object):
    def __init__(self, file):
        self.file = file

    def __enter__(self):
        self.conn = sqlite3.connect(self.file)
        self.conn.row_factory = sqlite3.Row
        return self.conn.cursor()

    def __exit__(self, type, value, traceback):
        self.conn.commit()
        self.conn.close()


def create_table(cursor: sqlite3.Cursor, table: str, fields: dict, other_data: list = None) -> None:
    """
    Função para criar tabelas.

    :param cursor: um cursor para o banco de dados
    :param table: Nome da tabela
    :param fields: Um dicionário onde a chave é o nome da coluna, e o valor o tipo/modificadores (e.g. primary key)
    :param other_data: Para definir foreign keys, ou outras configurações.
    """
    command = "CREATE TABLE %s (%s)" % (
        table,
        ','.join([k + ' ' + v for k, v in fields.items()] + (
            other_data if other_data is not None else []))
    )
    cursor.execute(command)


def insert_rows(cursor: sqlite3.Cursor, table: str, tuples: list) -> None:
    """
    Função para inserir tuplas numa tabela.

    :param cursor: um cursor para o banco de dados
    :param table: Nome da tabela
    :param tuples: Uma lista de dicionários. Para cada dicionário, a chave é o nome da coluna, e o valor, o valor da tupla
    para aquela coluna.
    """
    for some_tuple in tuples:
        tuple_values = []
        for v in some_tuple.values():
            if isinstance(v, str):
                tuple_values += ['\'' + v + '\'']
            else:
                tuple_values += [str(v)]

        command = "INSERT INTO %s(%s) VALUES (%s)" % (
            table, ','.join(map(str, some_tuple.keys())), ','.join(tuple_values)
        )
        cursor.execute(command)


def select_rows(cursor: sqlite3.Cursor, clause: str) -> list:
    """
    Método para fazer seleção de tuplas de uma tabela. Aceita qualquer comando SQLITE.

    :param cursor: um cursor para o banco de dados
    :param clause: A cláusula de seleção (e.g. SELECT * FROM table)
    :return: Uma lista de tuplas
    """
    res = cursor.execute(clause)
    rows = []
    for row in res:  # type: sqlite3.Row
        rows += [tuple([row[k] for k in row.keys()])]

    return rows


def raw_execute(cursor: sqlite3.Cursor, clause: str) -> sqlite3.Cursor:
    """
    Executa qualquer comando SQLITE. Retorna o resultado.

    :param cursor: um cursor para o banco de dados
    :param clause: Qualquer cláusula SQLITE.
    :return: O resultado da execução da cláusula (se ela retorna um valor), ou None.
    """
    return cursor.execute(clause)


def remove_db(file: str) -> None:
    """
    Deleta o arquivo .db contido em file.

    :param file: Caminho para o banco .db.
    """
    try:
        os.remove(file)
    except FileNotFoundError:
        pass


def main(path: str = '.', db_name: str = 'test.db') -> None:
    remove_db(os.path.join(path, db_name))

    with SQLite(os.path.join(path, db_name)) as cursor:
        # TODO desenvolva seu código aqui
        create_table(
            cursor,
            'musica',
            {'id': 'INTEGER PRIMARY KEY', 'nome': 'text NOT NULL', 'link': 'text NOT NULL', 'tempo_de_musica': 'INTEGER NULL'}
        )
        create_table(
            cursor,
            'artista',
            {'id': 'INTEGER PRIMARY KEY', 'nome': 'text NOT NULL'}
        )
        create_table(
            cursor,
            'musica_do_artista',
            {'id_musica': 'INTEGER NOT NULL', 'id_artista': 'INTEGER NOT NULL'},
            ['PRIMARY KEY(id_musica, id_artista)', 'FOREIGN KEY(id_artista) REFERENCES artista(id)',
             'FOREIGN KEY(id_musica) REFERENCES musica(id)']
        )
        create_table(
            cursor,
            'genero',
            {'id_musica': 'INTEGER NOT NULL', 'id_genero': 'INTEGER NOT NULL', 'nome':'text NOT NULL'},
            ['PRIMARY KEY(id_musica, id_genero)', 'FOREIGN KEY(id_genero) REFERENCES genero(id)',
             'FOREIGN KEY(id_musica) REFERENCES musica(id)']
        )

        insert_rows(
            cursor,
            'musica',
            [
                {
                    'id': '10',
                    'nome': 'Pretty hurts',
                    'link': 'https://youtu.be/LXXQLa-5n5w',
                    'tempo_de_musica': '7:05'
                }
            ]
        )
        insert_rows(
            cursor,
            'artista',
            [
                {
                    'id': '1', 
                    'nome': 'Gotye'
                },
                {
                    'id': '2',
                    'nome': 'Tim Maia'
                },
                {
                    'id': '3',
                    'nome': 'Bruna Carla'
                },
                {
                    'id': '4', 
                    'nome': 'Lady Gaga'
                },
                {
                    'id': '5', 
                    'nome': 'Normani'
                },
                {
                    'id': '6', 
                    'nome': 'Grupo revelação'
                },
                {
                    'id': '7',
                    'nome': 'Anavitória'
                },
                {
                    'id': '8',
                    'nome': 'Kelly Key'
                },
                {
                    'id': '9',
                    'nome': 'Rihanna'
                },
                {
                    'id': '10',
                    'nome': 'Beyoncé'
                }
            ]
        )
        insert_rows(
            cursor,
            'musica_do_artista',
            [
                {
                    'id_musica': '1',
                    'id_artista': '1'
                },
                {
                    'id_musica': '2',
                    'id_artista': '2'
                },
                {
                    'id_musica': '3', 
                    'id_artista': '3'
                },
                {
                    'id_musica': '4', 
                    'id_artista': '4'
                },
                {
                    'id_musica': '5',
                    'id_artista': '5'
                },
                {
                    'id_musica': '6', 
                    'id_artista': '6'
                },
                {
                    'id_musica': '7',
                    'id_artista': '7'
                },
                {
                    'id_musica': '8', 
                    'id_artista': '8'
                },
                {
                    'id_musica': '9', 
                    'id_artista': '9'
                },
                {
                    'id_musica': '10', 
                    'id_artista': '10'
                }

            ]
        )
        insert_rows(
            cursor,
            'genero',
            [
                {
                    'id_musica': '1', 
                    'id_genero': '1',
                    'nome':'art pop'
                },
                {
                    'id_musica': '2', 
                    'id_genero': '2', 
                    'nome':'mpb'
                },
                {
                    'id_musica': '3', 
                    'id_genero': '3',
                    'nome':'gospel'},
                {
                    'id_musica': '4', 
                    'id_genero': '4',
                    'nome':'pop'
                },
                {
                    'id_musica': '5', 
                    'id_genero': '5',
                    'nome':'pop'
                },
                {
                    'id_musica': '6', 
                    'id_genero': '6',
                    'nome':'samba'
                },
                {
                    'id_musica': '7', 
                    'id_genero': '7', 
                    'nome':'mpb'
                },
                {
                    'id_musica': '8', 
                    'id_genero': '8', 
                    'nome':'dance-pop'
                },
                {
                    'id_musica': '9',
                    'id_genero': '9',
                    'nome':'pop'
                },
                {
                    'id_musica': '10', 
                    'id_genero': '10', 
                    'nome':'pop'
                }

            ]
        )
        # TODO desenvolva seu código aqui


if __name__ == '__main__':
    main()
