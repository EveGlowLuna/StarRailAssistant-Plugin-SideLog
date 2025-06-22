import sys
from PySide6.QtCore import Qt, QPoint, QTimer
from PySide6.QtWidgets import QApplication, QTextEdit, QVBoxLayout, QWidget
from SRACore.utils.Plugins import *
from SRACore.utils.Logger import logger

class TransparentLogWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("透明日志")
        self.setGeometry(100, 100, 500, 300)
        self.setAttribute(Qt.WA_TranslucentBackground)  # 设置透明背景
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)  # 去掉窗口边框并设置置顶，同时隐藏任务栏程序窗口选择
        self.setAttribute(Qt.WA_TransparentForMouseEvents)  # 允许鼠标穿透透明窗口
        self.move(QApplication.primaryScreen().geometry().bottomLeft() - self.rect().bottomLeft() + QPoint(0, -300))  # 调整位置到任务栏上方100像素处
        # 设置样式去除边框
        self.setStyleSheet("background-color: transparent; border: none;")
        
        # 创建文本框并设置透明背景
        self.log_view = QTextEdit(self)
        self.log_view.setStyleSheet("background-color: transparent; color: white;")
        self.log_view.setReadOnly(True)
        self.log_view.setLineWrapMode(QTextEdit.WidgetWidth)  # 启用自动换行
        self.log_view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)  # 隐藏水平滚动条
        self.log_view.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)  # 隐藏垂直滚动条
        self.log_view.setFocusPolicy(Qt.NoFocus)  # 禁止获取焦点
        self.log_view.setContextMenuPolicy(Qt.NoContextMenu)  # 禁用右键菜单
        # 自动滚动到底部
        # 使用QTimer延迟执行滚动操作，避免过于频繁的更新导致程序不稳定
        self.scroll_timer = QTimer()
        self.scroll_timer.setSingleShot(True)
        self.scroll_timer.setInterval(50)  # 50毫秒的延迟
        self.scroll_timer.timeout.connect(self.scroll_to_bottom)
        self.log_view.textChanged.connect(lambda: self.scroll_timer.start())

        layout = QVBoxLayout(self)
        layout.addWidget(self.log_view)

    def scroll_to_bottom(self):
        self.log_view.verticalScrollBar().setValue(self.log_view.verticalScrollBar().maximum())

    def update_log(self, msg):
        """更新日志内容，支持不同级别的颜色"""
        color_map = {
            "INFO": "#90EE90",
            "WARNING": "yellow",
            "ERROR": "red",
            "SUCCESS": "green",
            # "DEBUG": "lightblue" 测试可用
        }
        record = msg.record
        level = record["level"].name
        if level.upper() not in ["INFO", "WARNING", "ERROR", "SUCCESS"]:
            return
        message = record["message"]
        time = record["time"].strftime("%m-%d %H:%M:%S")

        color = color_map.get(level.upper(), "white")
        # 构建带有阴影效果和颜色的HTML格式日志文本
        font_family = "Microsoft YaHei Mono, Consolas, monospace"
        html_text = (
            f'<div style="font-size:14px; font-weight:bold; font-family:\'{font_family}\'; '
            f'padding: 2px 6px;">'
            f'<span style="color:#D8BFD8">{time}</span> <span style="color:{color}">[{level}] </span> <span style="color:#7B68EE"> {message}</span>'
            f'</div>'
        )

        self.log_view.append(html_text)

    def closeEvent(self, event):
        """优雅地关闭应用程序"""
        print("窗口关闭，退出程序")
        event.accept()  # 允许关闭事件，关闭窗口

class MainEntrance(PluginBase):
    def __init__(self):
        super().__init__()
        self.window = None
    
    def show_window(self):
        self.window = TransparentLogWindow()
        self.window.show()
        logger.info("插件启动成功。")

if __name__ != "__main__":
    plugin = MainEntrance()
    PluginManager.register(plugin)
    plugin.show_window()
    logger.add(plugin.window.update_log)

def run():
    pass

if __name__ == "__main__":
    input("还没想好如何实现主窗口，但你可以键入'Enter'退出程序喵~")
