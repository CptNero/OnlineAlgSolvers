from dataclasses import dataclass


@dataclass
class Bin:
    items: list
    value_sum: float


def FindBestBin(bins, item):
    bins.sort(key=lambda bin: bin.value_sum, reverse=True)

    for bin in bins:
        if bin.value_sum + item <= 1.0:
            return bin

    return None


def BestFit(items):
    bins = [Bin([], 0.0)]

    for i, item in enumerate(items):

        best_bin = FindBestBin(bins, item)
        if best_bin is not None:
            best_bin.items.append(item)
            best_bin.value_sum += item
        else:
            bins.append(Bin([item], item))

    return bins


items = [0.5, 0.6, 0.3, 0.4, 0.2, 0.5, 0.4]
bins = BestFit(items)

for idx, bin in enumerate(bins):
    print(f'Bin #{idx} Value sum: {bin.value_sum} {bin.items}')