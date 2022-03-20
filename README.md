# Create-Patterns-using-python
Create a pattern using python. 

This is the pattern that I drew: 
![image](https://user-images.githubusercontent.com/92804590/159185549-76f45617-48ed-4bbe-a7e2-ef032ea8d433.png)


To break the problem in small segments, I did the placing o in the middle, placing o randomly anywhere using the random function.
This was the first row. 
Depending on the first row, I calculated the 2nd row where I followed some particular rules: 
Place an "o" if the preceding row has an "o" at exactly one of its neighbors(but not both). In other words, place an "o" at index ``i`` of the second row
if there is an "o" at index ``i-1`` or index ``i+1`` of the first row, but notboth. For the beginning and end indices, place an "o" if there is an "o" at the
(only) neighbor. 
Then on the last function , createPattern, I used a loop to build up a string that contains multiple rows of pattern. 
