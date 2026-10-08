# 第7题：网吧上网资格判断
# 条件：
# 1. 年龄 >= 18
# 2. 有身份证
# 不使用 if

age = int(input("请输入年龄："))
has_id = input("是否有身份证(True/False)：")

result = age >= 18 and has_id == "True"

print("是否可以上网：", result)