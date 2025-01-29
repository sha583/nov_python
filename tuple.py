Q2 Create a tuple containing the following elements: &quot;apple&quot;, &quot;banana&quot;, &quot;cherry&quot;. How
would you access the second element?

tuple=("apple","banana","cherry")
print(tuple[1])

Q3 Write a Python program to find the length of a given tuple.

tuple=("apple","banana","cherry")
print(len(tuple))

Q4 Can you modify a tuple? Why or why not?

No, you cannot modify tuple because tuples are immutable you cannot add or delete the elements

Q5 Create a tuple containing numbers from 1 to 10. Use slicing to extract a sub-tuple containing
elements from index 3 to 7.

tuple=(1,2,3,4,5,6,7,8,9,10)
subtuple=tuple[3:8]
print(subtuple)