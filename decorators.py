

def decorator(func):
    def decorated(input_text):
        print('함수 시작!')
        func(input_text)
        print('함수 끝!')
    return decorated


@decorator
def hello_world(input_text):
    print(input_text)


hello_world('hello world!')


def positive_value(func):
    def decorated(width, height):
        if width >= 0 and height >= 0:
            return func(width, height)
        else:
            print('ERROR')
    return decorated


@positive_value
def triangle(width, height):
    print(width * height * 0.5)


@positive_value
def square(width, height):
    print(width * height)


square(-5, 10)
(triangle(10, 10))
