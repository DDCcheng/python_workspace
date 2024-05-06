
print("请输入您的每小时薪水")

salary_perhour = int(input())

print("请输入您的常规工作时间")

worktime_regularly = int(input())

print("请输入您的加班工作时间")

worktime_overtime = int(input())

if worktime_regularly <= 0 or worktime_regularly > 40 or salary_perhour < 15:
    print("您的常规工作时间已超时，或工作时薪<15rmb")
else:
    salary_all = salary_perhour*worktime_regularly+salary_perhour*1.5*worktime_overtime
    print(f'您的总工资为{salary_all}')
