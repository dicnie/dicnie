from time import ctime
import os
print('欢迎使用程序开发日志！')

answer = input('请问您想要查看记录还是写入记录呢？')

if answer == '写入':
    #记录标题
    title = input('程序:')
    print('程序：' + title)
    f = open('D:\桌面\程序开发日志content.txt', 'a')
    f.write('程序：' + title + '\n')

    #记录版本
    version = input('版本号：v')
    print('版本：' + version)
    f = open('D:\桌面\程序开发日志content.txt', 'a')
    f.write('版本：' + version + '\n')

    #记录内容
    content = input('更新内容：')
    print('更新内容：' + content)
    f = open('D:\桌面\程序开发日志content.txt', 'a')
    f.write('更新内容：' + content + '\n')

    #编辑器
    code_editor = input('编辑器：')
    print('编辑器：' + code_editor)
    f = open('D:\桌面\程序开发日志content.txt', 'a')
    f.write('编辑器：' + code_editor + '\n')

    #语言
    code_language = input('编程语言：')
    print('编程语言：' + code_language)
    f = open('D:\桌面\程序开发日志content.txt', 'a')
    f.write('编程语言：' + code_language + '\n')

    #时间
    f = open('D:\桌面\程序开发日志content.txt', 'a')
    times = ctime()
    f.write(times + '\n')

    #添加分割线
    f.write('=============================================' + '\n')

    #总览
    print('\n')
    print('程序：' + title)
    print('版本：' + version)
    print('更新内容：' + content)
    print('编辑器：' + code_editor)
    print('编程语言：' + code_language)
    print(times)
    f.close()

    input('按回车确定并退出')

elif answer == '查看':
    s = open('D:\桌面\程序开发日志content.txt', 'r')
    l = s.read()
    print(l)
    s.close()

    input('按回车确定并退出')