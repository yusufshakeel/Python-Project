from bmi import BMI         #import BMI class from bmi module (file)

def main():
    obj1 = BMI("Tom", 18, 145, 70)      #create object
    print("BMI for", obj1.getName(), "is", obj1.getBMI(), obj1.getStatus())

main()      #call main function
