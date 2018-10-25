"""Basic example of an adapter class to provide a stack interface to Python's list."""

#from ..exceptions import Empty

class ArrayStack:
  """LIFO Stack implementation using a Python list as underlying storage."""

  def __init__(self):
    """Create an empty stack."""
    self._data = []                       # nonpublic list instance

  def __len__(self):
    """Return the number of elements in the stack."""
    return len(self._data)

  def is_empty(self):
    """Return True if the stack is empty."""
    return len(self._data) == 0

  def push(self, e):
    """Add element e to the top of the stack."""
    self._data.append(e)                  # new item stored at end of list

  def top(self):
    """Return (but do not remove) the element at the top of the stack.

    Raise Empty exception if the stack is empty.
    """
    if self.is_empty():
      raise Exception('Stack is empty')
    return self._data[-1]                 # the last item in the list

  def pop(self):
    """Remove and return the element from the top of the stack (i.e., LIFO).

    Raise Empty exception if the stack is empty.
    """
    if self.is_empty():
      raise Exception('Stack is empty')
    return self._data.pop()               # remove last item from list


def evalPostFix(expr):
    """ using stack to eval the expression expr, then return this value

    Create stack S"""
    S = ArrayStack()

    """ Loop each character in expression. We have problem with the number greater than 9, it should be in () """

    big_num = ""                # this to make the number in all cases: 1 digit or more digits
    """ if the character in expression is '(' mean that the number has more than 1 digit, it end with ')'"""
    find_big_num = False
    for c in expr:
        """ Check if this character is digit or not. 
        If digit, then push it to stack S.
        If '(', then enable the flag find_big_num, and begin create this big num
        If ')', end of create big num, and disable the find_big_num
        If not digit pop two numbers and do calculate the value"""
        if c.isdigit():
            big_num += c
            if not find_big_num:
                S.push(big_num) # push number into stack
                big_num = ""    # reset the big_num to get next number in expression

        elif c == '(':
            find_big_num = True
        elif c == ')':
            find_big_num = False
            S.push(big_num)     # push number into stack
            big_num = ""        # reset the big_num to get next number in expression
        else:
            n1 = int(S.pop())   # pop first number
            n2 = int(S.pop())   # pop second number
            if c == '+':        # check if this is addition
                n3 = n1 + n2
            elif c == '-':      # check if this is subtraction
                n3 = n2 - n1
            elif c == '*':      # check if this is multi
                n3 = n2 * n1
            elif c == '/':      # check if this is div
                n3 = n2 / n1

            """ Push the value back to stack"""
            S.push(str(n3))

    """ Return the last results. It stored in stack"""
    return S.pop()


if __name__ == '__main__':
    """ Open file data.txt and read each expression in it, then cal the function evalPostFix to get the value
    Final, print the output this result"""
    with open('data.txt', 'r') as f:
        for line in f:
            print("The value of expression ", line.rstrip(), " is ", evalPostFix(line.rstrip()))


