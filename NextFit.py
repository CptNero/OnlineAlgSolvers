from dataclasses import dataclass


@dataclass
class Bin:
    items: list
    value_sum: float
    open: bool


def NextFit(items):
    bins = [Bin([], 0.0, True)]

    for i, item in enumerate(items):
        for idx, bin in enumerate(bins):
            if bin.open is True:
                if bin.value_sum + item >= 1.0:
                    bin.open = False
                    bins.append(Bin([item], item, True))
                    break
                bin.items.append(item)
                bin.value_sum += item
                break

    return bins


items = [0.9, 0.2, 0.9, 0.2, 0.9, 0.5, 0.4]
bins = NextFit(items)

for idx, bin in enumerate(bins):
    print(f'#{idx}, {bin}')