

# DC az egyenesen k gyengén versenyképes
# Az opt <= beta + c(A(theta))/k
def DoubleCoverage(config, input_list, lazy=False):
    cost_sum = 0

    for input in input_list:
        maxV = max(config)
        minV = min(config)

        if input in config:
            print(f'{input} is already in {config}')
        elif input < minV:
            for idx in range(0, len(config)):
                if config[idx] == minV:
                    cost = minV - input
                    cost_sum += cost
                    print(f'Swapped {config[idx]} with {input}, cost: {cost}')
                    config[idx] = input
                    break
        elif input > maxV:
            for idx in range(0, len(config)):
                if config[idx] == maxV:
                    cost = input - maxV
                    cost_sum += cost
                    print(f'Swapped {config[idx]} with {input}, cost: {cost}')
                    config[idx] = input
                    break
        elif maxV > input > minV:
            for idx in range(1, len(config)):
                if config[idx - 1] < input < config[idx]:
                    left_distance = input - config[idx - 1]
                    right_distance = config[idx] - input
                    smaller_distance = min(left_distance, right_distance)

                    if smaller_distance == right_distance:
                        cost = left_distance if not lazy else right_distance
                        cost_sum += cost
                        print(f'Swapped {config[idx]} with {input}, Cost: {cost}')
                        config[idx] = input
                        if not lazy:
                            config[idx - 1] += right_distance
                    elif smaller_distance == left_distance:
                        cost = right_distance if not lazy else left_distance
                        cost_sum += cost
                        print(f'Swapped {config[idx - 1]} with {input}, Cost: {cost}')
                        config[idx - 1] = input
                        if not lazy:
                            config[idx] -= left_distance

                    break
        print(config)
    return cost_sum


# config = [0, 3, 5]
# input_list = [2, 3, 0, 2, 0, 2, 5]

config = [1, 4, 10]
input_list = [6, 9, 0, 3, 7]
print(config)
cost_sum = DoubleCoverage(config, input_list, False)
print(f'Cost sum is {cost_sum}')

