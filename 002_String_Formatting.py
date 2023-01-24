name = 'Bob'

greeting = f'Hello, {name}'

print(greeting)

name  = 'Rudolf'

print(f'Hello, {name}')

name = 'John Tik'
greeting = "Hello, {}"
with_name = greeting.format(name)
with_name_two = greeting.format("Sumet")

print(with_name)
print(with_name_two)

longer_phrase = "Hello, {}. Today is {}."

formatted = longer_phrase.format("John Tik", "Thursday")
print(formatted)