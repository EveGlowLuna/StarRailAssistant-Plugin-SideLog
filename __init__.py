# MIT License
# Copyright (c) 2025 EveGlow

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
        self.setAttribute(Qt.WA_TranslucentBackground)  # 设置窗口背景透明
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)  # 无边框窗口，保持最前显示，隐藏任务栏图标
        self.setAttribute(Qt.WA_TransparentForMouseEvents)  # 设置鼠标事件穿透
        self.move(QApplication.primaryScreen().geometry().bottomLeft() - self.rect().bottomLeft() + QPoint(0, -300))  # 定位窗口到屏幕底部任务栏上方
        # 设置窗口无边框样式
        self.setStyleSheet("background-color: transparent; border: none;")
        
        # 初始化日志显示文本框
        self.log_view = QTextEdit(self)
        self.log_view.setStyleSheet("background-color: transparent; color: white;")  # 透明背景，白色文字
        self.log_view.setReadOnly(True)  # 只读模式
        self.log_view.setLineWrapMode(QTextEdit.WidgetWidth)  # 按窗口宽度自动换行
        self.log_view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)  # 禁用水平滚动条
        self.log_view.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)  # 禁用垂直滚动条
        self.log_view.setFocusPolicy(Qt.NoFocus)  # 禁止文本框获取焦点
        self.log_view.setContextMenuPolicy(Qt.NoContextMenu)  # 禁用右键菜单
        
        # 初始化自动滚动定时器
        self.scroll_timer = QTimer()
        self.scroll_timer.setSingleShot(True)  # 单次触发模式
        self.scroll_timer.setInterval(50)  # 50毫秒延迟
        self.scroll_timer.timeout.connect(self.scroll_to_bottom)  # 连接滚动槽函数
        self.log_view.textChanged.connect(lambda: self.scroll_timer.start())  # 文本变化时触发定时器

        layout = QVBoxLayout(self)
        layout.addWidget(self.log_view)

    def scroll_to_bottom(self):
        """自动滚动到文本框底部"""
        self.log_view.verticalScrollBar().setValue(self.log_view.verticalScrollBar().maximum())

    def update_log(self, msg):
        """
        更新日志显示内容
        
        参数:
            msg: 日志消息对象，包含level和message等信息
        """
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
        """
        窗口关闭事件处理
        
        参数:
            event: 关闭事件对象
        """
        print("窗口关闭，退出程序")
        event.accept()  # 接受关闭事件

class MainEntrance(PluginBase):
    """插件主入口类"""
    
    def __init__(self):
        """初始化插件"""
        super().__init__()
        self.window = None  # 日志窗口实例
    
    def show_window(self):
        """显示日志窗口"""
        self.window = TransparentLogWindow()
        self.window.show()
        logger.info("插件启动成功。")  # 记录启动日志

if __name__ != "__main__":
    """作为插件运行时注册插件"""
    plugin = MainEntrance()
    PluginManager.register(plugin)  # 注册插件
    plugin.show_window()  # 显示窗口
    logger.add(plugin.window.update_log)  # 添加日志输出处理

def run():
    """空运行函数，保留接口"""
    pass

if __name__ == "__main__":
    """直接运行时的提示信息"""
    input("还没想好如何实现主窗口，但你可以键入'Enter'退出程序喵~")
