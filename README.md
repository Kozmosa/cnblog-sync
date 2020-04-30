# Cnblog Sync
### Author: Xuyang1638
## 1. Quick Start
Clone this repository to your computer use:
```shell
git clone https://github.com/Xuyang1638/cnblog-sync.git
```
Then you need some packages to support this repo, You could install them through pip like this:
```shell
pip install selenium
```

If you do things correctly, you'll be able to sync your cnblog articles locally through 
```shell
python sync.py
```

It will open a browser(Chrome is default selected, you could change it in code), then you enter your username and password to login to your admin dashboard.
Then press an enter in the program window, then it will start to download markdown file article to ./posts directory.

## 2. License
This project open sourced with MIT License, youc could do anything you want to this code such as copying, editing, using in business...

But if you write my name and the url of my blog into your about/license file, I'll be really glad  :-)
This is an example of license information:
```markdown
Repo cnblog-sync written by Xuyang1638, Blog: [Kozumi Blog](https://xuyang1638.github.io)
```

Thanks for reading.