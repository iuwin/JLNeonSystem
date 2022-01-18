import sys
import PyQt5.QtGui     as Gui
import PyQt5.QtWidgets as Wid
import PyQt5.QtCore    as Cor 

class WinTable(Wid.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.title = "Table"
        self.top    = 150
        self.left   = 300
        self.width  = 870
        self.height = 500
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height) 

class mainWindow(Wid.QMainWindow):
    def __init__(self, parent=None):
        super(mainWindow, self).__init__(parent)

        self.qtMenu()

    def qtMenu(self):
        mainMenu = self.menuBar()
        pyGuiMenu = mainMenu.addMenu('File')

        subItemTable = Wid.QAction('New', self)
        subItemTable.setShortcut("Ctrl+N")
        subItemTable.setStatusTip("New Window")

        subItemTable.triggered.connect(self.newWindow)     # +++

        pyGuiMenu.addAction(subItemTable) 

        subItemExit = Wid.QAction('Exit', self)
        subItemExit.setShortcut("Ctrl+E")
        subItemExit.setStatusTip("Exit Application")
        subItemExit.triggered.connect(self.close_App)
        pyGuiMenu.addAction(subItemExit);

    def close_App(self):
        reply = Wid.QMessageBox.question(
            self, 
            "Exit Application", 
            "Are you sure to close the window?", 
            Wid.QMessageBox.Yes | Wid.QMessageBox.No, 
            Wid.QMessageBox.No
        )
        if reply == Wid.QMessageBox.Yes:
           sys.exit()

    def newWindow(self):                                    # +++
        print('def newWindow(self):')    
        self.winTable = WinTable()
        self.winTable.show()


def main():
    App = Wid.QApplication(sys.argv)
    homeWin = mainWindow()   
    homeWin.setWindowTitle("Trial GUI")
    homeWin.setGeometry (250, 200, 870, 500);
    homeWin.setWindowIcon (Gui.QIcon("D:/_Qt/img/pyqt.jpg"));
    homeWin.show();
    sys.exit(App.exec_()); 

if __name__ == "__main__":
    main()
