import unittest
from DSAproject import Node
from DSAproject import LinkedList

llist = LinkedList()
first_node = Node(1, "Gihozo Lando", "g.lando@alustudent.com", "10:54", "3/3/2021")
llist.head = first_node
second_node = Node(2, "Barezi Julien", "b.julien@alustudent.com", "12:59", "3/4/2021")
first_node.next = second_node
third_node = Node(3, "Diane Niyibaruta", "d.niyibarut@alustudent.com", "11:32", "04/03/2021")
second_node.next = third_node

class MyTestCase(unittest.TestCase):
    def test_search(self):
        self.assertEqual(llist.search(2), True)


if __name__ == '__main__':
    unittest.main()
