# Python Leetcode

Python version: 3.6.0

# Problem & Solution

| # | Title | Basic idea (One line) | Tags |
|---| ----- | -------- | --------------------- |
| [1](https://leetcode.com/problems/two-sum/) | [Two Sum](https://github.com/lowspace/leetcode/blob/main/code/1.%20Two%20Sum.ipynb) | |  |
| [7](https://leetcode.com/problems/reverse-integer/) | [Reverse Integer](https://github.com/lowspace/leetcode/blob/main/code/7.%20Reverse%20Integer.ipynb) |1. int -> string, reverse the string and add the sign; O(n) <br> 2. decompose the int one digit by one digit; O(n)|`decompose int`  |
| [9](https://leetcode.com/problems/palindrome-number/) | [Palindrome Number](https://github.com/lowspace/leetcode/blob/main/code/9.%20Palindrome%20Number.ipynb) |1. reverse(int) string = int string; O(n) <br> 2. int -> string, and compare the begining and the end; O(n/2) <br> 3. split the int in half, and compare; O(n/2)|`ambguity` overlapped-condition|
| [12](https://leetcode.com/problems/integer-to-roman/) | [Integer to Roman](https://github.com/lowspace/leetcode/blob/main/code/12.%20Integer%20to%20Roman.ipynb) | rule-based method; O(n) <br> 1. iterate by division <br> 2. iterate by substraction |`0 exclusive` two list a pair `construct rules`|
| [13](https://leetcode.com/problems/roman-to-integer/) | [Roman to Integer](https://github.com/lowspace/leetcode/blob/main/code/13.%20Roman%20to%20Integer.ipynb) | rule-based method; O(n)|`previous and current comparison`|
| [14](https://leetcode.com/problems/longest-common-prefix/) | [Longest Common Prefix](https://github.com/lowspace/leetcode/blob/main/code/14.%20Longest%20Common%20Prefix.ipynb) | 1. vertical scanning; O(nm) <br> 2. horizontal scanning;O(nm) <br> 3. divide and conquer; O(m\*log(n)) <br> 4. binary search; O(nm\*log(m)) | `input taxonomy` return taxonomy `vertical & horizontal`|
| [20](https://leetcode.com/problems/valid-parentheses/) | [Valid Parentheses](https://github.com/lowspace/leetcode/blob/main/code/20.%20Valid%20Parentheses.ipynb) | eliminate the pairs by proximity; O(n) | `stack`all comparison | 
| [21](https://leetcode.com/problems/merge-two-sorted-lists/) | [Merge Two Sorted Lists](https://github.com/lowspace/leetcode/blob/main/code/21.%20Merge%20Two%20Sorted%20Lists.ipynb) | | |
| [67](https://leetcode.com/problems/add-binary/) | [Add Binary](https://github.com/lowspace/leetcode/blob/main/code/67.%20Add%20Binary.ipynb) | 1. binary-decimal-binary; O(n) <br> 2. standard math binary addition; O(n) 3. bitwise operations; O(1)|`bitwise` `addition` |
| [69](https://leetcode.com/problems/sqrtx/) | [Sqrt(x)](https://github.com/lowspace/leetcode/blob/main/code/69.%20Sqrt(x).ipynb) | 1. binary search; O(nlog2) <br> 2. Newton method|`binary search` `newton`|
| [1512](https://leetcode.com/problems/number-of-good-pairs/) | [Number of Good Pairs](https://github.com/lowspace/leetcode/blob/main/code/1512.%20Number%20of%20Good%20Pairs.ipynb) | 1. brute force; O(n^2) <br> 2. combination formula; O(n)|`combination`|
| [564](https://leetcode.com/problems/find-the-closest-palindrome/submissions/) | [Find the Closest Palindrome](https://github.com/lowspace/leetcode/blob/main/code/564.%20Find%20the%20Closest%20Palindrome) | 1. brute force [DEPRECATE]; O(n) <br> 2. naive 5 forms; O(1) <br> 3. fancy 3 forms; O(1) <br> 4. fancy 4 forms; O(1)|`palindrome` `symmetry` `observation`|