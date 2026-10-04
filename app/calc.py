def add(a: int, b: int) -> int:
    return a + b


def fizzbuzz(n: int) -> str:
    if n % 10 == 0:
        return "FizzBuzz"
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    return str(n)
