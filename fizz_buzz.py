class FizzBuzz:
    def get(self,number):
        if number % 3 == 0 and number % 5 == 0:
            return 'FizzBuzz'
        elif number % 3 == 0 or number == 13:
            return 'Fizz'
        elif number % 5 == 0:
            return 'Buzz'
        else:
            if '3' in str(number) and '5' in str(number):
                return 'FizzBuzz'
            elif '3' in str(number):
                return 'Fizz'
            elif '5' in str(number):
                return 'Buzz'
        return number