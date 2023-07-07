'''
join 使用指定字符将序列中的元素连接起来
'''
str = ['a','n','c','e','e']
#case1  这里使用空字符将str中所有字符连接成立一个字符串
new_str = "".join(str)
print(new_str)

# case2 使用“-”将str中所有字符连接起来
new_str = "-".join(str)
print(new_str)

# case2 使用“+#”将str中所有字符连接起来
new_str = "+#".join(str)
print(new_str)


'''
列表解析语法：[expression for iter_val in iterable if cond_expr]
           [expression] 最后执行的结果
           [for iter_val in iterable] 循环：可以有多个
           [if cond_expr] 条件判断
'''
# case1 基本的生成0-9的列表
num = [number for number in range(10)]
print(num)

# case2 带有条件的
num = [number for number in range(10) if number % 3 == 0]
print(num)

# case 3 如果条件比较复杂，可以写成函数
def is_odd(number):
     if number % 2 == 0:
         return 1
     else:
         return 0

num = [number for number in range(10) if is_odd(number)]
print(num)

'''
Iterate with  enumerta():
将一个可遍历的数据对象(列表、元组、字符串等)组合成一个索引序列
'''
# case 1
numbers = [31,23,55,65,31]
for i,number in enumerate(numbers):

    print(i,number)
'''
output:
0 31
1 23
2 55
3 65
4 31
从输出可以看出会把每个索引的下标打印出来
'''

'''
使用ZIP方法：可以关联两个list
'''

#case1
a = [1,3,4]
b = [4,5,6]
for a_ele,b_ele in zip(a,b):
    print(a_ele,b_ele)

'''
排序方法
'''
print(sorted([21,3,2,4]))


