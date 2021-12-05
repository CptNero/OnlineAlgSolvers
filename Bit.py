from dataclasses import dataclass


@dataclass
class Element:
    value: int
    bit: bool


def BIT(input_list, toAccess):
    for idx, elem in enumerate(input_list):
        if elem.value == toAccess:
            print(input_list, f'Access: {toAccess}, Cost:{idx + 1}')

            elem.bit = not elem.bit
            if elem.bit is True:
                input_list[0].value, input_list[idx].value = input_list[idx].value, input_list[0].value
            return idx + 1


input_list = [Element(1, False), Element(2, False), Element(3, False), Element(4, True), Element(5, True)]
access_list = [4, 2, 3, 2, 1, 4, 2, 5]

cost_sum = 0

for access in access_list:
    cost_sum += BIT(input_list, access)

print(f'{input_list} Cost sum: {cost_sum}')