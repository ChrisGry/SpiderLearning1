import re #导入正则表达式

# python 匹配
pattern1 = "cat"
pattern2 = "bird"
string = "dog runs to cat"

print(pattern1 in string)
print(pattern2 in string)

# 正则表达式 regular expression
pattern1 = "cat"
pattern2 = "bird"
string = "dog runs to cat"

print(re.search(pattern1,string))
print(re.search(pattern2,string))

#寻找run或者ran
ptn = r"r[au]n" #第一个r表示是一个正则表达式;[]中的符号任取其一即可；此处为run和ran都可以
print(re.search(ptn,"dog runs to cat"))

#[]的演示
print("show[]")
print(re.search(r"r[a-z]n","dog runs to cat"))
print(re.search(r"r[0-9]n","dog r2ns to cat"))
print(re.search(r"r[a-z0-9]n","dog runs to cat"))

#正则表达式的特殊匹配
print(re.search(r"r\dn","run r4n")) #\d表示数字
print(re.search(r"r\Dn","run r4n")) #\D表示非数字

print(re.search(r"r\sn","r n, r  n")) #\s表示任意一种空白符；\s只能匹配一个空白符，空白符是有数量区别的
print(re.search(r"r\Sn","r n, r.n")) #\S表示任意不是空白符的符号

print(re.search(r"r\wn","ran")) #\w表示[0-9A-Za-z]

print(re.search(r"\bruns\b","dog runs to cat")) #\b，紧贴着单词头尾的空白符
print(re.search(r"\B r[au]n \B","dog runs to cat; dog  ran  to cat")) #\B，不贴着单词头尾的空白符
#\b,\B所指的符号不会出现在结果中

#\\ 表示匹配\
print(re.search(r"runs\\","runs\ "))
#. 表示除了\n的任何东西
print(re.search(r"r.n","r*n"))

#^xxx表示xxx出现在句首
print(re.search(r"^dog","dog runs to cat"))

#xxx$表示xxx出现在句末
print(re.search(r"cat$","dog runs to cat"))

#(xxx)?表示可有可无
print(re.search(r"Mon(day)?","Monday"))
print(re.search(r"Mon(day)?","Mon"))

#匹配多行字符串,使用re.search函数的flags参数
str = """
dog runs to cat
I run to dog
"""

print(re.search(r"^I",str))
print(re.search(r"^I",str,flags=re.M))

# * 0或多次；+ 1或多次
print(re.search(r"ab*","a"))
print(re.search(r"ab*","abbbbb"))
print(re.search(r"ab+","a"))
print(re.search(r"ab+","abbbbb"))

#出现可选次数，{n,m}，出现n到m次
print(re.search(r"ab{2,6}","a"))
print(re.search(r"ab{2,6}","abb"))
print(re.search(r"ab{2,6}","abbbbbb"))
print(re.search(r"ab{2,6}","abbbb"))

#gruop组，配合括号使用
match = re.search(r"(\d+), Date: (.+)","ID: 123456, Date: Nov/12/2019")
print(match.group()) #打印所有括号里的内容
print(match.group(1)) #打印一个括号里匹配的内容
print(match.group(2)) #打印第二个括号里匹配的内容

#(?P<name>...)给括号加一个名字
match = re.search(r"(?P<id>\d+), Date: (?P<date>.+)","ID: 123456, Date: Nov/12/2019")
print(match.group('id')) #打印id括号里匹配的内容
print(match.group('date')) #打印date括号里匹配的内容

#寻找所有匹配
print(re.findall(r"r[a-z0-9]n","ran run r4n r0n"))

#分割，用正则表达式里的符号去分割字符串
print(re.split(r"[,;\.:]","a,b;c.d:e"))

#compile，把正则表达式编译为re对象
c_re = re.compile(r"r[a-z0-9]n")
print(c_re.findall("ran run r4n r0n"))
