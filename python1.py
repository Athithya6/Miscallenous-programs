
#binary, hexadecimal and octal to decimal

'''
print("Binary form: {0:b}, Octal form: {1:o} and hexadecimal form: {2:X}".format(67,89,845))
#d=int(input("Enter a decimal number: "))
#print(f"Binary form: {d:b}, octal form: {d:o} and hexadecimal form is: {d:X}")
'''

'''
#practicing with format specifiers
print("My percentage in {0} this year is: {1:.2f}%".format("Maths",95.28756314))
print("My marks in {0} CT was: {1:.0f}".format("Antenna",11.0678))
print("The character equivalent of {0}, {1} and {2} are {0:c}, {1:c} and {2:c} respectively".format(65,112,42))
'''

'''
import os
print(os.name)
print(os.getcwd())
'''

'''
#threading1
import threading

def find_cube(num):
	print("Cube: {}".format(num*num*num))

def find_square(num):
	print("Square: {}".format(num*num))

if __name__=='__main__':
	t1=threading.Thread(target=find_square,args=(12,))
	t2=threading.Thread(target=find_cube,args=(15,))

t1.start()
t2.start()

t1.join()
t2.join()

print("Done!")
'''

'''
class Comedian:
	def __init__(self,first_name,last_name,age):
		self.first_name=first_name
		self.last_name=last_name
		self.age=age

	def __str__(self):
		print(f"{self.first_name} {self.last_name} is {self.age} years old.")

	def __repr__(self):
		print(f"{self.first_name} {self.last_name} is {self.age} years old.Surprise!")

comedian=Comedian("Athithya","Narayan",23)
print(comedian)
'''

'''
#threading2
import threading
import os

def task1():
	print("Task 1 is assigned to thread: {threading.current_thread()}")
	print(f"ID process of running task 1: {os.getpid()}")

def task2():
	print(f"Task 2 is assigned to thread: {threading.current_thread()}")
	print(f"ID process of running task 2: {os.getpid()}")

if __name__=='__main__':
	print(f"ID of process running main program: {os.getpid()}")

	print(f"Main thread name: {threading.current_thread().name}")

	t1=threading.Thread(target=task1,name='t1')
	t2=threading.Thread(target=task2,name='t2')

	t1.start()
	t2.start()

	t1.join()
	t2.join()
'''


#dictionary
d={'alpha':1,'gamma':3,'beta':5,'yamma':2,'thetta':6,'xi':4,'lambda':63}
l=[]

#first method of displaying the keys of the dictionary in alphabetical order
for key in d:
	l.append(key)

l.sort()
print(l)


#second method of displaying keys of a dictionary in order
for i in sorted(d.keys()):
	print(i)

#displaying a dictionary in order of keys and the in order of value
for i in sorted(d.keys()):
	print((i,d.get(i)))


#print(sorted(d.items(),key=lambda x:x[1])
#print(d.keys())
#print(d.values())
#print(d.items())


		



