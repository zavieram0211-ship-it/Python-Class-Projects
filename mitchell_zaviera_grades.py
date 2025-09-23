# Grades
# Zaviera Mitchell
# Store students exam grades (list) and attendence (set)

#Lists -> Data Structure -> methods
grades = [ 88, 96, 96, 76, 89, 74, 100, 85, 75, 77, 100, 98]

# Sets -> Data Sructure -> methods
day_1 = {'William' , 'Daphne' , 'Erika' , 'Adam' , 'Percy' , 'Brock' , 'Jessica' , 'Trent' , 'Mahmoud' }
day_2 = {'Daphne' , 'Alex' , 'Percy' , 'Mahmoud' , 'Jessica' , 'Adam' , 'Trent' , 'Caleb' , 'Zayne' , 'Erika' }

# How many students attended the class

overlap = day_1|day_2  #combination of sets
print(len(overlap), "students attended the class")

# Who attended both days of class? 
both_days = day_1 & day_2
print(both_days, "attended both class days.")

# Who attended only one class? 
one_day = day_1 ^ day_2
print(one_day, "attended one class day." )

# How many students took the exam? 12
print(len(grades), "Students took the exam. ")


# What was the highest grade? 100
highestGrade = max( grades )
print("The highest grade was a", highestGrade)

# What was the lowest grade? 74
lowestGrade = min( grades )
print("The lowest grade was a", lowestGrade)

# What was the average grade for the exam? 87.8
gradeSum = sum(grades)
avg = gradeSum/len(grades)
print(f"The average grade was a {avg:.1f}")