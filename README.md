# quizXue
## XueXi 挑战答题辅助

采用adb模块获取手机UI布局的xml文件，通过lxml解析出题目内容和选项，利用搜索引擎统计词频，完成答案提交。

### 使用步骤
1.安装[ADB](https://adb.clockworkmod.com/),并配置环境变量
> 参考[https://github.com/Skyexu/TopSup](https://github.com/Skyexu/TopSup)

2.手机连接电脑，开启USB调试模式

3.python安装虚拟环境
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
4.手机进入挑战答题

5.运行脚本
```python
$(venv):python run.py
```

> 展望：将题目和答案存入数据库中，提高题库覆盖率从而提高正确率

