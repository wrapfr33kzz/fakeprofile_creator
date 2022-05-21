from faker import Faker
fake = Faker()
print(fake.name())
print(" \n")
print(fake.email())
print(" \n")
print(fake.country())

print("\n ")
print(fake.profile())

print(" \n")
print(dir(Faker()))
