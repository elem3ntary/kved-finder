# Kved finder

A tool that allows you to find a kved tree for the specific kved.

## Usage

```bash
python3 main.py 01.11
```
The result will be saved to kved_result.json
Example output
```json
{
  "name": "Вирощування зернових культур (крім рису), бобових культур і насіння олійних культур",
  "type": "class",
  "parent": {
    "name": "Вирощування однорічних і дворічних культур",
    "type": "group",
    "num_children": 7,
    "parent": {
      "name": "Сільське господарство, мисливство та надання пов'язаних із ними послуг",
      "type": "division",
      "num_children": 7,
      "parent": {
        "name": "Сільське господарство, лісове господарство та рибне господарство",
        "type": "section",
        "num_children": 3
      }
    }
  }
}
```
