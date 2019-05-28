# quizXue
## 学习·强国 挑战答题

> 正如每日、每周、专项答题一样，目的是为了巩固知识，该脚本实现挑战答题辅助功能，不为刷分，不想喝茶。

采用adb模块获取手机UI布局的xml文件，通过lxml解析出题目内容和选项，答案提交并判断正确后将本题保存到数据库。

先进入挑战答题页面，然后启动脚本，根据控制台输出和自己的判断在手机提交答案，然后在控制台输入正确答案并回车提交数据库保存。若手机提交答案错误，请在控制台提交正确的答案后再输入‘N’退出脚本。复活后可以重新启动脚本继续答题。

> OCR截图： 不需针对不同案例设计相应的XPATH规则，但是对截图区域的设置提出要求，得到的数据准确度较高

> XML解析：需要根据具体情况设置合适的XPATH规则，获得的数据准确度极高

> 大一学的C语言，自学的python，所以代码不够面向对象，勉强实现功能。

### 使用步骤
1. 安装[ADB](https://adb.clockworkmod.com/),并配置环境变量
> 参考[https://github.com/Skyexu/TopSup](https://github.com/Skyexu/TopSup)

2. 手机连接电脑，开启USB调试模式

3. python安装虚拟环境
```python
python -m venv venv
```
python安装模块
```
$(venv):pip install -r requirements.txt
```
或
```python
$(venv):pip install lxml
$(venv):pip install requests
```
4. 手机进入挑战答题

5. 运行脚本
```python
$(venv):python main.py
```

> 答题出错请在手机上复活或再来一局，然后在控制台上提交上次失败的题目的正确答案后继续，或提交正确答案后输入N退出

6. 直接执行model.py可将数据库导出到[题库](./data/data-dev.md)，可直接使用Ctrl+F搜索答案，欢迎一起增加题库

```python
$(venv):python model.py
```

> 展望： 每次手机提交需要在控制台输入答案或回车继续流程不够自动化，希望通过*adb shell getevent*获取手机输入事件，直接驱动脚本完成数据库的提交和转入下一流程。