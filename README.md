# Python Leetcode

Python version: 3.6.0

# Problem & Solution

| # | Title | Basic idea (One line) | Tags |
|---| ----- | -------- | --------------------- |
| [1](https://leetcode.com/problems/two-sum/) | [Two Sum](https://github.com/lowspace/leetcode/blob/main/code/1.%20Two%20Sum.ipynb) | |  |
| [7](https://leetcode.com/problems/reverse-integer/) | [Reverse Integer](https://github.com/lowspace/leetcode/blob/main/code/7.%20Reverse%20Integer.ipynb) |1. int -> string, reverse the string and add the sign; O(n) <br> 2. decompose the int one digit by one digit; O(n)|`decompose int`  |
| [9](https://leetcode.com/problems/palindrome-number/) | [Palindrome Number](https://github.com/lowspace/leetcode/blob/main/code/9.%20Palindrome%20Number.ipynb) |1. reverse(int) string = int string; O(n) <br> 2. int -> string, and compare the begining and the end; O(n/2) <br> 3. split the int in half, and compare; O(n/2)|`ambguity` overlapped-condition|
| [12](https://leetcode.com/problems/integer-to-roman/) | [Integer to Roman]() | | |
| [13](https://leetcode.com/problems/roman-to-integer/) | [Roman to Integer]() | rule-based method; O(n)|`previous and current comparison`|