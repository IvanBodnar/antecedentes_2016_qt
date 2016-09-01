from database import Records, conn_dict

x, y = '-58.362289, -34.644632'.strip().split(',')
table = 'hechos'
distancia = 300
campos = ('fecha', 'hora', 'direccion_normalizada', 'anio')
alias = ('fecha', 'hora', 'lugar', 'año')
path = 'pedidos'
nombre_proyecto = 'tal_y_tal'

query_diametro = '''
    select {}, {}, {}, {} from hechos
    where ST_DWithin(ST_Transform(geom, 98334),
    ST_Transform(ST_SetSRID(ST_MakePoint({}, {})
    , 4326), 98334), {})
    order by anio;
'''

param = campos + (x, y, distancia)
r = Records(conn_dict, table, query_diametro.format(*param))

r.a_csv('{}/{}.csv'.format(path, nombre_proyecto), alias=alias)
