"""
@author:
    Sujit Debnath
    North South University
    Email: sujit.debnath@northsouth.edu
"""

class Stack:
    """
    Stack class which contains basic stack methods

    Attributes
    ----------
    elements: character list

    Methods
    -------
    push(item)
        push the item into the stack
    pop()
        pop the top item from the stack
    peek()
        peek the top item from the stack
    size()
        return the size of the stack
    isEmpty()
        check wether stack is empty or not
    display()
        display all elements in the stack
    """

    def __init__(self):
        self.elements = []
    
    def push(self, item):
        """
        Push the item into the stack

        Parameters
        ----------
        item: character
        """

        self.elements.append(item)
    
    def pop(self):
        """
        Pop the top item from the stack
        """

        return self.elements.pop()
    
    def peek(self):
        """
        Peek the top item from the stack

        Raises
        ------
        Exception
            if stack is empty
        """

        if self.isEmpty():
            raise Exception("Stack empty!")
        return self.elements[-1]
    
    def size(self):
        """
        Return the size of the stack
        """

        return len(self.elements)
    
    def isEmpty(self):
        """
        check wether stack is empty or not
        """

        return self.size() == 0
    
    def display(self):
        """
        Display all elements in the stack
        """

        return self.elements


def calculation(op, num1, num2):
    """
    Corresponding operation has been done on two operand and returns it

    Parameters
    ----------
    op: character
        represent the operator ( +, -, etc)
    num1: int
        1st operand
    num2: int
        2nd operand

    Returns
    -------
    int or float
        corresponding output
    
    Raises
    ------
    Exception
        at the time of division and when denomication is equal to zero
    """

    if op == '+':
        return num1+num2
    elif op == '-':
        return num2-num1
    elif op == '*':
        return num1*num2
    elif op == '/':
        if num1 == 0:
            raise Exception("Can't divide by zero!")
        return num2/num1


def rpn_calculator(input_list):
    """
    Calculate Reverse Polish Notation value and returns it

    Parameters
    ----------
    input_list: list of character
        represent input values which are character

    Returns
    -------
    int or float
        return desire value
    """

    stack = Stack()

    try:
        for item in input_list:
            if item.isdigit():
                stack.push(item)
            else:
                n1 = int(stack.pop())
                n2 = int(stack.pop())
                stack.push(calculation(item, n1, n2))
        
        return stack.peek()
    
    except Exception as e:
        print(e)


def infix_to_rpn(input_list):
    """
    Convert the Infix into Reverse Polish Notation and then returns the desire string

    Parameters
    ----------
    input_list: list of character
        represent input values which are characters

    Returns
    -------
    String
        return desire RPN notation str
    """

    stack = Stack()
    precendence = {'+': 1, '-': 1, '*': 2, '/': 2}

    output_rpn_list = []

    for item in input_list:
        if item.isdigit():
            output_rpn_list.append(item)
        elif item == ')':
            while stack.peek() != '(':
                output_rpn_list.append(stack.pop())
            stack.pop()
        else:
            if item == '(' or stack.isEmpty() or stack.peek() == '(' or precendence[item] > precendence[stack.peek()]:
                stack.push(item)
            else:
                while not(stack.isEmpty()) and precendence[item] < precendence[stack.peek()]:
                    output_rpn_list.append(stack.pop())
                stack.push(item)
    
    while not(stack.isEmpty()): output_rpn_list.append(stack.pop())

    return ' '.join(output_rpn_list)

if __name__ == "__main__":
    input_list = input().split(" ")

    print(rpn_calculator(input_list))
    # print(infix_to_rpn(input_list))