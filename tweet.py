''' 
Sample 1:
Input 
1
4
sachin tweet_id_1
sehwag tweet_id_2
sachin tweet_id_3
sachin tweet_id_4

Output
sachin 3

'''
from collections import Counter

# function for counting tweets
def counting_tweets():
	for element in set(repeat):
		pairs = ([(key, value) for key, value in sorted(occurences.items()) if value == element])
		if len(pairs) > 1:
			for (key, value) in pairs:
				print (key,"",value)
		maximum = max(occurences.values())
		max_value = [(key, value) for key, value in sorted(occurences.items()) if value == maximum]
		if max_value != pairs:
			for (key,value) in max_value:
				print (key,"",value)
                
test_cases = int(input("Test Cases: "))
test_count = 0
names = []

for i in range(0,test_cases):
	n = int(input("test case input : "))
	count = 0
	for i in range(0,n):
		name = str(input("name : "))
		names.append(name)
		count += 1

	test_count += 1

all_names = [name.split(" ")[0] for name in names]
occurences = Counter(all_names)

repeat = occurences.values()
counting_tweets()


	

	
		
			

	

	
		
			


