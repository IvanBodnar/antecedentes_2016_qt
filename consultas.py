from database import Records, conn_dict


def make_query(coords, distancia, path):
    y, x = coords.strip().split(',')
    table = 'hechos'
    distancia = distancia
    campos = ['fecha', 'hora', 'direccion_normalizada', 'anio', 'tipo_colision', 'causa', 'tipo_recod']
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

    param = campos + [x, y, distancia]

    r = Records(conn_dict, table, query_diametro.format(*param))

    r.a_csv(path, columns=campos, alias=alias)

