# What will be the output of the following code snippet?

x = 50
def func(x):
    x = 2
    func(x)
print("x is now", x)


# 2. What be the output of the following code snippet?

def say(message, times=1):
    print(message * times)  
say("Hello")
say("World",5)      
