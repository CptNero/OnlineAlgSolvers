from dataclasses import dataclass


@dataclass
class Bin:
    items: list
    value_sum: float

# optimumban van
def FirstFit(items):
    bins = [Bin([], 0.0)]

    for i, item in enumerate(items):
        fits = False
        for idx, bin in enumerate(bins):
            if item + bin.value_sum <= 1.0:
                bins[idx].items.append(item)
                bins[idx].value_sum += item
                fits = True
                break
        if not fits:
            bins.append(Bin([item], item))

    return bins


items = [0.5, 0.6, 0.3, 0.4, 0.2, 0.5, 0.4]
bins = FirstFit(items)

for idx, bin in enumerate(bins):
    print(f'Bin #{idx} Value sum: {bin.value_sum} {bin.items}')