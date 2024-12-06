class FlatIterator:
    def __init__(self, list_of_list):
        # Сохраняем исходный список, преобразуя его в стек
        self.stack = [list_of_list]

    def __iter__(self):
        # Итератор возвращает сам себя
        return self

    def __next__(self):
        # Работаем до тех пор, пока есть элементы в стеке
        while self.stack:
            current = self.stack.pop()  # Берём верхний элемент стека
            print("Command pop:",current)

            if isinstance(current, list):
                # Если это список, то добавляем его элементы обратно в стек в обратном порядке,
                # чтобы первый элемент списка оказался сверху стека.
                for item in reversed(current):
                    self.stack.append(item)
            else:
                # Если это не список, значит это обычный элемент - его и возвращаем.
                print("Current element:", current)  # Для отладки: вывод текущего элемента
                print("Stack after pop and processing:", list(self.stack))  # Для отладки: состояние стека
                return current

        # Если стек пуст, значит элементов больше нет
        raise StopIteration


def test_3():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()