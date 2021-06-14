# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
height1= float(height) ** 2
weight1=float(weight)
bmi=int(weight1//height1)
print("You BMI is: " + str(bmi))
