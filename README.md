## Water Overflow problem

There is a stack of water glasses in a form of triangle as illustrated. Each glass has a 250ml capacity.

When a liquid is poured into the top most glass any overflow is evenly distributed between the glasses in the next row. That is, half of the overflow pours into the left glass while the remainder of the overflow pours into the right glass

Write a program that is able to calculate and illustrate how much liquid is in the j’th glass of the i’th row when K litres are poured into the top most glass


```
        |_|         i = 0
       |_||_|       i = 1
     |_||_||_|      i = 2
    |_||_||_||_|    i = 3
    ...
```

### 

This problem is related to Pascal's triangle that could be drafted like below:

```
        1
       1 1
      1 2 1
     1 3 3 1
    1 4 6 4 1
    ...
```

I would be better to write some test to assert:


- Pour 7 unit of water, glass at position 0 in row 1 must be 1

- Pour 15 unit of water, glass at position 2 in row 3 must be 3

