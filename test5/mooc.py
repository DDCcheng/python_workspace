firend_list = []
print("1. 添加操作")
print("2. 删除操作")
print("3. 修改操作")
print("4. 展示操作")
print("5. 退出操作")
while(1):
    x=eval(input("请输入您所选择的选项\n"))
    if x==1:
        new_name=input("请输入您要添加的名字\n")
        firend_list.append(new_name)
        print("添加完成")
        continue
    if x==2:
        del_name=input("请输入您要删除的名字\n")
        firend_list.remove(del_name)
        print("删除完成")
        continue
    if x==3:
        old_name=input("请输入您要备注的名字\n")
        firend_list.remove(old_name)
        new_name=input("请输入您修改完成的名字\n")
        firend_list.append(new_name)
        print("修改完成")
        continue
    if x==4:
        if firend_list==[]:
            print("好友列表为空")
        else:
            print("列表为")
            for item in firend_list:
                print(item)
        continue
    if x==5:
        print("退出成功")
        break