# challenge 1

name = input("Enter you name: ")
#shoutout the name
print("Hi there", name)
print("Nice to meet you.")

# challenge 2

#the list
over_under_list = [1,45,32,21,5,17,43,93]

#traverse all numbers in the list
for num in over_under_list:
    #check if number greater than 25
    if num>25:
        #print "over"
        print("over")
    #check if number smaller than 25
    if num<25:
        print("under")

# challenge 3

names_list = ["bob", "jimmy", "max b", "bernie", "jordan", "future hendrix"]

max_len = -1
for name in names_list:
    if len(name) > max_len:
        max_len = len(name)
        resulted_name = name
print(resulted_name)

# challenge 4
def getLargestName(names_list):
    max_len = -1
    for name in names_list:
        if len(name) > max_len:
            max_len = len(name)
            resulted_name = name
    return resulted_name


###############################

# Testing

names_list = ["bob", "jimmy", "max b", "bernie", "jordan", "future hendrix"]
big_name = getLargestName(names_list)
print(big_name)

# challenge 5


def seperate_list(names_list):
    # even and odd list are initially empty
    even_list = []
    odd_list = []
    # iterate through list names_list
    for i in names_list:
        # if length is even
        if len(i) % 2 == 0:
            # add name to even list
            even_list.append(i)
        # if length is even
        else:
            # add name to odd list
            odd_list.append(i)
    # iterate though length of even list
    for j in range(len(even_list)):
        # First character is replaced with 'b' 
        even_list[j] = 'b' + even_list[j][1:]
    # iterate though length of odd list
    for k in range(len(odd_list)):
        # Last character is replaced with 'a #c'
        odd_list[k] = odd_list[k][:-1] + 'a #c'
    # print even and odd list 
    print("Even list = ", even_list)
    print("Odd list = ", odd_list)
    # return even list
    return even_list

names_list = ["bob","jimmy","max b", "bernie", "jordan", "future hendrix"]
print(seperate_list(names_list))