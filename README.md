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
To run this project you need to clone this repository and run the file named DSA project using PyCharm and make sure you have the library called “Tabulate” installed in your PyCharm. to install it run:<br>

<p>pip install tabulate</p>

<h3>correctness of algorithm</h3>
Please find in the repository a folder containing three test cases in which two of them give a correct oyput while the third one gives an incorrect output.
<h2>test number one</h2>
import unittest<br>
from DSAproject import Node<br>
from DSAproject import LinkedList<br>

llist = LinkedList()<br>
first_node = Node(1, "Gihozo Lando", "g.lando@alustudent.com", "10:54", "3/3/2021")<br>
llist.head = first_node<br>
second_node = Node(2, "Barezi Julien", "b.julien@alustudent.com", "12:59", "3/4/2021")<br>
first_node.next = second_node<br>
third_node = Node(3, "Diane Niyibaruta", "d.niyibarut@alustudent.com", "11:32", "04/03/2021")<br>
second_node.next = third_node<br>

class MyTestCase(unittest.TestCase):<br>
    def test_count(self):<br>
        self.assertEqual(llist.count(), 3)<br>


if __name__ == '__main__':<br>
    unittest.main())<br>
    
This test gives a correct output
<h2>test number two</h2>
  import unittest<br>
from DSAproject import Node<br>
from DSAproject import LinkedList<br>

llist = LinkedList()<br>
first_node = Node(1, "Gihozo Lando", "g.lando@alustudent.com", "10:54", "3/3/2021")<br>
llist.head = first_node<br>
second_node = Node(2, "Barezi Julien", "b.julien@alustudent.com", "12:59", "3/4/2021")<br>
first_node.next = second_node<br>
third_node = Node(3, "Diane Niyibaruta", "d.niyibarut@alustudent.com", "11:32", "04/03/2021")<br>
second_node.next = third_node<br>

class MyTestCase(unittest.TestCase):)<br>
    def test_search(self):)<br>
        self.assertEqual(llist.search(2), True))<br>


if __name__ == '__main__':)<br>
    unittest.main())<br>
    
This test gives a correct output)<br>
<h2>test number three</h3>
import unittest<br>
from DSAproject import Node<br>
from DSAproject import LinkedLis<br>t

llist = LinkedList()
first_node = Node(1, "Gihozo Lando", "g.lando@alustudent.com", "10:54", "3/3/2021")<br>
llist.head = first_node<br>
second_node = Node(2, "Barezi Julien", "b.julien@alustudent.com", "12:59", "3/4/2021")<br>
first_node.next = second_node<br>
third_node = Node(3, "Diane Niyibaruta", "d.niyibarut@alustudent.com", "11:32", "04/03/2021")<br>
second_node.next = third_node<br>

class MyTestCase(unittest.TestCase):<br>
    def test_count(self):<br>
        self.assertEqual(llist.count(), 6)<br>


if __name__ == '__main__':<br>
    unittest.main()<br>

This test gives a wrong output<br>


<h2> Analysis of Algorithm</h2>

First of all for deleting an element in our linked list the time complexity is ![first equation](https://latex.codecogs.com/gif.latex?O%5Cleft%20%28%201%20%5Cright%20%29)  while the space complexity <br> is ![second equation](https://latex.codecogs.com/gif.latex?O%5Cleft%20%28%20n%20%5Cright%20%29) <br>.

n stands for the number of nodes in our linked list<br>
This means that if for instance we have 3 nodes in our linked list<br>
The space complexity would be equal to ![third equation](https://latex.codecogs.com/gif.latex?O%5Cleft%20%28%203%20%5Cright%20%29) br>

For inserting an element the time complexity is ![](https://latex.codecogs.com/gif.latex?O%5Cleft%20%28%201%20%5Cright%20%29)  while the space complexity is ![](https://latex.codecogs.com/gif.latex?O%5Cleft%20%28%20n%20%5Cright%20%29) <br>

n stands for the number of nodes in our linked list<br>
This means that if for instance we have 3 nodes in our linked list<br>
The space complexity would be equal to ![](https://latex.codecogs.com/gif.latex?O%5Cleft%20%28%203%20%5Cright%20%29) <br>

For showing all nodes in our linked list both the time complexity and space complexity is ![](https://latex.codecogs.com/gif.latex?O%5Cleft%20%28%20n%20%5Cright%20%29) <br>

n stands for the number of nodes in our linked list<br>
This means that if for instance we have 3 nodes in our linked list<br>
The space complexity and time complexity would be equal to ![](https://latex.codecogs.com/gif.latex?O%5Cleft%20%28%203%20%5Cright%20%29)<br>

For counting all the nodes n our linked list both the time complexity and space complexity is ![](https://latex.codecogs.com/gif.latex?O%5Cleft%20%28%20n%20%5Cright%20%29) <br>

n stands for the number of nodes in our linked list<br>
This means that if for instance we have 3 nodes in our linked list<br>
The space complexity and time complexity would be equal to ![](https://latex.codecogs.com/gif.latex?O%5Cleft%20%28%203%20%5Cright%20%29) <br>

For searching a node in our linked list both the time complexity and space complexity is ![](https://latex.codecogs.com/gif.latex?O%5Cleft%20%28%20n%20%5Cright%20%29) <br>

n stands for the number of nodes in our linked list<br>
This means that if for instance we have 3 nodes in our linked list<br>
The space complexity would be equal to ![](https://latex.codecogs.com/gif.latex?O%5Cleft%20%28%203%20%5Cright%20%29) <br>

<h2>Solution</h2>
<p>During this period of coronavirus it is very important to control the number of people in any place to make sure that the number of people in any gathering does not exceed the limited amount of people allowed in any gathering. After seeing this our peer group sat down and tried to find a solution to this problem, after many hours of thinking we decided to use the knowledge we acquired from data structures and algorithms and decided to use a data structure called linked lists to make an app that records the people entering s building and removing them from the recordings when they leave.</p><br>

<p>This app is beneficial to the society for instance if people are gathered in a place and they want to know the number of people gathered there and make sure that they don’t exceed the number of people allowed there they can use our app because it has a functionality to count the number of people gathered at a certain event if every individual has been recorded upon them entering the event. This is very useful mostly in this period of coronavirus where it is important to knoe the number of people together in any event.</p><br>

<h2>Link to video</h2>


https://drive.google.com/file/d/1iwsPa7khIR2fJKs6LGn18hNFjBnQkwEM/view


<h2>Reference</h2>
 Linked List. Brilliant.org. Retrieved 18:45, April 25, 2021, from https://brilliant.org/wiki/linked-lists/ <br>







