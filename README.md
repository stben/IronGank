## IGProjec环境的配置


### 使用前安装如下软件
1. 在下面的网站上安装 VirtualBox:
    - https://www.virtualbox.org/wiki/Downloads

2. 在下面的网站上安装 Vagrant
    - https://www.vagrantup.com/downloads.html

### 环境配置


#### 数据库配置

在mysql命令窗口中建立一个新的数据库，在mysql下执行：

```
create database iggood default character set utf8 collate utf8_unicode_ci;
```

在iggood/settings.py中修改：

TIME_ZONE 修改为 'Asia/Shanghai' 

STATIC_URL 后增加⼀⾏ STATIC_ROOT = os.path.join(BASE_DIR, 'static') 

修改 ALLOWED_HOSTS 为 ['*']

修改 LANGUAGE_CODE 为 'zh-hans'

```
DATABASES = {
'default': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'iggood',
    'USER': 'root',
    'PASSWORD': '123456'
    }
}
```

> 将PASSWORD改为自己数据库的密码


后面是配置前后端运行环境所依赖的包

在合适的文件夹位置控制台下运行下面命令：

```
git clone git@se.jisuanke.com:course-qa-platform/iron-gank/IGProject.git
cd IGProject
vagrant up
```


#### 后端配置

然后运行下面的命令：

```
cd server
pip install package.txt
```

运行前面所有命令均无异常后进行下面的测试：

#### 后端测试：

```
pip list
```

运行上面的命令后应该在命令行输出：

> Package             Version
> ------------------- ----------
> certifi             2018.11.29
> chardet             3.0.4
> colorama            0.4.1
> Django              2.1.4
> djangorestframework 3.9.0
> httpie              1.0.2
> idna                2.8
> jieba               0.39
> pbr                 5.1.1
> pip                 18.1
> Pygments            2.3.1
> pytz                2018.7
> requests            2.21.0
> setuptools          39.0.1
> six                 1.12.0
> stevedore           1.30.0
> urllib3             1.24.1
> virtualenv          16.1.0
> virtualenv-clone    0.4.0
> virtualenvwrapper   4.8.2

若出现此结果则表示后端依赖包安装完成。

#### 前端配置：

在frontend文件夹下运行如下命令：

``` bash
# 安装依赖
npm install

# 输入如下命令测试
npm run dev
```

