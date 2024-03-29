# Python Leetcode

Python version: 3.7.11

Leetcode profile: https://leetcode.com/dnhb/

# User Guide

`init.py`: This script allows users to create a Jupyter notebook of a Leetcode problem by paste the **name** or **URL** of that problem in [leetcode.com](https://leetcode.com/) from computer clipboard, and this notebook consists of six parts:

+ Problem content
+ Summary
+ Problem Description
+ Method
+ Footnote
+ script that adds summary to `README.md` file

`Template.ipynb`: This file is an instance created by `init.py`.

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
| [125](https://leetcode.com/problems/valid-palindrome) | [Valid Palindrome](https://github.com/lowspace/leetcode/blob/main/code/125.%20Valid%20Palindrome.ipynb) | 1. holistic approach; O(n) <br> 2. atomistic approach (two pointer); O(n) | `palindrome` `two pointer` `string operation` |
| [680](https://leetcode.com/problems/valid-palindrome-ii) | [Valid Palindrome II](https://github.com/lowspace/leetcode/blob/main/code/680.%20Valid%20Palindrome%20II.ipynb) | 1. brute force [deprecated]; O(n) <br> 2. two pointer (linear) <br> [deprecated]; O(n/2) <br> 3. two pointer (binary); O(logn) <br> 4. two pointer (recursive); O(n) | `palindrome` `two pointer` `binary search` |
| [409](https://leetcode.com/problems/longest-palindrome) | [Longest Palindrome](https://github.com/lowspace/leetcode/blob/main/code/409.%20Longest%20Palindrome.ipynb) | 1. count pairs; O(n) <br> 2. count un-paired characters; O(n) | `palindrome` `complementary` `dict` `set` |
| [1332](https://leetcode.com/problems/remove-palindromic-subsequences) | [Remove Palindromic Subsequences](https://github.com/lowspace/leetcode/blob/main/code/1332.%20Remove%20Palindromic%20Subsequences.ipynb) | 1. intutive method; O(1) | `palindrome` `intuition` |
| [58](https://leetcode.com/problems/length-of-last-word) | [Length of Last Word](https://github.com/lowspace/leetcode/blob/main/code/58.%20Length%20of%20Last%20Word.ipynb) | brute force; O(n) | `string` |
| [8](https://leetcode.com/problems/string-to-integer-(atoi)) | [String to Integer (atoi)](https://github.com/lowspace/leetcode/blob/main/code/8.%20String%20to%20Integer%20(atoi).ipynb) | brute force; O(n) | `string` `regex` |
| [65](https://leetcode.com/problems/valid-number) | [Valid Number](https://github.com/lowspace/leetcode/blob/main/code/65.%20Valid%20Number.ipynb) | brute force; O(n) | `string` `regex` |
| [468](https://leetcode.com/problems/validate-ip-address) | [Validate IP Address](https://github.com/lowspace/leetcode/blob/main/code/468.%20Validate%20IP%20Address.ipynb) | 1. divide and conquer; O(n) <br> 2. regex; O(1) | `string` `regex` |
| [709](https://leetcode.com/problems/to-lower-case) | [To Lower Case](https://github.com/lowspace/leetcode/blob/main/code/709.%20To%20Lower%20Case.ipynb) | 1. lower(); O(n) <br> 2. dictionary mapping; O(n) <br> 3. XOR method; O(n) | `string` `XOR` `mapping` |
| [38](https://leetcode.com/problems/count-and-sa) | [Count and Sa](https://github.com/lowspace/leetcode/blob/main/code/38.%20Count%20and%20Say.ipynb) | 1. straightforward loop; O(n) <br> 2. recursive; O(n) | `string` `recursive` `while` |
| [151](https://leetcode.com/problems/reverse-words-in-a-string) | [Reverse Words in a String](https://github.com/lowspace/leetcode/blob/main/code/151.%20Reverse%20Words%20in%20a%20String.ipynb) | by steps; O(n) | `string` `split` |
| [6](https://leetcode.com/problems/zigzag-conversio) | [Zigzag Conversio](https://github.com/lowspace/leetcode/blob/main/code/6.%20Zigzag%20Conversion.ipynb) | 1. built by columns; O(n) <br> 2. built by rows; O(n) | `string` `sequence` `intuition` |
| [1694](https://leetcode.com/problems/reformat-phone-number) | [Reformat Phone Number](https://github.com/lowspace/leetcode/blob/main/code/1694.%20Reformat%20Phone%20Number.ipynb) | step by step; O(n) | `string` |
| [33](https://leetcode.com/problems/search-in-rotated-sorted-arra) | [Search in Rotated Sorted Arra](https://github.com/lowspace/leetcode/blob/main/code/33.%20Search%20in%20Rotated%20Sorted%20Array.ipynb) |1. binary search; O(logn) <br> 2. linear method; O(n) | `binary search` `generality` |
| [81](https://leetcode.com/problems/search-in-rotated-sorted-array-ii) | [Search in Rotated Sorted Array II](https://github.com/lowspace/leetcode/blob/main/code/81.%20Search%20in%20Rotated%20Sorted%20Array%20II.ipynb) | 1. linear search; O(n) <br> 2. binary search; O(logn)/O(n) | `binary search` `conduct condition` |
| [153](https://leetcode.com/problems/find-minimum-in-rotated-sorted-arra) | [Find Minimum in Rotated Sorted Arra](https://github.com/lowspace/leetcode/blob/main/code/153.%20Find%20Minimum%20in%20Rotated%20Sorted%20Array.ipynb) | 1. linear search; O(n) <br> 2. binary search; O(logn) | `binary search` `interval boundary` |
| [154](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii) | [Find Minimum in Rotated Sorted Array II](https://github.com/lowspace/leetcode/blob/main/code/154.%20Find%20Minimum%20in%20Rotated%20Sorted%20Array%20II.ipynb) | binary search; O(logn)/O(n) | `binary search` `categorized discussion` |
| [34](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-arra) | [Find First and Last Position of Element in Sorted Arra](https://github.com/lowspace/leetcode/blob/main/code/34.%20Find%20First%20and%20Last%20Position%20of%20Element%20in%20Sorted%20Array.ipynb) | 1. linear search; O(n) <br> 2. 2-time binary search; O(logn) | `binary search` `existence` `boundary` |
| [162](https://leetcode.com/problems/find-peak-element) | [Find Peak Element](https://github.com/lowspace/leetcode/blob/main/code/162.%20Find%20Peak%20Element.ipynb) | 1. linear scan; O(n) <br> 2. binary search; O(logn) | `binary search` `monotonicity` `inflection point` `mathematical assumption` |
| [540](https://leetcode.com/problems/single-element-in-a-sorted-arra) | [Single Element in a Sorted Arra](https://github.com/lowspace/leetcode/blob/main/code/540.%20Single%20Element%20in%20a%20Sorted%20Array.ipynb) | 1. linear scan; O(n) <br> 2. binary search; O(logn) | `binary search` `drop and pick` |
| [74](https://leetcode.com/problems/search-a-2d-matrix) | [Search a 2D Matrix](https://github.com/lowspace/leetcode/blob/main/code/74.%20Search%20a%202D%20Matrix.ipynb) | 1. linear scan; O(n) <br> 2. binary search; O(logn) | `binary search` `linear data` |
| [520](https://leetcode.com/problems/detect-capital) | [Detect Capital](https://github.com/lowspace/leetcode/blob/main/code/520.%20Detect%20Capital.ipynb) | 1. brute force; O(n) <br> 2. two pointer; O(n/2) <br> 3. regex; O(n) | `built-in method` `regex` `two pointer` |
| [941](https://leetcode.com/problems/valid-mountain-arra) | [Valid Mountain Arra](https://github.com/lowspace/leetcode/blob/main/code/941.%20Valid%20Mountain%20Array.ipynb) | 1. two pointer; O(n) <br> 2. one pass; O(n) | `two pointer` `one pass` |
| [62](https://leetcode.com/problems/unique-paths) | [Unique Paths](https://github.com/lowspace/leetcode/blob/main/code/62.%20Unique%20Paths.ipynb) | DP, O(mn) | `DP` |
| [63](https://leetcode.com/problems/unique-paths-ii) | [Unique Paths II](https://github.com/lowspace/leetcode/blob/main/code/63.%20Unique%20Paths%20II.ipynb) | DP, O(mn) | `DP` `boundary condition` |
| [64](https://leetcode.com/problems/minimum-path-sum) | [Minimum Path Sum](https://github.com/lowspace/leetcode/blob/main/code/64.%20Minimum%20Path%20Sum.ipynb) | 1. recursive DP; O(mn) <br> 2. iterative DP; O(mn) | `DP` `recursive` `iterative` |
| [70](https://leetcode.com/problems/climbing-stairs) | [Climbing Stairs](https://github.com/lowspace/leetcode/blob/main/code/70.%20Climbing%20Stairs.ipynb) | 1. combination method; O(n) <br> 2. DP; O(n) | `DP` `combination` |
| [66](https://leetcode.com/problems/plus-one) | [Plus One](https://github.com/lowspace/leetcode/blob/main/code/66.%20Plus%20One.ipynb) | 1. mathematical rule; O(n) <br> 2. built-in convert; O(n) | `mathematical` `built-in` |
