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
import os
import inspect
from pathlib import Path
from PySide6.QtWidgets import QWidget, QFileDialog
from file_renamer.rename import Rename
from file_renamer.lib.files import Files
from file_renamer.ui_form import Ui_Widget

logger = logging.getLogger(__name__)


class Widget(QWidget):
    def __init__(self, parent=None, **fr):
        super().__init__(parent)
        logger.info('class Widget')
        self.fr = fr
        # UI
        self.fr["ui"] = Ui_Widget()
        self.fr["ui"].setupUi(self)
        # Create rename
        self.rename = Rename(**self.fr)
        # Track lower or title case change
        self.fr["case_change"] = False

    def open_dir(self):
        dir_name = QFileDialog.getExistingDirectory(self, "Select a Directory")
        if dir_name:
            self.fr["path"] = Path(dir_name)
            self.fr["ui"].dir_txt.setText(str(self.fr["path"]))
            self.fr["ui"].label.setText('LIST FILES')
            self.fr["ui"].sort.setChecked(False)
            self.rename.list_files(**self.fr)

    def add_recursively(self):
        dir_name = ""
        self.fr["ui"].sort.setChecked(False)
        if self.fr["ui"].comboBox.currentIndex() > 0:
            self.fr["ui"].comboBox.setCurrentIndex(0)
            self.fr["ui"].comboBox.setCurrentText('PREVIEW')
        if self.fr["ui"].dir_txt.displayText():
            dir_name = self.fr["ui"].dir_txt.displayText()
            self.fr["path"] = dir_name
        if os.path.exists(self.fr["path"]):
            self.rename.list_files(**self.fr)
        else:
            self.fr["ui"].label.setText('LIST FILES')
            self.open_dir()

    def keep_id(self):
        if len(self.rename.files.filelist) <= 0:
            self.open_dir()
        elif len(self.rename.files.filelist) >= 1:
            self.fr["ui"].sort.setChecked(False)
            self.fr["ui"].comboBox.setCurrentIndex(0)
            self.fr["ui"].comboBox.setCurrentText('Select')
            self.rename.list_files(**self.fr)

    def keep_ext(self):
        if len(self.rename.files.filelist) <= 0:
            self.open_dir()
        elif len(self.rename.files.filelist) >= 1:
            self.fr["ui"].sort.setChecked(False)
            self.fr["ui"].comboBox.setCurrentIndex(0)
            self.fr["ui"].comboBox.setCurrentText('Select')
            self.rename.list_files(**self.fr)

    def sort(self):
        if len(self.rename.files.filelist) <= 0:
            self.open_dir()
        elif len(self.rename.files.filelist) <= 1:
            self.rename.list_files(**self.fr)
        elif self.fr["ui"].sort.isChecked():
            self.fr["ui"].comboBox.setCurrentIndex(0)
            self.fr["ui"].comboBox.setCurrentText('Select')
            self.rename.sort_files(**self.fr)

    def path(self):
        if len(self.rename.files.filelist) <= 0:
            self.open_dir()
        else:
            index = self.fr["ui"].comboBox.currentIndex()
            self.fr["ui"].sort.setChecked(False)
            if index == 0:
                self.rename.list_files(**self.fr)
            else:
                self.index_changed(index)

    def search_replace(self):
        self.fr["title"] = "Search & Replace"
        if len(self.fr["ui"].search.displayText()):
            self.rename.search_replace(**self.fr)

    def find(self):
        if self.fr["ui"].dir_txt.displayText():
            dir_name = self.fr["ui"].dir_txt.displayText()
        combo_text = self.fr["ui"].comboBox.currentText()
        if len(self.rename.files.filelist) <= 0:
            self.open_dir()
        else:
            if combo_text == "Select":
                if len(self.fr["ui"].search.displayText()) <= 0:
                    self.fr["ui"].search.setFocus()
                else:
                    self.fr["title"] = "Search & Replace"
                    self.rename.search_replace(**self.fr)
            else:
                self.fr["title"] = "Search & Replace"
                self.rename.search_replace(**self.fr)

    def regex(self):
        self.search_replace()

    def index_changed(self, index):
        self.fr["title"] = ""
        # Track lower or title case change
        if index == 7 or index == 8:
            self.case_change = True
        else:
            self.case_change = False
        if index >= 1 and len(self.rename.files.filelist) >= 1:
            self.fr["ui"].dir_output.clear()
            self.fr["title"] = self.fr["ui"].comboBox.currentText()
            if index == 1:
                self.rename.remove_chars(**self.fr)
            elif index == 2:
                self.rename.remove_accents(**self.fr)
            elif index == 3:
                self.rename.trim_spaces(**self.fr)
            elif index == 4:
                self.rename.replace_spaces(**self.fr)
            elif index == 5:
                self.rename.replace_dots(**self.fr)
            elif index == 6:
                self.rename.replace_hyphens(**self.fr)
            elif index == 7:
                self.rename.lower_case(**self.fr)
            elif index == 8:
                self.rename.title_case(**self.fr)
            elif index == 9:
                self.rename.remove_ids(**self.fr)
            elif index == 10:
                self.rename.number(**self.fr)
        elif index >= 1 and len(self.rename.files.filelist) == 0:
            self.open_dir()
            self.fr["title"] = self.fr["ui"].comboBox.currentText()
            if len(self.rename.files.filelist) >= 1:
                if index == 1:
                    self.rename.remove_chars(**self.fr)
                elif index == 2:
                    self.rename.remove_accents(**self.fr)
                elif index == 3:
                    self.rename.trim_spaces(**self.fr)
                elif index == 4:
                    self.rename.replace_spaces(**self.fr)
                elif index == 5:
                    self.rename.replace_dots(**self.fr)
                elif index == 6:
                    self.rename.replace_hyphens(**self.fr)
                elif index == 7:
                    self.rename.lower_case(**self.fr)
                elif index == 8:
                    self.rename.title_case(**self.fr)
                elif index == 9:
                    self.rename.remove_ids(**self.fr)
                elif index == 10:
                    self.rename.number(**self.fr)

    def clear(self):
        self.rename.files.filelist.clear()
        self.rename.files.changed.clear()
        self.fr["ui"].rename_btn.setEnabled(False)
        self.fr["ui"].label.setText("APP")
        self.fr["ui"].filter_txt.setText('*.*')
        self.fr["ui"].dir_txt.clear()
        self.fr["ui"].recursively.setChecked(False)
        self.fr["ui"].extension.setChecked(False)
        self.fr["ui"].id.setChecked(False)
        self.fr["ui"].path.setChecked(False)
        self.fr["ui"].regex.setChecked(False)
        self.fr["ui"].sort.setChecked(False)
        self.fr["ui"].comboBox.setCurrentIndex(0)
        self.fr["ui"].comboBox.setCurrentText('Select')
        if self.fr['theme'] == 'light':
            self.fr["ui"].label.setStyleSheet(
                "color: white; background-color: gray;"
            )
        elif self.fr['theme'] == 'dark':
            self.fr["ui"].label.setStyleSheet(
                "color: white; background-color: black;"
            )
        self.fr["ui"].dir_output.clear()
        self.fr["ui"].search.clear()
        self.fr["ui"].replace.clear()

    def rename_files(self):
        self.fr["title"] = ""
        index = self.fr["ui"].comboBox.currentIndex()
        if index == 0:
            self.fr["title"] = "Search & Replace"
        else:
            self.fr["title"] = self.fr["ui"].comboBox.currentText()
        self.rename.rename_files(**self.fr)
