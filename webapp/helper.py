from django.db import connection
import re


def db_table_exists(table_name):
    return table_name in connection.introspection.table_names()


def validatorPost(request, validate_array):
    default = {
        'number': (r'^\s*(?!\.)[\.\d]+\s*$', ' trebuie sa fie un numar.'),
        'required': (r'^\s*.+\s*$', ' trebuie sa nu fie goala.'),
        'string': (r'^\s*(?!\d+)[\w\d]+\s*$', ' trebuie sa fie  un sir de caractere nu un singur numar.')
    }
    error_message = {}
    values = {}
    for input_name in validate_array:
        if input_name not in values:
            values[input_name] = request.POST[input_name]
        for restrict in (validate_array[input_name]).split('|'):
            if restrict not in default or re.search(default[restrict][0], values[input_name], re.I):
                continue
            if input_name not in error_message:
                error_message[input_name] = set()
            error_message[input_name].add(str(input_name) + default[restrict][1])
    return error_message, values

