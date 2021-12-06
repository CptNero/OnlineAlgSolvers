from dataclasses import dataclass


@dataclass
class Item:
    x: float
    y: float


@dataclass
class Shelf:
    height_class: float
    width_sum: float
    items: list


def GetFirstFittingShelf(shelves, item, r):
    shelf_classes = []
    shelves.sort(key=lambda shelf: shelf.height_class)

    for i in reversed(range(0, 4)):
        shelf_classes.append(pow(r, i))

    fitting_shelf_class = next((shelf_class for shelf_class in shelf_classes if shelf_class > item.y))

    for shelf in shelves:
        if shelf.height_class == fitting_shelf_class and shelf.width_sum + item.x <= 1.0:
            return shelf, fitting_shelf_class

    return None, fitting_shelf_class

# az opt summa vi * hi
# az opt legalább annyi mint a legmagasabb tárgy
def NextFitShelf(items, r):
    shelves = []

    for item in items:
        fitting_shelf, fitting_shelf_class = GetFirstFittingShelf(shelves, item, r)

        if fitting_shelf is None:
            shelves.append(Shelf(fitting_shelf_class, item.x, [item]))
        else:
            fitting_shelf.items.append(item)
            fitting_shelf.width_sum += item.x

    return shelves


items = [
    Item(0.4, 0.6),
    Item(0.3, 0.3),
    Item(0.5, 0.4),
    Item(0.1, 0.7),
    Item(0.7, 0.1),
    Item(0.3, 0.4),
]

shelves = NextFitShelf(items, 0.5)
shelves.sort(key=lambda shelf: shelf.height_class, reverse=True)
for shelf in shelves:
    print(shelf)
