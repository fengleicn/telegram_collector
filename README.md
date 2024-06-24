# TGC
TGC 是一个全自动从电报群组收集图片视频转发到指定的群组的工具


### 功能
```txt
    支持两种方式收集:
       a. 从头收集群组老的图片和视频
       b. 实时轮询收集新的图片和视频
```

## 快速开始

### 步骤1 安装或自己编译
```shell
# 安装
> pip install telegram_collector
# 编译
> ...
```

### 步骤2 新建 tg.ini 文件 并填入自己的 app 信息 (app 可在电报官网申请)
```shell 
> vim tg.ini
#内容如下
[default]
; 你的 API ID
api_id=1234
; 你的 API HASH
api_hash=5678
; 是否使用代理
use_proxy=true
; 代理的IP地址 默认 127.0.0.1
; proxy_ip 
; 代理的端口 默认 7890
; proxy_port
; 来源群组ID 逗号分隔
src_dialog_ids=9012
; 保存群组ID 逗号分隔
dest_dialog_ids=3456
```

### 步骤3 执行tgc -p 获取已加入的群组信息
```shell 
> tgc -p
Please enter your phone (or bot token): 8613122223333 # 你的电话
Please enter the code you received: 12345             # APP 内收到的验证码
# 输出如下 群组ID 名称
1234 群组1
4567 群组2
```

### 步骤4 按上一步骤的群组信息 编辑 tg.ini 配置文件
```shell 
> vim tg.ini
...
; 来源群组ID 逗号分隔
src_dialog_ids=1234
; 保存群组ID 逗号分隔
dest_dialog_ids=4567
...
```

### 步骤5 开启收集
```shell
> tgc -a #实时收集最新消息
> tgc -b #从头收集历史消息
```

### Help 使用手册
```shell
> tgc
-a: collect new messages
-b: collect history messages
-c: create an example config
-p: print dialogs information
```
