<big>**自Cobra-W 2.0版本起，Cobra-W正式更名为Kunlun-M(昆仑镜)，**</big>

<big>**写在最前，Cobra-W就像手中的一把剑，这把剑好不好用是Cobra-W的事，如何使用是你的事，希望能有更多的人参与到Cobra-W的变化中来...**</big>

**请使用python3.6+运行该工具，已停止维护python2.7环境**

# Kunlun-Mirror
[![GitHub (pre-)release](https://img.shields.io/github/release/LoRexxar/Kunlun-M/all.svg)](https://github.com/LoRexxar/Cobra-W/releases)
[![license](https://img.shields.io/github/license/mashape/apistatus.svg?maxAge=2592000)](https://github.com/wufeifei/cobra/blob/master/LICENSE)
[![Build Status](https://travis-ci.org/LoRexxar/Kunlun-M.svg?branch=master)](https://travis-ci.org/LoRexxar/Cobra-W)
![](https://img.shields.io/badge/language-python3.6-orange.svg)

```
 _   __            _                      ___  ___
| | / /           | |                     |  \/  |
| |/ / _   _ _ __ | |    _   _ _ __ ______| .  . |
|    \| | | | '_ \| |   | | | | '_ \______| |\/| |
| |\  \ |_| | | | | |___| |_| | | | |     | |  | |
\_| \_/\__,_|_| |_\_____/\__,_|_| |_|     \_|  |_/  -v2.0 beta1

GitHub: https://github.com/LoRexxar/Kunlun-M

KunLun-M is a static code analysis system that automates the detecting vulnerabilities and security issue.

```

## Introduction
Cobra是一款**源代码安全审计**工具，支持检测多种开发语言源代码中的**大部分显著**的安全问题和漏洞。
[https://github.com/wufeifei/cobra](https://github.com/wufeifei/cobra)

Cobra-W是从Cobra2.0发展而来的分支，将工具重心从尽可能的发现威胁转变为提高发现漏洞的准确率以及精度。
[https://github.com/LoRexxar/Kunlun-M/tree/cobra-w](https://github.com/LoRexxar/Kunlun-M/tree/cobra-w)

Kunlun-Mirror是从Cobra-W2.0发展而来，在经历了痛苦的维护改进原工具之后，昆仑镜将工具的发展重心放在安全研究员的使用上，将会围绕工具化使用不断改进使用体验。

目前工具主要支持**php、javascript**的语义分析，以及**chrome ext, solidity**的基础扫描.

## 特点

与其他代码审计相比：
- 静态分析，环境依赖小。
- 语义分析，对漏洞有效性判断程度更深。
- 多种语言支持。
- 开源python实现，更易于二次开发。

与Cobra相比：
- 深度重写AST，大幅度减少漏洞误报率。
- 底层api重写，支持windows、linux等多平台。
- 多层语义解析、函数回溯，secret机制，新增多种机制应用于语义分析。
- 新增javascript语义分析，用于扫描包含js相关代码。

与Cobra-W相比(todo):
- 深度优化AST分析流程，使其更符合QL的概念，便于下一阶段的优化。
- 深度优化辅助审计的流程，使其更符合人类安全研究员审计辅助的习惯。
- 深度重构代码结构，使其更符合可拓展，可优化的开源理念。

## TODO
- <del>改写grep以及find，提供更好的底层支持</del>
- <del>去除不符合白帽子审计习惯的部分模式以及相关冗余代码</del>
- <del>重写rule规则方式</del>，改为更容易针对定制的方式（有待进一步优化）
- 重写AST
    - <del>递归回溯变量</del>
    - <del>递归回溯自定义函数</del>
    - <del>多级函数调用</del>
    - <del>自定义类调用</del>
    - 未知语法待解析
- <del>添加疑似漏洞分级，部分回溯存在问题但是不能回溯到可控变量的漏洞，通过疑似漏洞的方式展示。</del>
- <del>添加关于javascript的静态分析</del>
- 完成针对有关于javascript的多种特殊问题
    - 适配关于html中内联js的扫描
    - 添加区分前端js与nodejs功能，并为node_js添加专门的扫描
    - 未知语法待解析
- 完成关于java的静态分析
- 完善AST分析的路径记录以及分析流程，使其更符合QL的概念
- 添加Sqlite3作为灵活数据库用于记录以及管理扫描任务以及结果
- 重构tamper部分，使其更符合人类的配置文件思路
- 添加cli模式，使其更符合日常使用的工具逻辑
- 重构rule模式，使其更符合可扩展，可编辑的概念
- 重构Cobra-WA
    - 集成到Kunlun-M中的web管理平台
    - 提供平台化的漏洞管理方案
    - 添加图关系的审计分析流程

## 更新日志

[changelog.md](./docs/changelog.md)


## 安装

首先需要安装依赖
```
pip install -r requirements.txt
```

然后扫描测试样例查看结果
```
python kunlun.py -t ./tests/vulnerabilities/
```
## 开发文档

[dev.md](./docs/dev.md)

## Contributors

感谢如下贡献者对本工具发展过程中的贡献：
- Knownsec 404 Team [LoRexxar](https://github.com/LoRexxar)
- 北邮天枢 [Sissel](https://github.com/boke1208)