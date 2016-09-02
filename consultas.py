from database import Records, conn_dict
from mensajes import MessageCritical, MessageInfo
from psycopg2 import OperationalError


def make_query(coords, distancia, path):

    try:
        y, x = coords.strip().split(',')
    except ValueError as e:
        y, x = None, None
        m = MessageCritical('Coordenadas Inválidas', e.__str__())
        m.exec_()
    table = 'hechos'
    distancia = distancia
    campos = ('fecha', 'hora', 'direccion_normalizada', 'anio', 'tipo_colision', 'causa', 'tipo_recod')
    alias = ('fecha', 'hora', 'lugar', 'año', 'tipo de colision', 'causa', 'tipo de usuario')
    path = path

    query_diametro = '''
        select {}, {}, {}, {}, {}, {}, {} from hechos
        join victimas
        on hechos.id = victimas.id_hecho
        where ST_DWithin(ST_Transform(geom, 98334),
        ST_Transform(ST_SetSRID(ST_MakePoint({}, {})
        , 4326), 98334), {})
        and anio >= 2010
        order by anio;
    '''

    param = campos + (x, y, distancia)

    try:
        r = Records(conn_dict, table, query_diametro.format(*param))
        r.a_csv(path, columns=campos, alias=alias)
    except KeyError as e:
        m = MessageCritical('Ingrese Distancia Válida', e.__str__())
        m.exec_()
    except FileNotFoundError as e:
        m = MessageCritical('Ingrese Nombre de Archivo Válido', e.__str__())
        m.exec_()
    except OperationalError as e:
        m = MessageCritical('Error de Conexión a la Base de Datos', e.__str__())
        m.exec_()
    else:
        m = MessageInfo('Archivo Creado')
        m.exec_()



