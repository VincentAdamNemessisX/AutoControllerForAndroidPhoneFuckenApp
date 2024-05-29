# 一款简易的命令行自动化上传图片至某院校劳动照片

# 开始使用

```bash
pip install -r requirements.txt
```

## 程序入口



```bash
AutoControllerForAndroidPhoneFuckenApp/AutoSubmitFromAPI.py
```

## 关键输入说明：

X-ID-TOKEN： 加密和身份认证的Token，通过抓包或其他特殊工具可以获取到。

劳动类型：上传劳动的类型选择（根据提示输入）。

劳动次数：上传劳动的次数。

## 图片路径及编号说明：

AutoControllerForAndroidPhoneFuckenApp/*

编号按照阿拉伯数字排列，当前版本只支持png格式图片。

## 日志说明：

程序在运行过程中会输出日志，如果运行正常，只会输出info类型的日志，warning类型日志则是程序运行过程中用户输入有问题，error类型日志说明程序在某些部分中断并跳过了，其他类型日志本程序不涉及到。