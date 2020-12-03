from app import app
import pymysql
from make_json_to_display_on_the_page import formation_and_sending_json_file


def db_connector(user_data):
    try:
        connection = pymysql.connect(host=user_data['host'],
                                     port=int(user_data['port']),
                                     user=user_data['name'],
                                     password=user_data['passw'],
                                     db=user_data['db_name'])
    except Exception as e:
        print(e)
    else:
        return formation_and_sending_json_file(connection)