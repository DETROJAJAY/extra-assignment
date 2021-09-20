print("hello")
print('hello')

a = "hello"
print(a)

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

a = "Hello, World!"
print(a[1])

for x in "banana":
  print(x)

a = "Hello, World!"
print(len(a))  

txt = "The best things in life are free!"
print("free" in txt)

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

txt = "The best things in life are free!"
print("expensive" not in txt)

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

b = "Hello, World!"
print(b[2:5])

print(b[:5])

print(b[2 :])

print(b[-5 :-2])

a = "Hello, World!"
print(a.upper())

print(a.lower())

print(a.strip())

print(a.replace("H","J"))

print(a.split(","))

a = "Hello"
b = "World"
c = a + b
print(c)

c = a + " " + b
print(c)

age = "36"
txt = "My name is John, I am " + age
print(txt)

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

#txt = "We are the so-called "Vikings" from the north."
#we get error if we use double quote inside the double quote

txt = "We are the so-called \"Vikings\" from the north."

txt = 'It\'s alright.'
print(txt) 

txt = "This will insert one \\ (backslash)."
print(txt) 

txt = "Hello\nWorld!"
print(txt)

txt = "Hello\rWorld!"
print(txt) 

txt = "Hello\tWorld!"
print(txt) 

txt = "Hello \bWorld!"
print(txt) 

txt = "Hello \fWorld!"
print(txt) 

txt = "\110\145\154\154\157"
print(txt) 

txt = "\x48\x65\x6c\x6c\x6f"
print(txt) 

a = "hello world"

print(a.capitalize())
print(a.casefold())
print(a.center(1))
print(a.count(a))
print(a.encode())
print(a.endswith(a))
print(a.expandtabs())
print(a.find(a))
print(a.format())
print(a.format_map(3))
print(a.index(a))
print(a.isalnum())
print(a.isalpha())
print(a.isdecimal())
print(a.isdigit())
print(a.isidentifier())
print(a.islower())
print(a.isnumeric())
print(a.isprintable())
print(a.isspace())
print(a.istitle())
print(a.isupper())
print(a.join(c))
print(a.ljust(1))
print(a.lower())
print(a.lstrip())
print(a.maketrans("d","s"))
print(a.partition("world"))
print(a.replace("world","word"))
print(a.rfind("hello"))
print(a.rindex("hello"))
print(a.rjust(9))
print(a.rpartition("word"))
print(a.rsplit())
print(a.split())
print(a.splitlines())
print(a.startswith("hello"))
print(a.strip())
print(a.swapcase())
print(a.title())
b = {10: 20}
print(a.translate(a))
print(a.upper())
print(a.zfill(9))