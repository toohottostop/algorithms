# Algorithms
## decrypt
We have encoded string.  
Instruction for decode:
1) Each character of the string is either a letter, or a space, or a dot ".", Or two dots "..".
2) If there is a dot after a letter, then we leave the letter unchanged. In this case, the point itself must be deleted.
3) If there are two dots after a letter, then the previous character must be erased. In this case, both points must also be deleted.
4) It is possible that the message after decryption will be empty. As a result, you can return just an empty string
Time complexity: O(log N) where N - length of encode string
## search closest number in array
Solving the problem using binary search.  
Time complexity: O(log N)
## shifted array
Flask app to find pivot point in shifted and sorted array
Time complexity: O(log N)