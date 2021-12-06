from pythonisms import __version__


def test_version():
    assert __version__ == '0.1.0'


"""
this modul for testing sum,product and square for linkedlist values
"""
from pythonisms.pythonisms import Node,LinkedList,MathThings
import pytest 

def test_insert():
  # Arrange
  ll = LinkedList()
  ll.insert(5)
  ll.insert(2)
  ll.insert(25)
  expected = 25
  expected_ll = "{25}->{2}->{5}"
  # Actual
  actual = ll.head.data
  actual_ll = str(ll)
  # Assert
  assert actual == expected
  assert actual_ll == expected_ll

def test_ll_from_collection():
  ll = LinkedList([1,2])
  expected = "{1}->{2}"
  actual = str(ll)
  assert actual == expected

def test_boolean():
    ll = LinkedList()
    ll.insert(1)
    assert bool(ll) == True
    ll2 = LinkedList()
    assert bool(ll2) == False




def test_math_sum():
  ll = LinkedList()
  node1 = Node(5)
  node2 = Node(10)
  node3 = Node(5)
  ll.head = node1
  node1.next = node2
  node2.next = node3
  expected = 20
  math = MathThings()
  ll.walk(math.adder)
  actual = math.sum
  assert expected == actual


def test_math_product():
  # Arrange
  expected = 40
  #Act
  ll = LinkedList()
  node1 = Node(1)
  node2 = Node(5)
  node3 = Node(2)
  node4 = Node(4)
  ll.head = node1
  node1.next = node2
  node2.next = node3
  node3.next = node4
  math = MathThings()
  ll.walk(math.multiplier)
  actual = math.product
  #Assert
  assert actual == expected 

def test_math_squared():
  l1 =LinkedList()
  l1.insert(2)
  l1.insert(1)
  l1.insert(3)
  l1.insert(1)
  expected = [1,9,1,4]
  math = MathThings()
  l1.walk(math.squared)
  actual = math.squares
  assert actual == expected
 

