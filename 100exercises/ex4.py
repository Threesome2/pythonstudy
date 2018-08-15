#ex4.py

# 思路：
# 之前所有月份的天数总和+这个月的具体天数

# 特殊情况：
# 1.闰年输入月份大于2要多一天
# 2.闰年是能被4或400整除但不能被100整除的年份

# 输入：
year = int(input('请输入年份：\n'))
month = int(input('请输入月份：\n'))
days = int(input('请输入天数：\n'))

# 之前所有月份的天数总和
months = (0,31,59,90,120,151,181,212,243,273,304,334)

if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
    if month>2:
        days_add = months[month-1] + 1 + days
    else:
        days_add = months[month] + days
else:
    days_add = months[month] + days


print(days_add)

