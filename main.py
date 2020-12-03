from multiprocessing import Process
import time

def plus():
		for i in range(10):
			print("+")
			time.sleep(1)

def star():
	for i in range(10):
		print("*")
		time.sleep(1)

if __name__ == '__main__':
	p1=Process(target=plus)
	p1.start()
	p2=Process(target=star)
	p2.start()
	p1.join()
	p2.join()
	print('FINISH')