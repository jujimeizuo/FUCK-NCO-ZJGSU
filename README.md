# FUCK NCO ZJGSU

浙江工商大学 云战疫（支持新旧两个版本） & 我的商大 自动报送

## 本代码使用 GPL 3.0 开源，请遵循 GPL 3.0 进行开发使用

## 6.1 更新说明

学校给我过了一个不快乐的六一，没错，又更新了，而且这次看起来非常棘手了，我也不知道什么时候可以实现一些简单的破解方案

如果你想要即使收到信息，可以点亮项目右上角的 Watch -> Custom -> Releases

## 5.27 更新说明

学校新增加了两个字段的校验，看起来就是想要卡一卡我们写脚本的，本项目本着学习交流使用的目的，尝试学习如何破解学校的加密工作，
终于在我上班摸鱼的两个小时内，凭借只能阅读被混淆后的 js 代码，完成了破解，然后下班回来先吃顿好的，再来上传代码

## 说明

**本项目仅供学习交流使用，请勿使用本项目代码进行自动报送，依照 GPLv3 开源协议，本项目的相关人员不承担任何责任，请自行承担责任**

老版本云战役采用的是纯 web 的方式直接硬破解的，所以比较特殊，我的商大的报送以及新版本的云战役我都采用了 oAuth2 去获取 token，所以比较统一，于是这个项目的一些代码就变得奇怪了起来

所有带有 app 开头的文件均为 oAuth2 模式的开发，请注意区别。老版本云战役虽然停止使用，但是为了保留历史记录，我将其保留，并将所有历史文件移动至 archive 文件夹下

当然因为这部分的破解 token 的获取方式，也就导致了本项目其实可以衍生出很多很多很有意思的项目，比如抢选课，但是我已经不需要选课了，所以留给后人开发吧

同时不再介绍其他使用方法，仅介绍服务器使用方案。因为太乱了 如果有希望能够维护其他解决方案的，推荐 fork 本项目，然后自行开发，并可以通过 issues 的方式通知我，我将优秀的解决方案放在本 README 上来帮助其他用户跳转

**但是，如果你希望使用本项目的代码继续进行开发，则请务必按照 GPLv3 开源协议进行合法使用，并请注明本项目的地址**

## 其他开发版本

 - [自动报送 Github/云函数版](https://github.com/yujianke100/AUTO-FUCK-NCO-ZJGSU)

## 通用第一步

请先在服务器上进行如下操作

将代码复制至目标文件夹下

```shell script
cd /root/
git clone https://github.com/Hukeqing/FUCK-NCO-ZJGSU.git
cd FUCK-NCO-ZJGSU
pip install -r requirements.txt
chmod +x app-start.sh
chmod +x app-yzy.sh
```
**请注意，脚本使用的是 python3，如果下载包时使用了 python2 则会出现意料之外的情况**

## 云战役新版本-使用方法

### 第一步

执行通用第一步

### 第二步

**修改 app-userExample.json 文件的内容，并将文件重命名为 app-user.json**

### 第三步
然后为服务器添加定时任务
```shell script
crontab -e
```

添加下面的内容
```shell script
5 0 * * * /root/FUCK-NCO-ZJGSU/app-yzy.sh
```
此行代码的表示会在0点05分时自动打卡，如果你需要调整自动打卡时间，请自行修改，例如如下代码为在早上 8 点 32 分自动打卡
```shell script
32 8 * * * /root/FUCK-NCO-ZJGSU/app-yzy.sh
```

然后保存即可

## 云战役（老版本）—使用方法

请将所有 archive 内的文件复制到项目的 root 目录下

### 第一步

请执行上方的通用第一步

然后给脚本赋予权限

```shell
chmod +x start.sh
```

### 第二步

**修改 userExample.json 文件，并将文件重命名为 user.json**

### 第三步
然后为服务器添加定时任务
```shell script
crontab -e
```

添加下面的内容
```shell script
5 0 * * * /root/FUCK-NCO-ZJGSU/start.sh
```
此行代码的表示会在凌晨0点5分时自动打卡，如果你需要调整自动打卡时间，请自行修改，例如如下代码为在早上 8 点 32 分自动打卡
```shell script
32 8 * * * /root/FUCK-NCO-ZJGSU/start.sh
```

然后保存即可

## 我的商大-使用方法

### 第一步

执行通用第一步

### 第二步

**修改 app-userExample.json 文件，并将文件重命名为 app-user.json**

### 第三步
然后为服务器添加定时任务
```shell script
crontab -e
```

添加下面的内容
```shell script
5 20 * * * /root/FUCK-NCO-ZJGSU/app-start.sh
```
此行代码的表示会在20点05分时自动打卡，如果你需要调整自动打卡时间，请自行修改，例如如下代码为在早上 8 点 32 分自动打卡
```shell script
32 8 * * * /root/FUCK-NCO-ZJGSU/app-start.sh
```

然后保存即可

