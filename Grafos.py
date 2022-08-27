name = input("ing. nombre: ")
age = input("ing. edad: ")

print(name)
print(int(age) + 5)


print("\n")


def cuenta_atras(n): 
	while n>0: 
		print(n)
		n-=1
	print("Terminamos 7w7")


m = int(input("Ing. Num: "))
cuenta_atras(m)


print("\n")


nums = [4,78,9,84]

print(nums[3])

for n in nums:
	print(n)