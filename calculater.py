# add numbers
def add (n1,n2):
     return n1 + n2
# subtract numbers
def subtract (n1,n2):
     return n1 - n2
# multiply numbers
def multiply (n1,n2):
     return n1 * n2
# divide numbers
def divide (n1,n2):
     return n1 / n2



operation = {
     "+" : add,
     "-" : subtract,
     "*" : multiply,
     "/" : divide
}
num1 = float(input("Whats the first number? "))
num2 = float(input("Whats the second number? "))
for symbol in operation:
     print(symbol)
selectOp = input("Pick an opration from the line above: ")
first_answer = operation[selectOp](num1,num2)
print(f"{num1} {selectOp} {num2} = {first_answer}")
while True:
     select = input(f"Type 'y' to continue calculatring with {first_answer}, or type 'n' to exit.: ")
     if select == "y":
          num3 = float(input("Whats next number? "))
          for symbol in operation:
               print(symbol)
          selectOp = input("Pick an opration from the line above: ")
          second_answer = operation[selectOp](first_answer,num3)
          print(f"{first_answer} {selectOp} {num3} = {second_answer}")
     elif "no":
          print(f"{first_answer} {selectOp} {num3} = {second_answer}")
          break


