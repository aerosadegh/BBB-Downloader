import sys
import os
from dotenv import dotenv_values
import time
from PyQt5 import QtCore, QtGui, QtWidgets, QtWinExtras
from PyQt5.QtCore import QThread, pyqtSignal

from setting_page import Ui_Dialog as Setting
from main_page import Ui_MainWindow

from utils import Download


def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller"""
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class ProcessDownload(QThread):
    """
    Runs a counter thread.
    """

    count_changed = pyqtSignal(tuple)

    def __init__(self, params: dict) -> None:
        super().__init__()
        self.params = params

    def run(self):

        download = Download(
            self.params["dwpath_led"].rstrip("/") + "/",
            self.params["sessionid"],
            self.params["dwpath_led"]
        )
        # num_parts = 0

        for itr in download.get_iter_videos():
            for (dnl, totallength) in itr:
                self.count_changed.emit((dnl, totallength,)) # f"{old_file} split to {num_parts} part", "", 30000)) dnl / totallength


        # for i, filepath in enumerate(files):
        #     if i == 0:
        #         self.count_changed.emit((count, i, "", filepath, 30000))
        #     else:
        #         self.count_changed.emit(
        #             (count, i, f"{old_file} split to {num_parts} part", filepath, 30000)
        #         )
        #     time.sleep(1)
        #     count = (i + 1) / n * 100
        #     print((i + 1), n, count)
        #     try:
        #         num_parts = convert.get_iter_videos()
        #         old_file = filepath.replace("/", "\\").split("\\")[-1]
        #     except AssertionError:
        #         num_parts = f"Error"
        # self.count_changed.emit((count, i, f"{old_file} split to {num_parts} part", "", 30000))
        # time.sleep(5)
        # self.count_changed.emit(
        #     (
        #         100,
        #         n,
        #         f"Process took ~{(time.time()-self.params['start_t0'])/60:.1f} (min)!",
        #         "",
        #         100000,
        #     )
        # )


class UiMainWindow2(Ui_MainWindow):
    def extra_setupUi(self, MainWindow, windows):
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap(resource_path("assets/icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off
        )
        MainWindow.setWindowIcon(icon)

        self.settings = dict()
        self.task_btn = QtWinExtras.QWinTaskbarButton(MainWindow)
        self.task_btn.setOverlayIcon(QtGui.QIcon("process.png"))
        self.actionSettings.triggered.connect(self.open_setting)

        self.sessionid_led.textChanged.connect(self.update_sessionid)
        self.browse_btn.clicked.connect(self.on_set_target)
        self.download_btn.clicked.connect(self.on_donwload_clicked)

        self.statuspbar = self.task_btn.progress()
        self.statuspbar.setMaximum(10000)
        self.statuspbar.setVisible(True)
        self.statuspbar.setValue(5000)

        self.target_led.setText(os.getcwd())

        self.settings = {
            "dwpath_led": "",
        }

        self.load_settings()

    def show_msg_box(
        self,
        title="MessageBox demo",
        msg_text="This is a message box",
        sub_msg="This is additional information",
        detail=None,
    ):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Warning)
        msg.setText(msg_text)
        msg.setInformativeText(sub_msg)
        msg.setWindowTitle(title)
        if detail is not None:
            msg.setDetailedText(detail)
        msg.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)

        retval = msg.exec_()
        return retval

    def save_settings(self, **kwargs):
        allowd_kw = {
            "dwpath_led": "DWPATH",
        }
        if set(kwargs.keys()) > set(allowd_kw.values()):
            raise ValueError

        filename = os.path.join(self.target_led.text(), ".bbbdwrc")
        settings = {}
        if os.path.exists(filename):
            settings.update(dotenv_values(filename))

        for k, v in kwargs.items():
            settings[allowd_kw[k]] = v

        with open(filename, "w") as fout:
            fout.write(f"### BBB Setting\n")
            for k, v in settings.items():
                fout.write(f"{k}={v}\n")

    def load_settings(self):
        filename = os.path.join(self.target_led.text(), ".bbbdwrc")
        if os.path.exists(filename):
            settings = dotenv_values(filename)
            print("LOADED!", settings)
        else:
            return
        allowd_kw = {
            "DWPATH": "dwpath_led",
        }
        if set(settings.keys()) > set(allowd_kw.keys()):
            raise ValueError
        for k, v in allowd_kw.items():
            self.settings[v] = settings[k]

    def open_setting(self):
        dialog = QtWidgets.QDialog()
        dialog.ui = Setting()
        dialog.ui.setupUi(dialog)

        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap(resource_path("assets/setting.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off
        )
        dialog.setWindowIcon(icon)
        if self.settings:
            for k, v in self.settings.items():
                getattr(dialog.ui, k).setText(v)
        res = dialog.exec_()
        dialog.show()
        if res:
            self.settings = dict(
                dwpath_led=dialog.ui.dwpath_led.text(),
            )
            print(self.settings)
        self.save_settings(dwpath_led=self.settings["dwpath_led"])

    def update_sessionid(self, changed):
        ...

    def on_set_target(self, click):
        self.trg_path = QtWidgets.QFileDialog.getExistingDirectory(
            MainWindow, "Choose Directory", self.target_led.text()
        )

        print(self.trg_path.replace("/", "\\"))
        # if self.src_path.replace("/", "\\") in self.trg_path.replace("/", "\\"):
        #     retval = self.show_msg_box(title="Same Path", msg_text="Source Path is same to Target Path", sub_msg="In the future, this will lead to a conflict between converted and unconverted files.\nDo you want to continue in this path?")
        #     if retval==QtWidgets.QMessageBox.Yes:
        #         pass
        #     elif retval==QtWidgets.QMessageBox.No:
        #         return
        self.target_led.setText(self.trg_path.replace("/", "\\"))
        self.load_settings()

    def on_donwload_clicked(self, clicked):
        print("Clicked!")
        print(self.settings,)


if __name__ == "__main__":
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    # QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    # QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps)
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    windows = QtGui.QWindow()
    ui = UiMainWindow2()
    ui.setupUi(MainWindow)
    ui.extra_setupUi(MainWindow, windows)
    # windows.show()
    MainWindow.show()
    sys.exit(app.exec_())
