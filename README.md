# 消息集成服务

将不同 API / RSS 数据进行集成，并转化成统一的数据格式，进行不断更新。

> 好像和 RSSHub 做了一样的事情

## 特点

- 持续更新数据，可以设置更新数据的时间等
- 数据切片，一些数据可查询历史数据
- 可以和不同的 APP 结合，比 RSS 阅读更广泛使用

## 安装

```python
# 创建虚拟环境
python3 -m venv venv
source venv/bin/activate
# 安装依赖
python3 -m pip install -r requirements.txt
# 创建 instance 文件夹
mkdir instance
# 如果 click 版本不对报错了
python3 -m pip uninstall click
python3 -m pip install click==7.1.1
```

## 维护

请参考[ARCHITECTURE.md](./ARCHITECTURE.md)
