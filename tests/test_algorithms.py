import examples.algorithms

def test_get_missing_numbers():
    assert examples.algorithms.get_missing_numbers([1,2,4,5,6], 6) == 3
    assert examples.algorithms.get_missing_numbers([1,3,5,6,7,9], 10) == [2, 4, 8, 10]
