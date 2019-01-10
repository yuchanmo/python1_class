try:
    print(5/0)
except Exception as e:
    print('error')
    


try:
    x = 5 + 'ham'
except Exception as identifier:
    print('damn it')


try:
    x = 5 + 'ham'
except ZeroDivisionError as identifier:
    print('hingngngngng')
except TypeError as te:
    print('typeerror')
except Exception as e:
    print('general exception')