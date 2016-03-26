from two_way import Mapping
import pytest


def setup_tests():
    global my_dict
    my_dict = {
        "a": 1,
        "b": 2,
        "c": 3
    }


def test_init():
    my_mapping = Mapping(my_dict)

    for key, value in my_dict.iteritems():
        assert my_mapping.get_by_key(key) == value
        assert my_mapping.get_by_value(value) == key
    assert my_mapping.count() == len(my_dict)


def test_set():
    my_mapping = Mapping()

    my_mapping.set("a", 1)
    assert my_mapping.count() == 1
    assert my_mapping.get_by_key("a") == 1
    assert my_mapping.get_by_value(1) == "a"

    my_mapping.set("a", 2)
    assert my_mapping.count() == 1
    assert my_mapping.get_by_key("a") == 2
    assert my_mapping.get_by_value(2) == "a"

    my_mapping.set("b", 2)
    assert my_mapping.count() == 1
    assert my_mapping.get_by_key("b") == 2
    assert my_mapping.get_by_value(2) == "b"

    with pytest.raises(ValueError):
        my_mapping.set("b", 2)
    assert my_mapping.count() == 1
    assert my_mapping.get_by_key("b") == 2
    assert my_mapping.get_by_value(2) == "b"


def test_remove():
    my_mapping = Mapping(my_dict)

    my_mapping.remove_by_key("a")
    assert my_mapping.count() == 2
    assert "a" not in my_mapping.dict
    assert 1 not in my_mapping.rdict

    my_mapping.remove_by_value(2)
    assert my_mapping.count() == 1
    assert "b" not in my_mapping.dict
    assert 2 not in my_mapping.rdict


if __name__ == "__main__":
    setup_tests()
    test_init()
    test_set()
    test_remove()
