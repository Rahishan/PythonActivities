print("Numbers")
print("---------------------------------")
a=10
print(type(a),id(a),a)
a=23.7
print(type(a),id(a),a)
a=2+6j
print(type(a),id(a),a)


print("\nText")
print("---------------------------------")
a='h'
print(type(a),id(a),a)
a="h"
print(type(a),id(a),a)
a='hello'
print(type(a),id(a),a)
a="hello"
print(type(a),id(a),a)

print("\nBoolean")
print("---------------------------------")
a=True
print(type(a),id(a),a)

print("\nFunction")
print("---------------------------------")
def fun1():
    return "I am Function"
a=fun1
print(type(a),id(a),a())

print("\nObjects")
print("---------------------------------")
class Demo:
    def hi(self):
        return "Hi"
a=Demo()
print(type(a),id(a),a.hi())

print("\nCollections")
print("---------------------------------")
a=[1,2,3]
print(type(a),id(a),a)
a=[]
print(type(a),id(a),a)
a=(1,2,3)
print(type(a),id(a),a)
a=()
print(type(a),id(a),a)
a=1,2,3
print(type(a),id(a),a)
a={1,2,3}
print(type(a),id(a),a)
a={}
print(type(a),id(a),a)
a={"id":1,"name":"pooja"}
print(type(a),id(a),a)