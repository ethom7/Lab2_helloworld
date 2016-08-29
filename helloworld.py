"""
Created by Evan Thompson [ethom7@uis.edu]
August 29, 2016

Program will print "Hello, World!" and exit

"""
import sys



def printhw():
	print("Hello, World!")


def main():
	
	printhw()

if __name__ == '__main__':
	status = main()
	sys.exit(status)
