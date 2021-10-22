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

### Test first

This problem is related to Pascal's triangle that could be drafted like below:

```
        1
       1 1
      1 2 1
     1 3 3 1
    1 4 6 4 1
    ...
```

It would be better to write some test cases:

- Pour 7 unit of water, glass at position 0 in row 1 must be 1

- Pour 15 unit of water, glass at position 2 in row 3 must be ~~3~~ 1 (overflow)

### Problem solving

To solve this problem in machine code, we could translate the total rows and total glasses in row to a 2D arrays:

```
|_|             row = 0, glasses = [[0][0]]
|_||_|          row = 1, glasses = [[1,0], [1,1]]
|_||_||_|       row = 2, glasses = [[2,0], [2,1], [2,2]]
|_||_||_||_|    row = 3, glasses = [[3,0], [3,1], [3,2], [3,3]]
...
```

- Pour the water in row(0).

- If glass[0][0] is full and the water still remain, the remain water will be flowed to row(1).

- Glass[1,0] will receive half of remain water, glass [1,1] also receive half of remain water.

- If any of glass in row(1) is full and water still remain, repeat above process until no water remain.


### Testing
```

python -m unittest
```


### Running

```
python water_overflow/main.py {1} {2} {3} {4}
```
with {1} is total water in Litres, {2}, {3} is the row & position of glass to find. To see simple illustrate of the glasses triangle, put the {4} to true


### Example

```
python water_overflow/main.py 5.2 6 2 true
               \▇/
             \▇/ \▇/
           \▇/ \▇/ \▇/
         \▇/ \▇/ \▇/ \▇/
       \▂/ \▇/ \▇/ \▇/ \▂/
     \_/ \▅/ \▇/ \▇/ \▅/ \_/
   \_/ \_/ \▅/ \▇/ \▅/ \_/ \_/
 \_/ \_/ \_/ \▂/ \▂/ \_/ \_/ \_/
When pouring 5.2L of water, the level of glass in row 6 at pos 2 is 210.9375ml
```
