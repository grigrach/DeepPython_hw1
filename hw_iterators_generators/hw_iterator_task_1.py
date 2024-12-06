class FlatIterator:
    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.outer_index = 0
        self.inner_index = 0
        return self

    def __next__(self):
        # Если мы вышли за пределы списка списков, бросаем исключение
        if self.outer_index >= len(self.list_of_list):
            raise StopIteration

        # Пока не найдём элемент в текущем вложенном списке
        while self.outer_index < len(self.list_of_list):
            # Если внутренний индекс выходит за пределы текущего списка
            if self.inner_index >= len(self.list_of_list[self.outer_index]):
                self.outer_index += 1
                self.inner_index = 0
                continue

            item = self.list_of_list[self.outer_index][self.inner_index]
            self.inner_index += 1
            return item

        # Если вышли из цикла без возврата элемента, завершаем итерацию
        raise StopIteration


def test_1():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    #print(list(FlatIterator(list_of_lists_1)))
    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()