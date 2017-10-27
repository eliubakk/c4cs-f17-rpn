#!/usr/bin/env python3

import operator

ops = {
	'+': operator.add,
	'-': operator.sub,
}

def calculate(equation):
	stack = list()
	for arg in equation.split():
		try:
			stack.append(int(arg))
		except ValueError:
			arg2 = stack.pop()
			arg1 = stack.pop()
			function = ops[arg]
			result = function(arg1, arg2)
			stack.append(result)
	print(stack)
	return stack.pop()

def main():
	while True:
		calculate(input("rpn calc> "))

if __name__ == '__main__':
	main()