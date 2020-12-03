def add_components(connection, attribute_id, chunk):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM test")
    attribute_name = cursor.fetchall()
    for att_name in attribute_name:
        if attribute_id == att_name[0]:
            chunk['component'].append(att_name[1].rstrip())


def search_attribute_id(connection, chunk):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM test")
    attributes = cursor.fetchall()
    for attribute in attributes:
        if chunk['id'] == attribute[0]:
            add_components(connection, attribute[1], chunk)


def req_get_components(connection, chunk):
    for child_chunk in chunk:
        if len(child_chunk['child']) != 0:
            req_get_components(connection, child_chunk['child'])
        else:
            search_attribute_id(connection, child_chunk)


def get_components(connection, main_list):
    for chunk in main_list:
        if len(chunk['child']) != 0:
            req_get_components(connection, chunk['child'])
        else:
            search_attribute_id(connection, chunk)