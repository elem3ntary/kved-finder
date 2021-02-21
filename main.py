import json
import pprint
import functools.


def read_file(file_path='kved.json'):
    with open(file_path) as f:
        return json.loads(f.read())


def get_section_and_division(kved_obj, divisionCode):
    for section in kved_obj['sections'][0]:
        print(section)
        for division in section['divisions']:
            if division['divisionCode'] == divisionCode:
                return section, division


def get_group(groups, groupCode):
    for group in groups:
        if group['groupCode'] == groupCode:
            return group


def get_class(classes, classCode):
    for item in classes:
        if item['classCode'] == classCode:
            return item


def find(func, values):
    for i in values:
        if func(i):
            return i


def parse_kved(classCode: str):
    divisionCode = classCode.split()[0]
    groupCode = classCode[:-1]

    # value = find(lambda x: x['classCode'] == classCode, list1)

    kved_obj = read_file()
    value = (i break
             if i == classCode for i in kvedobj)
    kved_section = get_section_and_division(kved_obj, divisionCode)
    print(kved_section)
    kved_group = get_group(kved_division['groups'], groupCode)
    kved_class = get_class(kved_group['classes'], classCode)

    data = [
        ('section', kved_section['sectionName'], len(kved_section['divisions'])),
        ('division', kved_division['divisionName'], len(kved_division['groups'])),
        ('group', kved_group['groupName'], len(kved_group['classes'])),
        ('class', kved_class['className'])
    ]
    block = None
    start_block = dict()
    for idx, item in enumerate(reversed(data)):
        if idx == 0:
            start_block = {
                'type': item[0],
                'name': item[1]
            }
            block = start_block
        if item[2]:
            block['num_children'] = item[2]
        if idx != len(data) - 1:
            block['parent'] = dict()
            block = block['parent']
    print(start_block)


if __name__ == '__main__':
    parse_kved('01.10')
