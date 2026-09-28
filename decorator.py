def my_decorator(func): # this is our decorator function
    def wrapper():
        print("Function chalne se pehle ka extra kaam! 🛠️")
        func()  # Yahan hamara original function call hoga
        print("Function khatam hone ke baad ka kaam! ✅")
    return wrapper

@my_decorator
def greet(): # this our main function
    print("Hello, World! 👋")

# Function ko call karte hain
greet()

