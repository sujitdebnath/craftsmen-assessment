# Craftsmen Assessment

It's an implementation of a Reverse Polish Notation (RPN) calculator in Python which contains following things:

  - <b> Stack class </b>: Simple stack class with several methods such as push, pop, peek etc
  - <b> calculation method </b>: corresponding operator has been done on two operand and returns the value
  - <b> rpn_calculator method </b>: Calculate Reverse Polish Notation value and returns it
  - <b>infix_to_rpn method</b>: Convert the Infix into Reverse Polish Notation and then returns the desire string

The solution has been calculated using following steps:

  - Take the input and split it to create a list of characters, called input_list
  - Then passes the input_list into rpn_calculator methods which returns the desire output and prints it
  - When input is in infix notation, it can be convertable into RPN using infix_to_rpn methods (optional)
