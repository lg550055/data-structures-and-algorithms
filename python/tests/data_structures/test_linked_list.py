import pytest
from data_structures.linked_list import LinkedList


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

# custom test
def test_new_head_inserted_into_not_empty_list():
    linked = LinkedList()
    linked.insert('apple')
    linked.insert('banana')
    assert linked.head.value == 'banana'

def test_to_string_empty():
    linked_list = LinkedList()
    assert str(linked_list) == "NULL"

def test_to_string_single():
    linked_list = LinkedList()
    linked_list.insert("apple")
    assert str(linked_list) == "{ apple } -> NULL"

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

# custom tests to test: append, insert_before and insert_after methods

# test add node to the end of the list
def test_append():
    linked = LinkedList()
    linked.insert(2)
    linked.insert(3)
    linked.insert(1)
    linked.append(5)
    actual = str(linked)
    expected = "{ 1 } -> { 3 } -> { 2 } -> { 5 } -> NULL"
    assert actual == expected, actual # assert 2nd optional parameter displays if false

def test_append_to_empty_list():
    linked = LinkedList()
    linked.append(1)
    assert str(linked) == "{ 1 } -> NULL"

def test_insert_before_middle_of_list():
    linked = LinkedList()
    linked.insert(2)
    linked.insert(3)
    linked.insert(1)
    linked.insert_before(3,5)
    actual = str(linked)
    expected = "{ 1 } -> { 5 } -> { 3 } -> { 2 } -> NULL"
    assert actual == expected, actual

def test_insert_before_head():
    linked = LinkedList()
    linked.insert(2)
    linked.insert(3)
    linked.insert(1)
    linked.insert_before(1,5)
    actual = str(linked)
    expected = "{ 5 } -> { 1 } -> { 3 } -> { 2 } -> NULL"
    assert actual == expected, actual

def test_insert_before_first_occurrence():
    linked = LinkedList()
    linked.insert(2)
    linked.insert(2)
    linked.insert(1)
    linked.insert_before(2,5)
    actual = str(linked)
    expected = "{ 1 } -> { 5 } -> { 2 } -> { 2 } -> NULL"
    assert actual == expected, actual

def test_insert_before_item_not_in_list():
    linked = LinkedList()
    linked.insert(2)
    linked.insert(3)
    linked.insert(1)
    actual = linked.insert_before(4,5)
    expected = False
    assert actual == expected, actual
    assert str(linked) == "{ 1 } -> { 3 } -> { 2 } -> NULL"

def test_insert_after_middle_of_list():
    linked = LinkedList()
    linked.insert(2)
    linked.insert(3)
    linked.insert(1)
    linked.insert_after(3,5)
    actual = str(linked)
    expected = "{ 1 } -> { 3 } -> { 5 } -> { 2 } -> NULL"
    assert actual == expected, actual

def test_insert_after_last():
    linked = LinkedList()
    linked.insert(2)
    linked.insert(3)
    linked.insert(1)
    linked.insert_after(2,5)
    actual = str(linked)
    expected = "{ 1 } -> { 3 } -> { 2 } -> { 5 } -> NULL"
    assert actual == expected, actual

def test_insert_after_first_occurrence():
    linked = LinkedList()
    linked.insert(2)
    linked.insert(2)
    linked.insert(1)
    linked.insert_after(2,5)
    actual = str(linked)
    expected = "{ 1 } -> { 2 } -> { 5 } -> { 2 } -> NULL"
    assert actual == expected, actual

def test_insert_after_item_not_in_list():
    linked = LinkedList()
    linked.insert(2)
    linked.insert(3)
    linked.insert(1)
    actual = linked.insert_after(4,5)
    expected = None
    assert actual == expected, actual
    assert str(linked) == "{ 1 } -> { 3 } -> { 2 } -> NULL"
