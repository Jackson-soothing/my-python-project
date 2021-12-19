# v = 'hello'
def exist():
    try:
        v
        print('variable is defined')
    except:
        print('variable is not defined')