
def main():
	print("First 10 prime numbers")
	func()
def func(): # Funcction to find first 10 prime numbers
	cnt = 0
	num = 2
	cur = 2
	while(cnt < 10):
		while(cnt < 10):
			flag = 0	
			for x in range(2,int(num/2)):
				if(num % x == 0):
					flag = 1
					break;
				cur = x
			if(flag == 0):
				cnt = cnt + 1
				print(cur)
			num = num + 1
main()

