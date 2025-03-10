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
import re
import unidecode
import inspect
from pathlib import Path
from file_renamer.lib.files import Files

logger = logging.getLogger(__name__)


class Rename:

    def __init__(self, **fr):
        logger.info('class Rename')
        self.fr = fr
        self.files = Files(**self.fr)
        self.file = {}
        self.data = {
            "preview": True,
            "count": 0
        }
        self.chars = [' ', '.', '-', '_', '[', ']']  # Chars allowed

    def list_files(self, **fr):
        self.fr = fr
        self.files.list(**self.fr)

    def sort_files(self, **fr):
        self.fr = fr
        self.files.sort(**self.fr)

    def check_options(self, **fr):
        self.fr = fr
        filename = ""
        if self.fr["ui"].extension.isChecked():
            filename = self.file['name']
        else:
            filename = self.file['base']
        # Keep id
        if self.fr["ui"].id.isChecked():
            filename = filename.replace(self.file['id'], "")
        else:
            pass
        if self.fr["ui"].extension.isChecked() and \
                self.fr["ui"].id.isChecked():
            filename = self.file['name']
            filename = filename.replace(self.file['id'], "")
        else:
            pass
        return filename

    def update_options(self, **fr):
        self.fr = fr
        if self.file['new'] != "":
            if (fr["ui"].extension.isChecked() and
                    self.fr["ui"].id.isChecked()):
                self.file['new'] = self.file['new'] + self.file['id'] + \
                    self.file['ext']
            elif self.fr["ui"].extension.isChecked() and \
                    self.fr["ui"].id.isChecked() is False:
                self.file['new'] = self.file['new'] + self.file['ext']
            elif self.fr["ui"].extension.isChecked() is False and \
                    self.fr["ui"].id.isChecked():
                index = self.file['new'].find(self.file['ext'])
                self.file['new'] = self.file['new'][:index] + self.file['id'] \
                    + self.file['new'][index:]
            elif self.fr["ui"].extension.isChecked() is False and \
                    self.fr["ui"].id.isChecked() is False:
                pass
            else:
                pass
        else:
            pass

    def remove_chars(self, **fr):
        self.fr = fr
        self.data['count'] = 0
        self.files.print_title(**self.fr)
        filename = ""
        filename2 = ""
        try:
            for filename in self.files.filelist:
                self.fr["filename"] = Path(filename)
                self.file.clear()
                self.file = self.files.split_name(**self.fr)
                filename2 = self.check_options(**self.fr)
                self.file['new'] = ""
                for elem in filename2:
                    if elem.isalnum() or elem in self.chars:
                        self.file['new'] += elem
                self.update_options(**self.fr)
                self.files.compare(self.file, self.data, **self.fr)
        except Errors as err:
            kwargs = {
                "error": True,
                "msg": err
            }
            self.files.clear(**kwargs)
        else:
            self.files.preview(self.data, **self.fr)

    def remove_accents(self, **fr):
        self.fr = fr
        self.data['count'] = 0
        self.files.print_title(**self.fr)
        filename = ""
        filename2 = ""
        try:
            for filename in self.files.filelist:
                self.fr["filename"] = Path(filename)
                self.file.clear()
                self.file = self.files.split_name(**self.fr)
                filename2 = self.check_options(**self.fr)
                self.file['new'] = ""
                for i in range(len(filename2)):
                    # remove ascents
                    self.file['new'] += unidecode.unidecode(filename2[i])
                self.update_options(**self.fr)
                self.files.compare(self.file, self.data, **self.fr)
        except SystemError as err:
            kwargs = {
                "error": True,
                "msg": err
            }
            self.files.clear(**kwargs)
        else:
            self.files.preview(self.data, **self.fr)

    @staticmethod
    def remove_dots(string):
        pattern = re.compile(r'\.')
        return re.sub(pattern, '', string)

    @staticmethod
    def replace_dup_dots_w_spaces(string):
        pattern = re.compile(r'\.{2,}')
        return re.sub(pattern, ' ', string)

    @staticmethod
    def replace_dots_w_hyphens(string):
        pattern = re.compile(r'\.{1,}')
        return re.sub(pattern, '-', string)

    @staticmethod
    def replace_underscores_w_hyphens(string):
        pattern = re.compile(r'_')
        return re.sub(pattern, '-', string)

    @staticmethod
    def remove_dup_spaces(string):
        pattern = re.compile(r'\s{2,}')
        return re.sub(pattern, ' ', string)

    @staticmethod
    def replace_spaces_w_hyphens(string):
        pattern = re.compile(r'\s')
        return re.sub(pattern, '-', string)

    @staticmethod
    def remove_dup_hyphens(string):
        pattern = re.compile(r'-{2,}')
        return re.sub(pattern, '-', string)

    @staticmethod
    def replace_hyphens_w_spaces(string):
        pattern = re.compile(r'-{1,}')
        return re.sub(pattern, ' ', string)

    def trim_spaces(self, **fr):
        self.fr = fr
        self.data['count'] = 0
        self.files.print_title(**self.fr)
        filename = ""
        filename2 = ""
        try:
            for filename in self.files.filelist:
                self.fr["filename"] = Path(filename)
                self.file.clear()
                self.file = self.files.split_name(**self.fr)
                filename2 = self.check_options(**self.fr)
                self.file['new'] = filename2.strip()
                self.file['new'] = self.replace_dup_dots_w_spaces(
                    self.file['new'])
                self.file['new'] = self.remove_dup_spaces(self.file['new'])
                self.update_options(**self.fr)
                self.files.compare(self.file, self.data, **self.fr)
        except SystemError as err:
            kwargs = {
                "error": True,
                "msg": err
            }
            self.files.clear(**kwargs)
        else:
            self.files.preview(self.data, **self.fr)

    def replace_spaces(self, **fr):
        self.fr = fr
        self.data['count'] = 0
        self.files.print_title(**self.fr)
        filename = ""
        filename2 = ""
        try:
            for filename in self.files.filelist:
                self.fr["filename"] = Path(filename)
                self.file.clear()
                self.file = self.files.split_name(**self.fr)
                filename2 = self.check_options(**self.fr)
                self.file['new'] = self.replace_spaces_w_hyphens(
                    filename2)
                self.file['new'] = self.remove_dup_hyphens(
                    self.file['new'])
                self.update_options(**self.fr)
                self.files.compare(self.file, self.data, **self.fr)
        except SystemError as err:
            kwargs = {
                "error": True,
                "msg": err
            }
            self.files.clear(**kwargs)
        else:
            self.files.preview(self.data, **self.fr)

    def replace_dots(self, **fr):
        self.fr = fr
        self.data['count'] = 0
        self.files.print_title(**self.fr)
        filename = ""
        filename2 = ""
        try:
            for filename in self.files.filelist:
                self.fr["filename"] = Path(filename)
                self.file.clear()
                self.file = self.files.split_name(**self.fr)
                filename2 = self.check_options(**self.fr)
                self.file['new'] = self.replace_dots_w_hyphens(
                    filename2)
                self.update_options(**self.fr)
                self.files.compare(self.file, self.data, **self.fr)
        except SystemError as err:
            kwargs = {
                "error": True,
                "msg": err
            }
            self.files.clear(**kwargs)
        else:
            self.files.preview(self.data, **self.fr)

    def replace_hyphens(self, **fr):
        self.fr = fr
        self.data['count'] = 0
        self.files.print_title(**self.fr)
        filename = ""
        filename2 = ""
        try:
            for filename in self.files.filelist:
                self.fr["filename"] = Path(filename)
                self.file.clear()
                self.file = self.files.split_name(**self.fr)
                filename2 = self.check_options(**self.fr)
                self.file['new'] = self.replace_hyphens_w_spaces(
                    filename2)
                self.update_options(**self.fr)
                self.files.compare(self.file, self.data, **self.fr)
        except SystemError as err:
            kwargs = {
                "error": True,
                "msg": err
            }
            self.files.clear(**kwargs)
        else:
            self.files.preview(self.data, **self.fr)

    def lower_case(self, **fr):
        self.fr = fr
        self.data['count'] = 0
        self.files.print_title(**self.fr)
        filename = ""
        filename2 = ""
        try:
            for filename in self.files.filelist:
                self.fr["filename"] = Path(filename)
                self.file.clear()
                self.file = self.files.split_name(**self.fr)
                filename2 = self.check_options(**self.fr)
                self.file['new'] = filename2.lower()
                self.update_options(**self.fr)
                self.files.compare(self.file, self.data, **self.fr)
        except SystemError as err:
            kwargs = {
                "error": True,
                "msg": err
            }
            self.files.clear(**kwargs)
        else:
            self.files.preview(self.data, **self.fr)

    def title_case(self, **fr):
        self.fr = fr
        self.data['count'] = 0
        self.files.print_title(**self.fr)
        filename = ""
        filename2 = ""
        try:
            for filename in self.files.filelist:
                self.fr["filename"] = Path(filename)
                self.file.clear()
                self.file = self.files.split_name(**self.fr)
                filename2 = self.check_options(**self.fr)
                self.file['new'] = filename2.title()
                self.update_options(**self.fr)
                self.files.compare(self.file, self.data, **self.fr)
        except SystemError as err:
            kwargs = {
                "error": True,
                "msg": err
            }
            self.files.clear(**kwargs)
        else:
            self.files.preview(self.data, **self.fr)

    def remove_ids(self, **fr):
        self.fr = fr
        self.data['count'] = 0
        self.files.print_title(**self.fr)
        filename = ""
        filename2 = ""
        regex = ""
        try:
            for filename in self.files.filelist:
                self.fr["filename"] = Path(filename)
                self.file.clear()
                self.file = self.files.split_name(**self.fr)
                filename2 = self.check_options(**self.fr)
                if len(self.file['id']):
                    regex = (r'([- \.]' + re.escape(self.file['id']) + r')')
                    result = re.search(regex, filename2)
                    if result:
                        self.file['new'] = filename2.replace(
                            result.group(0), ""
                        )
                    else:
                        self.file['new'] = filename2
                else:
                    self.file['new'] = filename2
                self.update_options(**self.fr)
                self.files.compare(self.file, self.data, **self.fr)
        except SystemError as err:
            kwargs = {
                "error": True,
                "msg": err
            }
            self.files.clear(**kwargs)
        else:
            self.files.preview(self.data, **self.fr)

    def number(self, **fr):
        self.fr = fr
        self.data['count'] = 0
        self.files.print_title(**self.fr)
        filename = ""
        filename2 = ""
        regex = ""
        try:
            for filename in self.files.filelist:
                self.fr["filename"] = Path(filename)
                self.file.clear()
                self.file = self.files.split_name(**self.fr)
                filename2 = self.check_options(**self.fr)
                self.file['new'] = f"{self.data['count']:04d}"
                self.update_options(**self.fr)
                self.files.compare(self.file, self.data, **self.fr)
        except SystemError as err:
            self.files.clear()
            kwargs = {
                "error": True,
                "msg": err
            }
            self.files.clear(**kwargs)
        else:
            self.files.preview(self.data, **self.fr)

    def search_replace(self, **fr):
        self.fr = fr
        self.data['count'] = 0
        self.files.print_title(**self.fr)
        filename = ""
        filename2 = ""
        pattern = ''
        replace = ''
        try:
            for filename in self.files.filelist:
                self.fr["filename"] = Path(filename)
                self.file.clear()
                self.file = self.files.split_name(**self.fr)
                filename2 = self.check_options(**self.fr)
                if len(fr["ui"].search.displayText()):
                    pattern = self.fr["ui"].search.displayText()
                if self.fr["ui"].regex.isChecked():
                    p = re.compile(pattern)
                    result = p.search(filename2)
                    if result:
                        replace = self.fr["ui"].replace.displayText()
                        raw_replace = repr(replace)[1:-1]  # raw string
                        self.file['new'] = re.sub(pattern, replace, filename2)
                    else:
                        self.file['new'] = filename2
                else:
                    p = re.compile(re.escape(pattern))
                    result = p.search(filename2)
                    if result:
                        replace = self.fr["ui"].replace.displayText()
                        self.file['new'] = filename2.replace(
                            result.group(),
                            replace
                        )
                    else:
                        self.file['new'] = filename2
                self.update_options(**self.fr)
                self.files.compare(self.file, self.data, **self.fr)
        except SystemError as err:
            kwargs = {
                "error": True,
                "msg": err
            }
            self.files.clear(**kwargs)
        else:
            self.files.preview(self.data, **self.fr)

    def rename_files(self, **fr):
        self.fr = fr
        self.files.print_title(**self.fr)
        self.files.rename(**self.fr)
