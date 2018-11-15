import mysql.connector
import os

from .config import INIT_ENV

INIT_ENV()

def connectdb():
    mydb = mysql.connector.connect(
        host=os.environ['host_name'],
        user=os.environ['user'],
        passwd=os.environ['password']
    )

    return mydb