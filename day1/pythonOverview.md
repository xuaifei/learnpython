# python overview  
[《Python简史》](http://www.cnblogs.com/vamei/archive/2013/02/06/2892628.html)
## history  
author:Guido von Rossum  
name from: Monty Python's Flying Circus   
start year:   
- 1989 start writing python interpreter;   
- 1991 first python interpreter born;
- 1994 python 1.0

something else find interesting things.

## python 语法  
### 类型
基本类型：int string float complex bool  
复合类型：class list tuple map
###  运算符  
### 运算符

Python支持多种运算符，下表大致按照优先级从高到低的顺序列出了所有的运算符，我们会陆续使用到它们。

| 运算符                                                       | 描述                           |
| ------------------------------------------------------------ | ------------------------------ |
| `[]` `[:]`                                                   | 下标，切片                     |
| `**`                                                         | 指数                           |
| `~` `+` `-`                                                  | 按位取反, 正负号               |
| `*` `/` `%` `//`                                             | 乘，除，模，整除               |
| `+` `-`                                                      | 加，减                         |
| `>>` `<<`                                                    | 右移，左移                     |
| `&`                                                          | 按位与                         |
| `^` `|`                                                      | 按位异或，按位或               |
| `<=` `<` `>` `>=`                                            | 小于等于，小于，大于，大于等于 |
| `==` `!=`                                                    | 等于，不等于                   |
| `is`  `is not`                                               | 身份运算符                     |
| `in` `not in`                                                | 成员运算符                     |
| `not` `or` `and`                                             | 逻辑运算符                     |
| `=` `+=` `-=` `*=` `/=` `%=` `//=` `**=` `&=` `|=` `^=` `>>=` `<<=` | （复合）赋值运算符             |

>**说明：**在实际开发中，如果搞不清楚优先级可以使用括号来确保运算的执行顺序。

