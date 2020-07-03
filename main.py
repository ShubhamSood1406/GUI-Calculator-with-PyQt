import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import math

# This class will create a Button and then give it's own method to call when clicked.
class Button():
    def __init__(self, text, result):
        self.b = QPushButton(str(text))     # variable b will create PushButton for each button.
        self.text = text
        self.result = result
        self.b.clicked.connect(lambda: self.inputValue(self.text))      # connect Button to its event-handler and print value of text when clicked.

    def inputValue(self, value):
        if value == "=":        # if expression is "=" then evaluate the expression.
            final = eval(self.result.text())
            self.result.setText(str(final))     # change Text of result to final result.

        elif value == "CLEAR":      # clear the result textbox
            self.result.setText("")

        elif value == "√":
            v = float(self.result.text())       # convert the value to float and then apply operation on it.
            self.result.setText(str(math.sqrt(v)))

        elif value == "%":
            v = float(self.result.text())       # convert the value to float and then apply operation on it.
            self.result.setText(str(v/100))

        elif value == "DEL":
            old_value = self.result.text()
            self.result.setText(old_value[:-1])     # slice the text to remove last value of text.

        else:
            old_value = self.result.text()        # first value enter.
            new_value = old_value + str(value)        # concatenate new_value with old_value.
            self.result.setText(new_value)      # this will update new_value to result textbox.
            print("Clicked:", value)

        

class Application(QWidget):     # Inherits the QWidget class.
    def __init__(self):     # Initialise the class Application.
        super().__init__()      # Initialise the class QWidget that is inherited.
        self.setWindowTitle("Calculator (Made By:-SHUBHAM)")
        self.MainApp()      # This will Call the MainApp() to initialize.


    # An Internal Method of our Application, so that we can Initialize the entire Application from this method.
    def MainApp(self):
        result = QLineEdit()        # text box for Result

        grid = QGridLayout()        # Create our grid.

        # Making a list of buttons as of Calculator functionality.
        buttons = ["CLEAR", "DEL", "%", "/",
                    7, 8, 9, "*",
                    4, 5, 6, "-",
                    1, 2, 3, "+",
                    0, ".", "√", "="]

        grid.addWidget(result, 0, 0, 1, 4)      # first will be occupied by result's LineEdit

        row = 1     # from row 2 buttons will be placed
        col = 0
        # Placing buttons according to row & column.
        for button in buttons:
            if(col > 3):        # each Row consist of four buttons.
                row += 1        # goes to next Row when Column goes more than four.
                col = 0         # placed next row button from first column        

            buttonObject = Button(button, result)       # this will call the Button function that will button text and result when clicked.

            grid.addWidget(buttonObject.b, row, col, 1, 1)      # placing the button occupying one unit of row and column
            col += 1

        
        self.setLayout(grid)
        
        self.show()     # This will show the GUI Window that we made.

# Opening our Application
if __name__ == "__main__":
    app = QApplication(sys.argv)        # Passing the system argument variable.
    window = Application()      # To make window of our Application.
    sys.exit(app.exec_())       # System will make the Application execute till all the method passed in Application completes.

