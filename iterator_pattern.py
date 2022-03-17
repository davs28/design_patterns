from __future__ import annotations
from collections.abc import Iterable, Iterator
from typing import Any, List


class AlphabeticalOrderIterator(Iterator):

    position: int = None

    # This attribute indicates the traversal direction.
    reverse: bool = False

    def __init__(self, collection: WordsCollection, reverse: bool = False) -> None:
        self.collection = collection

        self.reverse = reverse
        if reverse:
            self.position = -1
        else: 
            self.position = 0

    def __next__(self):
        try:
            value = self.collection[self.position]

            if self.reverse:
                self.position += -1
            else: 
                self.position += 1

        except IndexError:
            raise StopIteration()

        return value


class WordsCollection(Iterable):

    def __init__(self, collection: List[Any] = []) -> None:
        self._collection = collection

    def __iter__(self) -> AlphabeticalOrderIterator:
        return AlphabeticalOrderIterator(self._collection)

    def get_reverse_iterator(self) -> AlphabeticalOrderIterator:
        return AlphabeticalOrderIterator(self._collection, True)

    def add_item(self, item: Any):
        self._collection.append(item)


if __name__ == "__main__":
    """Main function"""

    collection = WordsCollection()
    collection.add_item("First")
    collection.add_item("Second")
    collection.add_item("Third")

    print("Straight traversal:")
    print("\n".join(collection))
    print("")

    print("Reverse traversal:")
    print("\n".join(collection.get_reverse_iterator()), end="")
    
    
