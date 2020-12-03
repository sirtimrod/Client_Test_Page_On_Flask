def del_id_in_json_file(dicts_in_main_list):
    for child_dicts in dicts_in_main_list:
        child_dicts.pop('id', None)
        if child_dicts['child'] is not None:
            del_id_in_json_file(child_dicts['child'])


def del_id(main_list):
    for dicts_in_main_list in main_list:
        dicts_in_main_list.pop('id', None)
        if dicts_in_main_list['child'] is not None:
            del_id_in_json_file(dicts_in_main_list['child'])
