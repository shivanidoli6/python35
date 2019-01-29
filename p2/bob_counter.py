#'''Assume s is a string of lower case characters.

#Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print

#Number of times bob occurs is: 2'''

def main():
	s = input()
	count = 0
        for word in range(len(s)-2):
        	if s[i]=='b' and if s[i+1]=='o'and if s[i+2]=='b':
                	count=count+1
	print(count)


if __name__== "__main__":
	main()

