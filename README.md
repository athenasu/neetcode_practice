# neetcode_practice

## Introduction

Welcome to my Leetcode/Neetcode challenge workspace! This is where I document my adventures in solving coding problems, sharing my solutions, insights, and thoughts along the way. It's a collection of challenges that I tackled to train my brain. Each problem is like a puzzle waiting to be solved, and this repository captures my thought process and growth as a programmer.

- Note: Some of the functions have detailed steps or have the solutions on the bottom because I kept on revisiting them just to make sure I understood. Some functions I wrote with different languages, just to get in some extra practice.

## Prerequisites

1. Programming Languages:
   1. Python3
   2. JavaScript
2. Python libraries used:
   1. math
   2. timeit

## Data Structures

### I. Lists and Hashing

1. contains_duplicates
2. group_anagrams (Python and JavaScript)
3. is_anagram
4. k_most_frequent
5. longest_consecutive
6. product_of_list_except_self
7. two_sum (Python and JavaScript)
8. valid_sudoku

### II. Two Pointers

1. three_sum
2. two_sum
3. valid_palindrome

## Notes

1. contains_duplicates:
   - Notes: I ran a `timeit` test on the two functions because people on Leetcode were arguing about the performance of creating a new `dictionary` or just using the `len(set())` method. Using `len(set())` was faster.
2. k_most_frequent:
   - Notes: Tried a few ways to solve it. Tried to `del` and keep using the `max()` method, but it didn't seem as elegant. Finally ended up storing the `frequency` (list of lists) and the `count` (dictionary), and that looked a bit better.
3. longest_consecutive:
   - Notes: Came up with 2 other solutions after my first solution was only 22% faster.
4. product_of_list_except_self:
   - Notes: Had trouble understanding the question at first. Figured it out using just the `\\`, but got an exception whenever there was a `0` in the list passed in (and found out we're not allowed to use division). Tried `filter()` and `prod()`, but didn't work out. Finally, tried to understand what the given solution was and redid the problem a few times.
5. valid_sudoku:
   - Notes: This one was fun because it's so visually complicated.
