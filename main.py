from PyQt5 import QtWidgets
from controllers.homeController import HomeController
import sys

#pyuic5 -x .ui -o .py

#pyrcc5 image.qrc -o images.py


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    app = QtWidgets.QApplication(sys.argv)
    firstCintroller = HomeController()
    windowExample = firstCintroller
    windowExample.setWindowTitle('Home Nakama :D')
    windowExample.show()
    sys.exit(app.exec_())
