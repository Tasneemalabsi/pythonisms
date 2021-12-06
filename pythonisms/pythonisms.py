class Node :
    
    def __init__(self , data, next_=None):
        """method to create a new node """
        self.data = data 
        self.next = next_


class LinkedList :
    def __init__(self, collection=None):
        """method to create the linked list nodes  """
        self.head = None
        if collection:
        #[1,2,3]
        #{1}->{2}->{3}

            for item in reversed(collection):
                self.insert(item)

    def __iter__(self):
        def generator():
            current = self.head
            while current:
                yield current.data
                current = current.next
            return generator()

    def __getitem__(self, index):
        for i, item in enumerate(self):
            if i == index:
                return item
        raise IndexError('Index out of range')


    def insert(self,data):
        """
        function that called insert that insert data in to the linked list
        
        """
        self.head=Node(data, self.head)
    
            
    def __str__(self):
        current = self.head
        output = []
        while current:
            output.append(f"{{{current.data}}}")
            current = current.next
        
        return "->".join(output)

    def walk(self, action):
        current = self.head
        result = None
        while current :
            result = action(current.data)
            current = current.next
        return result

    def __bool__(self):
        if self.head:
            return True
        else:
            return False


class MathThings:
  def __init__(self):

    self.sum = 0
    self.product = 1
    self.squares = []

  def adder(self , value):
    self.sum += value

  def multiplier(self , value):
    self.product *= value


  def squared(self, value):
    self.squares.append(value**2)



from functools import wraps
from time import sleep

def procrastinate(func):
  @wraps(func)
  def wrapper(*args, **kwargs):
    """
    Wrapper wraps the stuff
    """
    sleep(3)
    return func(*args, **kwargs)
  return wrapper

def sarcastic_decorator(func):
  @wraps(func)
  def wrapper(*args, **kwargs):
    output =  func(*args, **kwargs)
    return f'Oh Sure, "{output}" sounds like a great book title'
  return wrapper


@procrastinate
@sarcastic_decorator
def say(text):
  """ 
  Say says the things
  """
  return text

if __name__ == "__main__":
  # print(say.__doc__)
  print("Running Now")
  print(say("anything"))