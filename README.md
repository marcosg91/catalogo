# catalogo
sitio de catalogos de productos desarrollado en el informatorio comision 3 2022

para levantar el proyecto hay que crear un archivo .env al mismo nivel del setting con la siguiente estructura:

metodo 1:
NAME=ssssss
USER=ssssss
PASSWORD=ss
HOST=ssssss

metodo 2:
crear el archivo local.py al mismo nivel que base.py en settings (catalogo/catalogo/settings), con la siguiente estructura: 

###########################################################
from .base import *
DATABASES = {
    'default': {
        'ENGINE': "mssql",
        'NAME':"catalogo",
        'USER': "sa",
        'PASSWORD': "123",
        'HOST': "DESKTOP-B6JPFO0",
        'OPTIONS':{
            'driver':'ODBC Driver 17 for SQL Server'
        }
    }
}
###########################################################