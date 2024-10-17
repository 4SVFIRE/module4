def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function()

test_function()


# def test_function():
#     def inner_function():
#         print('Я в области видимости функции test_function')
#
# inner_function() # будет ошибка, т.к Это значит, что
#                 # функция inner_function не существует снаружи test_function, и вы не можете вызвать её напрямую.



