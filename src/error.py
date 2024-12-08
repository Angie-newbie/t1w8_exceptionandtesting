def convert_to_interger(value):
    try:
        result = int(value)
        return result
        print(f'Concersion success! Result: {result}')
    except ValueError:
        print('Conversion fail, please enter a interger')
    except ZeroDivisionError:
        print('0')
    except Exception as e:
        print(f'an unexpected error {e}')
    else:
        print('else involved')
    finally:
        print('closing')

    # user input
# spam = input("enter a number to convert")

# convert_to_interger(spam)