#!/usr/bin/env python3

def calculate(equation):
	stack = list()
	for arg in equation.split():
		if arg == '+':
			arg1 = stack.pop()
			arg2 = stack.pop()
			result = arg1 + arg2
			stack.append(result)
		else:
			stack.append(int(arg))
	print(stack)
	return stack.pop()

def main():
	while True:
		calculate(input("rpn calc> "))

if __name__ == '__main__':
	main()