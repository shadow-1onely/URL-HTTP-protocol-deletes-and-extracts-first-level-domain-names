import urllib.parse
# 导入 URL 解析模块
print("请在文件中添加要操作的数据，一行一条")
print("-" * 20 + "\n1.输入文件路径\n2.处理单个URL" + "\n" + "-" * 20)
# 循环数字选择，保证用户输入错误时可以回到选择
while True:
    num = int(input("请输入数字选择："))
    if num > 2:
        print("别你妈乱选！")
        continue
    # 循环用户输入1和2时对应的功能
    while True:
        if num == 1:
            # 读取文件路径
            file_path = input("请输入文件路径：")
            try:
                # 打开文件，并将每行数据作为 URL 添加到列表中
                file = open(file_path, 'w+', encoding='utf-8')
                urls = []
                for get_url in file.readlines():
                    url = list(urllib.parse.urlparse(get_url))[1]
                    print(url)
                    urls.append(url)
                # 提示是否提取一级域名
                print("是否要提取一级域名：")
                print("-" * 20 + "\n1.是，继续" + "\n2.否，退出" + "\n" + "-" * 20)
                extract_domain = int(input("请输入选择："))
                if extract_domain == 1:
                    # 提取一级域名并添加到文件中
                    for domian in urls:
                        domain_list = domian.split(".")
                        levels1_domian = domain_list[-2] + "." + domain_list[-1]
                        print(levels1_domian)
                        file.write('\n' + levels1_domian)
                    # 提示重新打开文件查看结果
                    print("操作完成，请重新打开文件查看")
                    flag = True
                    break
                elif extract_domain == 2:
                    # 删除协议部分并添加到文件中
                    for del_protocol in urls:
                        print(del_protocol)
                        file.write('\n' + del_portal)
                    # 关闭文件，并提示重新打开文件查看结果
                    file.close()
                    print("操作完成，请重新打开文件查看")
                # 退出循环
                flag = True
                break
            except FileNotFoundError:
                print("文件路径错误，请重新输入")
                continue
            except PermissionError:
                print("请输入正确的文件路径")
                continue
        if num == 2:
            # 读取 URL
            url_line = input("请输入URL：")
            try:
                # 创建文件，并将输入的 URL 添加到文件中
                file_txt = open("url.txt", 'w+', encoding='utf-8')
                url_lines = list(urllib.parse.urlparse(url_line))[1]
                # 提示是否提取一级域名
                print("是否要提取一级域名：")
                print("-" * 20 + "\n1.是，继续" + "\n2.否，退出" + "\n" + "-" * 20)
                extract_domain = int(input("请输入选择："))
                if extract_domain == 1:
                    # 提取一级域名并添加到文件中
                    domain_list = url_lines.split(".")
                    levels1_domian = domain_list[-2] + "." + domain_list[-1]
                    print(levels1_domian)
                    file_txt.write('\n' + levels1_domian)
                    # 提示重新打开文件查看结果
                    print("操作完成，请重新打开文件查看")
                    flag = True
                    break
                elif extract_domain == 2:
                    # 删除协议部分并添加到文件中
                    file_txt.write('\n' + url_lines)
                    # 关闭文件，并提示重新打开文件查看结果
                    file_txt.close()
                    print("操作完成，请重新打开文件查看")
                # 退出循环
                flag = True
                break
            except FileNotFoundError:
                print("文件没找到，请创建！")
            except ValueError:
                print("不可为空，请选择！")
                continue
        # 操作完成，退出循环
        if flag:
            break