from operator import index
import pytest
from data_structures.hashtable import Hashtable


def test_exists():
    assert Hashtable


def test_hash_in_range():
    ht = Hashtable()
    index = ht.hash('cat')
    assert 0 <= index < ht.size
    index = ht.hash('roger')
    assert 0 <= index < ht.size
    index = ht.hash('zxyyxz')
    assert 0 <= index < ht.size


def test_get_apple():
    ht = Hashtable()
    ht.set("apple", "Used for apple sauce")
    actual = ht.get("apple")
    expected = "Used for apple sauce"
    assert actual == expected


def test_get_keys():
    ht = Hashtable()
    ht.set("ahmad", 30)
    ht.set("silent", True)
    ht.set("listen", "to me")
    actual = ht.keys()
    expected = ["ahmad", "listen", "silent"]
    assert actual == expected


def test_get_fake():
    ht = Hashtable()
    ht.set("ahmad", 30)
    ht.set("silent", True)
    ht.set("listen", "to me")
    actual = ht.get('fake')
    expected = None
    assert actual == expected


def test_contains_silent():
    ht = Hashtable()
    ht.set("ahmad", 30)
    ht.set("silent", True)
    ht.set("listen", "to me")
    actual = ht.contains('silent')
    expected = True
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_collisions():
    ht = Hashtable()
    ht.set("cat", "Josie")
    ht.set("act", "A Contemporary Theater")
    ht.set("tac", "Taco Tuesday")

    assert ht.get("cat") == "Josie"
    assert ht.get("act") == "A Contemporary Theater"
    assert ht.get("tac") == "Taco Tuesday"
