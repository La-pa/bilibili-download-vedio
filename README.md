# 哔哩哔哩视频下载脚本

## 项目简介

本脚本所使用Python代码，用于下载`bilibili`视频，并将视频转化为音频的形式。

## 项目启动

只需要将脚本中的 `url_list` ，改为自己想要批量下载的`bilibili`视频地址列表。脚本会在脚本所在的地址新建`视频`和`音频`的文件夹，用于存放相应的文件。

## 项目依赖

| 依赖模块      | 描述                                                         | 安装包                       |
| ------------- | ------------------------------------------------------------ | ---------------------------- |
| requests      | 用于进行HTTP请求的库，用于从网络上获取数据。                 | `pip install requests`       |
| BeautifulSoup | 用于解析HTML和XML文档的Python库，提供浏览、搜索和修改文档树的功能。 | `pip install beautifulsoup4` |
| tqdm          | 用于在命令行界面中显示进度条，提升用户体验。                 | `pip install tqdm`           |
| re            | Python的正则表达式模块，用于字符串匹配和搜索。               | 已内置，无需额外安装         |
| VideoFileClip | moviepy库中的一个类，用于处理视频文件，包括提取视频和音频，用于将视频转换为音频的部分。 | `pip install moviepy`        |
| os            | 提供系统操作                                                 | 已内置，无需额外安装         |

## 相关链接

[1]: https://www.bilibili.com/read/cv20609928/	"python爬取B站视频"