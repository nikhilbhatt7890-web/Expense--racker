# l = ["new application","key","login"]
# s = ""
# n = []
# for object in l :
#     for a in object :
#         s = s + str(ord(a))
#     n.append(s)
#     s = ''
# def o ():
#     print("c")

# def f():
#     print("e")
# D = {"c":o,"e":f}

# output = D.get("c")
# output()
# l = [1,4,3]
# y = (2,3,-2,3)
# x = {3,7}

# print(list(reversed(list(x))))


# if x == set():
#     print("got it ")

# # l.insert(1,4)
# # print(l)
# # l.extend(l[:3])
# # l.pop(-3)
# # l.remove()
# # l[4] = None
# # l[4] 
# l[::2] = [None,None]
# print(l)
n = 4
for i in range(n):
    row = ''
    for j in range(n):
        if i in [0, n-1] or j in [0, n-1]:
            row += '1'
        elif i == j:
            row += '0'
        else:
            row += '1'
    print(row)

result = 0
for i in range(1, 4):
    for j in range(1, 4):
        if i == j:
            continue
        if i + j > 4:
            break
        result += i + j
print(result)
# l = "nikhil bhatt"
# a = "".join(l.split())
# print(l,a)

# l = [1,23,4,3,2,9]


# # print(l[-4:] + l[:-4])
# # items
# l.pop(1)
# print(l)

# print(isinstance(0,bool))
# print(ord("T"))