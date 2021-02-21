import json
import argparse
import os.path


def read_file(file_path='kved.json') -> dict:
    '''
    Reads json file and returns it parsed
    '''
    current_dir = os.path.dirname(__file__)
    with open(os.path.join(current_dir, file_path)) as f:
        return json.load(f)


def find(func, values):
    '''
    Returns first value in values that matches a criterion
    '''
    for value in values:
        if func(value):
            return value


def parse_kved(classCode: str):
    '''
    Parses kved tree and writes results to kved_result.json
    '''
    divisionCode = classCode.split('.')[0]
    groupCode = classCode[:-1]

    kved_obj = read_file()
    for section in kved_obj['sections'][0]:
        divisions = section['divisions']
        division = find(lambda i: i['divisionCode'] == divisionCode, divisions)

        if not division:
            continue

        groups = division['groups']
        group = find(lambda i: i['groupCode'] == groupCode, groups)

        if not group:
            continue

        classes = group['classes']
        class_name = find(lambda i: i['classCode'] == classCode, classes)['className']

        if class_name:
            break

    result = {
        "name": class_name,
        "type": "class",
        "parent": {
            "name": group['groupName'],
            "type": "group",
            "num_children": len(group['classes']),
            "parent": {
                "name": division['divisionName'],
                "type": "division",
                "num_children": len(division['groups']),
                "parent": {
                    "name": section['sectionName'],
                    "type": "section",
                    "num_children": len(section['divisions'])
                }
            }
        }
    }
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('kved', help='kved you want to find (example: 01.11)', type=str)
    args = parser.parse_args()

    result = parse_kved(args.kved)
    with open('kved_result.json', 'w') as file:
        json.dump(result, file, indent=2, ensure_ascii=False)
