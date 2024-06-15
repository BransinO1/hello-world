# First Hello World - Simple
print ('Hello World')

# Second Hello World - More Complex
def hello(name):
    print(f'Hello, {name}!')

#Print Hello [Person's name] instead of the basic Hello [World]
if __name__ == "__main__":
    user_name = input("Enter your name: ")
    hello(user_name)