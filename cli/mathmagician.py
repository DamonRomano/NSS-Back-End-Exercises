import time


class MathMagic():
    def __init__(self):




    def generate_integers(self, number):
        '''
        Return integers in sequence
        as generated by a loop below.
        '''
        return(number)

    def generate_fibonacci_sequence(self, number):
        '''
        Return numbers in the Fibonacci Sequence
        as generated by a loop below.
        '''
        if number <= 1:
            return number
        else:
            return(self.fibonacci_sequence(number - 1) + self.fibonacci_sequence(number-2))

    def generate_prime_numbers(self, number = 2):
        '''
        Return prime numbers in sequence
        as generated by a loop below.
        '''
        def generate_primes(self, count):
            i, x = 2, 1
            result = list()

            # x starts at 2 and ends at whatever the user typed in
            # for number of numbers to display
            while x <= count:

                # Start by assuming it is a prime number
                isPrime = True

                # Using the range 2...(square root of current number)
                for n in range(2, int(math.sqrt(i) + 1)):

                    # If there is not a remainder with modulo calculation
                    # then it's not a prime number
                    if i % n == 0:
                        isPrime = False
                        break

              # Range loop is done, check if prime got negated
              # If not then we know it's a prime number
              if isPrime:
                result.append(i)
                x += 1

              i += 1

    return result



    def main():
        '''
        User-defined input fires one of these functions that gives back
        a sequnetial list of either
        1. integers,
        2. numbers in the Fibonacci Sequence, or
        3. prime numbers.
        '''
        mathyObject = MathyThings()



if __name__ == '__main__':
    main()




