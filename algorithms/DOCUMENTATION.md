#### Jul 28, 2022

### Starting with the **Algorithm** section of _hackerrank_. 

### The __compare_points.py__ problem was to take two lists, compare the elements and award points to the greater element when comparing the elements with same indexes. Interestingly, I stumbled upon a problem where i could not return a list as an output. I tried making a list with ```list(alice_point).append(list(bob_point))``` but it's just wrong. Then i simply did this: 
```python
return [alice_point, bob_point]
```

### **Sum Big Numbers** is to add the big numbers, or say floating numbers. Shouldn't forget to round the sum before returning it. 

### I loved solving the **matrix_diagonal** problem. For in this i needed to see the pattern. Any matrix would look like this
```
(0,0)   (0,1)   (0,2)   (0,3)
(1,0)   (1,1)   (1,2)   (1,3)
(2,0)   (2,1)   (2,2)   (2,3)
(3,0)   (3,1)   (3,2)   (3,3)
```
### All i need is the sum of elements (0,0), (1,1), (2,2) and (3,3) and of (0,3), (1,2), (2,1), (3,0). So four elements from each diagonal. How? Run the for loop four times from 0 and add array[i][i] to temporary variable. And for the backward diagonal, the parrent goes like: the row element increases from 0 - 3 and the column element decreases from 3 - 0. So, applying this logic will surely solve for any order square matrix. 

#### Jul 29, 2022

### In `plusMinus` i had to find the average of numbers of the positive, negative and zeros. It's easy per se but i had to display it in the format like `4.200000`. So had to use format() method to do it. The syntax goes:

```python
format(variableName, '.6f')
```

### Another easy 10 points for solving the `staircase` problem. Strings manipulation in python makes this real easy.

### The `minMaxSum` was about finding the max and min sum from 5 integers using only four of them. 