"""
File Renamer
https://github.com/flossapps/file-renamer

A desktop app for Linux and Windows for batch renaming files.
It's Free, Libre, Open Source Software (FLOSS).

Copyright (C) 2024 Carlos
GNU General Public License
https://www.gnu.org/licenses/gpl-3.0.html
"""

import logging
import inspect
from PySide6.QtWidgets import (
    QMainWindow, QMessageBox
)

logger = logging.getLogger(__name__)


class Messages(QMainWindow):

    def __init__(self, **fr):
        super().__init__()
        logger.info('class Messages')
        self.fr = fr
        if self.fr['msg-type'] == 'info':
            self.info()
        elif self.fr['msg-type'] == 'critical':
            self.critical()

    def info(self):
        button = QMessageBox.information(
            self,
            self.fr['msg-title'],
            self.fr['msg-info'],
        )

    def critical(self):
        button = QMessageBox.critical(
            self,
            self.fr['msg-title'],
            self.fr['msg-info'],
        )
