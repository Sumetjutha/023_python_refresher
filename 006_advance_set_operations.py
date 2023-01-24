friends = {'Bob', 'Rolf', 'Anne'}
abroad = {'Bob', 'Anne'}

local_friends = friends.difference(abroad)
print(local_friends)

local_friends_2 = abroad.difference(friends)
print(local_friends_2)

#############################################

local = {'John'}
abod = {'Bob', 'Jane'}

friends_all = local.union(abod)
print(friends_all)

#############################################

art = {"Bob", "Jane", 'Rolf', 'Charlie'}
science = {"Bob", "Jane", "Adam", "Anne"}

both = art.intersection(science)
print(both)

#############################################

my_list = [20, 30, 50]

# Create a tuple with 1 value
my_tuple = 15,

set1 = {14, 5, 9, 31, 12, 77, 67, 8}
set2 = {5, 77, 9, 12}

# Hello This is My World
