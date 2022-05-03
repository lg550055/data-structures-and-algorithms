import pytest
from code_challenges.stack_queue_animal_shelter import AnimalShelter, Dog, Cat


def test_single_cat():
    shelter = AnimalShelter()
    cat = Cat()
    shelter.enqueue(cat)
    actual = shelter.dequeue("cat")
    expected = cat
    assert actual == expected


def test_single_dog():
    shelter = AnimalShelter()
    dog = Dog()
    shelter.enqueue(dog)
    actual = shelter.dequeue("dog")
    expected = dog
    assert actual == expected


def test_dog_preferred_but_cat_in_front():
    shelter = AnimalShelter()
    cat = Cat()
    dog = Dog()
    shelter.enqueue(cat)
    shelter.enqueue(dog)
    actual = shelter.dequeue("dog")
    expected = dog
    assert actual == expected


def test_dog_then_cat():
    shelter = AnimalShelter()
    cat = Cat()
    dog = Dog()
    shelter.enqueue(dog)
    shelter.enqueue(cat)
    shelter.dequeue("dog")
    actual = shelter.dequeue("cat")
    expected = cat
    assert actual == expected


def test_bad_pref():
    shelter = AnimalShelter()
    cat = Cat()
    dog = Dog()
    shelter.enqueue(dog)
    shelter.enqueue(cat)
    shelter.dequeue("dog")
    actual = shelter.dequeue("lizard")
    expected = None
    assert expected == actual


def test_2cats_dog_cat_dog():
    shelter = AnimalShelter()
    cat1 = Cat()
    cat2 = Cat()
    dog1 = Dog()
    cat3 = Cat()
    dog2 = Dog()
    shelter.enqueue(cat1)
    shelter.enqueue(cat2)
    shelter.enqueue(dog1)
    shelter.enqueue(cat3)
    shelter.enqueue(dog2)
    shelter.dequeue("dog")
    actual = shelter.dequeue("cat")
    expected = cat1
    assert actual == expected
