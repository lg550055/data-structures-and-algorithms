import pytest
from linked_list.linked_list import LinkedList


def test_exists():
    assert LinkedList

def test_instantiate():
    assert LinkedList()

def test_empty_head():
    linked = LinkedList()
    assert linked.head is None

def test_populated_head():
    linked = LinkedList()
    linked.insert("apple")
    assert linked.head.value == "apple"

# custom test -delete
def test_new_head_inserted_into_not_empty_list():
    linked = LinkedList()
    linked.insert('apple')
    linked.insert('banana')
    assert linked.head.value == 'banana'


@pytest.mark.skip("TODO")
def test_to_string_empty():
    linked_list = LinkedList()
    assert str(linked_list) == "NULL"


@pytest.mark.skip("TODO")
def test_to_string_single():
    linked_list = LinkedList()
    linked_list.insert("apple")
    assert str(linked_list) == "{ apple } -> NULL"


@pytest.mark.skip("TODO")
def test_to_string_double():
    linked_list = LinkedList()
    linked_list.insert("apple")
    assert str(linked_list) == "{ apple } -> NULL"
    linked_list.insert("banana")
    assert str(linked_list) == "{ banana } -> { apple } -> NULL"

def test_includes_true():
    linked_list = LinkedList()
    linked_list.insert("apple")
    linked_list.insert("banana")
    assert linked_list.includes("apple")

def test_includes_false():
    linked_list = LinkedList()
    linked_list.insert("apple")
    linked_list.insert("banana")
    assert not linked_list.includes("cucumber")
