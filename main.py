def HeatWarning(temperature, humidity):
    if temperature < 80:
        print("Low Temperature: Not Classified")
        return
    
    if temperature > 110:
        print("Extreme Danger")
        return
    
    if humidity < 0 or humidity > 100:
        print("Invalid Humidity Value")
        return
    
    #set equation variables, y is 100 for both coordinates being used
    m1 = -60/13
    x1 = 85
    y = 100
    b1 = y - (m1*x1)
    m2 = -60/19
    x2 = 89
    b2 = y - (m2*x2)

    #make the comparison
    if humidity < m1*temperature + b1:
        print("Caution")
    elif humidity < m2*temperature + b2:
        print("Danger")
    else:
        print("Extreme Danger")
    

temperature = int(input("What is the temperature?"))
humidity = int(input("What is the humidity?"))
HeatWarning(temperature, humidity)