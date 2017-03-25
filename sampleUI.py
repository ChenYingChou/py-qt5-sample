# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sample.ui'
#
# Created by: PyQt5 UI code generator 5.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(424, 418)
        font = QtGui.QFont()
        font.setPointSize(15)
        Dialog.setFont(font)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.editStkid = QtWidgets.QLineEdit(Dialog)
        self.editStkid.setMinimumSize(QtCore.QSize(250, 32))
        self.editStkid.setObjectName("editStkid")
        self.horizontalLayout.addWidget(self.editStkid)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.listStock = QtWidgets.QListWidget(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(19)
        sizePolicy.setHeightForWidth(self.listStock.sizePolicy().hasHeightForWidth())
        self.listStock.setSizePolicy(sizePolicy)
        self.listStock.setMinimumSize(QtCore.QSize(400, 192))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.listStock.setFont(font)
        self.listStock.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.listStock.setAlternatingRowColors(True)
        self.listStock.setObjectName("listStock")
        self.verticalLayout_3.addWidget(self.listStock)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(4, -1, -1, -1)
        self.horizontalLayout_3.setSpacing(4)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.dateStart = QtWidgets.QDateEdit(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateStart.sizePolicy().hasHeightForWidth())
        self.dateStart.setSizePolicy(sizePolicy)
        self.dateStart.setCalendarPopup(True)
        self.dateStart.setObjectName("dateStart")
        self.verticalLayout.addWidget(self.dateStart)
        self.dateEnd = QtWidgets.QDateEdit(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateEnd.sizePolicy().hasHeightForWidth())
        self.dateEnd.setSizePolicy(sizePolicy)
        self.dateEnd.setCalendarPopup(True)
        self.dateEnd.setObjectName("dateEnd")
        self.verticalLayout.addWidget(self.dateEnd)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.widget = QtWidgets.QWidget(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_4.setContentsMargins(4, 0, 4, 0)
        self.horizontalLayout_4.setSpacing(8)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btnRun = QtWidgets.QPushButton(self.widget)
        self.btnRun.setObjectName("btnRun")
        self.horizontalLayout_4.addWidget(self.btnRun)
        self.btnClose = QtWidgets.QPushButton(self.widget)
        self.btnClose.setObjectName("btnClose")
        self.horizontalLayout_4.addWidget(self.btnClose)
        self.horizontalLayout_3.addWidget(self.widget)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.txtLog = QtWidgets.QPlainTextEdit(Dialog)
        self.txtLog.setMinimumSize(QtCore.QSize(0, 82))
        self.txtLog.setMaximumSize(QtCore.QSize(16777215, 170))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(13)
        self.txtLog.setFont(font)
        self.txtLog.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.txtLog.setReadOnly(True)
        self.txtLog.setPlainText("")
        self.txtLog.setTabStopWidth(4)
        self.txtLog.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)
        self.txtLog.setObjectName("txtLog")
        self.verticalLayout_3.addWidget(self.txtLog)
        self.listStock.raise_()
        self.txtLog.raise_()
        self.dateStart.raise_()
        self.dateEnd.raise_()

        self.retranslateUi(Dialog)
        self.btnClose.clicked.connect(Dialog.close)
        self.btnRun.clicked.connect(Dialog.run_stock)
        self.listStock.currentRowChanged['int'].connect(Dialog.set_stock_id)
        self.listStock.doubleClicked['QModelIndex'].connect(Dialog.set_run_stock)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.editStkid, self.listStock)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Stock Close Price Chart"))
        self.label.setText(_translate("Dialog", "Symbol:"))
        self.listStock.setSortingEnabled(True)
        self.label_3.setText(_translate("Dialog", "Date Range:"))
        self.label_2.setText(_translate("Dialog", "Log:"))
        self.dateStart.setDisplayFormat(_translate("Dialog", "yyyy/MM/dd"))
        self.dateEnd.setDisplayFormat(_translate("Dialog", "yyyy/MM/dd"))
        self.btnRun.setText(_translate("Dialog", "Draw"))
        self.btnClose.setText(_translate("Dialog", "Close"))
