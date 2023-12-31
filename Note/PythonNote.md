# Python笔记

## 常用语法小记

- `*args` & `**kwargs`

  可选的参数输入：其中`*args`为元组类型，`**kwargs`为字典类型。

  在方法定义中用`kwargs.item[]`读取输入的参数，并根据键值执行相应的功能

- `class` & `def`

  `class`：定义类，其下可以包含多个方法，第一个方法一般为`__init__`；其下所有方法第一个参数必须为`self`，方便在将类实例化后的自我调用，且`self`不接收参数；

  `def`：定义方法，一定存在`return`

- 在方法实参中加入条件判定

```python
mpl_fonts = set(f.name for f in FontManager().ttflist)
```

## Python库的学习

### Numpy

内容



### Manim

#### 内容

#### 运行方法

```shell
# 终端输入
manim/manimgl foldername.py classname

```



### Matplotlib

- 画图中存在中文乱码的问题

```python
# 1.使用plt.rcParams
# 指定默认字体：解决plot不能显示中文问题
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
# 解决保存图像是负号'-'显示为方块的问题
plt.rcParams['axes.unicode_minus'] = False

# 2.使用matplotlib.rc
# 查询当前系统所有字体
from matplotlib.font_manager import FontManager
import subprocess

mpl_fonts = set(f.name for f in FontManager().ttflist)

print('all font list get from matplotlib.font_manager:')
for f in sorted(mpl_fonts):
    print('\t' + f)
# 修改字体
import matplotlib
matplotlib.rc("font",family='YouYuan')

```

### Git基础语法

- 初始化

```
git init
```

- 生成密钥

```shell
# 使用rsa算法生成密钥
ssh-keygen -t rsa –C "youremail@example.com"
# 命令行执行后会在.ssh中生成两个文件id_rsa（私钥）和id_rsa.pub（公钥）
```

- 关联远程仓库

```
# 在github新建SSH Key，并粘贴id_rsa.pub的内容
# 添加远程仓库
git remote add origin "http://....git"
```

- 克隆仓库到本地

```
git clone "url"
```

- 查询状态

```
git status
```

- 本地文件上传过程

```
# Git将文件分为四个部分，工作区、暂存区、仓库区和远程仓库
# 将指定文件或者所有文件从工作区添加至暂存区
git add filename/.
# 将文件提交至仓库区
git commit filename/. -m "commit log"
# 将文件推送至远程仓库
git push origin main
# 应当注意，若远程仓库修改，本地版本落后于远程，无法推送，可以先获取修改，再推送
git pull origin main
```

