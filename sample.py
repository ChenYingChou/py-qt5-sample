# -*- coding: utf-8 -*-
import sys
import os.path
import time
import datetime as dt
import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt

from matplotlib import style
style.use('ggplot')

# from PyQt5 import QtWidgets
from sampleUI import Ui_Dialog, QtWidgets

# Company source
# URL = 'https://raw.githubusercontent.com/datasets/s-and-p-500-companies/master/data/constituents-financials.csv'
# FIELDS = ['Symbol', 'Name', 'Earnings/Share']
URL = 'https://raw.githubusercontent.com/datasets/s-and-p-500-companies/master/data/constituents.csv'
FIELDS = ['Symbol', 'Name']
STOCK_LIST = 'stock.csv'    # Get the URL for the first time and save it to the local STOCK_LIST
STOCK_SOURCE = 'yahoo'      # pandas_datareader from 'google' or 'yahoo'

class My_Dialog(QtWidgets.QDialog):
    def __init__(self, ui: Ui_Dialog):
        super().__init__()
        self.ui = ui
        self.lastText = ''

    def log(self, msg: str):
        txtLog = self.ui.txtLog
        txtLog.appendPlainText('{} {}'.format(time.strftime('%m-%d %H:%M:%S'), msg))

    def load_stock_list(self, url: str, fields: list):
        try:
            # load stock.csv from url or local file STOCK_LIST
            if not os.path.exists(STOCK_LIST):
                self.log('{}> Loading from {} ...'.format(STOCK_LIST, url))
                df = pd.read_csv(url, usecols=fields)
                df.to_csv(STOCK_LIST)
            else:
                self.log(STOCK_LIST+'> Loading from local ...')
                df = pd.read_csv(STOCK_LIST, usecols=fields)

            self.log('Done.')
        except Exception as E:
            self.log('Exception> '+str(E))

        #  convert stock.csv to string('id name') of list
        slist = ['\t'.join(str(col) for col in row) for row in df.values]

        # fill stock id/name into ui.listStock
        self.ui.listStock.addItems(slist)

        # default get last 3 years data
        today = dt.date.today()
        start = dt.date(today.year-3, today.month, today.day)
        self.ui.dateStart.setDate(start)
        self.ui.dateEnd.setDate(today)

    # Trigger by: ui.listStock.CurrentRowChanged
    def set_stock_id(self):
        listStock = self.ui.listStock
        row = listStock.currentRow()
        text = listStock.item(row).text()
        ui.editStkid.setText(text)

    # Trigger by: ui.listStock.DoubleClicked
    def set_run_stock(self):
        self.set_stock_id()
        self.run_stock()

    # Trigger by: ui.btnRun.clicked
    def run_stock(self):
        text = self.ui.editStkid.text()
        flds = text.split('\t')
        stkid = flds[0].upper()
        if len(stkid) == 0:
            self.log('Warning> Please input stock id.')
            return

        stkname = ' @ $'.join(flds[1:])
        title = text if stkname == '' else '{} ({})'.format(stkname, stkid)

        date_start = self.ui.dateStart.date().toPyDate()
        date_end = self.ui.dateEnd.date().toPyDate()

        # draw close-price line for the symbol (stkid)
        try:
            if STOCK_SOURCE == 'yahoo':
                # Yahoo does not like "." in the symbol, so replace "." with "-"
                stkid = stkid.replace('.', '-')
            self.log('{}> Draw {} ...'.format(STOCK_SOURCE, stkid))
            quotes = web.DataReader(stkid, STOCK_SOURCE, date_start, date_end)

            # close current figure window
            plt.close()
            ax = quotes['Close'].plot()
            ax.set_xlabel('Date', fontsize=12)
            ax.set_ylabel('Price', fontsize=12)
            ax.set_title(title, fontsize=15)

            # Do not use plt.show(), it will wait until plot figure exit.
            plt.draw()
            plt.pause(0.000001)
            self.log('Done.')

        except Exception as E:
            self.log('{} : {}'.format(type(E), stkid))
            self.log('Exception> '+str(E))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    ui = Ui_Dialog()
    Dialog = My_Dialog(ui)

    ### Windows stays on top
    # from PyQt5.QtCore import Qt
    # Dialog.setWindowFlags(Dialog.windowFlags() | Qt.WindowStaysOnTopHint)

    ui.setupUi(Dialog)
    Dialog.load_stock_list(URL, FIELDS)
    Dialog.show()

    sys.exit(app.exec_())
