def my_decorateor(func):
    def wrapper():
        print("함수 호출 전")
        func()
        print("함수 호출 후")

    return wrapper

@my_decorateor
def say_hello():
    print("안녕하세요")

say_hello()