from dataclasses import dataclass


@dataclass
class Bin:
    category: int
    items: list
    value_sum: float


def CalcCategory(item, k):
    for idx in range(1, k + 1):
        a = 1 / (idx + 1)
        b = 1 / idx
        if a < item <= b:
            return idx
    return k

# Tujduk, h 1.69 kompetitiv tehát
# Annyit tudunkk, h legalább 3 ládát fog használni, mert kicsi átrendezéssel látható
def HarmonicFit(items, k):
    bins = []

    for i, item in enumerate(items):
        category = CalcCategory(item, k)

        fitting_bin = next((bin for bin in bins if bin.category == category and bin.value_sum + item <= 1.0), None)

        if fitting_bin is None:
            bins.append(Bin(category, [item], item))
        else:
            fitting_bin.items.append(item)
            fitting_bin.value_sum += item
    return bins


input_list = [0.4, 0.2, 0.3, 0.6, 0.4, 0.4, 0.2, 0.3]
k = 4

bins = HarmonicFit(input_list, k)
bins.sort(key=lambda bin: bin.category)
for idx, bin in enumerate(bins):
    print(f'Bin #{idx} {bin}')