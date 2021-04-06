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

# Given a month as an integer from 1 to 12, return to which quarter of the year it belongs as an integer number.
# For example: month 2 (February), is part of the first quarter; month 6 (June), is part of the second quarter; and month 11 (November), is part of the fourth quarter.

def quarter_of(month):
    if month in range(1, 4):
        return 1
    elif month in range(4, 7):
        return 2
    elif month in range(7, 10):
        return 3
    elif month in range(10, 13):
        return 4

# You are given an array with positive numbers and a number N. You should find the N-th power of the element in the array with the index N. If N is outside of the array, then return -1. Don't forget that the first element has the index 0.
# Let's look at a few examples:
# array = [1, 2, 3, 4] and N = 2, then the result is 3^2 == 9;
# array = [1, 2, 3] and N = 3, but N is outside of the array, so the result is -1.

def index(array, n):
    try:
        return array[n]**n
    except:
        return -1

# Given 2 strings, a and b, return a string of the form short+long+short, with the shorter string on the outside and the longer string on the inside. The strings will not be the same length, but they may be empty ( length 0 ).
# For example:
# solution("1", "22") # returns "1221"

def solution(a, b):
    return a+b+a if len(a)<len(b) else b+a+b

# Write a program that finds the summation of every number from 1 to num. The number will always be a positive integer greater than 0.
# For example:
# summation(2) -> 3
# 1 + 2
# summation(8) -> 36

def summation(num):
    return sum(xrange(num + 1))

# Given a year, return the century it is in.

# Input , Output Examples ::
# centuryFromYear(1705)  returns (18)
# centuryFromYear(1900)  returns (19)
# centuryFromYear(1601)  returns (17)
# centuryFromYear(2000)  returns (20)

def century(year):
    return (year + 99) // 100

# Your task is to make two functions, max and min (maximum and minimum in PHP and Python) that take a(n) array/vector of integers list as input and outputs, respectively, the largest and lowest number in that array/vector.

def minimum(arr):
    return min(arr)

def maximum(arr):
    return max(arr)

#  Switch gravity of the boxes
# flip('R', [3, 2, 1, 2])     =>  [1, 2, 2, 3]
#
 def flip(d,a):
    return sorted(a, reverse=d=='L')

# You are given two interior angles (in degrees) of a triangle.
# Write a function to return the 3rd.
# Note: only positive integers will be tested.

def other_angle(a, b):
    return 180 - (a + b)

# Write a function that rearranges an integer into its largest possible value.
# super_size(123456) # 654321
# super_size(105)    # 510
# super_size(12)     # 21
def super_size(n):
    return int(''.join(sorted(str(n), reverse = True)))

# In this Kata, you will be given an array of numbers in which two numbers occur once and the rest occur only twice. Your task will be to return the sum of the numbers that occur only once.
# For example, repeats([4,5,7,5,4,8]) = 15 because only the numbers 7 and 8 occur once, and their sum is 15. Every other number occurs twice.

def repeats(arr):
    return sum([x for x in arr if arr.count(x) == 1])

# In this kata, we will be using a more complicated sequence: 0, 1, 3, 6, 10, 15, 21, 28, ... This sequence is generated with the pattern: "the nth term is the sum of numbers from 0 to n, inclusive".
from itertools import accumulate

def sum_of_n(n):
    if n >= 0:
        return list(accumulate(range(n+1)))
    return list(accumulate(range(0, n-1, -1)))

#  Given an array of integers as strings and numbers, return the sum of the array values as if all were numbers.
#  Return your answer as a number.

def sum_mix(arr):
    return sum([int(i) for i in arr])

# This kata is about multiplying a given number by eight if it is an even number and by nine otherwise.

def simple_multiplication(number) :
    return number * 9 if number % 2 else number * 8

# Given a number n, return the number of positive odd numbers below n, EASY!
def odd_count(n):
    return len(range(1, n, 2))

# Timmy & Sarah think they are in love, but around where they live, they will only know once they pick a flower each. If one of the flowers has an even number of petals and the other has an odd number of petals it means they are in love.
# Write a function that will take the number of petals of each flower and return true if they are in love and false if they aren't.

def lovefunc(flower1, flower2):
    return flower1 % 2 != flower2 % 2

#  Write a function named setAlarm which receives two parameters. The first parameter, employed, is true whenever you are employed and the second parameter, vacation is true whenever you are on vacation.
#  The function should return true if you are employed and not on vacation (because these are the circumstances under which you need to set an alarm). It should return false otherwise.

def set_alarm(employed, vacation):
    return employed and not vacation

# The first input array is the key to the correct answers to an exam, like ["a", "a", "b", "d"]. The second one contains a student's submitted answers.
# The two arrays are not empty and are the same length. Return the score for this array of answers, giving +4 for each correct answer, -1 for each incorrect answer, and +0 for each blank answer, represented as an empty string (in C the space character is used).
# If the score < 0, return 0.
def check_exam(arr1,arr2):
    score = 0
    for i in range(0,4):
        if arr1[i] == arr2[i]:
            score += 4
        elif arr1[i] == "" or arr2[i] == "":
            score += 0
        else:
            score -= 1

    return score if score >= 0  else 0

# Make a function that will return a greeting statement that uses an input; your program should return, "Hello, <name> how are you doing today?".

def greet(name):
    return "Hello, {} how are you doing today?".format(name)

# Create a method is_uppercase() to see whether the string is ALL CAPS.
def is_uppercase(inp):
    return inp.isupper()

# Create a function that will return a string that combines all of the letters of the three inputed strings in groups. Taking the first letter of all of the inputs and grouping them next to each other. Do this for every letter, see example below!
# E.g. Input: "aa", "bb" , "cc" => Output: "abcabc"
# Note: You can expect all of the inputs to be the same length.
def triple_trouble(one, two, three):
    return "".join(a+b+c for a,b,c in zip(one,two,three))

# Your goal is to return multiplication table for number that is always an integer from 1 to 10.
def multi_table(number):
    return '\n'.join(f'{i} * {number} = {i * number}' for i in range(1, 11))

# Character recognition software is widely used to digitise printed texts. Thus the texts can be edited, searched and stored on a computer.
# When documents (especially pretty old ones written with a typewriter), are digitised character recognition softwares often make mistakes.
# Your task is correct the errors in the digitised text. You only have to handle the following mistakes:
# S is misinterpreted as 5
# O is misinterpreted as 0
# I is misinterpreted as 1
# The test cases contain numbers only by mistake.
def correct(string):
    return string.replace('5', 'S').replace('0', 'O').replace('1', 'I')

# You are provided with an array of positive integers and an additional integer n (n > 1).
# Calculate the sum of each value in the array to the nth power. Then subtract the sum of the original array.
# Examples
# {1, 2, 3}, 3  -->  (1^3 + 2^3 + 3^3 ) - (1 + 2 + 3)  -->  36 - 6  -->  30
# {1, 2}, 5     -->  (1^5 + 2^5) - (1 + 2)             -->  33 - 3  -->  30

def modified_sum(a, n):
    return sum([item**n for item in a]) - sum([item for item in a])

# Create the function consecutive(arr) that takes an array of integers and return the minimum number of integers needed to make the contents of arr consecutive from the lowest number to the highest number.
# For example:
# If arr contains [4, 8, 6] then the output should be 2 because two numbers need to be added to the array (5 and 7) to make it a consecutive array of numbers from 4 to 8. Numbers in arr will be unique.

def consecutive(arr):
    return max(arr) - min(arr) + 1 - len(arr) if arr else 0

# The purpose of this kata is to work out just how many bottles of duty free whiskey you would have to buy such that the saving over the normal high street price would effectively cover the cost of your holiday.
# You will be given the high street price (normPrice), the duty free discount (discount) and the cost of the holiday.
# For example, if a bottle cost £10 normally and the discount in duty free was 10%, you would save £1 per bottle. If your holiday cost £500, the answer you should return would be 500.
# All inputs will be integers. Please return an integer. Round down.

def duty_free(price, discount, holiday_cost):
    saving = price * discount / 100.0
    return int(holiday_cost / saving)

# Create a function that takes 2 positive integers in form of a string as an input, and outputs the sum (also as a string):

#   sum_str("4", "5")    # should output "9"
#   sum_str("34", "5")   # should output "39"

def sum_str(a, b):
    return str(int(a or 0) + int(b or 0))

# Your function takes two arguments:
# current father's age (years)
# current age of his son (years)
# Сalculate how many years ago the father was twice as old as his son (or in how many years he will be twice as old).

def twice_as_old(dad_years_old, son_years_old):
    #. if son 15 , dad 50 = son * 2 = 30
    return abs(dad_years_old - son_years_old * 2)

# Write a function to split a string and convert it into an array of words. For example:
def string_to_split(s):
    return s.split(' ')

# Write function bmi that calculates body mass index (bmi = weight / height2).

# if bmi <= 18.5 return "Underweight"
# if bmi <= 25.0 return "Normal"
# if bmi <= 30.0 return "Overweight"
# if bmi > 30 return "Obese"

def bmi(weight, height):
    bmi = weight / height ** 2
    if bmi <= 18.5:
        return "Underweight"
    elif bmi <= 25:
        return "Normal"
    elif bmi <= 30:
        return "Overweight"
    else:
        return "Obese"

# Print a list of numbers the length of n
def pre_fizz(n):
    return list(range(1, n+1))

# You're at the zoo... all the meerkats look weird. Something has gone terribly wrong - someone has gone and switched their heads and tails around!
# Save the animals by switching them back. You will be given an array which will have three values (tail, body, head). It is your job to re-arrange the array so that the animal is the right way round (head, body, tail).
# Same goes for all the other arrays/lists that you will get in the tests: you have to change the element positions with the same exact logics

def fix_the_meerkat(arr):
    return arr[::-1]

# or

def fix_the_meerkat(arr):
    arr.reverse()
    return arr

# Return the Nth Even Number
# nthEven(1) //=> 0, the first even number is 0
# nthEven(3) //=> 4, the 3rd even number is 4 (0, 2, 4)
# nthEven(100) //=> 198
# nthEven(1298734) //=> 2597466

def nth_even(n):
    return 2 * (n - 1);

# Task
# Your task is to return the correct string using the Template String Feature.
# Input
# Two Strings, no validation is needed.
# Output
# You must output a string containing the two strings with the word ```' are '```
def temple_strings(obj, feature):
    return "{} are {}".format(obj, feature)

# Write a function, gooseFilter / goose-filter / goose_filter / GooseFilter, that takes an array of strings as an argument and returns a filtered array containing the same elements but with the 'geese' removed.
geese = {"African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"}

def goose_filter(birds):
    return [bird for bird in birds if bird not in geese]

# There's a "3 for 2" (or "2+1" if you like) offer on mangoes. For a given quantity and price (per mango), calculate the total cost of the mangoes.

def mango(quantity, price):
    return (quantity - quantity // 3) * price

# I would like to be able to pass an array with two elements to my swapValues function to swap the values. However it appears that the values aren't changing.
def swap_values(args):
    args[0], args[1] = args[1], args[0]
    return args
