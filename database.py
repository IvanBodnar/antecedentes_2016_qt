import psycopg2
from psycopg2 import extras
import pandas as pd

conn_dict = {
    'host': 'localhost',
    'dbname': 'pfa_dgc_nueva',
    'user': 'ivan',
    'password': 'ivan'
}


class Records:
    """
    Conecta con la base de datos y realiza consultas

    :param conn_dict: Diccionario con los parametros de conexión
                      a la base de datos:
                      > host
                      > dbname
                      > user
                      > password
    :param: table: string con el nombre de la tabla
    :param: query: string con la consulta a realizar
    :param: schema='public': string con el nombre del schema
    """
    def __init__(self, conn_dict, table, query, schema='public'):
        self.schema = schema
        self.table = table
        self.query = query
        self.conn = psycopg2.connect(**conn_dict)
        self.cur = self.conn.cursor(cursor_factory=psycopg2.extras.NamedTupleCursor)
        self.cur.execute(self.query)
        self.executed = self.cur.fetchall()

    def records(self):
        """
        Devuelve una lista de objetos 'record' con los datos
        de la consulta

        :return: list de namedtuples
        """
        return [row for row in self.executed]

    def a_ord_dicts(self):
        """
        Devuelve una lista de ordereddicts

        :return: list de ordereddicts
        """
        return [row._asdict() for row in self.executed]

    def a_pandas(self):
        """
        Devuelve un DataFrame de pandas
        :return: pandas DataFrame
        """
        return pd.DataFrame.from_dict([row._asdict() for row in self.executed])

    def a_csv(self, path, alias=None):
        """
        Devuelve un csv

        :param: path: path donde se va a grabar el csv
        :param: alias: iterable con los alias de las columnas en el orden deseado
        :return: csv
        """
        return pd.DataFrame.from_dict([row._asdict() for row in self.executed]).to_csv(path, header=alias, index=False)





# q = 'table hechos limit 2;'
# p = Records(conn_dict, 'hechos', q)
#
# cs = p.a_csv('prueba.csv')

