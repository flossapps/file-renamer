"""
File Renamer is a desktop app for Linux and Windows for batch renaming files.
https://github.com/flossapps/file-renamer

Copyright (C) 2024 Carlos, GNU General Public License
https://www.gnu.org/licenses/gpl-3.0.html
"""

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTextEdit, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(800, 600)
        self.gridLayout = QGridLayout(Widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(Widget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.browse = QGroupBox(Widget)
        self.browse.setObjectName(u"browse")
        self.browse.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.horizontalLayout = QHBoxLayout(self.browse)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.filter_label = QLabel(self.browse)
        self.filter_label.setObjectName(u"filter_label")

        self.horizontalLayout.addWidget(self.filter_label)

        self.filter_txt = QLineEdit(self.browse)
        self.filter_txt.setObjectName(u"filter_txt")

        self.horizontalLayout.addWidget(self.filter_txt)

        self.dir_btn = QPushButton(self.browse)
        self.dir_btn.setObjectName(u"dir_btn")

        self.horizontalLayout.addWidget(self.dir_btn)

        self.dir_txt = QLineEdit(self.browse)
        self.dir_txt.setObjectName(u"dir_txt")
        self.dir_txt.setReadOnly(True)

        self.horizontalLayout.addWidget(self.dir_txt)


        self.gridLayout.addWidget(self.browse, 1, 0, 1, 1)

        self.dir_output = QTextEdit(Widget)
        self.dir_output.setObjectName(u"dir_output")
        self.dir_output.setReadOnly(True)

        self.gridLayout.addWidget(self.dir_output, 2, 0, 1, 1)

        self.options = QGroupBox(Widget)
        self.options.setObjectName(u"options")
        self.options.setMinimumSize(QSize(788, 0))
        self.options.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.horizontalLayout_2 = QHBoxLayout(self.options)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.recursively = QCheckBox(self.options)
        self.recursively.setObjectName(u"recursively")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.recursively.sizePolicy().hasHeightForWidth())
        self.recursively.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.recursively)

        self.extension = QCheckBox(self.options)
        self.extension.setObjectName(u"extension")

        self.horizontalLayout_2.addWidget(self.extension)

        self.path = QCheckBox(self.options)
        self.path.setObjectName(u"path")
        self.path.setMinimumSize(QSize(160, 0))

        self.horizontalLayout_2.addWidget(self.path)

        self.id = QCheckBox(self.options)
        self.id.setObjectName(u"id")
        self.id.setMinimumSize(QSize(160, 0))

        self.horizontalLayout_2.addWidget(self.id)

        self.sort = QCheckBox(self.options)
        self.sort.setObjectName(u"sort")
        self.sort.setEnabled(True)
        sizePolicy.setHeightForWidth(self.sort.sizePolicy().hasHeightForWidth())
        self.sort.setSizePolicy(sizePolicy)
        self.sort.setMinimumSize(QSize(160, 0))
        self.sort.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.horizontalLayout_2.addWidget(self.sort)


        self.gridLayout.addWidget(self.options, 3, 0, 1, 1)

        self.groupBox = QGroupBox(Widget)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_3 = QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.comboBox = QComboBox(self.groupBox)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout_3.addWidget(self.comboBox, 0, 0, 1, 1)

        self.clear_btn = QPushButton(self.groupBox)
        self.clear_btn.setObjectName(u"clear_btn")

        self.gridLayout_3.addWidget(self.clear_btn, 0, 1, 1, 1)

        self.rename_btn = QPushButton(self.groupBox)
        self.rename_btn.setObjectName(u"rename_btn")
        self.rename_btn.setEnabled(False)

        self.gridLayout_3.addWidget(self.rename_btn, 0, 2, 1, 1)


        self.gridLayout.addWidget(self.groupBox, 4, 0, 1, 1)

        self.search_replace = QGroupBox(Widget)
        self.search_replace.setObjectName(u"search_replace")
        self.gridLayout_5 = QGridLayout(self.search_replace)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.search_label = QLabel(self.search_replace)
        self.search_label.setObjectName(u"search_label")

        self.gridLayout_5.addWidget(self.search_label, 0, 0, 1, 1)

        self.search = QLineEdit(self.search_replace)
        self.search.setObjectName(u"search")
        self.search.setTabletTracking(False)
        self.search.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.search.setText(u"")
        self.search.setPlaceholderText(u"")

        self.gridLayout_5.addWidget(self.search, 0, 1, 1, 1)

        self.replace_label = QLabel(self.search_replace)
        self.replace_label.setObjectName(u"replace_label")

        self.gridLayout_5.addWidget(self.replace_label, 0, 2, 1, 1)

        self.replace = QLineEdit(self.search_replace)
        self.replace.setObjectName(u"replace")
        self.replace.setTabletTracking(False)
        self.replace.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

        self.gridLayout_5.addWidget(self.replace, 0, 3, 1, 1)

        self.regex = QCheckBox(self.search_replace)
        self.regex.setObjectName(u"regex")

        self.gridLayout_5.addWidget(self.regex, 0, 4, 1, 1)

        self.find_btn = QPushButton(self.search_replace)
        self.find_btn.setObjectName(u"find_btn")

        self.gridLayout_5.addWidget(self.find_btn, 0, 5, 1, 1)


        self.gridLayout.addWidget(self.search_replace, 5, 0, 1, 1)

        QWidget.setTabOrder(self.dir_btn, self.dir_txt)
        QWidget.setTabOrder(self.dir_txt, self.dir_output)
        QWidget.setTabOrder(self.dir_output, self.recursively)
        QWidget.setTabOrder(self.recursively, self.id)
        QWidget.setTabOrder(self.id, self.extension)
        QWidget.setTabOrder(self.extension, self.comboBox)
        QWidget.setTabOrder(self.comboBox, self.clear_btn)
        QWidget.setTabOrder(self.clear_btn, self.rename_btn)
        QWidget.setTabOrder(self.rename_btn, self.search)
        QWidget.setTabOrder(self.search, self.replace)
        QWidget.setTabOrder(self.replace, self.regex)
        QWidget.setTabOrder(self.regex, self.find_btn)

        self.retranslateUi(Widget)
        self.dir_btn.clicked.connect(Widget.open_dir)
        self.dir_btn.clicked.connect(self.dir_txt.update)
        self.clear_btn.clicked.connect(Widget.clear)
        self.comboBox.currentIndexChanged.connect(Widget.index_changed)
        self.rename_btn.clicked.connect(Widget.rename_files)
        self.recursively.clicked.connect(Widget.add_recursively)
        self.id.clicked.connect(Widget.keep_id)
        self.extension.clicked.connect(Widget.keep_ext)
        self.regex.clicked.connect(Widget.regex)
        self.find_btn.clicked.connect(Widget.find)
        self.sort.clicked.connect(Widget.sort)
        self.path.clicked.connect(Widget.path)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"File Renamer", None))
        self.label.setText(QCoreApplication.translate("Widget", u"APP", None))
        self.browse.setTitle("")
        self.filter_label.setText(QCoreApplication.translate("Widget", u"Filter", None))
        self.filter_txt.setText(QCoreApplication.translate("Widget", u"*.*", None))
        self.dir_btn.setText(QCoreApplication.translate("Widget", u"Browse", None))
        self.options.setTitle("")
        self.recursively.setText(QCoreApplication.translate("Widget", u"Recursively", None))
#if QT_CONFIG(tooltip)
        self.extension.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.extension.setText(QCoreApplication.translate("Widget", u"Keep Extension", None))
        self.path.setText(QCoreApplication.translate("Widget", u"Path", None))
        self.id.setText(QCoreApplication.translate("Widget", u"Keep ID", None))
        self.sort.setText(QCoreApplication.translate("Widget", u"Sort", None))
        self.groupBox.setTitle("")
        self.comboBox.setItemText(0, QCoreApplication.translate("Widget", u"Select", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Widget", u"Remove Non-Alphanum Chars", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Widget", u"Remove Accents", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Widget", u"Trim Spaces", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("Widget", u"Replace Spaces With Hyphens", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("Widget", u"Replace Dots With Hyphens", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("Widget", u"Replace Hyphens With Spaces", None))
        self.comboBox.setItemText(7, QCoreApplication.translate("Widget", u"Lower Case", None))
        self.comboBox.setItemText(8, QCoreApplication.translate("Widget", u"Title Case", None))
        self.comboBox.setItemText(9, QCoreApplication.translate("Widget", u"Remove ID", None))
        self.comboBox.setItemText(10, QCoreApplication.translate("Widget", u"Number", None))

        self.clear_btn.setText(QCoreApplication.translate("Widget", u"CLEAR", None))
        self.rename_btn.setText(QCoreApplication.translate("Widget", u"RENAME", None))
        self.search_replace.setTitle("")
        self.search_label.setText(QCoreApplication.translate("Widget", u"Search", None))
        self.replace_label.setText(QCoreApplication.translate("Widget", u"Replace", None))
        self.replace.setText("")
#if QT_CONFIG(tooltip)
        self.regex.setToolTip(QCoreApplication.translate("Widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Noto Sans'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Google Python Regex Examples</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.regex.setText(QCoreApplication.translate("Widget", u"Regular Expression", None))
        self.find_btn.setText(QCoreApplication.translate("Widget", u"Find", None))
    # retranslateUi

