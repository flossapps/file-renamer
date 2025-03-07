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

    def __init__(self):
        super().__init__()
        logger.info('class Messages')

    def info(self, **kwargs):
        button = QMessageBox.information(
            self,
            kwargs['title'],
            kwargs['body'],
        )

    def critical(self, **kwargs):
        button = QMessageBox.critical(
            self,
            kwargs['title'],
            kwargs['body'],
        )
