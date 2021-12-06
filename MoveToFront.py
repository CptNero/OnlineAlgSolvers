


# Mivel 2 komptetitív így tudjuk, h pl ha 30 az eredmény akkor az opt >= 15
# Mást nem tudunk kiszámolni papíron
def MoveToFront(input_list, toAccess):
    for idx, elem in enumerate(input_list):
        if elem == toAccess:
            print(input_list, f'Access: {toAccess}, Cost:{idx + 1}')
            input_list[0], input_list[idx] = input_list[idx], input_list[0]
            return idx + 1


input_list = [1, 2, 3, 4, 5]
access_list = [4, 2, 3, 2, 1, 4, 2, 5]

cost_sum = 0

for access in access_list:
    cost_sum += MoveToFront(input_list, access)

print(f'{input_list} Cost sum: {cost_sum}')