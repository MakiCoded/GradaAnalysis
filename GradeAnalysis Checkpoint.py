# import numpy 
import numpy as np

#create the "grades" array as specified above.
grades = [85,90,88,92,95,80,75,98,89,83]
print(grades)

# Create an Array of the grades
grades_array = np.array(grades)
print(grades_array)

## Use numpy functions to calculate the mean, median, and standard deviation of the grades.
#mean
print(np.mean(grades))

#median
print(np.median(grades))

#standard deviation of the grades
print(np.std(grades))

#Use numpy function to sort the grades in ascending order.
print(np.max(grades))
print(np.min(grades))
print(np.sort(grades))

#Use numpy function to find the index of the highest grade in the array.
print(np.argmax(grades))

#Use numpy function to count the number of students who scored above 90.
above_90 = np.sum(grades_array > 90)
print(above_90)

#Use numpy function to calculate the percentage of students who scored above 90.
total_students = grades_array.size
percentage_above_90 = (above_90 / total_students) *100
print(f"the Percentage of students above {percentage_above_90} percent ")

#Use numpy function to extract all the grades above 90 and put them in a new array called "high_performers".
high_performers = grades_array[grades_array > 90]
print(f"This is a the list of performers above 90 {high_performers}")

#Create a new array called "passing_grades" that contains all the grades above 75.
passing_grades = grades_array[grades_array > 75]
print(f" this is a list of performers above 75 {passing_grades}") 

