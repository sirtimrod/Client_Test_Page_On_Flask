from flask import render_template, request
from app import app
from do_sql_connection import db_connector


@app.route('/', methods=['GET', 'POST'])
def get_user_data_from_page():
    if request.method == 'POST':
        return db_connector(request.form)
    return render_template('index.html')
