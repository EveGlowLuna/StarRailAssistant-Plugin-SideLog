
# StarRailAssistant-Plugin-SideLog - 边窗日志  


## 📌 项目简介  
SideLog 是一款专为 [StarRailAssistant（星穹铁道助手）](https://github.com/Shasnow/StarRailAssistant) 设计的**实时日志可视化插件**。它通过一个**透明、无干扰的侧栏窗口**，将程序运行日志以直观的方式展示在屏幕边缘，解决了传统日志查看需切换窗口、遮挡主界面的痛点，是调试、运行监控的高效工具。  


## ✨ 核心功能  
| 功能特性 | 细节说明 |  
|----------|----------|  
| **透明侧栏窗口** | 窗口背景透明、无边框，自动吸附于屏幕右侧（可自定义位置），默认置顶且不遮挡主程序，任务栏上方显示（适配不同系统任务栏位置） |  
| **鼠标穿透交互** | 窗口支持 `WA_TransparentForMouseEvents` 特性，鼠标可直接穿透操作底层界面（如点击游戏窗口或主程序按钮），无需手动隐藏 |  
| **多级别日志着色** | 自动识别 `INFO`/`WARNING`/`ERROR`/`SUCCESS` 日志级别，匹配不同颜色高亮（可自定义调色）：<br>- `INFO`: 浅绿（`#90EE90`）<br>- `WARNING`: 亮黄（`#FFD700`）<br>- `ERROR`: 橙红（`#FF4040`）<br>- `SUCCESS`: 墨绿（`#228B22`） |  
| **智能滚动控制** | 新增日志时自动滚动至底部（50ms延迟优化流畅度），手动滚动后暂停自动滚动（避免干扰查看历史日志） |  
| **无干扰界面设计** | 隐藏滚动条、禁用右键菜单、拒绝焦点获取，所有操作仅关注日志内容本身 |  


## 🚀 安装与配置  

### 前置要求  
- StarRailAssistant 主程序版本 ≥ `0.8.2`（依赖主程序日志接口）    


### 安装步骤  
1. **下载插件**：从 [Release 页面](https://github.com/EveGlowLuna/StarRailAssistant-Plugin-SideLog/releases) 下载最新版 `SideLog.zip`（或直接克隆仓库）。  
2. **放置插件**：将解压后的 `StarRailAssistant-Plugin-SideLog` 文件夹复制到 StarRailAssistant 的插件目录（默认路径：`主程序根目录/plugins/`）。  
3. **启动验证**：重启 StarRailAssistant，插件会自动加载（可通过主程序「插件管理」界面确认状态）。  


### 自定义配置（可选）  
若需调整窗口位置、颜色方案等，可修改 `__init__.py` 中的配置项：  
```python  
# 窗口初始位置（x, y），默认右侧居中（根据屏幕分辨率自动计算）  
WINDOW_POSITION = (screen_width - 300, screen_height // 2 - 200)  

# 日志级别颜色映射（支持HEX/RGB/颜色名称）  
LOG_LEVEL_COLOR = {  
    "INFO": "#90EE90",  
    "WARNING": "#FFD700",  
    "ERROR": "#FF4040",  
    "SUCCESS": "#228B22"  
}  
```  


## 📖 使用指南  

### 日志查看  
开始执行任务后，屏幕右侧会出现半透明日志窗口，可快速查看是否有错误发生。


### 常见操作  
- **调整位置**：修改 `WINDOW_POSITION` 配置项，重启插件生效（支持手动拖动窗口，位置会自动保存）。  


## 📦 项目结构  
```  
StarRailAssistant-Plugin-SideLog/  
├── plugin.toml       # 插件元数据（名称、版本、作者、依赖声明）  
├── __init__.py       # 核心逻辑（窗口创建、日志监听、UI更新）  
├── LICENSE           # MIT 许可证文件  
└── README.md         # 当前文档（使用说明与项目介绍）  
```  


## 🤝 贡献与反馈  
欢迎参与项目优化！  
- **问题反馈**：在 [Issues](https://github.com/EveGlowLuna/StarRailAssistant-Plugin-SideLog/issues) 中提交BUG或建议（请注明环境：系统版本、主程序版本、插件版本）。  
- **代码贡献**：通过PR提交功能扩展（如新增日志级别、支持窗口透明度调节等），提交前请同步更新文档。  


## 📜 许可证  
本项目采用 [MIT 许可证](LICENSE)，允许自由修改、分发和商业使用，但需保留原作者版权声明。  


**开发者**：EveGlowLuna  
**联系**：[邮箱](mailto:ychen4514@outlook.com)
