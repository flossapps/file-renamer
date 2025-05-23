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
from abc import ABC, abstractmethod
from random import randrange

logger = logging.getLogger(__name__)


class Case(ABC):

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


class CaseSensitive(Case):

    def __init__(self, **fr):
        logger.info('class CaseSensitive')
        self.fr = fr
        self.case_sensitive_val = False
        self.write = False  # File system write permission
        random_num = str(randrange(1000, 1000000))
        self.new_file_1 = "case-" + random_num + ".txt"
        self.new_file_2 = "CASE-" + random_num + ".TXT"

    def validate(self, value):
        pass

    def check(self, path):
        count = 0  # Num of files created
        self.new_file_1 = Path(os.path.join(path), self.new_file_1)
        self.new_file_2 = Path(os.path.join(path), self.new_file_2)
        if self.fr['write'] is False:
            try:
                with open(self.new_file_1, 'x') as f1:
                    pass
            except FileExistsError:
                logger.info(f"File '{self.new_file_1}' already exists")
            else:
                count += 1
                self.write = True
                self.fr["write"] = self.write
                logger.info('self.fr["write"]: %s', self.fr["write"])
                logger.info(f"File '{self.new_file_1}' created")
                try:
                    with open(self.new_file_2, 'x') as f2:
                        count += 1
                        logger.info(f"File '{self.new_file_2}' created")
                except FileExistsError:
                    logger.info(f"File '{self.new_file_2}' already exists")
                logger.info('count: %s', count)
                if count == 2:
                    self.case_sensitive_val = True
                    self.fr['case_sensitive'] = self.case_sensitive_val
                    logger.info(
                        'self.case_sensitive_val: %s', self.case_sensitive_val
                    )
                    os.remove(self.new_file_1)
                    os.remove(self.new_file_2)
                    logger.info(f"File '{self.new_file_1}' deleted")
                    logger.info(f"File '{self.new_file_2}' deleted")
                elif count == 1:
                    self.case_sensitive_val = False
                    logger.info(
                        'self.case_sensitive_val: %s', self.case_sensitive_val
                    )
                    os.remove(self.new_file_1)
                    logger.info(f"File '{self.new_file_1}' deleted")
        return self.case_sensitive_val
