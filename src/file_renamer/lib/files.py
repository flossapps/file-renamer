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
import re
import inspect
import os.path
from pathlib import Path
from abc import ABC, abstractmethod
from PySide6.QtWidgets import QWidget, QLineEdit
from PySide6.QtCore import Slot
from file_renamer.lib.case import CaseSensitive
from random import randrange

logger = logging.getLogger(__name__)


class File(ABC):

    def __set_name__(self, owner, name):
        self.private_name = '_' + name

    def __get__(self, obj, objtype=None):
        return getattr(obj, self.private_name)

    def __set__(self, obj, value):
        self.validate(value)
        setattr(obj, self.private_name, value)

    @abstractmethod
    def validate(self, value):
        pass


class Files(File):

    def __init__(self, **fr):
        logger.info('class Files')
        self.fr = fr
        self.filelist = []  # List of files in directory
        self.changed = {}
        self.file = dict(
            path="", base="", dir="", name="", ext="", id="", new="",
            current=""
        )
        self.limit = 200  # max number in self.filelist
        self.separator = r"[- \.]"  # hyphen or space or dot

        # Regex id
        self.regexid = r'\[.+\]'

        # Check case sensitive file systems
        self.case_sensitive = CaseSensitive(**self.fr)
        self.case_sensitive_val = False

    def validate(self, value):
        pass

    def __iter__(self):
        self.filelist = []
        return self

    @Slot()
    def print_title(self, **fr):
        self.fr = fr
        self.fr["ui"].dir_output.clear()
        self.fr["ui"].label.setText(self.fr["title"])

    @Slot()
    def list(self, **fr):
        self.fr = fr
        self.filelist.clear()
        self.changed.clear()
        self.fr["ui"].dir_output.clear()
        count = 0
        text = ""
        msg = "PLEASE WAIT..."
        self.label_style(**self.fr)
        """
        if self.fr['theme'] == 'light':
            self.fr["ui"].label.setStyleSheet(
                "color: white; background-color: gray;"
            )
        elif self.fr['theme'] == 'dark':
            self.fr["ui"].label.setStyleSheet(
                "color: white; background-color: black;"
            )
        """
        self.fr["title"] = "LIST FILES"
        self.print_title(**fr)
        filter = self.fr["ui"].filter_txt.text()
        if filter == "":
            filter = "*.*"
        try:
            if self.fr["ui"].recursively.isChecked():
                for file in Path(fr["path"]).rglob(filter):
                    if os.path.isfile(file):
                        if count < self.limit:
                            self.filelist.append(file)
                            count += 1
                            self.print_files(file, count)
                        else:
                            raise Exception()
                    else:
                        pass
                        # logger.info('Directories not support for now')
            else:
                for file in Path(fr["path"]).glob(filter):
                    if os.path.isfile(file):
                        if count < self.limit:
                            self.filelist.append(file)
                            count += 1
                            self.print_files(file, count)
                        else:
                            raise Exception()
                    else:
                        pass
                        # logger.info('Directories not support for now')
            if count == 0:
                raise FileNotFoundError()
        except FileNotFoundError:
            kwargs = {
                "error": True,
                "msg": "NO FILES FOUND!"
            }
            self.clear(**kwargs)
        except Exception:
            text = 'Total Files: ' + str(len(self.filelist)) + ' (MAX REACHED)'
            self.fr["ui"].dir_output.append(text)
        else:
            text = 'Total Files: ' + str(len(self.filelist))
            self.fr["ui"].dir_output.append(text)
            self.case_sensitive_val = self.case_sensitive.check(fr["path"])
            logger.info(
                'self.case_sensitive_val: %s',
                self.case_sensitive_val
            )

    def print_files(self, file, count):
        text = "File " + str(count)
        self.fr["ui"].dir_output.append(text)
        if self.fr["ui"].path.isChecked():
            self.fr["ui"].dir_output.append(str(file))
        else:
            self.fr["ui"].dir_output.append(str(os.path.basename(file)))
        self.fr["ui"].dir_output.append("")

    @Slot()
    def sort(self, **fr):
        logger.info('Files sort')
        self.fr = fr
        if self.fr["ui"].sort.isChecked():
            self.fr["ui"].dir_output.clear()
            self.filelist.sort()
            count = 0
            for file in self.filelist:
                count += 1
                self.print_files(file, count)

    def split_name(self, **fr):
        self.fr = fr
        filename = ""
        try:
            if os.path.exists(fr["filename"]):
                self.file["path"] = self.fr["filename"]
                self.file["base"] = os.path.basename(fr["filename"])
                self.file["dir"] = os.path.dirname(fr["filename"])
                split_tup = os.path.splitext(self.file["base"])
                self.file["name"] = split_tup[0]
                self.file["ext"] = split_tup[1]
                filename = ""
                if self.fr["ui"].extension.isChecked():
                    filename = self.file['name']
                else:
                    filename = self.file['base']
                result = re.search(self.regexid, filename)
                if result:
                    self.file['id'] = result.group()
                else:
                    self.file['id'] = ""
            else:
                raise FileNotFoundError()
        except FileNotFoundError:
            kwargs = {
                "error": True,
                "msg": "FILE NOT FOUND!"
            }
            self.clear(**kwargs)
            return None
        else:
            return self.file

    @Slot()
    def compare(self, file, data, **fr):
        self.fr = fr
        file["current"] = ""
        new_file = ""
        text = ""
        file_exists = False
        file_conflict = False

        self.fr["error"] = False
        self.fr["start"] = False
        self.fr["list"] = False
        self.fr["preview"] = True
        self.fr["renamed"] = False
        self.label_style(**self.fr)
        """
        self.fr["ui"].label.setText('PREVIEW -> ' + self.fr["title"])
        self.fr["ui"].label.setStyleSheet(
            "color: white; background-color: #0080ff;"
        )
        """

        if self.fr["ui"].extension.isChecked():
            if file["name"] != file["new"] and file['new'] != "":
                file["current"] = file["name"] + file["ext"]
        else:
            if file["base"] != file["new"] and file['new'] != "":
                file["current"] = file["base"]
            else:
                file["current"] = file["base"]
        if file["current"] == file["new"]:
            # logger.info('No change')
            file_exists = True
            # logger.info('1) file_exists: %s', file_exists)
        elif file["current"] != file["new"]:
            # logger.info('Changed')
            # logger.info('file["current"]: %s', file["current"])
            # logger.info('file["new"]: %s', file["new"])
            for filename in self.filelist:
                file2 = os.path.basename(filename)
                # logger.info('file2: %s', file2)
                new_file = (Path(os.path.join(file["dir"]), file["new"]))
                # logger.info('new_file: %s', new_file)
                # logger.info('Path(filename): %s', Path(filename))
                if file["new"] == file2:
                    # if new_file == Path(filename):
                    file_exists = True
                    # logger.info('2) file_exists: %s', file_exists)
                    break
                else:
                    file_exists = False
                    # logger.info('3) file_exists: %s', file_exists)
                    # logger.info('self.changed: %s', self.changed)
                    for current_file in self.changed.keys():
                        # logger.info('current_file: %s', current_file)
                        if new_file == self.changed[current_file]:
                            file_conflict = True
                            """
                            logger.info(
                                'file_conflict: %s',
                                file_conflict
                            )
                            """
                            break
            if self.case_sensitive_val is False:
                if self.fr["case_change"]:
                    if file["current"].lower() == file["new"].lower():
                        file_exists = True
                        # logger.info('4) file_exists: %s', file_exists)
                    elif file["current"].lower() != file["new"].lower():
                        file_exists = False
                        # logger.info('5) file_exists: %s', file_exists)
                else:
                    pass
            else:
                pass

        if file_exists is False and file_conflict is False:
            data["count"] += 1
            self.changed[self.fr["filename"]] = new_file
            text = "Preview " + str(data["count"])
            self.fr["ui"].dir_output.append(text)
            if self.fr["ui"].path.isChecked():
                self.fr["ui"].dir_output.append(str(self.fr["filename"]))
                self.fr["ui"].dir_output.append(str(new_file))
            else:
                self.fr["ui"].dir_output.append(str(os.path.basename(self.fr["filename"])))
                self.fr["ui"].dir_output.append(str(os.path.basename(new_file)))
            self.fr["ui"].dir_output.append("")

    @Slot()
    def rename(self, **fr):
        self.fr = fr
        count = 0
        current_file = ""
        new_file = ""
        for current_file in self.changed.keys():
            new_file = self.changed[current_file]
            if self.case_sensitive_val:
                tmp_file = str(current_file) + '.tmp'
                os.replace(current_file, tmp_file)
                os.replace(tmp_file, new_file)
            else:
                os.replace(current_file, new_file)
            count += 1
            text = "Renamed " + str(count)
            self.fr["ui"].dir_output.append(text)
            if self.fr["ui"].path.isChecked():
                self.fr["ui"].dir_output.append(str(current_file))
                self.fr["ui"].dir_output.append(str(new_file))
            else:
                self.fr["ui"].dir_output.append(str(os.path.basename(current_file)))
                self.fr["ui"].dir_output.append(str(os.path.basename(new_file)))
            self.fr["ui"].dir_output.append("")
        text = 'Total Files: ' + str(count)
        self.fr["ui"].dir_output.append(text)

        self.fr["error"] = False
        self.fr["start"] = False
        self.fr["list"] = False
        self.fr["preview"] =  False
        self.fr["renamed"] = True
        self.label_style(**self.fr)
        """
        self.fr["ui"].label.setText('RENAMED -> ' + self.fr["title"])
        self.fr["ui"].label.setStyleSheet(
            "color: white; background-color: maroon;"
        )
        """

        self.fr["ui"].rename_btn.setEnabled(False)
        self.filelist.clear()
        self.changed.clear()

    @Slot()
    def preview(self, data, **fr):
        self.fr = fr
        if data["count"] == 0:
            self.fr["ui"].dir_output.append("No changes")
            self.fr["ui"].dir_output.append("")
            self.fr["ui"].rename_btn.setEnabled(False)
        elif data["count"] > 0:
            text = 'Total Files: ' + str(data["count"])
            self.fr["ui"].dir_output.append(text)
            self.fr["ui"].rename_btn.setEnabled(True)
        else:
            logger.info('data["count"] unknown')

    @Slot()
    def clear(self, **fr):
        self.filelist.clear()
        self.changed.clear()
        fr["ui"].dir_output.clear()
        fr["ui"].search.clear()
        fr["ui"].replace.clear()
        fr["ui"].rename_btn.setEnabled(False)
        fr["ui"].filter_txt.setText('*.*')
        fr["ui"].recursively.setChecked(False)
        fr["ui"].extension.setChecked(False)
        fr["ui"].id.setChecked(False)
        fr["ui"].path.setChecked(False)
        fr["ui"].regex.setChecked(False)
        fr["ui"].sort.setChecked(False)
        fr["ui"].comboBox.setCurrentIndex(0)
        fr["ui"].comboBox.setCurrentText('Select')
        # self.label_style(**fr)

    def label_style(self, **fr):
        logger.info('fr: %s', fr)
        # logger.info('self.fr: %s', self.fr)
        if fr["error"]:
            fr["ui"].label.setText(fr["msg-title"])
            fr["ui"].dir_output.setText(fr["msg-body"])
            fr["ui"].label.setStyleSheet(
                "color: white; background-color: maroon;"
            )
        elif fr["start"]:
            fr["ui"].label.setText("APP")
            if fr['platform'] == 'Windows':
                if fr['theme'] == 'light':
                    fr["ui"].label.setStyleSheet(
                        "color: white; background-color: gray;"
                    )
                else:
                    fr["ui"].label.setStyleSheet(
                        "color: black; background-color: #9e9e9e;"
                    )
            else:
                if fr['theme'] == 'light':
                    fr["ui"].label.setStyleSheet(
                        "color: white; background-color: gray;"
                    )
                else:
                    fr["ui"].label.setStyleSheet(
                        "color: black; background-color: #9e9e9e;"
                    )
        elif fr["list"]:
            fr["ui"].label.setText("LIST FILES")
            if fr['platform'] == 'Windows':
                if fr['theme'] == 'light':
                    fr["ui"].label.setStyleSheet(
                        "color: white; background-color: gray;"
                    )
                else:
                    fr["ui"].label.setStyleSheet(
                        "color: black; background-color: #9e9e9e;"
                    )
            else:
                if fr['theme'] == 'light':
                    fr["ui"].label.setStyleSheet(
                        "color: white; background-color: gray;"
                    )
                else:
                    fr["ui"].label.setStyleSheet(
                        "color: black; background-color: #9e9e9e;"
                    )
        elif fr["preview"]:
            fr["ui"].label.setText('PREVIEW -> ' + fr["title"])
            fr["ui"].label.setStyleSheet(
                "color: white; background-color: #0080ff;"
            )
        elif fr["renamed"]:
            fr["ui"].label.setText('RENAMED -> ' + fr["title"])
            fr["ui"].label.setStyleSheet(
                "color: white; background-color: maroon;"
            )
        else:
            fr["ui"].label.setText("UNKOWN")
            fr["ui"].dir_output.setText("UNKOWN")
            fr["ui"].label.setStyleSheet(
                "color: white; background-color: maroon;"
            )

    def writeable(self, path):
        random_num = str(randrange(1000, 1000000))
        file = Path(path + "/" +random_num + ".txt")
        try:
            with open(file, "w") as f:
                f.write("Testing...")
                os.remove(file)
                return True
        except PermissionError as err:
            return False
