# kiro-rs 配置一键生成器

从 kiro-cli 的本地数据库 (`~/.local/share/kiro-cli/data.sqlite3`) 自动提取凭据，生成 kiro-rs 所需的 `config.json` 和 `credentials.json`。

## 使用方法

```bash
python3 gen_kiro_rs_config.py
```

生成的配置文件在 `~/kiro-rs-config/` 目录下。
可以搭配我这个版本使用[kiro-re-cli](https://github.com/fjh1997/kiro.rs/releases/download/climode/kiro-rs-linux-x64-climode.zip)
## 生成的文件

- `config.json` — 服务配置（监听 `0.0.0.0:8990`，自动生成随机 apiKey）
- `credentials.json` — 凭据配置（accessToken、refreshToken、profileArn 等）

## 前提条件

- 已安装并登录 kiro-cli
- Python 3（无需额外依赖）

## 注意

- 每次运行会重新生成 apiKey，如需固定请手动修改生成后的 config.json
- kiro-rs 支持自动用 refreshToken 刷新 accessToken

## 社区讨论贴
- https://linux.do/t/topic/1571986
