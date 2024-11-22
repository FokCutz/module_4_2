from html.parser import interesting_normal


def test_function():
    def inner_function():
        print('я в области видимости функции test_function')
    inner_function()


test_function()
inner_function() # выдает ошибку NameError: / без вызова данной функции все работает