numbers = [1,2,3,4,5,6,7,8,9,10]
window = 3

mean_values = []

for index in range(window - 1): 
    group = numbers[0 : index + 1]
    mean = sum(group) / len(group)
    mean_values.append(mean)



for index in range(len(numbers) - window + 1):
    group = ( numbers [index:index + window] )
    mean = sum(group) / window
    mean_values.append(mean)

print(mean_values)