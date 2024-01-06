# This is a Simple calculator made by me 
print("......Welcome to My mini Calculator.....")
while True:
  print("""The rules are 
            1. Addition
            2. Subtractions
            3. Multiplication
            4. Divisions """)


  A = int(input("Enter the First Number: "))
  B = int(input("Enter the Second Number: "))
  
  
  
  def Addition(A,B):
    c = A+B
    return c
    
  
  
  def Subtraction(A,B):
    c = A-B
    print("The Subtraction is ",c)
  
  
  def Multiplication(A,B):
    c = A*B
    print("The Multiplication is ",c)
  
  
  def Division(A,B):
    c = round(A/B,2)
    print("The Division is ",c)
  
  
  
  ch = int(input("Enter the key According to the rules: "))
  match ch:
      case 1:
        print("you have choosed Addition")
        D = Addition(A,B)
        print("The Addition is ",D)
      case 2:
        print("you have choosed Subtraction")
        Subtraction(A,B)
      case 3:
        print("you have choosed Multiplication")
        Multiplication(A,B)
      case 4:
        print("you have choosed Division")
        Division(A,B)
      case _:
       ch1 =  int((input("Enter valid key: ")))
       if ch1 == 1:
         print("you have choosed Addition")
         Addition(A,B)
       elif ch1 == 2:
         print("you have choosed Subtraction")
         Subtraction(A,B)
       elif ch1 == 3:
         print("you have choosed Multiplication")
         Multiplication(A,B)
       else:
         print("you have choosed Division")
         Division(A,B)


   
      
  repeat = input("Want to calculate again, Say yes or no: ")
  if repeat == 'no':
    break
    
  
  


   

    