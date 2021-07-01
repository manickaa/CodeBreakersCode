# def function(N):
#     sum = 0
#     i = 1
#     while i < N:				#this loop executes logN time		
#         for j in range(0, N):		#this loop executes N times since it is independent of i
#             sum += 1
#         i = i * 2

#     print(sum)
#     return

def function_one(N):
	#O(N) runtime
	sum = 0;										
	n = N
	while n > 0: 					
		for i in range(0, n):	#this loop executes N + N/2 + N/4 +..+1 times which is 2N-1 times
			sum += 1
		n = n // 2
	print(sum)
	return

def function_two(N):
	#O(N) runtime
	sum = 0
	i = 1
	while i < N:
		for j in range(0, i):		#this loop executes 1 + 2+ 4 + 8 + ... + 2^(logN) times which is 2^logN - 1 => N-1 times 
			sum += 1			
		i = i * 2
	print(sum)
	return

def function_three(N):
	#O(NlogN) runtime
	sum = 0
	i = 1
	while i < N:				#this loop executes logN time		
		for j in range(0, N):		#this loop executes N times since it is independent of i
			sum += 1
		i = i * 2
	print(sum)
	return

def linear_arithmetic(n):
	i = 1
	total = 0
	while(i < n):
		print("i ",i)
		j = 1
		while(j < n):
			print("j ",j)
			k = 1
			while(k < n):
				print("k ",k)
				total += 1
				k *= 2
			j *= 2
		i += 1
	print(total)
	return


#linear_arithmetic(8)
function_one(8)   #runs 2N-1 time => 2*8 - 1 => 15 #sum must be 15
function_two(8)   #runs N-1 time => 8-1 => sum must be 7
function_three(8) #runs N logN time => 8*log8 => sum must be 24
