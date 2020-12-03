def recursively_adding_childs(child_list, row_parent, name, row_parent_id, id_):
    for item_list in child_list:
        if item_list["name"] == row_parent and item_list["id"] == row_parent_id:
            item_list["child"].append({'id': id_, 'name': name, 'child': [], 'component': []})
        else:
            recursively_adding_childs(item_list['child'], row_parent, name, row_parent_id, id_)


def make_json(rows, rows_parent, main_list):
    for row in rows:
        if row[2] is None:
            main_list.append({'id': row[0], 'name': row[1], 'child': [], 'component': []})
        else:
            for row_parent in rows_parent:
                if row[2] == row_parent[0]:
                    for item_list in main_list:
                        if item_list["name"] == row_parent[1] and item_list["id"] == row_parent[0]:
                            item_list["child"].append({'id': row[0], 'name': row[1], 'child': [], 'component': []})
                        else:
                            recursively_adding_childs(item_list["child"], row_parent[1], row[1], row_parent[0], row[0])
