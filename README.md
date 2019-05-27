# quizXue
## 学习·强国 挑战答题辅助

采用adb模块获取手机UI布局的xml文件，通过lxml解析出题目内容和选项，利用搜索引擎统计词频，完成答案提交。
先进入挑战答题页面，然后启动脚本，根据console输入和自己的判断在手机提交答案，然后在console输入正确答案并回车提交数据库保存。若手机提交答案错误，请在console提交正确的答案后再输入‘N’退出脚本。复活后可以重新启动脚本继续刷题。

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

6. 直接执行model.py可将题库导出到[题库](data-prod.md)

```python
$(venv):python model.py
```

