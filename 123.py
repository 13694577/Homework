


def calculator(x, y, operation): 
    if operation == '+': 
        return x + y 
    elif operation == '-': 
        return x - y  
    elif operation == '*': 
        return x * y 
    elif operation == '/': 
        if y != 0: 
            return x / y 
        else: 
            return "На ноль делить нельзя"
if __name__ == "__main__":
    print(calculator(2 ,4 ,'+' ))
    print(calculator(99 ,-1 ,'-' ))
    print(calculator(-5 ,-1 ,'*' ))
    print(calculator(10 ,0 ,'/'))

    operation = input("Введите операцию: +, -, *, /\n").strip()
    
    
    try:
        first = float(input("Введите первый аргумент:\n"))
    except ValueError:
        print("Первый аргумент должен быть числом! Попробуйте снова.")
        
    try:
        second = float(input("Введите второй аргумент:\n"))
    except ValueError:
        print("Второй аргумент должен быть числом! Попробуйте снова.")
    
    result = calculator(first, second, operation)
    
  
    if result is not None:
        print(f"{first} {operation} {second} = {result}")