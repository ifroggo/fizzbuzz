def fizzBuzz(number):
    output = ""
    if(number % 3 == 0):
        output += "Fizz"
    if(number % 5 == 0):
        output += "Buzz"   
    if(output == ""):
        output += str(number)
    output += ","
    return output



if __name__ == '__main__':
    output = ""
    for i in range(100):
        output += fizzBuzz(i)
    print(output)
