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
import inspect
import re
import PySide6.QtCore
from PySide6.QtCore import (Slot, QDir)
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import (
    QWidget, QMainWindow, QTextEdit, QToolBar
)
from PySide6.QtWebEngineWidgets import QWebEngineView
from file_renamer.widget import Widget
from file_renamer.lib.html import WebUI

logger = logging.getLogger(__name__)


class MainWindow(QMainWindow):

    def __init__(self, parent: QWidget = None, **fr):
        super().__init__(parent)
        self.fr = fr
        self.title = "File Renamer"
        self.qdir = QDir()
        self.dir_output = QTextEdit()

        tool_bar = QToolBar()
        self.addToolBar(tool_bar)
        self.menu()

        # Create widget
        self.widget = Widget(**self.fr)
        self.widget.show()
        self.setCentralWidget(self.widget)
        self.setWindowTitle(self.title)
        self.fr['page-id'] = 'app'

    def menu(self):
        app_icon = QIcon.fromTheme("application-x-executable")
        html_icon = QIcon.fromTheme("text-html")
        exit_icon = QIcon.fromTheme("application-exit")
        video_icon = QIcon.fromTheme("video-x-generic")

        app_menu = self.menuBar().addMenu("&App")
        app_action = QAction(
            app_icon, "&Load", self, triggered=self.show_widget
        )
        app_menu.addAction(app_action)
        version_action = QAction(
            html_icon, "&Version", self, triggered=self.show_version
        )
        app_menu.addAction(version_action)
        privacy_action = QAction(
            html_icon, "&Privacy", self, triggered=self.show_privacy
        )
        app_menu.addAction(privacy_action)
        malware_action = QAction(
            html_icon, "&Malware", self, triggered=self.show_malware
        )
        app_menu.addAction(malware_action)
        exit_action = QAction(
            exit_icon, "&Exit", self, shortcut="Ctrl+Q",
            triggered=self.close
        )
        app_menu.addAction(exit_action)

        theme_menu = self.menuBar().addMenu("&Theme")
        dark_theme_action = QAction(
            html_icon, 'Dark', self, triggered=self.set_dark_theme
        )
        theme_menu.addAction(dark_theme_action)

        light_theme_action = QAction(
            html_icon, 'Light', self, triggered=self.set_light_theme
        )
        theme_menu.addAction(light_theme_action)

        license_menu = self.menuBar().addMenu("&License")
        license_action = QAction(
            html_icon, "GPL", self, triggered=self.show_license
        )
        license_menu.addAction(license_action)

        about_menu = self.menuBar().addMenu("&About")
        python_action = QAction(
            html_icon, 'Python3', self, triggered=self.show_python
        )
        about_menu.addAction(python_action)
        pyside_action = QAction(
            html_icon, 'PySide6', self, triggered=self.show_pyside
        )
        about_menu.addAction(pyside_action)
        bootstrap_action = QAction(
            html_icon, 'Bootstrap', self, triggered=self.show_bootstrap
        )
        about_menu.addAction(bootstrap_action)
        xonsh_action = QAction(
            html_icon, 'XONSH', self, triggered=self.show_xonsh
        )
        about_menu.addAction(xonsh_action)

    def show_widget(self):
        if not self.dir_output:
            self.dir_output.hide()
        self.widget = Widget(**self.fr)
        self.widget.show()
        self.setCentralWidget(self.widget)
        self.setWindowTitle(self.title)
        self.fr['page-id'] = 'app'

    def render_html(self):
        qweb = QWebEngineView()
        webui = WebUI(**self.fr)
        html = webui.html_page.strip()
        qweb.setHtml(html)
        self.setCentralWidget(qweb)
        self.setWindowTitle(self.fr['html_title'])

    @Slot()
    def show_version(self):
        from file_renamer.__version__ import __version__
        title = "Version"
        body = """
        <div class="container">
            <h1>File Renamer """ + __version__ + """</h1>
            <p>
                File Renamer is a desktop app for Linux and Windows for batch
                renaming files. It's Free, Libre, Open Source Software (FLOSS).
            </p>
            <p><strong>GitHub</strong><br>
                https://github.com/flossapps/file-renamer
            </p>
            <p><strong>Python Package Index (PyPI)</strong><br>
                https://pypi.org/project/io.github.flossapps.file-renamer/
            </p>
        </div>"""
        self.fr['html_title'] = title
        self.fr['html_body'] = body
        self.fr['page-id'] = 'version'
        self.render_html()

    @Slot()
    def show_privacy(self):
        from file_renamer.__version__ import __version__
        title = "Privacy"
        body = """
        <div class="container">
            <h1>Privacy</h1>
            <div class="p-3 text-primary-emphasis bg-danger border \
            bs-danger-border-subtle rounded-3">
                <strong>NO DATA IS SENT OVER THE INTERNET</strong>
            </div>
            <p>The following data is collected for the app to work. The data\
stays on your desktop:<p>
            <ol>
                <li>Filenames including path</li>
                <li>Operating system</li>
            </ol>
            <p>File Renamer is 100% PRIVATE.</p>
            <p>Feel free to inspect the source code at:<br>
            https://github.com/flossapps/file-renamer</p>
        </div>
        </div>"""
        self.fr['html_title'] = title
        self.fr['html_body'] = body
        self.fr['page-id'] = 'privacy'
        self.render_html()

    @Slot()
    def show_malware(self):
        from file_renamer.__version__ import __version__
        title = "Malware"
        body = """
        <div class="container">
            <h1>Malware</h1>
            <div class="p-3 text-primary-emphasis bg-danger border \
            bs-danger-border-subtle rounded-3">
                <strong>NO MALWARE EVER</strong>
            </div>
            <p>Malware is software that is designed to damage computers.</p>
            <p>File Renamer is 100% <strong>FREE OF ANY TYPE OF\
            MALWARE</strong>.</p>
            <p>Some common types of malware are:</p>
            <ol>
                <li>Keyloggers</li>
                <li>Spyware</li>
                <li>Trojans</li>
                <li>Viruses</li>
                <li>Worms</li>
                <li>Ransomware</li>
              </ol>
            <p>Feel free to inspect the source code at:<br>
            https://github.com/flossapps/file-renamer</p>
        </div>
        </div>"""
        self.fr['html_title'] = title
        self.fr['html_body'] = body
        self.fr['page-id'] = 'malware'
        self.render_html()

    def set_theme(self):
        qss = ""
        if self.fr["platform"] == "Windows":
            if self.fr['theme'] == 'light':
                from file_renamer.themes.light.light_windows import (
                    LightWindows
                )
                style = LightWindows()
                qss = style.theme
            elif self.fr['theme'] == 'dark':
                from file_renamer.themes.dark.dark_windows import DarkWindows
                style = DarkWindows()
                qss = style.theme
        else:
            if self.fr['theme'] == 'light':
                from file_renamer.themes.light.light_linux import LightLinux
                style = LightLinux()
                qss = style.theme
            elif self.fr['theme'] == 'dark':
                from file_renamer.themes.dark.dark_linux import DarkLinux
                style = DarkLinux()
                qss = style.theme
        if qss:
            self.fr['app'].setStyleSheet(qss)
            if self.fr['page-id'] == 'version':
                self.show_version()
            elif self.fr['page-id'] == 'privacy':
                    self.show_privacy()
            elif self.fr['page-id'] == 'malware':
                self.show_malware()
            elif self.fr['page-id'] == 'license':
                self.show_license()
            elif self.fr['page-id'] == 'python':
                self.show_python()
            elif self.fr['page-id'] == 'pyside':
                self.show_pyside()
            elif self.fr['page-id'] == 'bootstrap':
                self.show_bootstrap()
            elif self.fr['page-id'] == 'xonsh':
                self.show_xonsh()
            else:
                logger.info('PAGE NOT FOUND')
        else:
            logger.info('theme NOT set: %s', self.fr['theme'])

    @Slot()
    def set_dark_theme(self):
        if self.fr['theme'] != 'dark':
            self.fr['theme'] = 'dark'
            self.set_theme()

    @Slot()
    def set_light_theme(self):
        if self.fr['theme'] != 'light':
            self.fr['theme'] = 'light'
            self.set_theme()

    @Slot()
    def show_license(self):
        title = "License"
        body = """
        <div class="container">
            <h1>Copyright (C) 2024  Carlos</h1>

            <p>This program is free software: you can redistribute it
            and/or modify it under the terms of the <strong>GNU General
            Public License</strong> as published by the Free Software
            Foundation, either version 3 of the License, or (at your option)
            any later version.</p>

            <p>This program is distributed in the hope that it will be
            useful, but WITHOUT ANY WARRANTY; without even the implied
            warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR
            PURPOSE.  See the GNU General Public License for more
            details.</p>

            <p>You should have received a copy of the GNU General Public
            License along with this program.  If not, see
            https://www.gnu.org/licenses/.</p>
        </div>"""
        self.fr['html_title'] = title
        self.fr['html_body'] = body
        self.fr['page-id'] = 'license'
        self.render_html()

    @Slot()
    def show_python(self):
        title = "Python"
        regex = r'(^\d{1,2}\.\d{1,2}\.\d{1,2})'
        result = re.search(regex, sys.version)
        if result.group() != "":
            version = result.group()
        else:
            version = '3.13'
        body = """
        <div class="container">
            <h1>Python """ + version + """</h1>
            <p>Python is an interpreted, interactive, object-oriented
 programming language.</p>
            <p><strong>Python</strong><br>
            https://www.python.org</p>
            <p><strong>Docs</strong><br>
            https://docs.python.org</p>
        </div>"""
        self.fr['html_title'] = title
        self.fr['html_body'] = body
        self.fr['page-id'] = 'python'
        self.render_html()

    @Slot()
    def show_pyside(self):
        title = "Qt for Python"
        body = """
        <div class="container">
            <h1>Qt for Python """ + PySide6.QtCore.__version__ + """</h1>
            <p>Qt for Python offers the official Python bindings for Qt,
            which enables you to use Python to write your Qt applications.
            The project has two main components:</p>
                <ol>
                    <li>PySide6, so that you can use Qt6 APIs in your
                        Python applications, and</li>

                    <li>Shiboken6, a binding generator tool, which can be
                        used to expose C++ projects to Python, and a Python
                        module with some utility functions.</li>
                </ol>
            <p>This project is available under the LGPLv3/GPLv3 and the Qt
            commercial license.</p>
            <p><strong>Qt for Python</strong><br>
            https://www.qt.io/qt-for-python</p>
            <p><strong>Docs</strong><br>
            https://doc.qt.io/qtforpython-6</p>
        </div>"""
        self.fr['html_title'] = title
        self.fr['html_body'] = body
        self.fr['page-id'] = 'pyside'
        self.render_html()

    @Slot()
    def show_bootstrap(self):
        title = "Bootstrap"
        version = "5.3.3"
        body = """
        <div class="container">
            <h1>Bootstrap """ + version + """</h1>
            <p>Bootstrap is a powerful, feature-packed frontend toolkit.</p>
            <p><strong>Bootstrap</strong><br>
            https://getbootstrap.com</p>
            <p><strong>Docs</strong><br>
            https://getbootstrap.com/docs/</p>
        </div>"""
        self.fr['html_title'] = title
        self.fr['html_body'] = body
        self.fr['page-id'] = 'bootstrap'
        self.render_html()

    @Slot()
    def show_xonsh(self):
        title = "XONSH"
        version = "0.19.1"
        body = """
        <div class="container">
            <h1>XONSH """ + version + """</h1>
            <p>XONSH is a Python-powered shell</p>
            <p><strong>XONSH</strong><br>
            https://xon.sh/</p>
            <p><strong>Docs</strong><br>
            https://xon.sh/contents.html</p>
        </div>"""
        self.fr['html_title'] = title
        self.fr['html_body'] = body
        self.fr['page-id'] = 'xonsh'
        self.render_html()
