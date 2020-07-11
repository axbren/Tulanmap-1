import web

'''
Configurar los parametros para una base de datos localhost
'''
# Base de datos local
db_host = 'localhost'
db_name = 'demo_google'
db_user = 'demo_google'
db_pw = '1234'
db_port = 3306

db_localhost = web.database(
    dbn = 'mysql',
    host = db_host,
    db = db_name,
    user = db_user,
    pw = db_pw,
    port = db_port
    )

'''
Configurar los parametros para una base de datos remota
'''
# Base de datos en la nube
db_host_cloud = 'remote_server'
db_name_cloud = 'remote_db_name'
db_user_cloud = 'remote_user'
db_pw_cloud = 'remote_password'
db_port_cloud = 3306

db_cloud = web.database(
    dbn = 'mysql',
    host = db_host_cloud,
    db = db_name_cloud,
    user = db_user_cloud,
    pw = db_pw_cloud,
    port = db_port_cloud
    )
