def BestFit(items):
    bins = [0.0]

    for i, item in enumerate(items):
        fits = False
        for idx, bin in enumerate(bins):
            if item + bin <= 1.0:
                bins[idx] += item
                fits = True
                break
        if not fits:
            bins.append(0.0 + item)
        print(f'Item #{i} Value: {item}', bins)

    return bins


items = [0.5, 0.6, 0.3, 0.4, 0.2, 0.5, 0.4]
bins = BestFit(items)

print(bins)