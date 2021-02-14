def flat_dict(flat_data: dict, data: dict, separator: str, previous_key = None):
    for key, value in data.items():
        if previous_key:
            key = '{}{}{}'.format(previous_key, separator, key)
        if isinstance(value, dict):
            flat_dict(flat_data, value, '_', key)
        else:
            flat_data.__setitem__(key, value)



data = {
    'member_id': '2228560-01',
    'member_name': 'Clay, Brandon',
    'check_in': {
        'date': '2021-01-06T01:51:36.7670000Z',
        'location': {
            'id': 'B716',
            'type': 'branch',
            'name': 'Y at Work - Norton Hospital Downtown'
        }
    }
}


flat_data = {}
flat_dict(flat_data, data, '_')

print(flat_data)
