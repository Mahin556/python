square= {f"square of {num}":num**2 for num in range(1,11)}
print(square)

ch="mahin"
word_count={char:ch.count(char) for char in ch}
print(word_count)

even={num:("even" if num%2==0 else "odd") for num in range(1,11)}
print(even)



# sets comprehension only one video 
s = {k**2 for k in range(1,11)}
print(s)
names = ['harshit', 'mohit', 'rohit'] 
first = {name[0] for name in names} 
print (first)
