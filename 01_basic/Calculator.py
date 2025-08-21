# Calculator using Match Case ?

num1 = int(input("Enter your first Number: "))
num2 = int(input("Enter your second Number: "))

operator = input("Enter Operator: ")

match operator:
    case "+":
        print("Sum is", num1 + num2)
    case "-":
        print("Difference is", num1 - num2)
    case "*":
        print("Product is", num1 * num2)
    case "/":
        print("Division is", num1 / num2)
    case _ :
        print("Enter a valid orerator")                
