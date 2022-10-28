import sys

from PyQt5.QtGui import QIcon, QContextMenuEvent, QCloseEvent
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp, QMenu, QTextEdit, QMessageBox


class LoginWidget(QMainWindow):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        edit = QTextEdit()
        self.setCentralWidget(edit)
        # 状态栏句柄
        status_bar = self.statusBar()
        status_bar.showMessage('启动成功')

        # 菜单栏句柄
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu('File')
        edit_menu = menu_bar.addMenu('Edit')

        # 功能控件一
        exit_action = QAction(QIcon("东吴人寿.png"), "退出", self)
        exit_action.setShortcut('Ctrl+Q')  # 快捷键
        exit_action.setStatusTip('Exit Application')  # 功能提示
        exit_action.triggered.connect(qApp.quit)  # 事件绑定

        # 功能控件二
        other_action = QAction("无状态", self)
        other_action.setCheckable(True)
        other_action.setChecked(True)
        other_action.setShortcut('Ctrl+Q')
        other_action.setStatusTip('Exit Application')

        # 功能控件绑定到菜单
        file_menu.addAction(exit_action)
        edit_menu.addAction(other_action)

        # 子菜单控件
        child_menu = QMenu("子菜单", self)
        child_menu.addAction(exit_action)

        # 子菜单绑定要父菜单
        file_menu.addMenu(child_menu)

        # 工具栏句柄
        tool_bar = self.addToolBar("Exit")
        tool_bar.addAction(exit_action)

        self.setGeometry(600, 300, 600, 600)  # 设置窗口坐标大小
        self.setWindowTitle('窗口标题')
        self.show()

    # X窗口事件
    def closeEvent(self, event: QCloseEvent) -> None:
        reply = QMessageBox.question(self, '消息', "确认关闭?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    # 右键事件
    def contextMenuEvent(self, event: QContextMenuEvent) -> None:
        q_menu = QMenu(self)
        new = q_menu.addAction("新建")
        open = q_menu.addAction("打开")
        close = q_menu.addAction("关闭")
        exec_ = q_menu.exec_(self.mapToGlobal(event.pos()))
        if exec_ == close:
            qApp.quit()


if __name__ == '__main__':
    # 启动程序
    q_application = QApplication(sys.argv)
    # 创建登录窗口
    login_widget = LoginWidget()
    # 销毁程序
    sys.exit(q_application.exec_())