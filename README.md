<h1>Check-in and Check out program implemented in python using linked lists</h1><br>
<h3>Team members:</h3>
Barezi Julien,
Gihozo Landelin,
Diane Niyibaruta.

<h3>Data structures and algorithm used:</h3>
Linked lists

<h3>Purpose of linked lists:</h3> 

Linked lists allow efficient insertion and deletion of elements which is the main reason we found them effective for our project.
<h2>Project description</h2>
In this project, we are going to create a check-in and check-out program which will allow the users of the program to register people who come to the campus and be able to know the number of people on the campus at any given moment. This is a program needed especially at this moment because as we are in the middle of a pandemic, coronavirus covid 19, and it is very important for people to practice social distancing as it is one of the main important methods to prevent the spreading of the virus. When there is a program like this one it is very useful because it allows the management of the campus to know the number of people on the campus and make sure that they don’t exceed the number of people allowed on the premises in order to favor the practicing of social distancing.

By the end of this project, we believe that we will have a program that is able to register users who enter any building and record their information and remove them when they leave the building. We will use linked lists to implement this because it eases the insertion and removal of data. 

<h2>Motivation</h2>
The idea of doing this program came up when our campus was closed due to an increase in covid 19 cases in Rwanda which led to the closing of schools. After the lockdown schools were reopened but for our campus, only a certain number of people was allowed to be on campus and it was not allowed to exceed that number. This is when the idea of developing a program that could allow recording the number of people on campus and be able to make sure only the allowed number of people is on campus and not exceed it.

<h2>Technology used</h2>
Python programming language
<h2>How to run</h2>
To run this project you need to clone this repository and run the file named DSA project using PyCharm and make sure you have the library called “Tabulate” installed in your PyCharm.

<h3>correctness of algorithm</h3>
Please find in the repository a folder containing three test cases in which two of them give a correct oyput while the third one gives an incorrect output.
<h2>test number one</h2>
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
    def test_count(self):
        self.assertEqual(llist.count(), 3)


if __name__ == '__main__':
    unittest.main()
    
This test gives a correct output
<h2>test number two</h2.
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
    
This test gives a correct output
<h2>test number three</h3>
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
    def test_count(self):
        self.assertEqual(llist.count(), 6)


if __name__ == '__main__':
    unittest.main()

This test gives a wrong output




