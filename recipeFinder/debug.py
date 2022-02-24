def area_circle(r):
    area = 3.14*r**2
    return area

def dumb_calc(x):
    breakpoint()
    result = 5/x
    if result > 1:
        print("greater than 1")
    else:
        print("less than 1")
        for i in range(100):
            result += i
        print("modifying result: ", result)
    return result

num = int(input("please enter a number: "))
area_result = area_circle(num)
print(area_result)
calc_result = dumb_calc(num)
print(calc_result)
