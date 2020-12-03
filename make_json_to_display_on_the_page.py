from flask import render_template
from form_json import make_json, recursively_adding_childs
from del_folders_id import del_id, del_id_in_json_file
from get_components_attributes import get_components
import json
from app import app


def formation_and_sending_json_file(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM test")
    rows = rows_parent = cursor.fetchall()
    main_list = []
    make_json(rows, rows_parent, main_list)
    get_components(connection, main_list)
    del_id(main_list)
    main_list = json.dumps(main_list)
    return render_template('tree.html', data_of_json=main_list)
