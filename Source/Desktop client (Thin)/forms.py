from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_main_menu_window(object):
    def setupUi(self, main_menu_window):
        main_menu_window.setObjectName("main_menu_window")
        main_menu_window.resize(360, 210)
        main_menu_window.setMaximumSize(QtCore.QSize(360, 210))
        main_menu_window.setStyleSheet("background-color: white;")
        self.centralwidget = QtWidgets.QWidget(main_menu_window)
        self.centralwidget.setObjectName("centralwidget")
        self.main_menu_label = QtWidgets.QLabel(self.centralwidget)
        self.main_menu_label.setGeometry(QtCore.QRect(0, 0, 360, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.main_menu_label.setFont(font)
        self.main_menu_label.setAlignment(QtCore.Qt.AlignCenter)
        self.main_menu_label.setObjectName("main_menu_label")
        self.transactions_button = QtWidgets.QPushButton(self.centralwidget)
        self.transactions_button.setGeometry(QtCore.QRect(40, 60, 280, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.transactions_button.setFont(font)
        self.transactions_button.setObjectName("transactions_button")
        self.wallets_button = QtWidgets.QPushButton(self.centralwidget)
        self.wallets_button.setGeometry(QtCore.QRect(40, 110, 280, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.wallets_button.setFont(font)
        self.wallets_button.setObjectName("wallets_button")
        self.settings_button = QtWidgets.QPushButton(self.centralwidget)
        self.settings_button.setGeometry(QtCore.QRect(40, 160, 280, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.settings_button.setFont(font)
        self.settings_button.setObjectName("settings_button")
        main_menu_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(main_menu_window)
        QtCore.QMetaObject.connectSlotsByName(main_menu_window)

    def retranslateUi(self, main_menu_window):
        _translate = QtCore.QCoreApplication.translate
        main_menu_window.setWindowTitle(_translate("main_menu_window", "MainWindow"))
        self.main_menu_label.setText(_translate("main_menu_window", "Главное меню"))
        self.transactions_button.setText(_translate("main_menu_window", "Транзакции"))
        self.wallets_button.setText(_translate("main_menu_window", "Кошельки"))
        self.settings_button.setText(_translate("main_menu_window", "Настройки"))

class Ui_wallet_window(object):
    def setupUi(self, wallet_window):
        wallet_window.setObjectName("wallet_window")
        wallet_window.resize(360, 214)
        wallet_window.setMaximumSize(QtCore.QSize(360, 214))
        self.centralwidget = QtWidgets.QWidget(wallet_window)
        self.centralwidget.setObjectName("centralwidget")
        self.wallet_label = QtWidgets.QLabel(self.centralwidget)
        self.wallet_label.setGeometry(QtCore.QRect(0, 0, 360, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.wallet_label.setFont(font)
        self.wallet_label.setAlignment(QtCore.Qt.AlignCenter)
        self.wallet_label.setObjectName("wallet_label")
        self.title_label = QtWidgets.QLabel(self.centralwidget)
        self.title_label.setGeometry(QtCore.QRect(20, 90, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.title_label.setFont(font)
        self.title_label.setObjectName("title_label")
        self.title_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.title_line_edit.setGeometry(QtCore.QRect(120, 90, 221, 20))
        self.title_line_edit.setObjectName("title_line_edit")
        self.save_button = QtWidgets.QPushButton(self.centralwidget)
        self.save_button.setGeometry(QtCore.QRect(40, 160, 280, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.save_button.setFont(font)
        self.save_button.setObjectName("save_button")
        self.id_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.id_line_edit.setGeometry(QtCore.QRect(60, 60, 281, 20))
        self.id_line_edit.setText("")
        self.id_line_edit.setObjectName("id_line_edit")
        self.id_label = QtWidgets.QLabel(self.centralwidget)
        self.id_label.setGeometry(QtCore.QRect(20, 60, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.id_label.setFont(font)
        self.id_label.setObjectName("id_label")
        self.wallet_type_combo_box = QtWidgets.QComboBox(self.centralwidget)
        self.wallet_type_combo_box.setGeometry(QtCore.QRect(70, 120, 271, 22))
        self.wallet_type_combo_box.setObjectName("wallet_type_combo_box")
        self.wallet_type_label = QtWidgets.QLabel(self.centralwidget)
        self.wallet_type_label.setGeometry(QtCore.QRect(20, 120, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.wallet_type_label.setFont(font)
        self.wallet_type_label.setObjectName("wallet_type_label")
        wallet_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(wallet_window)
        QtCore.QMetaObject.connectSlotsByName(wallet_window)

    def retranslateUi(self, wallet_window):
        _translate = QtCore.QCoreApplication.translate
        wallet_window.setWindowTitle(_translate("wallet_window", "MainWindow"))
        self.wallet_label.setText(_translate("wallet_window", "Кошелёк"))
        self.title_label.setText(_translate("wallet_window", "Название:"))
        self.save_button.setText(_translate("wallet_window", "Сохранить"))
        self.id_label.setText(_translate("wallet_window", "ID:"))
        self.wallet_type_label.setText(_translate("wallet_window", "Тип:"))

class Ui_item_window(object):
    def setupUi(self, item_window):
        item_window.setObjectName("item_window")
        item_window.resize(360, 214)
        item_window.setMaximumSize(QtCore.QSize(360, 214))
        self.centralwidget = QtWidgets.QWidget(item_window)
        self.centralwidget.setObjectName("centralwidget")
        self.wallet_label = QtWidgets.QLabel(self.centralwidget)
        self.wallet_label.setGeometry(QtCore.QRect(0, 0, 360, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.wallet_label.setFont(font)
        self.wallet_label.setAlignment(QtCore.Qt.AlignCenter)
        self.wallet_label.setObjectName("wallet_label")
        self.save_button = QtWidgets.QPushButton(self.centralwidget)
        self.save_button.setGeometry(QtCore.QRect(40, 150, 280, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.save_button.setFont(font)
        self.save_button.setStyleSheet("")
        self.save_button.setDefault(False)
        self.save_button.setFlat(False)
        self.save_button.setObjectName("save_button")
        self.id_label = QtWidgets.QLabel(self.centralwidget)
        self.id_label.setGeometry(QtCore.QRect(20, 70, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.id_label.setFont(font)
        self.id_label.setObjectName("id_label")
        self.title_label = QtWidgets.QLabel(self.centralwidget)
        self.title_label.setGeometry(QtCore.QRect(20, 100, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.title_label.setFont(font)
        self.title_label.setObjectName("title_label")
        self.title_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.title_line_edit.setGeometry(QtCore.QRect(120, 100, 221, 20))
        self.title_line_edit.setObjectName("title_line_edit")
        self.id_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.id_line_edit.setGeometry(QtCore.QRect(60, 70, 281, 20))
        self.id_line_edit.setText("")
        self.id_line_edit.setObjectName("id_line_edit")
        item_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(item_window)
        QtCore.QMetaObject.connectSlotsByName(item_window)

    def retranslateUi(self, item_window):
        _translate = QtCore.QCoreApplication.translate
        item_window.setWindowTitle(_translate("item_window", "MainWindow"))
        self.wallet_label.setText(_translate("item_window", "Статья доходов / расходов"))
        self.save_button.setText(_translate("item_window", "Сохранить"))
        self.id_label.setText(_translate("item_window", "ID:"))
        self.title_label.setText(_translate("item_window", "Название:"))

class Ui_items_window(object):
    def setupUi(self, items_window):
        items_window.setObjectName("items_window")
        items_window.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(items_window)
        self.centralwidget.setObjectName("centralwidget")
        self.revenue_items_table_widget = QtWidgets.QTableWidget(self.centralwidget)
        self.revenue_items_table_widget.setGeometry(QtCore.QRect(30, 70, 350, 420))
        self.revenue_items_table_widget.setObjectName("revenue_items_table_widget")
        self.revenue_items_table_widget.setColumnCount(2)
        self.revenue_items_table_widget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.revenue_items_table_widget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.revenue_items_table_widget.setHorizontalHeaderItem(1, item)
        self.items_label = QtWidgets.QLabel(self.centralwidget)
        self.items_label.setGeometry(QtCore.QRect(0, 0, 801, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.items_label.setFont(font)
        self.items_label.setAlignment(QtCore.Qt.AlignCenter)
        self.items_label.setObjectName("items_label")
        self.cost_items_table_widget = QtWidgets.QTableWidget(self.centralwidget)
        self.cost_items_table_widget.setGeometry(QtCore.QRect(420, 70, 350, 420))
        self.cost_items_table_widget.setObjectName("cost_items_table_widget")
        self.cost_items_table_widget.setColumnCount(2)
        self.cost_items_table_widget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.cost_items_table_widget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.cost_items_table_widget.setHorizontalHeaderItem(1, item)
        self.create_revenue_item_button = QtWidgets.QPushButton(self.centralwidget)
        self.create_revenue_item_button.setGeometry(QtCore.QRect(70, 500, 280, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.create_revenue_item_button.setFont(font)
        self.create_revenue_item_button.setObjectName("create_revenue_item_button")
        self.delete_revenue_item_button = QtWidgets.QPushButton(self.centralwidget)
        self.delete_revenue_item_button.setGeometry(QtCore.QRect(70, 550, 280, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.delete_revenue_item_button.setFont(font)
        self.delete_revenue_item_button.setObjectName("delete_revenue_item_button")
        self.create_cost_item_button = QtWidgets.QPushButton(self.centralwidget)
        self.create_cost_item_button.setGeometry(QtCore.QRect(460, 500, 280, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.create_cost_item_button.setFont(font)
        self.create_cost_item_button.setObjectName("create_cost_item_button")
        self.delete_cost_item_button = QtWidgets.QPushButton(self.centralwidget)
        self.delete_cost_item_button.setGeometry(QtCore.QRect(460, 550, 280, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.delete_cost_item_button.setFont(font)
        self.delete_cost_item_button.setObjectName("delete_cost_item_button")
        items_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(items_window)
        QtCore.QMetaObject.connectSlotsByName(items_window)

    def retranslateUi(self, items_window):
        _translate = QtCore.QCoreApplication.translate
        items_window.setWindowTitle(_translate("items_window", "MainWindow"))
        item = self.revenue_items_table_widget.horizontalHeaderItem(0)
        item.setText(_translate("items_window", "ID"))
        item = self.revenue_items_table_widget.horizontalHeaderItem(1)
        item.setText(_translate("items_window", "Название"))
        self.items_label.setText(_translate("items_window", "Статьи доходов / расходов"))
        item = self.cost_items_table_widget.horizontalHeaderItem(0)
        item.setText(_translate("items_window", "ID"))
        item = self.cost_items_table_widget.horizontalHeaderItem(1)
        item.setText(_translate("items_window", "Название"))
        self.create_revenue_item_button.setText(_translate("items_window", "Создать статью доходов"))
        self.delete_revenue_item_button.setText(_translate("items_window", "Удалить статью доходов"))
        self.create_cost_item_button.setText(_translate("items_window", "Создать статью расходов"))
        self.delete_cost_item_button.setText(_translate("items_window", "Удалить статью расходов"))

class Ui_settings_window(object):
    def setupUi(self, settings_window):
        settings_window.setObjectName("settings_window")
        settings_window.resize(360, 194)
        settings_window.setMaximumSize(QtCore.QSize(360, 194))
        self.centralwidget = QtWidgets.QWidget(settings_window)
        self.centralwidget.setObjectName("centralwidget")
        self.settings_label = QtWidgets.QLabel(self.centralwidget)
        self.settings_label.setGeometry(QtCore.QRect(0, 0, 360, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.settings_label.setFont(font)
        self.settings_label.setAlignment(QtCore.Qt.AlignCenter)
        self.settings_label.setObjectName("settings_label")
        self.clear_base_button = QtWidgets.QPushButton(self.centralwidget)
        self.clear_base_button.setGeometry(QtCore.QRect(40, 140, 280, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.clear_base_button.setFont(font)
        self.clear_base_button.setObjectName("clear_base_button")
        self.save_button = QtWidgets.QPushButton(self.centralwidget)
        self.save_button.setGeometry(QtCore.QRect(40, 100, 280, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.save_button.setFont(font)
        self.save_button.setObjectName("save_button")
        self.server_label = QtWidgets.QLabel(self.centralwidget)
        self.server_label.setGeometry(QtCore.QRect(40, 60, 55, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.server_label.setFont(font)
        self.server_label.setObjectName("server_label")
        self.server_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.server_line_edit.setGeometry(QtCore.QRect(100, 60, 221, 22))
        self.server_line_edit.setObjectName("server_line_edit")
        settings_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(settings_window)
        QtCore.QMetaObject.connectSlotsByName(settings_window)

    def retranslateUi(self, settings_window):
        _translate = QtCore.QCoreApplication.translate
        settings_window.setWindowTitle(_translate("settings_window", "MainWindow"))
        self.settings_label.setText(_translate("settings_window", "Настройки"))
        self.clear_base_button.setText(_translate("settings_window", "Очистить базу"))
        self.save_button.setText(_translate("settings_window", "Сохранить"))
        self.server_label.setText(_translate("settings_window", "Сервер"))

class Ui_transaction_window(object):
    def setupUi(self, transaction_window):
        transaction_window.setObjectName("transaction_window")
        transaction_window.resize(360, 291)
        transaction_window.setMaximumSize(QtCore.QSize(360, 300))
        self.centralwidget = QtWidgets.QWidget(transaction_window)
        self.centralwidget.setObjectName("centralwidget")
        self.transaction_label = QtWidgets.QLabel(self.centralwidget)
        self.transaction_label.setGeometry(QtCore.QRect(0, 0, 360, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.transaction_label.setFont(font)
        self.transaction_label.setAlignment(QtCore.Qt.AlignCenter)
        self.transaction_label.setObjectName("transaction_label")
        self.save_button = QtWidgets.QPushButton(self.centralwidget)
        self.save_button.setGeometry(QtCore.QRect(40, 240, 280, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.save_button.setFont(font)
        self.save_button.setObjectName("save_button")
        self.summ_label = QtWidgets.QLabel(self.centralwidget)
        self.summ_label.setGeometry(QtCore.QRect(31, 110, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.summ_label.setFont(font)
        self.summ_label.setObjectName("summ_label")
        self.summ_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.summ_line_edit.setGeometry(QtCore.QRect(110, 110, 221, 20))
        self.summ_line_edit.setObjectName("summ_line_edit")
        self.transaction_type_label = QtWidgets.QLabel(self.centralwidget)
        self.transaction_type_label.setGeometry(QtCore.QRect(30, 140, 161, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.transaction_type_label.setFont(font)
        self.transaction_type_label.setObjectName("transaction_type_label")
        self.transaction_type_combo_box = QtWidgets.QComboBox(self.centralwidget)
        self.transaction_type_combo_box.setGeometry(QtCore.QRect(190, 140, 141, 22))
        self.transaction_type_combo_box.setObjectName("transaction_type_combo_box")
        self.wallet_label = QtWidgets.QLabel(self.centralwidget)
        self.wallet_label.setGeometry(QtCore.QRect(30, 170, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.wallet_label.setFont(font)
        self.wallet_label.setObjectName("wallet_label")
        self.wallet_combo_box = QtWidgets.QComboBox(self.centralwidget)
        self.wallet_combo_box.setGeometry(QtCore.QRect(130, 170, 201, 22))
        self.wallet_combo_box.setObjectName("wallet_combo_box")
        self.id_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.id_line_edit.setGeometry(QtCore.QRect(69, 50, 261, 20))
        self.id_line_edit.setText("")
        self.id_line_edit.setReadOnly(True)
        self.id_line_edit.setObjectName("id_line_edit")
        self.id_label = QtWidgets.QLabel(self.centralwidget)
        self.id_label.setGeometry(QtCore.QRect(30, 50, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.id_label.setFont(font)
        self.id_label.setObjectName("id_label")
        self.date_label = QtWidgets.QLabel(self.centralwidget)
        self.date_label.setGeometry(QtCore.QRect(31, 80, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.date_label.setFont(font)
        self.date_label.setObjectName("date_label")
        self.date_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.date_line_edit.setGeometry(QtCore.QRect(100, 80, 231, 20))
        self.date_line_edit.setObjectName("date_line_edit")
        self.item_label = QtWidgets.QLabel(self.centralwidget)
        self.item_label.setGeometry(QtCore.QRect(30, 200, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.item_label.setFont(font)
        self.item_label.setObjectName("item_label")
        self.item_combo_box = QtWidgets.QComboBox(self.centralwidget)
        self.item_combo_box.setGeometry(QtCore.QRect(110, 200, 221, 22))
        self.item_combo_box.setObjectName("item_combo_box")
        transaction_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(transaction_window)
        QtCore.QMetaObject.connectSlotsByName(transaction_window)

    def retranslateUi(self, transaction_window):
        _translate = QtCore.QCoreApplication.translate
        transaction_window.setWindowTitle(_translate("transaction_window", "MainWindow"))
        self.transaction_label.setText(_translate("transaction_window", "Транзакция"))
        self.save_button.setText(_translate("transaction_window", "Сохранить"))
        self.summ_label.setText(_translate("transaction_window", "Сумма:"))
        self.transaction_type_label.setText(_translate("transaction_window", "Вид транзакции:"))
        self.wallet_label.setText(_translate("transaction_window", "Кошелёк:"))
        self.id_label.setText(_translate("transaction_window", "ID:"))
        self.date_label.setText(_translate("transaction_window", "Дата:"))
        self.item_label.setText(_translate("transaction_window", "Статья:"))

class Ui_transactions_window(object):
    def setupUi(self, transactions_window):
        transactions_window.setObjectName("transactions_window")
        transactions_window.resize(850, 540)
        transactions_window.setMinimumSize(QtCore.QSize(850, 540))
        transactions_window.setMaximumSize(QtCore.QSize(850, 540))
        self.centralwidget = QtWidgets.QWidget(transactions_window)
        self.centralwidget.setObjectName("centralwidget")
        self.transactions_label = QtWidgets.QLabel(self.centralwidget)
        self.transactions_label.setGeometry(QtCore.QRect(0, 0, 851, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.transactions_label.setFont(font)
        self.transactions_label.setAlignment(QtCore.Qt.AlignCenter)
        self.transactions_label.setObjectName("transactions_label")
        self.create_transaction_button = QtWidgets.QPushButton(self.centralwidget)
        self.create_transaction_button.setGeometry(QtCore.QRect(40, 480, 211, 40))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.create_transaction_button.setFont(font)
        self.create_transaction_button.setObjectName("create_transaction_button")
        self.delete_transaction_button = QtWidgets.QPushButton(self.centralwidget)
        self.delete_transaction_button.setGeometry(QtCore.QRect(310, 480, 211, 40))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.delete_transaction_button.setFont(font)
        self.delete_transaction_button.setObjectName("delete_transaction_button")
        self.items_button = QtWidgets.QPushButton(self.centralwidget)
        self.items_button.setGeometry(QtCore.QRect(590, 480, 211, 40))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.items_button.setFont(font)
        self.items_button.setObjectName("items_button")
        self.transactions_list_table_widget = QtWidgets.QTableWidget(self.centralwidget)
        self.transactions_list_table_widget.setGeometry(QtCore.QRect(45, 60, 761, 401))
        self.transactions_list_table_widget.setObjectName("transactions_list_table_widget")
        self.transactions_list_table_widget.setColumnCount(6)
        self.transactions_list_table_widget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.transactions_list_table_widget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.transactions_list_table_widget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.transactions_list_table_widget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.transactions_list_table_widget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.transactions_list_table_widget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.transactions_list_table_widget.setHorizontalHeaderItem(5, item)
        transactions_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(transactions_window)
        QtCore.QMetaObject.connectSlotsByName(transactions_window)

    def retranslateUi(self, transactions_window):
        _translate = QtCore.QCoreApplication.translate
        transactions_window.setWindowTitle(_translate("transactions_window", "MainWindow"))
        self.transactions_label.setText(_translate("transactions_window", "Транзакции"))
        self.create_transaction_button.setText(_translate("transactions_window", "Создать транзакцию"))
        self.delete_transaction_button.setText(_translate("transactions_window", "Удалить транзакцию"))
        self.items_button.setText(_translate("transactions_window", "Статьи доходов / расходов"))
        item = self.transactions_list_table_widget.horizontalHeaderItem(0)
        item.setText(_translate("transactions_window", "ID"))
        item = self.transactions_list_table_widget.horizontalHeaderItem(1)
        item.setText(_translate("transactions_window", "Тип"))
        item = self.transactions_list_table_widget.horizontalHeaderItem(2)
        item.setText(_translate("transactions_window", "Дата"))
        item = self.transactions_list_table_widget.horizontalHeaderItem(3)
        item.setText(_translate("transactions_window", "Кошелёк"))
        item = self.transactions_list_table_widget.horizontalHeaderItem(4)
        item.setText(_translate("transactions_window", "Сумма"))
        item = self.transactions_list_table_widget.horizontalHeaderItem(5)
        item.setText(_translate("transactions_window", "Статья"))

class Ui_wallets_window(object):
    def setupUi(self, wallets_window):
        wallets_window.setObjectName("wallets_window")
        wallets_window.resize(800, 530)
        wallets_window.setMinimumSize(QtCore.QSize(800, 530))
        wallets_window.setMaximumSize(QtCore.QSize(800, 530))
        self.centralwidget = QtWidgets.QWidget(wallets_window)
        self.centralwidget.setObjectName("centralwidget")
        self.wallets_label = QtWidgets.QLabel(self.centralwidget)
        self.wallets_label.setGeometry(QtCore.QRect(0, 0, 801, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.wallets_label.setFont(font)
        self.wallets_label.setAlignment(QtCore.Qt.AlignCenter)
        self.wallets_label.setObjectName("wallets_label")
        self.create_wallet_button = QtWidgets.QPushButton(self.centralwidget)
        self.create_wallet_button.setGeometry(QtCore.QRect(40, 480, 220, 40))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.create_wallet_button.setFont(font)
        self.create_wallet_button.setObjectName("create_wallet_button")
        self.delete_wallet_button = QtWidgets.QPushButton(self.centralwidget)
        self.delete_wallet_button.setGeometry(QtCore.QRect(290, 480, 220, 40))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.delete_wallet_button.setFont(font)
        self.delete_wallet_button.setObjectName("delete_wallet_button")
        self.wallets_list_table_widget = QtWidgets.QTableWidget(self.centralwidget)
        self.wallets_list_table_widget.setGeometry(QtCore.QRect(40, 50, 721, 401))
        self.wallets_list_table_widget.setObjectName("wallets_list_table_widget")
        self.wallets_list_table_widget.setColumnCount(4)
        self.wallets_list_table_widget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.wallets_list_table_widget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.wallets_list_table_widget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.wallets_list_table_widget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.wallets_list_table_widget.setHorizontalHeaderItem(3, item)
        self.wallets_types_button = QtWidgets.QPushButton(self.centralwidget)
        self.wallets_types_button.setGeometry(QtCore.QRect(540, 480, 220, 40))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.wallets_types_button.setFont(font)
        self.wallets_types_button.setObjectName("wallets_types_button")
        wallets_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(wallets_window)
        QtCore.QMetaObject.connectSlotsByName(wallets_window)

    def retranslateUi(self, wallets_window):
        _translate = QtCore.QCoreApplication.translate
        wallets_window.setWindowTitle(_translate("wallets_window", "MainWindow"))
        self.wallets_label.setText(_translate("wallets_window", "Кошельки"))
        self.create_wallet_button.setText(_translate("wallets_window", "Создать кошелёк"))
        self.delete_wallet_button.setText(_translate("wallets_window", "Удалить кошелёк"))
        item = self.wallets_list_table_widget.horizontalHeaderItem(0)
        item.setText(_translate("wallets_window", "ID"))
        item = self.wallets_list_table_widget.horizontalHeaderItem(1)
        item.setText(_translate("wallets_window", "Наименование"))
        item = self.wallets_list_table_widget.horizontalHeaderItem(2)
        item.setText(_translate("wallets_window", "Тип"))
        item = self.wallets_list_table_widget.horizontalHeaderItem(3)
        item.setText(_translate("wallets_window", "Баланс"))
        self.wallets_types_button.setText(_translate("wallets_window", "Типы кошельков"))

class Ui_wallets_type_window(object):
    def setupUi(self, wallets_type_window):
        wallets_type_window.setObjectName("wallets_type_window")
        wallets_type_window.resize(360, 214)
        wallets_type_window.setMaximumSize(QtCore.QSize(360, 214))
        self.centralwidget = QtWidgets.QWidget(wallets_type_window)
        self.centralwidget.setObjectName("centralwidget")
        self.wallets_type_label = QtWidgets.QLabel(self.centralwidget)
        self.wallets_type_label.setGeometry(QtCore.QRect(0, 0, 360, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.wallets_type_label.setFont(font)
        self.wallets_type_label.setAlignment(QtCore.Qt.AlignCenter)
        self.wallets_type_label.setObjectName("wallets_type_label")
        self.save_button = QtWidgets.QPushButton(self.centralwidget)
        self.save_button.setGeometry(QtCore.QRect(40, 150, 280, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.save_button.setFont(font)
        self.save_button.setStyleSheet("")
        self.save_button.setDefault(False)
        self.save_button.setFlat(False)
        self.save_button.setObjectName("save_button")
        self.id_label = QtWidgets.QLabel(self.centralwidget)
        self.id_label.setGeometry(QtCore.QRect(20, 70, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.id_label.setFont(font)
        self.id_label.setObjectName("id_label")
        self.title_label = QtWidgets.QLabel(self.centralwidget)
        self.title_label.setGeometry(QtCore.QRect(20, 100, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.title_label.setFont(font)
        self.title_label.setObjectName("title_label")
        self.title_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.title_line_edit.setGeometry(QtCore.QRect(120, 100, 221, 20))
        self.title_line_edit.setObjectName("title_line_edit")
        self.id_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.id_line_edit.setGeometry(QtCore.QRect(60, 70, 281, 20))
        self.id_line_edit.setText("")
        self.id_line_edit.setObjectName("id_line_edit")
        wallets_type_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(wallets_type_window)
        QtCore.QMetaObject.connectSlotsByName(wallets_type_window)

    def retranslateUi(self, wallets_type_window):
        _translate = QtCore.QCoreApplication.translate
        wallets_type_window.setWindowTitle(_translate("wallets_type_window", "MainWindow"))
        self.wallets_type_label.setText(_translate("wallets_type_window", "Тип кошельков"))
        self.save_button.setText(_translate("wallets_type_window", "Сохранить"))
        self.id_label.setText(_translate("wallets_type_window", "ID:"))
        self.title_label.setText(_translate("wallets_type_window", "Название:"))

class Ui_wallets_types_window(object):
    def setupUi(self, wallets_types_window):
        wallets_types_window.setObjectName("wallets_types_window")
        wallets_types_window.resize(550, 530)
        wallets_types_window.setMinimumSize(QtCore.QSize(550, 530))
        wallets_types_window.setMaximumSize(QtCore.QSize(550, 530))
        self.centralwidget = QtWidgets.QWidget(wallets_types_window)
        self.centralwidget.setObjectName("centralwidget")
        self.wallets_types_label = QtWidgets.QLabel(self.centralwidget)
        self.wallets_types_label.setGeometry(QtCore.QRect(0, 0, 551, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.wallets_types_label.setFont(font)
        self.wallets_types_label.setAlignment(QtCore.Qt.AlignCenter)
        self.wallets_types_label.setObjectName("wallets_types_label")
        self.create_wallets_types_button = QtWidgets.QPushButton(self.centralwidget)
        self.create_wallets_types_button.setGeometry(QtCore.QRect(40, 480, 220, 40))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.create_wallets_types_button.setFont(font)
        self.create_wallets_types_button.setObjectName("create_wallets_types_button")
        self.delete_wallets_types_button = QtWidgets.QPushButton(self.centralwidget)
        self.delete_wallets_types_button.setGeometry(QtCore.QRect(290, 480, 220, 40))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.delete_wallets_types_button.setFont(font)
        self.delete_wallets_types_button.setObjectName("delete_wallets_types_button")
        self.wallets_types_list_table_widget = QtWidgets.QTableWidget(self.centralwidget)
        self.wallets_types_list_table_widget.setGeometry(QtCore.QRect(40, 50, 471, 401))
        self.wallets_types_list_table_widget.setObjectName("wallets_types_list_table_widget")
        self.wallets_types_list_table_widget.setColumnCount(2)
        self.wallets_types_list_table_widget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.wallets_types_list_table_widget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.wallets_types_list_table_widget.setHorizontalHeaderItem(1, item)
        wallets_types_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(wallets_types_window)
        QtCore.QMetaObject.connectSlotsByName(wallets_types_window)

    def retranslateUi(self, wallets_types_window):
        _translate = QtCore.QCoreApplication.translate
        wallets_types_window.setWindowTitle(_translate("wallets_types_window", "MainWindow"))
        self.wallets_types_label.setText(_translate("wallets_types_window", "Типы кошельков"))
        self.create_wallets_types_button.setText(_translate("wallets_types_window", "Создать тип кошельков"))
        self.delete_wallets_types_button.setText(_translate("wallets_types_window", "Удалить тип кошельков"))
        item = self.wallets_types_list_table_widget.horizontalHeaderItem(0)
        item.setText(_translate("wallets_types_window", "ID"))
        item = self.wallets_types_list_table_widget.horizontalHeaderItem(1)
        item.setText(_translate("wallets_types_window", "Наименование"))
