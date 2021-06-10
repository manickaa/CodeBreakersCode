class Cat:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

def hash(object):
    M = 1000 #size of the array
    age = object.age
    name = object.name
    #print(name)
    hashValue = 0
    R = 256
    for char in name:
        hashValue = (R * hashValue + ord(char))
    hashValue += age
    return hashValue % M

def hash_string(string_key):
	#print(type(string_key))
	M = 1001
	# R is the size of the alphabet. Becuase we are working with ASCII 256, we set R = 256.
	R = 256
	hash_value = 0
	for char in string_key:
		#print(type(char))
		hash_value = (hash_value * R + ord(char)) % M
	return hash_value


kitty = Cat('kitty', 23)
cat = Cat('kitty', 23)
print(hash(kitty))
print(hash(cat))
#print(hash_string('kitty'))
#print(hash_string('kitty'))

# string = 'kitty'
# for char in string:
# 	print(ord(char))