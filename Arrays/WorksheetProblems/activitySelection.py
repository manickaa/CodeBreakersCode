def maximumActivity(tasks):
	maxActivity = 1
#base case if there are no tasks or only one task given:
	if tasks is None or len(tasks)==0:
		return 0
	if len(tasks) == 1:
		return 1
	#sort tasks based on end time
	tasks.sort(key = lambda x:x[1])
	endTimeOfPrevTask = tasks[0][1]
	for i in range(1, len(tasks)):
		if tasks[i][0] >= endTimeOfPrevTask:
			maxActivity += 1
			endTimeOfPrevTask = tasks[i][1]
	return maxActivity

tasks = []
print(maximumActivity(tasks))
tasks = [(0,2)]
print(maximumActivity(tasks))
tasks = [(3,3),(0,2),(1,6), (6,7)]
print(maximumActivity(tasks))
tasks = [(0,20),(1,2),(2,3),(3,5)]	#counter example for start time based sorting
print(maximumActivity(tasks))
