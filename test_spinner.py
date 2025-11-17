from qtpy import QtWidgets, QtGui, QtCore
import sys

app = QtWidgets.QApplication([])

label = QtWidgets.QLabel()
label.setWindowTitle("Test GIF")
label.resize(200, 200)

movie = QtGui.QMovie("./resources/gif/Loading.gif")
print("GIF isValid:", movie.isValid())

label.setMovie(movie)
movie.start()
label.show()

sys.exit(app.exec_())
