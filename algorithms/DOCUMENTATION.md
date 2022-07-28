#### Jul 28, 2022

## Starting with the **Algorithm** section of _hackerrank_. 

## The __compare_points.py__ problem was to take two lists, compare the elements and award points to the greater element when comparing the elements with same indexes. Interestingly, I stumbled upon a problem where i could not return a list as an output. I tried making a list with ```list(alice_point).append(list(bob_point))``` but it's just wrong. Then i simply did this: 
```python
return [alice_point, bob_point]
```