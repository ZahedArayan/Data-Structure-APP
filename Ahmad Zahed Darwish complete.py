import os
import time
from collections import deque

#Create a class for array
class Array:
   
    def __init__(self,size,A_type):   # create an inializer
        self.size=size
        self.array=[None]*size
        self.A_type=A_type

    def display(self):              #It displays the array
        print(self.array)
    def insert(self,data,index):
                print(type(data))
                try:
                    if type(data)==type(self.A_type):               #It checks the type and then insert
                        if self.array[index]==None:
                            self.array[index]=data
                        else:
                            print(L)
                            print("Cannot add other data\nthere another data exist")
                            print(L)
                    else:           
                        print(L) 
                        print("Cannot add other data type!")
                        print(L)
                        # print("or may there another data exist")
                except IndexError:
                    print("Array is full\nCan not add other items ")
                    print("list Index out of range")
                
    def delete(self,data):       #It checks whether the item exist or not 
        if data in self.array:
            self.array.remove(data)
            print("Element deleted!")
        else:
             print("Item not found")






#create the stack here 
class Stack:
    def __init__(self):   # Initialize the array (constructor)
        self.array = []

    def push(self, item):  # Push an item onto the stack
        self.array.append(item)
        print("Item Pushed!")
        print(self.array)
        
    def pop(self):  # Pop an item from the stack
        if not self.isEmpty():
            self.array.pop()
            print("Item popped!")
        print(self.array)
        
    def isEmpty(self):  # Check if the stack is empty
        if self.array == []:
            print("Stack is Empty")
        else:
            print("Stack is not empty")

    def display(self):  # Display the stack
        print("Stack:", self.array)
        
    def peek(self):  # Get the top item of the stack
        if self.array != []:
            print("The peek is:", self.array[-1])
        else:
            print("Stack is Empty")

  #the last array before update

        # class Array:
        #     def __init__(self):
        #         self.array=[]

        #     def insert(self,item,index):
        #         self.array.insert(index,item)
        #         print(item,"inserted in index :",index)
        #     def delete(self,item):
        #         if item in self.array:
        #             self.array.remove(item)
        #             print(item," Item deleted!")
        #         else:
        #             print("Item not found !")
        #     def display(self):
        #         print(self.array)



#create the queue class
class Queue:
    def __init__(self):
        self.queue=[]
    def is_empty(self):  #this function is for checking if the queue is empty to use for others
        return len(self.queue)==0

    def enqueue(self,item): #this function is inserting elements inside qeueu
        self.queue.append(item)
        print("Element Queued!")
        
    def dequeue(self): #this fucntion is adding elemetn to the qeueu
        if self.is_empty():
            print("Queue is empty!")
            return None
            
        print("Element dequeued")
        return self.queue.pop(0)
        
    
    def display(self): #this function is used to display qeueu
        print(self.queue)

    def size(self): #this fucntion checks the size of the qeueu
        return len(self.queue)
    
#Node class for the linked list

class LinkedListNode:
    def __init__(self, data): # this function is making the node of linkedlist and its properties which are data and pointer
        self.data = data
        self.next = None

class LinkedList: #this is a class of linked list and its methods 
    def __init__(self):
        self.head = None

    def insert(self, data):#by this function we can add an element to the linked list
        if not self.head:
            self.head = LinkedListNode(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = LinkedListNode(data)
        print("Element inserted.")

    def Delete(self, data): #this function first checks whether the linked list is empty or not
                            #if it was, it return "list is empty" otherwise it will delete an element
        if not self.head:
            print("List is empty.")
            return

        if self.head.data == data:
            self.head = self.head.next
            print("Element deleted.")
            return

        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                print("Element deleted.")
                return
            current = current.next

        print("Element not found.")

    def display(self): #this function first checks whether the linked list is empty or not
                       #if it was, it return "list is empty" otherwise it will diplay the list.
        if not self.head:
            print("List is empty.")
            return

        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

L="**********************************"
#Node for the binary class 

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

#This the BST class 
class BinaryTree:
    def __init__(self):
        self.root = None #initialize the init method for root

    def insert(self, data): 
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_recursive(data, self.root)

    def _insert_recursive(self, data, node): #this function is for checking every node in this tree 
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert_recursive(data, node.left)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert_recursive(data, node.right)

    def delete(self, data):
        self.root = self._delete_recursive(data, self.root)

    def _delete_recursive(self, data, node):   # this the recursive method for finding the node 
        if node is None:
            return node
        if data < node.data:                #checks if data is less than node call the recursive function back 
            node.left = self._delete_recursive(data, node.left)
        elif data > node.data:
            node.right = self._delete_recursive(data, node.right)
        else:
            # Found the node to delete
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            # Node has two children
            min_node = self._find_min(node.right)
            node.data = min_node.data
            node.right = self._delete_recursive(min_node.data, node.right)
        return node

    def _find_min(self, node): # finds minimium 
        current = node
        while current.left is not None:  # checks if it is not none
            current = current.left
        return current

    def display(self):
        self._display_recursive(self.root) # displays node

    def _display_recursive(self, node):
        if node is not None:
            self._display_recursive(node.left) # 
            print(node.data)
            self._display_recursive(node.right) 


class BSNode: # class of binary search tree node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree: # class of binary search tre
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = BSNode(data)
        else:
            self._insert_recursive(data, self.root)

    def _insert_recursive(self, data, node): #Funciton of recursion
        if data < node.data:
            if node.left is None:
                node.left = BSNode(data)
            else:
                self._insert_recursive(data, node.left)
        else:
            if node.right is None:
                node.right = BSNode(data)
            else:
                self._insert_recursive(data, node.right)

    def delete(self, data): # delete function if it duplicate
        self.root = self._delete_recursive(data, self.root)

    def _delete_recursive(self, data, node): # 
        if node is None:
            return node
        if data < node.data:
            node.left = self._delete_recursive(data, node.left)
        elif data > node.data:
            node.right = self._delete_recursive(data, node.right)
        else:
            # Found the node to delete
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            # Node has two children
            min_node = self._find_min(node.right)
            node.data = min_node.data
            node.right = self._delete_recursive(min_node.data, node.right)
        return node

    def _find_min(self, node): # Check if the stack is empty
        current = node
        while current.left is not None:
            current = current.left
        return current

    def search(self, data): # function for search
        return self._search_recursive(data, self.root)

    def _search_recursive(self, data, node):
        if node is None or node.data == data:
            return node
        if data < node.data:
            return self._search_recursive(data, node.left)
        else:
            return self._search_recursive(data, node.right)

    def display(self): # fucntion of display
        self._display_recursive(self.root)

    def _display_recursive(self, node): 
        if node is not None:
            self._display_recursive(node.left)
            print(node.data)
            self._display_recursive(node.right)


class TernaryNode: #  a class for ternary node
    def __init__(self, data):
        self.data = data
        self.children = [None, None, None]

class TernaryTree: # ternary tree node
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = TernaryNode(data)
        else:
            self._insert_recursive(data, self.root)

    def _insert_recursive(self, data, node): 
        if data < node.data:
            if node.children[0] is None:
                node.children[0] = TernaryNode(data)
            else:
                self._insert_recursive(data, node.children[0])
        elif data == node.data:
            if node.children[1] is None:
                node.children[1] = TernaryNode(data)
            else:
                self._insert_recursive(data, node.children[1])
        else:
            if node.children[2] is None:
                node.children[2] = TernaryNode(data)
            else:
                self._insert_recursive(data, node.children[2])

    def delete(self, data): # delets duplication
        if self.root is None:
            return
        self.root = self._delete_recursive(data, self.root)

    def _delete_recursive(self, data, node): 
        if node is None:
            return None

        if data < node.data:
            node.children[0] = self._delete_recursive(data, node.children[0]) # Check if the stack is empty
        elif data > node.data:
            node.children[2] = self._delete_recursive(data, node.children[2])
        else:
            if node.children[1] is not None:
                node.children[1] = self._delete_recursive(data, node.children[1])
            else:
                if node.children[0] is None and node.children[2] is None:
                    return None
                elif node.children[0] is not None:
                    return node.children[0]
                else:
                    return node.children[2]
        return node

    def search(self, data): # Check if the stack is empty
        return self._search_recursive(data, self.root)

    def _search_recursive(self, data, node): # Check if the stack is empty
        if node is None:
            return False
        elif data == node.data:
            return True
        elif data < node.data:
            return self._search_recursive(data, node.children[0])
        else:
            return self._search_recursive(data, node.children[2])

    def display(self): # Check if the stack is empty
        self._display_recursive(self.root, 0)

    def _display_recursive(self, node, level):
        if node is not None:
            self._display_recursive(node.children[2], level + 1)
            print('   ' * level + '|__' + str(node.data))
            self._display_recursive(node.children[0], level + 1)
            self._display_recursive(node.children[1], level + 1)



class AVLNode: # Check if the stack is empty
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

class AVLTree: # Check if the stack is empty
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self._insert_recursive(data, self.root)

    def _insert_recursive(self, data, node):
        if node is None:
            return AVLNode(data)
        
        if data < node.data:
            node.left = self._insert_recursive(data, node.left)
        else:
            node.right = self._insert_recursive(data, node.right)
        
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        
        balance_factor = self._get_balance_factor(node)
        
        if balance_factor > 1:
            if data < node.left.data:
                return self._rotate_right(node)
            else:
                node.left = self._rotate_left(node.left)
                return self._rotate_right(node)
        
        if balance_factor < -1:
            if data > node.right.data:
                return self._rotate_left(node)
            else:
                node.right = self._rotate_right(node.right)
                return self._rotate_left(node)
        
        return node

    def delete(self, data):
        self.root = self._delete_recursive(data, self.root)

    def _delete_recursive(self, data, node):
        if node is None:
            return node
        
        if data < node.data:
            node.left = self._delete_recursive(data, node.left)
        elif data > node.data:
            node.right = self._delete_recursive(data, node.right)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                min_node = self._find_min(node.right)
                node.data = min_node.data
                node.right = self._delete_recursive(min_node.data, node.right)
        
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        
        balance_factor = self._get_balance_factor(node)
        
        if balance_factor > 1:
            if self._get_balance_factor(node.left) >= 0:
                return self._rotate_right(node)
            else:
                node.left = self._rotate_left(node.left)
                return self._rotate_right(node)
        
        if balance_factor < -1:
            if self._get_balance_factor(node.right) <= 0:
                return self._rotate_left(node)
            else:
                node.right = self._rotate_right(node.right)
                return self._rotate_left(node)
        
        return node

    def search(self, data):
        return self._search_recursive(data, self.root)

    def _search_recursive(self, data, node):
        if node is None:
            return False
        
        if data == node.data:
            return True
        elif data < node.data:
            return self._search_recursive(data, node.left)
        else:
            return self._search_recursive(data, node.right)

    def display(self):
        self._display_recursive(self.root, 0)

    def _display_recursive(self, node, level):
        if node is not None:
            self._display_recursive(node.right, level + 1)
            print('   ' * level + '|__' + str(node.data))
            self._display_recursive(node.left, level + 1)

    def _get_height(self, node):
        if node is None:
            return 0
        return node.height

    def _get_balance_factor(self, node):
        if node is None:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    def _rotate_left(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        return y

    def _rotate_right(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        return y

    def _find_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current



class BTreeNode:
    def __init__(self, leaf=False):
        self.leaf = leaf
        self.keys = []
        self.child = []


class BTree:
    def __init__(self, t):
        self.root = BTreeNode(True)
        self.t = t

    def insert(self, k):
        root = self.root
        if len(root.keys) == (2 * self.t) - 1:
            temp = BTreeNode()
            self.root = temp
            temp.child.insert(0, root)
            self.split_child(temp, 0)
            self.insert_non_full(temp, k)
        else:
            self.insert_non_full(root, k)

    def insert_non_full(self, x, k):
        i = len(x.keys) - 1
        if x.leaf:
            while i >= 0 and k < x.keys[i]:
                i -= 1
            x.keys.insert(i + 1, k)
        else:
            while i >= 0 and k < x.keys[i]:
                i -= 1
            i += 1
            if len(x.child[i].keys) == (2 * self.t) - 1:
                self.split_child(x, i)
                if k > x.keys[i]:
                    i += 1
            self.insert_non_full(x.child[i], k)

    def split_child(self, x, i):
        t = self.t
        y = x.child[i]
        z = BTreeNode(y.leaf)
        x.child.insert(i + 1, z)
        x.keys.insert(i, y.keys[t - 1])
        z.keys = y.keys[t: (2 * t) - 1]
        y.keys = y.keys[0: t - 1]
        if not y.leaf:
            z.child = y.child[t: 2 * t]
            y.child = y.child[0: t - 1]

    def delete(self, k):
        root = self.root
        self.delete_key(root, k)
        if len(root.keys) == 0 and not root.leaf:
            self.root = root.child[0]

    def delete_key(self, x, k):
        t = self.t
        i = 0
        while i < len(x.keys) and k > x.keys[i]:
            i += 1

        if i < len(x.keys) and k == x.keys[i]:
            if x.leaf:
                x.keys.remove(k)
            else:
                self.delete_key_internal(x, k, i)
        else:
            if x.leaf:
                return
            if len(x.child[i].keys) < t:
                self.fill(x, i)
            if i > len(x.keys):
                self.delete_key(x.child[i - 1], k)
            else:
                self.delete_key(x.child[i], k)

    def delete_key_internal(self, x, k, i):
        t = self.t
        if x.child[i].leaf:
            x.keys[i] = x.child[i].keys.pop()
        else:
            pred = x.child[i]
            succ = x.child[i + 1]
            if len(pred.keys) >= t:
                x.keys[i] = pred.keys.pop()
                self.delete_key(pred, x.keys[i])
            elif len(succ.keys) >= t:
                x.keys[i] = succ.keys.pop(0)
                self.delete_key(succ, x.keys[i])
            else:
                pred.keys.append(x.keys.pop(i))
                pred.keys.extend(succ.keys)
                pred.child.extend(succ.child)
                x.child.pop(i + 1)
                self.delete_key(pred, k)

    def fill(self, x, i):
        t = self.t
        if i != 0 and len(x.child[i - 1].keys) >= t:
            self.borrow_from_prev(x, i)
        elif i != len(x.keys) and len(x.child[i + 1].keys) >= t:
            self.borrow_from_next(x, i)
        else:
            if i != len(x.keys):
                self.merge(x, i)
            else:
                self.merge(x, i - 1)

    def borrow_from_prev(self, x, i):
        child = x.child[i]
        sibling = x.child[i - 1]
        child.keys.insert(0, x.keys[i - 1])
        x.keys[i - 1] = sibling.keys.pop()
        if not child.leaf:
            child.child.insert(0, sibling.child.pop())

    def borrow_from_next(self, x, i):
        child = x.child[i]
        sibling = x.child[i + 1]
        child.keys.append(x.keys[i])
        x.keys[i] = sibling.keys.pop(0)
        if not child.leaf:
            child.child.insert(sibling.child.pop(0))

    def merge(self, x, i):
        child = x.child[i]
        sibling = x.child[i + 1]
        child.keys.append(x.keys.pop(i))
        child.keys.extend(sibling.keys)
        if not child.leaf:
            child.child.extend(sibling.child)
        x.child.pop(i + 1)

    def search(self, k):
        return self.search_key(self.root, k)

    def search_key(self, x, k):
        i = 0
        while i < len(x.keys) and k > x.keys[i]:
            i += 1
        if i < len(x.keys) and k == x.keys[i]:
            return True
        elif x.leaf:
            return False
        else:
            return self.search_key(x.child[i], k)

    def display(self):
        self.display_tree(self.root)

    def display_tree(self, x, indent=0):
        if not x.leaf:
            for i in range(len(x.child) - 1, -1, -1):
                self.display_tree(x.child[i], indent + 1)
        print(' ' * 4 * indent + '->', x.keys)
        if not x.leaf:
            for i in range(len(x.child) - 1, -1, -1):
                self.display_tree(x.child[i], indent + 1)




class RBNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        self.color = "RED"


class RedBlackTree:
    def __init__(self):
        self.NULL_NODE = RBNode(None)
        self.NULL_NODE.color = "BLACK"
        self.NULL_NODE.left = None
        self.NULL_NODE.right = None
        self.root = self.NULL_NODE

    def insert(self, key):
        new_node = RBNode(key)
        new_node.parent = None
        new_node.left = self.NULL_NODE
        new_node.right = self.NULL_NODE
        new_node.color = "RED"

        current = self.root
        parent = None
        while current != self.NULL_NODE:
            parent = current
            if new_node.key < current.key:
                current = current.left
            else:
                current = current.right

        new_node.parent = parent
        if parent is None:
            self.root = new_node
        elif new_node.key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node

        self.fix_insert(new_node)

    def fix_insert(self, node):
        while node.parent.color == "RED":
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right

                if uncle.color == "RED":
                    node.parent.color = "BLACK"
                    uncle.color = "BLACK"
                    node.parent.parent.color = "RED"
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.left_rotate(node)

                    node.parent.color = "BLACK"
                    node.parent.parent.color = "RED"
                    self.right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left

                if uncle.color == "RED":
                    node.parent.color = "BLACK"
                    uncle.color = "BLACK"
                    node.parent.parent.color = "RED"
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotate(node)

                    node.parent.color = "BLACK"
                    node.parent.parent.color = "RED"
                    self.left_rotate(node.parent.parent)

            if node == self.root:
                break

        self.root.color = "BLACK"

    def delete(self, key):
        node = self.search(key)
        if node:
            self.delete_node(node)

    def search(self, key):
        return self.search_helper(self.root, key)

    def search_helper(self, node, key):
        if node == self.NULL_NODE or key == node.key:
            return node

        if key < node.key:
            return self.search_helper(node.left, key)
        else:
            return self.search_helper(node.right, key)

    def delete_node(self, node):
        y = node
        y_original_color = y.color
        if node.left == self.NULL_NODE:
            x = node.right
            self.transplant(node, node.right)
        elif node.right == self.NULL_NODE:
            x = node.left
            self.transplant(node, node.left)
        else:
            y = self.minimum(node.right)
            y_original_color = y.color
            x = y.right
            if y.parent == node:
                x.parent = y
            else:
                self.transplant(y, y.right)
                y.right = node.right
                y.right.parent = y

            self.transplant(node, y)
            y.left = node.left
            y.left.parent = y
            y.color = node.color

        if y_original_color == "BLACK":
            self.fix_delete(x)

    def minimum(self, node):
        while node.left != self.NULL_NODE:
            node = node.left
        return node

    def transplant(self, u, v):
        if u.parent == self.NULL_NODE:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NULL_NODE:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == self.NULL_NODE:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, y):
        x = y.left
        y.left = x.right
        if x.right != self.NULL_NODE:
            x.right.parent = y
        x.parent = y.parent
        if y.parent == self.NULL_NODE:
            self.root = x
        elif y == y.parent.left:
            y.parent.left = x
        else:
            y.parent.right = x
        x.right = y
        y.parent = x

    def fix_delete(self, node):
        while node != self.root and node.color == "BLACK":
            if node == node.parent.left:
                sibling = node.parent.right

                if sibling.color == "RED":
                    sibling.color = "BLACK"
                    node.parent.color = "RED"
                    self.left_rotate(node.parent)
                    sibling = node.parent.right

                if sibling.left.color == "BLACK" and sibling.right.color == "BLACK":
                    sibling.color = "RED"
                    node = node.parent
                else:
                    if sibling.right.color == "BLACK":
                        sibling.left.color = "BLACK"
                        sibling.color = "RED"
                        self.right_rotate(sibling)
                        sibling = node.parent.right

                    sibling.color = node.parent.color
                    node.parent.color = "BLACK"
                    sibling.right.color = "BLACK"
                    self.left_rotate(node.parent)
                    node = self.root
            else:
                sibling = node.parent.left

                if sibling.color == "RED":
                    sibling.color = "BLACK"
                    node.parent.color = "RED"
                    self.right_rotate(node.parent)
                    sibling = node.parent.left

                if sibling.right.color == "BLACK" and sibling.left.color == "BLACK":
                    sibling.color = "RED"
                    node = node.parent
                else:
                    if sibling.left.color == "BLACK":
                        sibling.right.color = "BLACK"
                        sibling.color = "RED"
                        self.left_rotate(sibling)
                        sibling = node.parent.left

                    sibling.color = node.parent.color
                    node.parent.color = "BLACK"
                    sibling.left.color = "BLACK"
                    self.right_rotate(node.parent)
                    node = self.root

        node.color = "BLACK"

    def display(self):
        self.display_helper(self.root)

    def display_helper(self, node):
        if node != self.NULL_NODE:
            self.display_helper(node.left)
            print(node.key, end=" ")
            self.display_helper(node.right)


class DirectedWeightedGraph:
    def __init__(self):
        self.graph = {}

    def insert_edge(self, source, destination, weight):
        if source in self.graph:
            self.graph[source].append((destination, weight))
        else:
            self.graph[source] = [(destination, weight)]

    def delete_edge(self, source, destination):
        if source in self.graph:
            edges = self.graph[source]
            updated_edges = [(dest, weight) for dest, weight in edges if dest != destination]
            self.graph[source] = updated_edges

    def display(self):
        for source in self.graph:
            edges = self.graph[source]
            for destination, weight in edges:
                print(f"Source: {source}, Destination: {destination}, Weight: {weight}")

    def search(self, source, destination):
        if source in self.graph:
            edges = self.graph[source]
            for dest, weight in edges:
                if dest == destination:
                    return weight
        return None




class UndirectedGraph:
    def __init__(self):
        self.graph = {}

    def insert_edge(self, v1, v2):
        if v1 in self.graph:
            self.graph[v1].append(v2)
        else:
            self.graph[v1] = [v2]

        if v2 in self.graph:
            self.graph[v2].append(v1)
        else:
            self.graph[v2] = [v1]

    def delete_edge(self, v1, v2):
        if v1 in self.graph and v2 in self.graph:
            self.graph[v1].remove(v2)
            self.graph[v2].remove(v1)

    def display(self):
        for vertex in self.graph:
            neighbors = self.graph[vertex]
            for neighbor in neighbors:
                print(f"Vertex: {vertex}, Neighbor: {neighbor}")

    def search(self, v1, v2):
        if v1 in self.graph and v2 in self.graph:
            return v2 in self.graph[v1]
        return False

 


class Graph:
    def __init__(self):
        self.graph = {}

    def insert_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def delete_vertex(self, vertex):
        if vertex in self.graph:
            del self.graph[vertex]
            # Remove the vertex from all adjacency lists
            for adj_list in self.graph.values():
                if vertex in adj_list:
                    adj_list.remove(vertex)

    def insert_edge(self, start_vertex, end_vertex):
        if start_vertex in self.graph and end_vertex in self.graph:
            self.graph[start_vertex].append(end_vertex)
            self.graph[end_vertex].append(start_vertex)

    def delete_edge(self, start_vertex, end_vertex):
        if start_vertex in self.graph and end_vertex in self.graph:
            self.graph[start_vertex].remove(end_vertex)
            self.graph[end_vertex].remove(start_vertex)

    def display(self):
        for vertex, adj_list in self.graph.items():
            print(vertex, "->", ", ".join(adj_list))

    def search_vertex(self, vertex):
        if vertex in self.graph:
            print(f"Vertex {vertex} exists in the graph.")
        else:
            print(f"Vertex {vertex} does not exist in the graph.")
    def breadth_first_search(self, start_vertex):
        visited = set()  # Set to track visited vertices
        queue = deque([start_vertex])  # Queue to store vertices to visit

        while queue:
            vertex = queue.popleft()  # Get the next vertex from the queue
            print(vertex)  # Process the vertex (e.g., print or perform other operations)
            visited.add(vertex)  # Mark the vertex as visited

            # Add the unvisited neighboring vertices to the queue
            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)

    def depth_first_search(self, start_vertex):
        visited = set()  # Set to track visited vertices
        self._dfs_util(start_vertex, visited)

    def _dfs_util(self, vertex, visited):
        visited.add(vertex)
        print(vertex)  # Process the vertex (e.g., print or perform other operations)

        for neighbor in self.graph[vertex]:
            if neighbor not in visited:
                self._dfs_util(neighbor, visited)




class LinearProbingHashTable:
    def __init__(self, size):
        self.size = size
        self.keys = [None] * size
        self.values = [None] * size

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)

        while self.keys[index] is not None:
            if self.keys[index] == key:
                self.values[index] = value  # Update value if key already exists
                return

            index = (index + 1) % self.size

        self.keys[index] = key
        self.values[index] = value

    def delete(self, key):
        index = self._hash(key)

        while self.keys[index] is not None:
            if self.keys[index] == key:
                self.keys[index] = None
                self.values[index] = None
                return

            index = (index + 1) % self.size

    def search(self, key):
        index = self._hash(key)

        while self.keys[index] is not None:
            if self.keys[index] == key:
                return self.values[index]

            index = (index + 1) % self.size

        return None

    def display(self):
        for i in range(self.size):
            if self.keys[i] is not None:
                print(f"Key: {self.keys[i]}, Value: {self.values[i]}")




class DoubleHashingHashTable:
    def __init__(self, size):
        self.size = size
        self.keys = [None] * size
        self.values = [None] * size

    def _hash1(self, key):
        """Primary hash function"""
        return hash(key) % self.size

    def _hash2(self, key):
        """Secondary hash function"""
        return 1 + (hash(key) % (self.size - 1))

    def insert(self, key, value):
        """Inserts a key-value pair into the hash table"""
        index = self._hash1(key)  # Calculate the initial index using the primary hash function
        step = self._hash2(key)  # Calculate the step size using the secondary hash function

        while self.keys[index] is not None:  # If the slot is not empty
            if self.keys[index] == key:  # If the key already exists, update the value
                self.values[index] = value
                return

            index = (index + step) % self.size  # Move to the next slot using double hashing

        self.keys[index] = key  # Insert the key into the slot
        self.values[index] = value  # Insert the value into the slot

    def delete(self, key):
        """Deletes a key-value pair from the hash table"""
        index = self._hash1(key)  # Calculate the initial index using the primary hash function
        step = self._hash2(key)  # Calculate the step size using the secondary hash function

        while self.keys[index] is not None:  # If the slot is not empty
            if self.keys[index] == key:  # If the key is found
                self.keys[index] = None  # Remove the key
                self.values[index] = None  # Remove the value
                return

            index = (index + step) % self.size  # Move to the next slot using double hashing

    def search(self, key):
        """Searches for a key and returns its corresponding value"""
        index = self._hash1(key)  # Calculate the initial index using the primary hash function
        step = self._hash2(key)  # Calculate the step size using the secondary hash function

        while self.keys[index] is not None:  # If the slot is not empty
            if self.keys[index] == key:  # If the key is found
                return self.values[index]  # Return the corresponding value

            index = (index + step) % self.size  # Move to the next slot using double hashing

        return None  # Key not found

    def display(self):
        """Displays all key-value pairs in the hash table"""
        for i in range(self.size):
            if self.keys[i] is not None:
                print(f"Key: {self.keys[i]}, Value: {self.values[i]}")




class SeparateChainingHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        """Hash function to calculate the index"""
        return hash(key) % self.size

    def insert(self, key, value):
        """Inserts a key-value pair into the hash table"""
        index = self._hash(key)  # Calculate the index using the hash function
        chain = self.table[index]  # Get the chain at the calculated index

        for pair in chain:
            if pair[0] == key:  # If the key already exists, update the value
                pair[1] = value
                return

        chain.append([key, value])  # Add the key-value pair to the chain

    def delete(self, key):
        """Deletes a key-value pair from the hash table"""
        index = self._hash(key)  # Calculate the index using the hash function
        chain = self.table[index]  # Get the chain at the calculated index

        for pair in chain:
            if pair[0] == key:  # If the key is found
                chain.remove(pair)  # Remove the key-value pair
                return

    def search(self, key):
        """Searches for a key and returns its corresponding value"""
        index = self._hash(key)  # Calculate the index using the hash function
        chain = self.table[index]  # Get the chain at the calculated index

        for pair in chain:
            if pair[0] == key:  # If the key is found
                return pair[1]  # Return the corresponding value

        return None  # Key not found

    def display(self):
        """Displays all key-value pairs in the hash table"""
        for index, chain in enumerate(self.table):
            for pair in chain:
                print(f"Index: {index}, Key: {pair[0]}, Value: {pair[1]}")





class QuadraticProbingHashTable:
    def __init__(self, size):
        self.size = size
        self.keys = [None] * size
        self.values = [None] * size

    def _hash(self, key):
        """Hash function to calculate the index"""
        return hash(key) % self.size

    def _quadratic_probe(self, index, i):
        """Quadratic probing to resolve collisions"""
        return (index + i**2) % self.size

    def insert(self, key, value):
        """Inserts a key-value pair into the hash table"""
        index = self._hash(key)  # Calculate the initial index using the hash function

        i = 0
        while self.keys[index] is not None:  # If the slot is not empty
            if self.keys[index] == key:  # If the key already exists, update the value
                self.values[index] = value
                return

            i += 1
            index = self._quadratic_probe(index, i)  # Move to the next slot using quadratic probing

        self.keys[index] = key  # Insert the key into the slot
        self.values[index] = value  # Insert the value into the slot

    def delete(self, key):
        """Deletes a key-value pair from the hash table"""
        index = self._hash(key)  # Calculate the initial index using the hash function

        i = 0
        while self.keys[index] is not None:  # If the slot is not empty
            if self.keys[index] == key:  # If the key is found
                self.keys[index] = None  # Remove the key
                self.values[index] = None  # Remove the value
                return

            i += 1
            index = self._quadratic_probe(index, i)  # Move to the next slot using quadratic probing

    def search(self, key):
        """Searches for a key and returns its corresponding value"""
        index = self._hash(key)  # Calculate the initial index using the hash function

        i = 0
        while self.keys[index] is not None:  # If the slot is not empty
            if self.keys[index] == key:  # If the key is found
                return self.values[index]  # Return the corresponding value

            i += 1
            index = self._quadratic_probe(index, i)  # Move to the next slot using quadratic probing

        return None  # Key not found

    def display(self):
        """Displays all key-value pairs in the hash table"""
        for i in range(self.size):
            if self.keys[i] is not None:
                print(f"Key: {self.keys[i]}, Value: {self.values[i]}")





def Linear_search(array,item):
    for i in range(len(array)):
        if array[i]==item:
            print(item,"Item found at index : ",i)
    
    print(-1)



def binary_search(list, item):
    low = 0 
    high = len(list)-1 
    while low <= high: 
        mid = (low + high)
        guess = list[mid]
        if guess == item:
            
            return mid
        if guess > item: 
            high = mid - 1
        else: 
            low = mid + 1
        
    return -1
   

def jump_search(arr, target):
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0

    while arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1

    while arr[prev] < target:
        prev += 1
        if prev == min(step, n):
            return -1

    if arr[prev] == target:
        return prev

    return -1



class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def _hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash_function(key)
        if self.table[index] is None:
            self.table[index] = [(key, value)]
        else:
            for i, (existing_key, existing_value) in enumerate(self.table[index]):
                if existing_key == key:
                    self.table[index][i] = (key, value)
                    break
            else:
                self.table[index].append((key, value))

    def delete(self, key):
        index = self._hash_function(key)
        if self.table[index] is not None:
            for i, (existing_key, existing_value) in enumerate(self.table[index]):
                if existing_key == key:
                    del self.table[index][i]
                    break

    def display(self):
        for index, slot in enumerate(self.table):
            if slot is not None:
                for key, value in slot:
                    print(f"Index: {index}, Key: {key}, Value: {value}")

    def search(self, key):
        index = self._hash_function(key)
        if self.table[index] is not None:
            for existing_key, value in self.table[index]:
                if existing_key == key:
                    return value
        return None





def display_BST_menu():

    print("1: Insert Element\n",
        "2: Delete Element\n",
        "3: Display Tree\n",
        "4: Search\n",
        "5 :Back ",sep="")

def display_queue_menu():
    print("1)Enqueue\n2)Dequeue\n3)Display Queue\n4)Back")


def display_mainMenu():
    print("|  1 : Data Structures ")
    print("|  2 : Algorithms  ")
    print("|  3 : Exit ")

def display_DSA_menu():
    print(L)
    print("   Data Structures Menu")
    print(L)
    print(" 1 : Array")
   
    print(" 2 : Stack"  )
    print(" 3 : Queue " )
    print(" 4 : Linked-List ")
    print(" 5 : Tree")
    print(" 6 : Graph")
    print(" 7 : Hash Tables")
    print(" 8 : Back")
    print(L)
   
def display_DS_submenu():
    os.system("cls")
    print(L)
    print("\t   Data Structures Sub Menu")
    print(L)
    print("1 : Defination")
    print("2 : Implementation")
    print("3 : Back to Data Structures menu " )
    print(L)
def Graph_DS_submenu():
    os.system("cls")
    print(L)
    print("\tGraph Data structure Sub-Menu")
    print(L)
    print("1: Defination")
    print("2: Implementation")
    print("3: Kinds of Graph")
    print("4: Back to Data Structures menu " )
    print(L)



def Algorithm_menu():
    print("1) Searching algorithm ")
    print("2) Sorting algorithm ")
    # print("3) Inserting algorithm ")
    # print("4) Deleting algorithm ") 
    print("3) Back ")
def display_array_menu():
    print("1)Insert\n2)Delete\n3)Display\n4)Back")

def stack_display_menu():
    print("1)Push item\n2)Pop item\n3)Display Stack\n4)Back")


def display_linkedList_menu():
    print("1 :Insert Element\n",
          "2 :Delete Element\n",
          "3 :Display LinkedList\n",
          "4 :Back ",sep="")
    
def display_Tree_menu():
    print("Tree Types menu")
    print("1: Binary Tree")
    print("2: Binary Search Tree")
    print("3: Ternary Tree")
    print("4: AVL Tree")
    print("5: B Tree ")
    print("6: Red-Black Tree")
    print("7: Back")

def display_sorting_menu():
    print("-------------------------------------")
    print("1: Bubble sort\t|5: Counting sort")
    print("2: Merge sort\t|6: buckket sort")
    print("3: heap sort \t|7: Radix sort")
    print("4: Quick sort\t|8: Selection sort")
    print("\t  9: Back")
    print("-------------------------------------")

def display_searching_menu():
    print(L)
    print("1: Linear Search")
    print("2: Binary Search ")
    print("3: Jump Search")
    print("4: Back")
    print(L)


def display_Tree_submenu():
    print("1 :Insert Element\n",
        "2 :Delete Element\n",
        "3 :Display Tree\n",
        "4 :Back ",sep="")
    

def display_Graph_menu():
    print("1: Directed weighted graph")
    print("2: Undirected graph ")
    # print("3: Null graph")
    # print("4: ")
    print("3: Back")

def display_graph_implementation_menu():
    print("1: Insert Vertex\n",
        "2: Delete Vertex\n",
        "3: Display Graph\n",
        "4: Search Vertex\n",
        "5: Insert Edge \n",
        "6: Breadth first search\n",
        "7: Depth First search\n",
        "8: Back ",sep="")

def display_DWgraph_menu():
    print("1: Insert Vertex\n",
        "2: Delete Vertex\n",
        "3: Display Graph\n",
        "4: Search Vertex\n",
        "5: Back ",sep="")



def Display_ternary_tree_menu():
    print("1: Insert Node\n",
        "2: Delete node\n",
        "3: Display ternary Tree\n",
        "4: Search node\n",
        "5: Back",sep="")



def Display_AVL_menu():
    print("1: Insert Node\n",
        "2: Delete node\n",
        "3: Display AVL Tree\n",
        "4: Search node\n",
        "5: Back",sep="")

def Display_BTree_menu():
    print("1: Insert Node\n",
        "2: Delete node\n",
        "3: Display  B Tree\n",
        "4: Search node\n",
        "5: Back",sep="")

def Display_RBTree_menu():
    print("1: Insert Node\n",
        "2: Delete node\n",
        "3: Display Red black Tree\n",
        "4: Search node\n",
        "5: Back",sep="")
    


def HashT_DS_submenu():
    os.system("cls")
    print(L)
    print("  Hash Tables Data structure Sub-Menu")
    print(L)
    print("1: Defination")
    print("2: Implementation")
    print("3: Kinds of Hash Tables")
    print("4: Back to Data Structures menu " )
    print(L)






def display_hash_tables_menu():
    print("1: Insert Node\n",
        "2: Delete node\n",
        "3: Display Hash tables\n",
        "4: Search node\n",
        "5: Back",sep="")




def display_Htables_kinds():
    print("1: Linear Probing hash Table\n",
          "2: Double hashing hash Table\n",
          "3: Separate Chaining Hash Table\n", 
          "4: Quadratic Probing Hash Table\n",
          "5: Back to hash menu",sep="")




def bubble_sort(arr):
    # Bubble sort algorithm implementation
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    print("Bubble Sorted Array:\n", arr)

def selection_sort(arr):
    # Selection sort algorithm implementation
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    print("-------------------------------")
    print("Selection Sorted Array:\n", arr)
    print("-------------------------------")


def merge_sort(arr):
    # Merge sort algorithm implementation
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    print("Merge Sorted Array:", arr)


def quick_sort(arr):
    # Quick sort algorithm implementation
    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i+1], arr[high] = arr[high], arr[i+1]
        return i + 1

    def quick_sort_helper(arr, low, high):
        if low < high:
            pi = partition(arr, low, high)
            quick_sort_helper(arr, low, pi - 1)
            quick_sort_helper(arr, pi + 1, high)

    quick_sort_helper(arr, 0, len(arr) - 1)
    print("Quick Sorted Array:", arr)

def heap_sort(arr):
    # Heap sort algorithm implementation
    def heapify(arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[i] < arr[left]:
            largest = left

        if right < n and arr[largest] < arr[right]:
            largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)

    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

    print("Heap Sorted Array:", arr)


def counting_sort(arr):
    # Find the maximum element in the array
    max_element = max(arr)
    
    # Create a count array to store the count of each element
    count = [0] * (max_element + 1)
    
    # Count the occurrences of each element
    for num in arr:
        count[num] += 1
    
    # Calculate the cumulative count
    for i in range(1, max_element + 1):
        count[i] += count[i - 1]
    
    # Create a sorted array
    sorted_arr = [0] * len(arr)
    
    # Place the elements in the sorted order
    for num in arr:
        sorted_arr[count[num] - 1] = num
        count[num] -= 1
    
    print("Counting sorted array\n",sorted_arr)


def bucket_sort(arr):
    # Find the maximum and minimum values in the array
    max_value = max(arr)
    min_value = min(arr)
    range_value = max_value - min_value + 1
    
    # Create empty buckets
    bucket_count = range_value
    buckets = [[] for _ in range(bucket_count)]
    
    # Distribute elements into buckets based on their range
    for num in arr:
        index = int((num - min_value) * (bucket_count - 1) / range_value)
        buckets[index].append(num)
    
    # Sort each bucket individually
    for i in range(bucket_count):
        buckets[i].sort()
    
    # Concatenate the sorted buckets
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(bucket)
    
    print("Buckket sorted array :\n",sorted_arr,sep="")


def radix_sort(arr):
    # Find the maximum value in the array to determine the number of digits
    max_value = max(arr)
    num_digits = len(str(max_value))
    
    # Perform counting sort for each digit
    for digit in range(num_digits):
        # Create the buckets for each digit (0-9)
        buckets = [[] for _ in range(10)]
        
        # Distribute elements into buckets based on the current digit
        for num in arr:
            bucket_index = (num // 10 ** digit) % 10
            buckets[bucket_index].append(num)
        
        # Concatenate the elements from the buckets
        arr = [num for bucket in buckets for num in bucket]
    
    print("Radix sorted array\n",arr,sep="")

while True:
    os.system("cls")
    print(L)
    # color = colored.fg(120)
    # print(color)
     # color= colored.fg(130)
    # print(color)
    try:
        
        print(L)
        display_mainMenu()
        print(L)
        choice=int(input("Enter your choice (1-3) : "))
        print(L)        
        if choice==1:
            # color=colored.fg(120)
            # print(color)
            os.system("cls")
            while True:
                display_DSA_menu()
                choice=int(input("Enter your choice (1-8): "))
                if choice==1:
                    while True:
                        display_DS_submenu() 
                       
                        choice=int(input("Enter your choice (1-3) : "))
                        if choice==1:
                            # os.system("cls")
                            print("A contiguous collection of data \nvalues that share a common name.\n",
                                "An array is a collection of elements\n",
                                "with the same name and same data type\n", 
                                "stored in contiguous memory locations.",sep="")
                            input()
                        elif choice==2:
                            size=int(input("Enter array Size : "))
                            type_of_array=input("Enter array type(int, float, str)  : ").lower()
                            if type_of_array=='int':
                                array=Array(size,int())
                            elif type_of_array=='float':
                                array=Array(size,float())
                            elif type_of_array=='str':
                                array=Array(size,str())
                            else:
                                print("Invalid type!")
                            
                            while True:
                                display_array_menu()
                                choice=int(input("Enter your choice (1-4) : "))
                                if choice==1:
                                    # item=input("Enter data to be inserted : ")
                                    # index=int(input("Enter the index : "))
                                    # array.insert(item,index)
                                    data=input("Enter item or type quit : ")
                                    while data!='quit': 
                                        if type_of_array=='int':
                                            data=int(data)
                                        elif type_of_array=='float':
                                            data=float(data)
                                        index=int(input("Enter the index : "))
                                        array.insert(data,index)
                                        array.display()
                                        data=input("Enter item you want to add or type quit : " )
                                elif choice==2:
                                    item=input("Enter the Data to be deleted : ")
                                    array.delete(item)
                                elif choice==3:
                                    array.display()
                                elif choice==4:
                                    break
                                
                                else:
                                    print("Invalid choice!")
                        
                        elif choice==3:
                            break


                        else:
                            print("Invalid choice!")
                elif choice==2:
                    # color=colored.fg(145)
                    # print(color)
                    stack=Stack()
                    while True:
                        display_DS_submenu()
                        choice=int(input("Enter your choice (1-3): "))
                    
                        if choice==1:
                            print("Stack is a linear data structure based on\n",
                                "the Last-In-First-Out (LIFO) principle. It\n",
                                "supports two main operations: push(insert element)\n",
                                "and pop (remove element).",sep="")
                            input()
                        elif choice==2:    
                            while True:
                                stack_display_menu()
                                choice=int(input("Enter your choice (1-4): "))
                                if choice==1:
                                    item=input("Enter the data to push : ")
                                    stack.push(item)
                                elif choice==2:
                                    stack.pop()
                                elif choice==3:
                                    stack.display()
                                elif choice==4:
                                    break
                                else:
                                    print("Invalid choice!")

                        elif choice==3:
                            break
                        else:
                            print("Invalid choice!")

                elif choice==3:
                    # color=colored.fg(165)
                    # print(color)
                    queue=Queue()
                    while True:
                        display_DS_submenu()
                        print("-------------------------------")
                        choice=int(input("Enter your choice (1-3): "))
                        if choice==1:
                            print("-------------------------------")
                            print("Queue is a linear data structure based\n",
                                "on the First-In-First-Out (FIFO) principle.\n",
                                "It supports two main operations: enqueue(insert element)\n",
                                "and dequeue (remove element).",sep="")
                            print("-------------------------------")
                            input()
                        if choice==2:
                            while True:
                                display_queue_menu()
                                choice=int(input("Enter your choice(1-4): "))
                                if choice==1:
                                    data=input("Enter data to enqueue : ")
                                    queue.enqueue(data)   
                                elif choice==2:
                                    queue.dequeue()
                                elif choice==3:
                                    queue.display()
                                elif choice==4:
                                    break 
                                else:
                                    print("Invalid choice!")
                        elif choice==3:
                            print("--------------------------------")
                            break
                            
                        else:
                            print("Invalid choice ")
                            
                elif choice==4:
                    # color=colored.fg(175)
                    # print(color)
                    while True:
                        linkedlist=LinkedList()
                        display_DS_submenu()
                        choice=int(input("Enter your choice : "))
                        if choice==1:
                            print("-------------------------------------")
                            print("Linked List is a linear data structure\n",
                                "where the elements are not stored at contiguous\n",
                                "memory locations. Each element of the linked list \n",
                                "is called node. Each node in the linked list contains\n",
                                "two fields, one for storing the data and another\n",
                                "for storing the address of the next node.",sep="")
                            print("-------------------------------------")
                            input()
                        elif choice==2:
                            while True:
                                display_linkedList_menu()
                                choice=int(input("Enter choice (1-5): "))
                                if choice==1:
                                    data=input("Enter data to add :")
                                    linkedlist.insert(data)
                                elif choice==2:
                                    data=input("Enter data to delete :")
                                    linkedlist.Delete(data)
                                elif choice==3:
                                    linkedlist.display()

                                elif choice==4:
                                    print("--------------------------------")
                                    break
                                else:
                                    print("Invalid choice!")
                        elif choice==3:
                            print("--------------------------------")
                            break
                        else:
                            print("Invalid choice!")



                elif choice==5:
                    # color=colored.fg(125)
                    # print(color)
                    while True:
                        display_Tree_menu()
                        choice=int(input("Enter your choice(1-7): "))
                        if choice==1:
                            display_DS_submenu()
                            choice=int(input("Enter your choice(1-3): "))
                            if choice==1:
                                print(L)
                                print("Binary Tree is defined as a tree data structure\n",
                                    "where each node has at most 2 children. Since each\n",
                                    "element in a binary tree can have only 2 children,\n",
                                     "we typically name them the left and right child.",sep="")
                                print(L)
                                input()
                                image = Image.open('BTimage.png')
                                image.show()
                            elif choice==2:
                                tree=BinaryTree()
                                while True:
                                    display_Tree_submenu()
                                    choice=int(input("Enter your choice(1-4): "))
                                    if choice == 1:
                                        data=input("Enter data to be inserted : ")
                                        while data!= 'q':
                                            tree.insert(data)
                                            data=input("Enter data to be inserted or type 0 for quit: ")
                                        print("Value inserted successfully.")
                                    elif choice == 2 :
                                        data = input ("Enter data to delete : ")
                                        tree.delete(data)
                                        print("Value deleted successfully.")
                                    elif choice == 3:
                                        print("Binary tree!")
                                        tree.display()
                                    elif choice == 4:
                                        break
                                        
                                    else:
                                        print("Invalid choice!")
                            elif choice==3:
                                break
                            else:
                                print("Invalid choice!")

                        elif choice==2:
                            while True:
                                display_DS_submenu()
                                choice=int(input("Enter your choice(1-3): "))
                                if choice ==1:
                                    print(L)
                                    print("Binary Search Tree is a node-based binary tree data structure")
                                    print("The left subtree of a node contains only nodes with keys lesser than the nodes key.")
                                    print("The right subtree of a node contains only nodes with keys greater than the nodes key.")
                                    print("The left and right subtree each must also be a binary search tree.")
                                    print(L)
                                elif choice==2:
                                    BST=BinarySearchTree()
                                    while True:
                                        display_BST_menu()
                                        choice=int(input("Enter your choice(1-5): "))
                                        if choice == 1:
                                            data=input("Enter data to be inserted : ")
                                            while data!='q':
                                                BST.insert(data)
                                                data=input("Enter data to be inserted or type q for quit: ")
                                            print("Value inserted successfully.")
                                        elif choice == 2 :
                                            data = input ("Enter data to delete : ")
                                            BST.delete(data)
                                            print("Value deleted successfully.")
                                        elif choice == 3:
                                            print("Binary Search tree!")
                                            BST.display()
                                        elif choice == 4:
                                            item = input("Enter item to search for : ")
                                            BST.search(item)
                                        elif choice == 5:
                                            break
                                        else:
                                            print("Invalid choice!")
                                elif choice == 3:
                                    break
                                else:
                                    print("Invalid choice!")
                                        
                                # elif choice == 7: 
                                #     break
                                # else:
                                #     print("Invalid choice!")

                        elif choice == 3:
                                T_tree=TernaryTree()
                                while True :
                                    display_DS_submenu()
                                    choice=int(input("Enter your choice(1-5): "))
                                    if choice == 1:
                                        print("A Ternary Tree is a tree data structure in which each node\n",
                                              "has at most three child nodes, usually distinguished as\n",
                                                "“left”, “mid” and “right”",sep="")
                                        image=Image.open("ternary_tree.png")
                                        image.show()
                                        input()
                                    elif choice == 2:
                                        while True:
                                            Display_ternary_tree_menu()
                                            choice=int(input("Enter your choice(1-5) : "))
                                            if choice == 1:
                                                data=input("Enter data to be inserted : ")
                                                while data!='q':
                                                    T_tree.insert(data)
                                                    data=input("Enter data to be inserted or type q for quit: ")
                                                print("Value inserted successfully.")
                                            elif choice == 2 :
                                                data = input ("Enter data to delete : ")
                                                T_tree.delete(data)
                                                print("Value deleted successfully.")
                                            elif choice == 3:
                                                print("Ternary tree!")
                                                T_tree.display()
                                            elif choice == 4:
                                                item = input("Enter item to search for : ")
                                                if T_tree.search(item):
                                                    print(f"{item } found in the Tree!")
                                                else:
                                                    print(f"{item} not found in tree!")
                                                #  print(T_tree.search(item))
                                            elif choice == 5:
                                                break
                                            else:
                                                print("Invalid choice!")
                                    

                                    elif choice == 3:
                                        break
                                    else:
                                        print("Invalid choice!")
                        elif choice == 4:
                            avlTree=AVLTree()
                            while True :
                                    display_DS_submenu()
                                    choice=int(input("Enter your choice(1-3): "))
                                    if choice == 1:
                                        print("An AVL tree defined as a self-balancing Binary Search Tree (BST)\n",
                                            "where the difference between heights of left and right subtrees for\n",
                                            "any node cannot be more than one."
                                            "The difference between the heights of the left subtree and the right\n",
                                            "subtree for any node is known as the balance factor of the node.",sep="")
                                        
                                        image=Image.open("avltree.png")
                                        image.show()
                                        print(L)
                                        input()

                                    elif choice == 2:
                                        while True:
                                            Display_AVL_menu()
                                            choice=int(input("Enter your choice(1-5) : "))
                                            if choice == 1:
                                                data=input("Enter data to be inserted : ")
                                                while data!='q':
                                                    avlTree.insert(data)
                                                    data=input("Enter data to be inserted or type q for quit: ")
                                                print("Value inserted successfully.")
                                            elif choice == 2 :
                                                data = input ("Enter data to delete : ")
                                                avlTree.delete(data)
                                                print("Value deleted successfully.")
                                            elif choice == 3:
                                                print("Binary Search tree!")
                                                avlTree.display()
                                            elif choice == 4:
                                                item = input("Enter item to search for : ")
                                                # avlTree.search(item)
                                                if avlTree.search(item):
                                                    print(f"{item } found in the Tree!")
                                                else:
                                                    print(f"{item} not found in tree!")
                                            elif choice == 5:
                                                break
                                            else:
                                                print("Invalid choice!")

                                    elif choice ==3:
                                        break
                                    else:
                                        print("Invalid choice!")
                        elif choice == 5:
                            degree=int(input("Enter the degree of tree : "))
                            btree=BTree(degree)
                            while True :
                                    display_DS_submenu()
                                    choice=int(input("Enter your choice(1-3): "))
                                    if choice == 1:
                                        print("A B-tree is a self-balancing tree where all the leaf nodes are\n",
                                              "at the same level which allows for efficient searching, insertion\n",
                                               "and deletion of records. Because of all the leaf nodes being on the\n",
                                                "same level, the access time of data is fixed regardless of the size\n",
                                                 "of the data set.",sep="")
                                        
                                        # image=Image.open("avltree.png")
                                        # image.show()
                                        print(L)
                                       

                                    elif choice == 2:
                                        
                                        
                                        while True:
                                            Display_BTree_menu()
                                            choice=int(input("Enter your choice(1-5) : "))
                                            if choice == 1:
                                                data=input("Enter data to be inserted : ")
                                                while data!='q':
                                                    btree.insert(data)
                                                    data=input("Enter data to be inserted or type q for quit: ")
                                                print("Value inserted successfully.")
                                            elif choice == 2 :
                                                data = input ("Enter data to delete : ")
                                                # if btree.delete(data)==None:
                                                #     print(f"{data} not found in Tree")
                                                # else:
                                                btree.delete(data)
                                                print("Value deleted successfully.")
                                            elif choice == 3:
                                                print("Binary Search tree!")
                                                btree.display()
                                            elif choice == 4:
                                                item = input("Enter item to search for : ")
                                                # avlTree.search(item)
                                                if btree.search(item):
                                                    print(f"{item } found in the Tree!")
                                                else:
                                                    print(f"{item} not found in tree!")
                                            elif choice == 5:
                                                break
                                            else:
                                                print("Invalid choice!")

                                    elif choice ==3:
                                        break
                                    else:
                                        print("Invalid choice!")
                        elif choice == 6:
                            rbtree=RedBlackTree()
                            while True :
                                display_DS_submenu()
                                choice=int(input("Enter your choice(1-3): "))
                                if choice == 1:
                                    print("Red-Black tree is a binary search tree in which every node\n",
                                          "is colored with either red or black. It is a type of self balancing\n",
                                          "binary search tree. It has a good efficient worst case running time complexity",sep="")
                                    
                                    # image=Image.open("avltree.png")
                                    # image.show()
                                    print(L)
                                    

                                elif choice == 2:
                                    while True:
                                        Display_RBTree_menu()
                                        choice=int(input("Enter your choice(1-5) : "))
                                        if choice == 1:
                                            data=input("Enter data to be inserted : ")
                                            # while data!='q':
                                            rbtree.insert(data)
                                            #     data=input("Enter data to be inserted or type q for quit: ")
                                            print("Value inserted successfully.")
                                        elif choice == 2 :
                                            data = input ("Enter data to delete : ")
                                            # if btree.delete(data)==None:
                                            #     print(f"{data} not found in Tree")
                                            # else:
                                            rbtree.delete(data)
                                            print("Value deleted successfully.")
                                        elif choice == 3:
                                            print("Red Black tree!")
                                            rbtree.display()
                                        elif choice == 4:
                                            item = input("Enter item to search for : ")
                                            # avlTree.search(item)
                                            if rbtree.search(item):
                                                print(f"{item } found in the Tree!")
                                            else:
                                                print(f"{item} not found in tree!")
                                        elif choice == 5:
                                            break
                                        else:
                                            print("Invalid choice!")

                                elif choice ==3:
                                    break
                                else:
                                    print("Invalid choice!")




                        elif choice ==7:
                            break
                        else:
                            print("Invalid choice!")






                elif choice==6:
                    # color=colored.fg(151)
                    # print(color)
                    while True:
                        Graph_DS_submenu()
                        choice=int(input("Enter your choice(1-4): "))
                        if choice == 1:
                            print("A Graph is a non-linear data structure consisting of vertices and edges.")
                            print("The vertices are sometimes also referred to as nodes and the edges are")
                            print("lines or arcs that connect any two nodes in the graph. More formally ")
                            print("A Graph is composed of a set of vertices( V ) and a set of edges( E ). ")
                            print("The graph is denoted by G(E, V).")
                            image=Image.open("graph.png")
                            image.show()
                        elif choice == 2:
                            graph=Graph()
                            while True :
                                display_graph_implementation_menu()
                                print(L)
                                choice=int(input("Enter your choice(1-5): "))
                                if choice == 1:
                                    data=input("Enter data to be inserted : ")
                                    graph.insert_vertex(data)
                                    print("Value inserted successfully.")
                                elif choice == 2 :
                                    data = input ("Enter data to delete : ")
                                    graph.delete_vertex(data)
                                    print("Value deleted successfully.")
                                elif choice == 3:
                                    print("Binary Search tree!")
                                    graph.display()
                                elif choice == 4:
                                    item = input("Enter item to search for : ")
                                    graph.search_vertex(item)
                                elif choice == 5:
                                    edge1=input("Enter edge first : ")
                                    edge2=input("Enter edge Second : ")
                                    graph.insert_edge(edge1,edge2)
                                elif choice == 6:
                                    vertex=input("Enter first vertex to B search for : ")
                                    graph.breadth_first_search(vertex)
                                elif choice ==7:
                                    vertex=input("Enter first vertex to Depth search for : ")
                                    graph.depth_first_search(vertex)
                                elif choice ==8:    
                                    break
                                else:
                                    print("Invalid choice!")

                        elif choice == 3:
                            os.system("cls")
                            while True:
                                print(L)
                                display_Graph_menu()
                                print(L)                                
                                choice = int(input("Enter your choice  (1-3): "))
                                if choice == 1 :
                                    while True:
                                        DWGraph=DirectedWeightedGraph()
                                        display_DS_submenu()
                                        choice = int(input("Enter your choice  (1-3): "))
                                        if choice ==1:       
                                            print("Defination")
                                        elif choice ==2:
                                            while True:
                                                display_DWgraph_menu()               
                                                choice =int(input("Enter Your choice (1-5) : "))
                                                if choice == 1:
                                                    edge1=input("Enter Source Edge :")
                                                    edge2=input("Enter Distination Edge :")
                                                    wgt=input("Enter the weight : ")
                                                    DWGraph.insert_edge(edge1,edge2,wgt)
                                                elif choice == 2:
                                                    edge1=input("Enter Source Edge :")
                                                    edge2=input("Enter Distination Edge :")
                                                    DWGraph.delete_edge(edge1,edge2)
                                                    print("work on this part")
                                                    # if E1 and E2:
                                                    #     print("Edges deleted successfully!")
                                                    # else:
                                                    #     print("Edges not exist!")
                                                elif choice ==3 :
                                                    DWGraph.display()

                                                elif choice == 4:
                                                    edge1=input("Enter Source Edge :")
                                                    edge2=input("Enter Distination Edge :")
                                                    weight = DWGraph.search(edge1,edge2)
                                                    if weight is not None:
                                                        print(f"Weight from {edge1}to {edge2}: {weight}")
                                                    else:
                                                        print("Edge not found.")
                                                elif choice == 5:
                                                    break
                                                else:
                                                    print(L)
                                                    print("Invalid Choice!")
                                                    print(L)
                                        elif choice == 3:
                                            break
                                        else:
                                            print(L)
                                            print("Invalid Choice!")
                                            print(L)
                                            
                                elif choice ==2:
                                    UDgraph=UndirectedGraph()
                                    
                                    while True:
                                        display_DS_submenu()
                                        choice = int(input("Enter your choice  (1-3): "))
                                        if choice ==1:       
                                            print("Defination")
                                        elif choice ==2:
                                            while True:
                                                display_DWgraph_menu()               
                                                choice =int(input("Enter Your choice (1-5) : "))
                                                if choice == 1:
                                                    edge1=input("Enter Source Edge :")
                                                    edge2=input("Enter Distination Edge :")
                                                    
                                                    UDgraph.insert_edge(edge1,edge2)
                                                elif choice == 2:
                                                    edge1=input("Enter Source Edge :")
                                                    edge2=input("Enter Distination Edge :")
                                                    UDgraph.delete_edge(edge1,edge2)
                                                    print("work on this part")
                                                    # if E1 and E2:
                                                    #     print("Edges deleted successfully!")
                                                    # else:
                                                    #     print("Edges not exist!")
                                                elif choice ==3 :
                                                    UDgraph.display()

                                                elif choice == 4:
                                                    edge1=input("Enter Source Edge :")
                                                    edge2=input("Enter Distination Edge :")
                                                    weight = UDgraph.search(edge1,edge2)
                                                    if weight:
                                                        print(f"Weight from {edge1} to {edge2} : found")
                                                    else:
                                                        print("Edge not found.")
                                                elif choice == 5:
                                                    break
                                                else:
                                                    print(L)
                                                    print("Invalid Choice!")
                                                    print(L)
                                        elif choice == 3:
                                            break
                                        else:
                                            print(L)
                                            print("Invalid Choice!")
                                            print(L)
                                        

                                
                                elif choice == 3 :
                                    break
                                else:
                                    print(L)
                                    print("Invalid Choice!")
                                    print(L)
                            

                                # elif choice == 4 :
                                #    break
                                # else:
                                #     print(L)
                                #     print("Invalid Choice!")
                                #     print(L)
                        


                        elif choice == 4 :
                            break
                        else:
                            print(L)
                            print("Invalid Choice!")
                            print(L)
                elif choice == 7:
                    # color=colored.fg(126)
                    # print(color)
                    while True:
                        HashT_DS_submenu()
                        choice =int(input("Enter your choice (1-4): "))
                        if choice == 1:
                            print(L)
                            print("A Hash table is defined as a data structure used to insert,\n",
                                  "look up, and remove key-value pairs quickly. It operates on the\n",
                                "hashing concept, where each key is translated by a hash function into\n",
                                "a distinct index in an array. The index functions as a storage location\n",
                                "for the matching value. In simple words, it maps the keys with the value.",sep="")
                            print(L)
                            input()

                        elif choice == 2:
                            print(L)
                            size=int(input("Enter the hash table size :"))
                            print(L)
                            hashT=HashTable(size)
                            print(L)
                            while True:
                                display_hash_tables_menu()
                                choice =int(input("Enter your choice (1-4): "))
                                if choice ==1:
                                    key = input("Enter key for value : ")
                                    value=input("Enter value : ")
                                    hashT.insert(key,value)
                                elif choice == 2:
                                    key = input("Enter key to delete : ")
                                    hashT.delete(key)
                                elif choice==3:
                                    hashT.display()
                                elif choice == 4:
                                    key = input("Enter key to Search : ")
                                    hashT.search(key)
                                    print("Work on this ")
                                elif choice == 5:
                                    break
                                else:
                                    print("Invalid choice!")
                        elif choice == 3:
                            while True :
                                print(L)
                                display_Htables_kinds()
                                print(L)
                                choice=int(input("Enter your choice (1-5): "))
                                if choice == 1:
                                    
                                    print(L)
                                    size=int(input("Enter the hash table size :"))
                                    print(L)    
                                    linearHash=LinearProbingHashTable(size)
                                    while True:
                                        print(L)
                                        display_DS_submenu()
                                        choice = int(input("Enter Your Choice(1-3) : "))
                                        if choice == 1:
                                            print("A linear probing hash table is a data structure that stores key-value pairs\n",
                                                  "in an array of fixed size. It uses a hash function to calculate an initial index\n",
                                                "for a given key. When a collision occurs, meaning the calculated index is already occupied,\n",
                                                 "linear probing checks the next consecutive slot in the array until an empty slot is found.\n",
                                                  "The key and value are then inserted into that slot.",sep="")
                                            input()       
                                        elif choice ==2:
                                            while True:
                                                display_hash_tables_menu()
                                                
                                                print("Linear probing Hash Table")
                                                choice =int(input("Enter Your choice (1-5):"))
                                                if choice == 1:
                                                    key = input("Enter key for value : ")
                                                    value=input("Enter value : ")
                                                    linearHash.insert(key, value)
                                                elif choice == 2:
                                                    key = input("Enter key to delete : ")
                                                    linearHash.delete(key)
                                                    print(L)
                                                elif choice == 3:
                                                    print(L)
                                                    linearHash.display()
                                                    print(L)
                                                elif choice == 4:
                                                    print(L)
                                                    key = input("Enter key to Search : ")
                                                    linearHash.search(key)
                                                    print("Work on this ")
                                                    print(L)
                                                elif choice == 5:
                                                    print(L)
                                                    break
                                                else:
                                                    print("Invalid choice!")

                                        elif choice == 3:
                                            break
                                        else:
                                            print("Invalid choice!")
                                elif choice == 2:
                                    print(L)
                                    
                                    print("Double Hashing Hash Table")
                                    print(L)
                                    size=int(input("Enter the hash table size :"))
                                    print(L)    
                                    doubleHash=DoubleHashingHashTable(size)
                                    display_hash_tables_menu()
                                    while True:
                                        print(L)
                                        display_DS_submenu()
                                        choice = int(input("Enter Your Choice(1-3) : "))
                                        if choice == 1:
                                            print("A double hashing hash table is a data structure that uses two hash functions\n",
                                                "to handle collisions and store key-value pairs. The hash table is implemented as\n",
                                                "an array of fixed size. The first hash function, called the primary hash function,\n",
                                                "is used to calculate the initial index for a given key. If the calculated index is\n",
                                                "already occupied, collisions occur.",sep="") 
                                            input()       
                                        elif choice ==2:
                                            while True:
                                                display_hash_tables_menu()
                                                
                                                print("Double Hashing Hash Table")
                                                choice =int(input("Enter Your choice (1-5):"))
                                                if choice == 1:
                                                    key = input("Enter key for value : ")
                                                    value=input("Enter value : ")
                                                    doubleHash.insert(key, value)
                                                elif choice == 2:
                                                    key = input("Enter key to delete : ")
                                                    doubleHash.delete(key)
                                                    print(L)
                                                elif choice == 3:
                                                    print(L)
                                                    doubleHash.display()
                                                    print(L)
                                                elif choice == 4:
                                                    print(L)
                                                    key = input("Enter key to Search : ")
                                                    doubleHash.search(key)
                                                    print("Work on this ")
                                                    print(L)
                                                elif choice == 5:
                                                    print(L)
                                                    break
                                                else:
                                                    print("Invalid choice!")

                                        elif choice == 3:
                                            break
                                        else:
                                            print("Invalid choice!")
                                elif choice == 3:
                                   
                                    size=int(input("Enter the hash table size :"))
                                    print(L)    
                                    seperateHash=SeparateChainingHashTable(size)
                                    print(L)
                                    display_hash_tables_menu()
                                    print("Seperate Chaining Hash Table")
                                    print(L)
                                    while True:
                                        print(L)
                                        display_DS_submenu()
                                        choice = int(input("Enter Your Choice(1-3) : "))
                                        if choice == 1:
                                            print("A separate chaining hash table is a data structure that stores key-value pairs\n",
                                                  "using an array of linked lists. The hash table uses a hash function to calculate\n",
                                                "an index for a given key. When a collision occurs, meaning multiple keys map to the same\n",
                                                "index, separate chaining creates a linked list at that index to handle the collisions.",sep="") 
                                            input()       
                                        elif choice ==2:
                                            while True:
                                                display_hash_tables_menu()
                                                
                                                print("Seperate Chaining Hash Table")
                                                choice =int(input("Enter Your choice (1-5):"))
                                                if choice == 1:
                                                    key = input("Enter key for value : ")
                                                    value=input("Enter value : ")
                                                    seperateHash.insert(key, value)
                                                elif choice == 2:
                                                    key = input("Enter key to delete : ")
                                                    seperateHash.delete(key)
                                                    print(L)
                                                elif choice == 3:
                                                    print(L)
                                                    seperateHash.display()
                                                    print(L)
                                                elif choice == 4:
                                                    print(L)
                                                    key = input("Enter key to Search : ")
                                                    seperateHash.search(key)
                                                    print("Work on this ")
                                                    print(L)
                                                elif choice == 5:
                                                    print(L)
                                                    break
                                                else:
                                                    print("Invalid choice!")

                                        elif choice == 3:
                                            break
                                        else:
                                            print("Invalid choice!")
                                elif choice == 4:
                                   
                                    size=int(input("Enter the hash table size :"))
                                    print(L)    
                                    quadriticHash=QuadraticProbingHashTable(size)
                                    print(L)
                                    display_hash_tables_menu()
                                    print("Quadritic probing Hash Table")
                                    print(L)
                                    while True:
                                        print(L)
                                        display_DS_submenu()
                                        choice = int(input("Enter Your Choice(1-3) : "))
                                        if choice == 1:
                                            print("A quadratic probing hash table is a data structure that stores key-value\n",
                                                "pairs in an array using a hash function to calculate an initial index for a given key.\n",
                                                "When a collision occurs, meaning the calculated index is already occupied, quadratic\n",
                                                "probing is used to find the next available slot in the table.",sep="") 
                                            input()       
                                        elif choice ==2:
                                            while True:
                                                display_hash_tables_menu()
                                                print("Quadritic probing Hash Table")
                                                choice =int(input("Enter Your choice (1-5):"))
                                                if choice == 1:
                                                    key = input("Enter key for value : ")
                                                    value=input("Enter value : ")
                                                    quadriticHash.insert(key, value)
                                                elif choice == 2:
                                                    key = input("Enter key to delete : ")
                                                    quadriticHash.delete(key)
                                                    print(L)
                                                elif choice == 3:
                                                    print(L)
                                                    quadriticHash.display()
                                                    print(L)
                                                elif choice == 4:
                                                    print(L)
                                                    key = input("Enter key to Search : ")
                                                    quadriticHash.search(key)
                                                    print("Work on this ")
                                                    print(L)
                                                elif choice == 5:
                                                    print(L)
                                                    break
                                                else:
                                                    print("Invalid choice!")

                                        elif choice == 3:
                                            break
                                        else:
                                            print("Invalid choice!")
                                elif choice == 5:
                                    break
                                else:
                                    print("Invalid Choice!")

                        elif choice ==4:
                            break
                        else:
                            print("Invalid choice!")

                        



                   
                
                
                elif choice==8:
                    # color=colored.fg(138)
                    # print(color)
                    print("Back to Main mneu")
                    break
                else:
                    print("Invalid Choice!")
                
        elif choice==2:
            while True:
                Algorithm_menu()
                print(L)
                print("This is the array now choose a search to search it.")
                array=[100,2,34,33,55,44,34,54,56,3,1,0]
                print(array)
                print(L)
                choice=int(input("Enter your choice (1-3) : "))
                if choice == 1 :
                    while True:
                        display_searching_menu()
                        choice = int(input("Enter your choice (1-4) : "))
                        if choice == 1: 
                            print(L)
                            print(array)
                            print(L)
                            item=int(input("Enter the number to search for : "))
                            Linear_search(array,item)
                        elif choice == 2:
                            os.system("cls")
                            print(L)
                            array.sort()
                            print(array)
                            print(L)
                            
                            item=int(input("Enter number to binary search for : " ))
                            BS=binary_search(array,item)
                            
                            print(L)
                            if  BS!=-1:
                                print(f"Element {item} found in array")
                            else:
                                print(f"Element {item} not found in the array.")

                        elif choice == 3:
                            print(L)
                            array.sort()
                            print(array)

                            print(L)
                            target=int(input("Enter the number to jump search for : "))
                            result = jump_search(array, target)
                            if result!= -1:
                                print(f"Element {target} found at index {result}")
                            else:
                                print(f"Element {target} not found in the array.")


                        elif choice == 4:
                            break

                        else:
                            print("Invalid choice!")





                elif choice == 2 :
                    
                    while True:
                        print("---------------------------------------")
                        # print("This is the array now choose a sort to sort it.")
                        array=[100,2,34,33,55,44,34,54,56,3,1,0]
                        # print(array)
                        display_sorting_menu()
                        
                        print("---------------------------------------")
                        choice= int(input("Enter a choice (1-9): "))
                        start_time = time.time()
                        
                        if choice== 1 :
                            bubble_sort(array)
                        elif choice == 2:
                            merge_sort(array)
                        elif choice == 3:
                            heap_sort(array)
                        elif choice ==4:
                            quick_sort(array)
                        elif choice == 5 :
                            counting_sort(array)
                        elif choice == 6:
                            bucket_sort(array)
                        elif choice == 7:
                            radix_sort(array)
                        elif choice == 8:
                            selection_sort(array)
                        elif choice == 9:
                            break
                        else:
                            print("Invalid  choice!")

                        end_time = time.time()
    
                        execution_time = end_time - start_time

                        # print("Sorted array:", array)
                        print("Time taken:", execution_time, "seconds")

                elif choice==3:
                    break
                else:
                    print("Invalid choice!")
                    print(L)    
                            
        elif choice==3:
            print("Exiting the program...")
            break
        else:
            print("Invalid choice!" )

    except ValueError:
        print("-----------------------------------------------")
        print("You cannot Enter string while choosing choice!")
        print("Please Enter valid numbers for choosing choice!")
        print("-----------------------------------------------")

    







# class Array:
#     def __init__(self,array_type,size):
#         self.array_type=array_type
#         self.size=size
#         self.array=[0]*size
#     def insert(self):
#         self.choice=input("Enter the Record  :" )
#         while self.choice !="quit":
#             if self.choice:
#                 self.array.append(self.choice)
#             else:
#                 print("cannot add other data types just :",self.array_type)
#             self.choice=input("Add record or type quit :" )
#         self.array.remove("quit")
#         return self.array 
#     def delete(self):

#         self.choice=input("delt record or type quit :" )
#         print("Here is the array ")
#         print(self.array)
#         while self.choice !="quit":
#             if self.choice==self.array_type:
                
#                 self.array.remove(self.choice)
#             else:
#                 print("Item not found ")
#             self.choice=input("delt record or type quit :" )   
#         return self.array
#     def display(self):
#         print("Here is the array ")
#         print(self.array)



#  display_DS_submenu()
#                         choice=int(input("Enter your choice (1-3): "))
#                         if choice == 1:
#                             print("-----------------------------------------")
#                             print("Tree is a data structure that is used to store\n",
#                                   "data in a hierarchy. Tree is a non-linear data\n",
#                                    "structure. Each element of the tree is known as node.\n",
#                                     "The top element of the tree is known as the root.\n" ,sep="")
#                             print("------------------------------------------")
#                             image = Image.open('image.png')
#                             image.show()

#                         elif choice == 2:
#                             while True:
#                                 display_Tree_menu()
#                                 choice= int(input("Enter your choice(1-7) : "))
#                                 if choice == 1:
#                                     while True:
#                                         display_Tree_submenu()
#                                         choice =int(input("Enter your choice (1-4) : "))
                                            
