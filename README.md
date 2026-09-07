# BookManager 图书管理系统测试项目
## 项目简介
本项目为一套完整的软件测试实战项目，针对简易图书管理Web后台开展**功能手工测试 + 接口自动化测试**。
系统功能：管理员登录、图书新增、图书查询、图书编辑、图书删除、图书分页列表。

## 测试内容
1. 编写测试计划、测试需求分析
2. 设计功能测试用例（等价类、边界值、场景法）
3. 执行手工测试，提交缺陷
4. Python + Requests + Pytest 接口自动化脚本开发
5. Allure生成可视化测试报告
6. 测试总结评估

## 环境信息
- 测试浏览器：Chrome 120+
- 接口测试工具：Postman
- 自动化环境：Python3.9 / pytest / requests / allure-pytest
- Mock接口地址：https://jsonplaceholder.typicode.com（公共免费mock接口，无需部署服务）

## 目录说明
docs：全套测试文档
test_case：Excel手工测试用例
api_test：自动化测试脚本
report：Allure测试报告
