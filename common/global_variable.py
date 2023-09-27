import json
from config.all_path import get_case_data_path

customize_dict = {
    'restime_now': None
}


def global_end():
    path = get_case_data_path('variable.json')
    with open(path, 'w', encoding='utf-8') as variable_wf:
        json.dump(customize_dict, variable_wf)

if __name__ == '__main__':
    print(customize_dict)
