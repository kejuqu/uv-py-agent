

## Start

```
git clone git@github.com:kejuqu/uv-py-agent.git

cd uv-py-agent

uv venv # 创建虚拟环境
uv sync # 同步下载依赖

# 配置环境变量， 需要指定对应的 key 或者 url 等环境变量
cp .env.example .env

uv run main.py
# 或者打开 xxx.ipynb 运行相关内容
```

