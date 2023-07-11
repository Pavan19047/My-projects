# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
avg_height = 0
for n in range(0, len(student_heights)):
    avg_height += student_heights[n]/len(student_heights)

final_height = "{:.2f}".format(avg_height)
print(final_height)  



