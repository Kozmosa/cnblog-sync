# Cnblog Sync
### 作者: Xuyang1638
## 1. 快速开始
克隆仓库:
```shell
git clone https://github.com/Xuyang1638/cnblog-sync.git
```
安装依赖:
```shell
pip install selenium
```

如果你正确的做好了上述事情，你可以使用下面的命令启动程序：
```shell
python sync.py
```

他会打开一个浏览器窗口，只需要在里面如往常一样登录进管理后台即可。
然后在程序窗口里按下回车（就是运行sync.py的控制台窗口），程序就会下载Markdown源文件并自动转码为UTF-8编码。

## 2. 许可
这个项目根据MIT协议开源，你可以把它用在任何需要的地方（虽然代码写的很烂并且没有设计估计没有人会用）

但如果你能在你项目的授权文件（License）中保留我的名字和博客地址，我会非常高兴:-)

这是署名信息的一个范例（不一定非要遵守）:
```markdown
Repo cnblog-sync written by Xuyang1638, Blog: [Kozumi Blog](https://xuyang1638.github.io)
```

谢谢阅读.