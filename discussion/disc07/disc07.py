# discussion 07

# Object Oriented Programming
# 01 - use interative to check answers
class Student:
    students = 0 # this is a class attribute

    def __init__(self, name, staff):
        self.name = name # this is an instance attribute
        self.understanding = 0
        Student.students += 1
        print("There are now", Student.students, "students")
        staff.add_student(self)

    def visit_office_hours(self, staff):
        staff.assist(self)
        print("Thanks, " + staff.name)


class Professor:

    def __init__(self, name):
        self.name = name
        self.students = {}

    def add_student(self, student):
        self.students[student.name] = student

    def assist(self, student):
        student.understanding += 1


# 02 MinList
# In this question, we will implement a special version of a list called a MinList.
# A MinList acts similarly to a list in that you can append items and pop items from it,
# but it only can pop the smallest number.
# Implement the class MinList such it contains the following methods:
# 1. append(self, item): add an element to the MinList
# 2. pop(self): remove and return the smallest element.
# Each instance also contains an attribute size that represents how many elements it contains. 
# Remember to update size in append and pop!
# When you initialize a MinList, it will start out with no elements.
class MinList:
    """A list that can only pop the smallest element """
    
    def __init__(self):
        self.items = []
        self.size = 0
    
    def append(self, item):
        """Appends an item to the MinList
        >>> m = MinList()
        >>> m.append(4)
        >>> m.append(2)
        >>> m.size
        2
        """
        self.items.append(item)
        self.size = len(self.items)

    def pop(self):
        """ 
        Removes and returns the smallest item from the MinList
        >>> n = MinList()
        >>> n.append(4)
        >>> n.append(1)
        >>> n.append(5)
        >>> n.pop()
        1
        >>> n.size
        2
        """
        min_value = min(self.items)
        value_index = self.items.index(min_value)
        m = self.items.pop(value_index)
        self.size = len(self.items)
        return m
    # 我这里犯了一个错误，我以为pop就可以直接返回删掉的值，但是由于封装在这个方法里
    # 在pop之后又有更新self.size，pop返回值没有显示，无法通过doctest。
    # 参考了网上的解法，需要使用return。我自己写的代码如下：
    # min_value = min(self.items)
    # value_index = self.items.index(min_value)
    # self.items.pop(value_index)
    # self.size = len(self.items)


# 03
# We now want to write three di erent classes, Server, Client, and Email to simulate email. 
# We suggest that you approach this problem by first filling out the Email class, 
# then fill out the register client method of Server, then implement the Client class,
# and lastly fill out the send method of the Server class.

class Email:
    """
    Every email object has 3 instance attributes: 
    the message, the sender name, and the recipient name.
    """

    def __init__(self, msg, sender_name, recipient_name):
        self.msg = msg
        self.sender_name = sender_name
        self.recipient_name = recipient_name


class Server:
    """
    Each Server has an instance attribute clients,
    which is a dictionary that associates client names with client objects.
    """
    
    def __init__(self):
        self.clients = {}
    
    def send(self, email):
        """
        Take an email and put it in the inbox of the client it is addressed to.
        """
        recipient = self.clients[email.recipient_name]
        recipient.receive(email)


    def register_client(self, client, client_name):
        """
        Takes a client object and client_name 
        and adds them to the clients instance attribute.
        """
        self.clients[client_name] = client


class Client:
    """
    Every Client has instance attributes 
    name (which is used for addressing emails to the client), 
    server(which is used to send emails out to other clients), 
    and inbox (a list of all emails the client has received).
    """
    def __init__(self, server, name):
        self.inbox = []
        self.server = server
        self.name = name
    
    def compose(self, msg, recipient_name):
        """
        Send an email with the given message msg to the given recipient client.
        """
        mail = Email(msg, self.name, recipient_name)
        self.server.send(mail)
        

    def receive(self, email):
        """
        Take an email and add it to the inbox of this client.
        """
        self.inbox.append(email)


# Inheritance

# 01
class Pet():
    def __init__(self, name, owner):
        self.is_alive = True
        # It's alive!!!
        self.name = name
        self.owner = owner

    def eat(self, thing):
        print(self.name + " ate a " + str(thing) + "!")

    def talk(self):
        print(self.name)


class Dog(Pet):
    def talk(self):
        print(self.name + ' says woof!')


class Cat(Pet):
    def __init__(self, name, owner, lives=9):
        Pet.__init(self, name, owner)
        self.lives = lives
    
    def talk(self):
        """ Print out a cat's greeting.
        >>> Cat('Thomas', 'Tammy').talk()
        Thomas says meow!
        """
        print(self.name, "says meow!")

    def lose_life(self):
        """Decrements a cat's life by 1. When lives reaches zero, 'is_alive'
        becomes False. If this is called after lives has reached zero, print out
        that the cat has no more lives to lose.
        """
        if self.lives == 0:
            print(self.name, 'has no more lives to lose')
        else:
            self.lives -= 1
            if self.lives == 0:
                self.is_alive = False


# 
# Tutorial: More cats! Fill in this implemention of a class called NoisyCat, 
# which is just like a normal Cat. However, NoisyCat talks a lot twice as much as a regular
# Cat! Make sure to also ll in the __repr__ method for NoisyCat, so we know how to construct it!
# As a hint: You can use several string formatting methods to make this easier.
# E.g.:
# >>> 'filling in {} spaces {} and {}'.format('blank', 'here', 'here')
# 'filling in blank spaces here and here'
class NoisyCat(Cat): # Fill me in!
    """A Cat that repeats things twice."""

    def talk(self):
        """Talks twice as much as a regular cat.
        >>> NoisyCat('Magic', 'James').talk()
        Magic says meow!
        Magic says meow!
        """
        print(self.name, 'says meow!')
        print(self.name, 'says meow!')

    def __repr__(self):
        """
        The interpreter-readable representation of a NoisyCat
        >>> muffin = NoisyCat('Muffin', 'Catherine')
        >>> repr(muffin)
        "NoisyCat('Muffin', 'Catherine')"
        >>> muffin
        NoisyCat('Muffin', 'Catherine')
        """
        return "NoisyCat('{}', '{}')".format(self.name, self.owner)