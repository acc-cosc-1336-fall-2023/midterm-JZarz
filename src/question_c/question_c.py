#write functions here, don't add input('') statements here!

def get_fahrenheit(celsius):
    f = (9/5 *celsius) +32
    return f

def get_table_range():
    word1 = "Celsius"
    word2 = "fahrenheit"
    print(word1.ljust(10, " ") + word2.rjust(10," "))

    celsius = 20
    c = 0
    for c in range(0, celsius+ 1):     
        j = 0
        for j in range(0, 1):
            f = round(get_fahrenheit(c))
            #print(f"celsius: {c} fahrenheit: {f}")
            print(str(c).rjust(5," ") + str(f).rjust(10 , " "), end = " ")
            j += 1
        c += 1
        print (" ")

        