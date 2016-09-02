import sys
import psycopg2
from psycopg2 import extras
import pandas as pd
from yaml import load
from designer.gui import QtGui
from mensajes import MessageCritical

"""
Abrir el archivo config.yml donde estan los dato de
conexion a la db. El except ejecuta un mensaje critico.
"""
try:
    with open('config.yml', 'r') as fh:
        config = load(fh)
except FileNotFoundError as e:
    config = None
    app = QtGui.QApplication(sys.argv)
    m = MessageCritical('Error', e.__str__())
    m.exec_()

conn_dict = config['conn_dict']


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

    def a_csv(self, path, columns=None, alias=None):
        """
        Devuelve un csv

        :param: path: path donde se va a grabar el csv
        :param: columns: iterable con los nombres de las columnas
                         como figuran en la base de datos
        :param: alias: iterable con los alias de las columnas en el orden deseado
        :return: csv
        """
        return pd.DataFrame.from_dict([row._asdict() for row in self.executed]).to_csv(path, header=alias,
                                                                                       columns=columns, index=False)


# q = 'table hechos limit 5;'
#
# rec = Records(conn_dict, 'hechos', q)
# rec1 = rec.a_ord_dicts()
#
# print([x['id'] for x in rec1])