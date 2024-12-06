import types


def flat_generator(nested_list):
    for item in nested_list:
        if isinstance(item, list):  # Если элемент — это список, рекурсивно обрабатываем его
            yield from flat_generator(item)
        else:
            yield item  # Если элемент не список, возвращаем его через yield


def test_2():
    nested_list = [
        ['a', ['b', 'c']],
        ['d', ['e', ['f', 'h']], False],
        [1, [2, [None]]]
    ]

    expected_result = ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    for flat_iterator_item, check_item in zip(
            flat_generator(nested_list),
            expected_result
    ):
        assert flat_iterator_item == check_item

    assert list(flat_generator(nested_list)) == expected_result

    assert isinstance(flat_generator(nested_list), types.GeneratorType)


if __name__ == '__main__':
    test_2()