#  Your task is to find the first element of an array that is not consecutive.
#  If the whole array is consecutive then return null

def first_non_consecutive(arr):
    for i, v in enumerate(arr, arr[0]):
        if v != i:
            return v

#  Think of a way to store the languages as a database (eg an object). The languages are listed below so you can copy and paste!
#  Write a 'welcome' function that takes a parameter 'language' (always a string), and returns a greeting - if you have it in your database. It should default to English if the language is not in the database, or in the event of an invalid input.

def greet(language):
    return {
        'czech': 'Vitejte',
        'danish': 'Velkomst',
        'dutch': 'Welkom',
        'english': 'Welcome',
        'estonian': 'Tere tulemast',
        'finnish': 'Tervetuloa',
        'flemish': 'Welgekomen',
        'french': 'Bienvenue',
        'german': 'Willkommen',
        'irish': 'Failte',
        'italian': 'Benvenuto',
        'latvian': 'Gaidits',
        'lithuanian': 'Laukiamas',
        'polish': 'Witamy',
        'spanish': 'Bienvenido',
        'swedish': 'Valkommen',
        'welsh': 'Croeso'
    }.get(language, 'Welcome')

#  Create a method take that accepts a list/array and a number n, and returns a list/array array of the first n elements from the list/array.

def take(arr,n):
    return arr[:n]

#  You were camping with your friends far away from home, but when it's time to go back, you realize that your fuel is running out and the nearest pump is 50 miles away! You know that on average, your car runs on about 25 miles per gallon. There are 2 gallons left. Considering these factors, write a function that tells you if it is possible to get to the pump or not. Function should return true (1 in Prolog) if it is possible and false (0 in Prolog) if not. The input values are always positive.

def zeroFuel(distance_to_pump, mpg, fuel_left):
    return distance_to_pump <= mpg * fuel_left


#  Simple, given a string of words, return the length of the shortest word(s).
def find_short(s):
    return min(len(x) for x in s.split())

#  Complete the function which takes two arguments and returns all numbers which are divisible by the given divisor. First argument is an array of numbers and the second is the divisor.

def divisible_by(numbers, divisor):
    return [x for x in numbers if x%divisor == 0]

#  You have to write a function that accepts three parameters:

cap is the amount of people the bus can hold excluding the driver.
on is the number of people on the bus.
wait is the number of people waiting to get on to the bus.
If there is enough space, return 0, and if there isn't, return the number of passengers he can't take.

def enough(cap, on, wait):
    return max(0, wait - (cap - on))

#  Given 2 elevators (named "left" and "right") in a building with 3 floors (numbered 0 to 2), write a function elevator accepting 3 arguments (in order):

left - The current floor of the left elevator
right - The current floor of the right elevator
call - The floor that called an elevator
It should return the name of the elevator closest to the called floor ("left"/"right").

In the case where both elevators are equally distant from the called floor, choose the elevator to the right.

def elevator(left, right, call):
    return "left" if abs(call - left) < abs(call - right) else "right"

#  Simple, remove the spaces from the string, then return the resultant string.

def no_space(x):
    return x.replace(' ' ,'')

#  Your goal is to create a function that removes the first and last characters of a string. You're given one parameter, the original string. You don't have to worry with strings with less than two characters.

def remove_char(s):
    return s[1 : -1]

#  Consider an array/list of sheep where some sheep may be missing from their place. We need a function that counts the number of sheep present in the array (true means present).

def count_sheeps(arrayOfSheeps):
  return arrayOfSheeps.count(True)

#  Because Nathan knows it is important to stay hydrated, he drinks 0.5 litres of water per hour of cycling.
#  You get given the time in hours and you need to return the number of litres Nathan will drink, rounded to the smallest value.

def litres(time):
    return time // 2

# Given a set of numbers, return the additive inverse of each. Each positive becomes negatives, and the negatives become positives.
def invert(lst):
    return [-x for x in lst]

# The cockroach is one of the fastest insects. Write a function which takes its speed in km per hour and returns it in cm per second, rounded down to the integer (= floored).
import math

def cockroach_speed(s):
    return math.floor(s * 27.7778)
    # or
    # return s // 0.036

#  The starship Enterprise has run into some problem when creating a program to greet everyone as they come aboard. It is your job to fix the code and get the program working again!
#  Hello, Mr. Spock

def say_hello(name):
    return "Hello, " + name

# Your coworker was supposed to write a simple helper function to capitalize a string (that contains a single word) before they went on vacation.
# Unfortunately, they have now left and the code they gave you doesn't work. Fix the helper function they wrote so that it works as intended (i.e. make the first character in the string "word" upper case).
# Don't worry about numbers, special characters, or non-string types being passed to the function. The string lengths will be from 1 character up to 10 characters, but will never be empty.

def capitalize_word(word):
    return word.capitalize()

# You are given the length and width of a 4-sided polygon. The polygon can either be a rectangle or a square.
# If it is a square, return its area. If it is a rectangle, return its perimeter.

def area_or_perimeter(l , w):
    if l == w:
        return l * w
    return l * 2 + w * 2

#  Jenny has written a function that returns a greeting for a user. However, she's in love with Johnny, and would like to greet him slightly different. She added a special case to her function, but she made a mistake.

def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, {name}!".format(name=name)

#  In this simple exercise, you will build a program that takes a value, integer, and returns a list of its multiples up to another value, limit. If limit is a multiple of integer, it should be included as well. There will only ever be positive integers passed into the function, not consisting of 0. The limit will always be higher than the base.
#  For example, if the parameters passed are (2, 6), the function should return [2, 4, 6] as 2, 4, and 6 are the multiples of 2 up to 6.
#  If you can, try writing it in only one line of code.

def find_multiples(integer, limit):
    return list(range(integer, limit+1, integer))

#  Define a method hello that returns "Hello, Name!" to a given name, or says Hello, World! if name is not given (or passed as an empty String).
#  Assuming that name is a String and it checks for user typos to return a name with a first capital letter (Xxxx).

def hello(name=''):
    return f"Hello, {name.title() or 'World'}!"

#You take your son to the forest to see the monkeys. You know that there are a certain number there (n), but your son is too young to just appreciate the full number, he has to start counting them from 1.
# As a good parent, you will sit and count with him. Given the number (n), populate an array with all numbers up to and including that number, but excluding zero.
# For example:
# monkeyCount(10) # --> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def monkey_count(n):
    return [n for n in range(1, n + 1)]

#or

def monkey_count(n):
    return range(1, n+1)

# Deoxyribonucleic acid, DNA is the primary information storage molecule in biological systems. It is composed of four nucleic acid bases Guanine ('G'), Cytosine ('C'), Adenine ('A'), and Thymine ('T').
# Ribonucleic acid, RNA, is the primary messenger molecule in cells. RNA differs slightly from DNA its chemical structure and contains no Thymine. In RNA Thymine is replaced by another nucleic acid Uracil ('U').
# Create a function which translates a given DNA string into RNA.
# For example:
# "GCAT"  =>  "GCAU"
# The input string can be of arbitrary length - in particular, it may be empty. All input is guaranteed to be valid, i.e. each input string will only ever consist of 'G', 'C', 'A' and/or 'T'.

def dna_to_rna(dna):
    return dna.replace('T', 'U')

# Write a method sum (sum_array in python, sumarray in julia, SumArray in C#) that takes an array of numbers and returns the sum of the numbers. These may be integers or decimals for Ruby and any instance of Num for Haskell. The numbers can also be negative. If the array does not contain any numbers then you should return 0.

def sum_array(a):
    return sum(a)

# Sum all the numbers of the array (in F# and Haskell you get a list) except the highest and the lowest element (the value, not the index!).
# (The highest/lowest element is respectively only one element at each edge, even if there are more than

def sum_array(arr):
    if arr == None or len(arr) < 3:
        return 0
    return sum(arr) - max(arr) - min(arr)

# We want an array, but not just any old array, an array with contents!
# Write a function that produces an array with the numbers 0 to N-1 in it.

def arr(n=0):
    return list(range(n))

# Given a non-empty array of integers, return the result of multiplying the values together in order. Example:
# [1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24

def grow(arr):
    return reduce(lambda x, y: x * y, arr)

# or

def grow(arr):
    product = 1
    for i in arr:
        product *= i
    return product

# Your task is to create functionisDivideBy (or is_divide_by) to check if an integer number is divisible by each out of two arguments.
# A few cases:
# (-12, 2, -6)  ->  true
# (-12, 2, -5)  ->  false
# (45, 1, 6)    ->  false
# (45, 5, 15)   ->  true
# (4, 1, 4)     ->  true
# (15, -5, 3)   ->  true

def is_divide_by(number, a, b):
    return number % a == 0 and number % b == 0

# Your function will be called char_freq/charFreq/CharFreq and you will get passed a string, you will then return a dictionary
# (object in JavaScript) with as keys the characters,
# and as values how many times that character is in the string. You can assume you will be given valid input.

def char_freq(message):
    result = {}
    for letter in message:
        result[letter] = result.get(letter, 0) + 1
    return result

# or

from collections import Counter

def char_freq(message):
    return Counter(message)

# Your friend invites you out to a cool floating pontoon around 1km off the beach. Among other things, the pontoon has a huge slide that drops you out right into the ocean, a small way from a set of stairs used to climb out.
# As you plunge out of the slide into the water, you see a shark hovering in the darkness under the pontoon... Crap!
# You need to work out if the shark will get to you before you can get to the pontoon. To make it easier... as you do the mental calculations in the water you either freeze when you realise you are dead, or swim when you realise you can make it!
# You are given 5 variables: sharkDistance = distance the shark needs to cover to eat you in metres, sharkSpeed = how fast it can move in metres/second, pontoonDistance = how far you need to swim to safety in metres, youSpeed = how fast you can swim in metres/second, dolphin = a boolean, if true, you can half the swimming speed of the shark as the dolphin will attack it.
# If you make it, return "Alive!", if not, return "Shark Bait!".

def shark(pontoon_distance, shark_distance, you_speed, shark_speed, dolphin):
    if dolphin:
        shark_speed = shark_speed / 2

    shark_eat_time = shark_distance / shark_speed
    you_safe_time = pontoon_distance / you_speed

    return "Shark Bait!" if you_safe_time > shark_eat_time else "Alive!"

# Implement a function which convert the given boolean value into its string representation.

def boolean_to_string(b):
    return str(b)

# When it's spring Japanese cherries blossom, it's called "sakura" and it's admired a lot. The petals start to fall in late April.
# Suppose that the falling speed of a petal is 5 centimeters per second (5 cm/s), and it takes 80 seconds for the petal to reach the ground from a certain branch.
# Write a function that receives the speed (in cm/s) of a petal as input, and returns the time it takes for that petal to reach the ground from the same branch.
# Notes:
# The movement of the petal is quite complicated, so in this case we can see the velocity as a constant during its falling.
# Pay attention to the data types.
# If the initial velocity is non-positive, the return value should be 0

def SakuraFall(v):
    return 400/v if v > 0 else 0



