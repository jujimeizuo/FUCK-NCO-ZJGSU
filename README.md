# FUCK NCO ZJGSU

浙江工商大学 云战疫 & 我的商大 自动报送

**如果希望使用，请认真阅读完整的使用说明。若希望更改路径，请自行修改说明中的所有路径**

## 云战役—使用方法

*点击即可展开或收起*

<details>
    <summary>直接拉取源码部署</summary>
<br>

优点是本地部署，便于管理，理论上不会被记录，稳定。缺点是需要一台服务器（？）

以下所有操作均在配置有git和python3的Linux系统下进行

### 第一步
请先在服务器上进行如下操作

将代码复制至目标文件夹下

```shell script
cd /root/
git clone https://github.com/Hukeqing/FUCK-NCO-ZJGSU.git
cd FUCK-NCO-ZJGSU
pip install -r requirements.txt
chmod +x start.sh
chmod +x app-start.sh
```
**请注意，脚本使用的是 python3，如果下载包时使用了 python2 则会出现意料之外的情况**

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

***

</details>

<details>
    <summary>通过腾讯云函数（SCF）部署</summary>
<br>

优点是不需要服务器，且报送时IP在境内。缺点是一定程度存在被记录的风险，以及对SCF新手不友好。

### 第一步

下载 [SCF 版本的压缩包](https://github.com/uselessbug/FUCK-NCoV-ZJGSU/releases/download/v0.01_scf/v0.01_scf.zip)

### 第二步

直接访问腾讯云函数控制台创建云函数： [https://console.cloud.tencent.com/scf/list-create](https://console.cloud.tencent.com/scf/list-create) ，按照下图所示的说明进行创建。

![scf01](https://i0.hdslb.com/bfs/album/a3759fa1bf6939fd3a6c524df90a51ef651334f0.png)
![scf02](https://i0.hdslb.com/bfs/album/2d484412bf8054a042dbd60fb4cbc1d498584ab2.png)
![scf03](https://i0.hdslb.com/bfs/album/782946ff930e170614f5e4c285815ab849370166.png)

配置完成后，点击下方“完成”进行保存，并检查运行情况

***

</details>

<details>
    <summary>使用GitHub Action进行部署</summary>
<br>


优点是不需要服务器，部署步骤最快。缺点是使用美国IP，较大可能存在被记录的风险。

### 第一步
Fork本仓库，而后在Settings-Secrets中添加以下secret
|变量名|含义|
| --- | --- |
|NAME |用户名（学号）|
|PASSWORD|密码|

### 第二步
到Action页面，启用workflow。然后随意修改`README.md`并提交一次commit，检查workflow运行情况

此项目默认会在每天十点左右上午执行，如需变更请修改`.github/workflows/main.yml`

如果一个项目超过60天不活跃，其workflow会被禁用。如需永动请参考https://github.com/zhzhzhy/Workflow-Keep-Alive
***

</details>

## 我的商大-使用方法

### 第一步（若已经执行过 云战役 的第一步，则可以跳过）
请先在服务器上进行如下操作

将代码复制至目标文件夹下

```shell script
cd /root/
git clone https://github.com/Hukeqing/FUCK-NCO-ZJGSU.git
cd FUCK-NCO-ZJGSU
pip install -r requirements.txt
chmod +x start.sh
chmod +x app-start.sh
```
**请注意，脚本使用的是 python3，如果下载包时使用了 python2 则会出现意料之外的情况**

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
5 20 * * * /root/FUCK-NCO-ZJGSU/app-start.sh
```

然后保存即可
# 本代码使用 GPL 3.0 开源，请遵循 GPL 3.0 进行开发使用
# 仅供学习交流使用，如有意外，自行承担责任
