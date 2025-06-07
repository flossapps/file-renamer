"""
File Renamer
https://github.com/flossapps/file-renamer

A desktop app for Linux and Windows for batch renaming files.
It's Free, Libre, Open Source Software (FLOSS).

Copyright (C) 2024 Carlos
GNU General Public License
https://www.gnu.org/licenses/gpl-3.0.html
"""

import sys
import logging
import os
import platform
import inspect
from pathlib import Path
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QDir, QFile, QFileInfo, QIODevice, QTextStream
from file_renamer.gui import MainWindow
from file_renamer.__version__ import __version__
from file_renamer.settings import ROOT_DIR

logger = logging.getLogger(__name__)


def main(**fr):
    # Logs
    home = os.path.expanduser('~')
    logfile = Path(home + "/file-renamer.log")
    logging.basicConfig(
        format='%(asctime)s - %(levelname)s - %(message)s',
        filename=logfile,
        encoding='utf-8',
        filemode='w',
        level=logging.DEBUG
    )
    logger.info('File Renamer %s Logs', __version__)
    logger.info('ROOT_DIR: %s', ROOT_DIR)
    function = inspect.stack()[0].function
    logger.info(function)
    sys_platform = platform.system()
    logger.info('sys_platform: %s', sys_platform)

    # File Renamer dict
    fr = {
        "home": home,
        "logfile": logfile,
        "app": "",
        "platform": sys_platform,
        "case_sensitive": False,
        "write": False,
        "widget": None,
        "ui": None,
        "path": "",
        "base": "",
        "dir": "",
        "name": "",
        "ext": "",
        "id": "",
        "new": "",
        "current": "",
        "html_title": "",
        "html_body": "",
        "page-id": "app",
        "theme": 'light',
        "msg-type": "info",
        "msg-title": "MESSAGE",
        "msg-info": "Unknown"
    }

    # File Renamer app
    app = QApplication(sys.argv)
    fr['app'] = app

    # Default screen resolution
    width = 800
    height = 600

    window = MainWindow(**fr)
    window.resize(width, height)
    window.show()

    # Set theme
    if fr["platform"] == "Windows":
        if fr['theme'] == 'light':
            qss = ROOT_DIR + "/themes/windows_light.qss"
        elif fr['theme'] == 'dark':
            qss = ROOT_DIR + "/themes/windows_dark.qss"
    else:
        if fr['theme'] == 'light':
            qss = ROOT_DIR + "/themes/linux_light.qss"
        elif fr['theme'] == 'dark':
            qss = ROOT_DIR + "/themes/linux_dark.qss"
    with open(Path(qss), "r") as f:
        style = f.read()
        app.setStyleSheet(style)
    logger.info('theme set: %s', fr['theme'])
    app.exec()
