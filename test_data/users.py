import mysql.connector

from helpers import create_random_user


def get_user():
    connection = mysql.connector.connect(
        user='bn_opencart',
        host='127.0.0.1',
        database='bitnami_opencart'
    )
    return create_random_user(connection), "test"
