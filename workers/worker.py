from qtpy.QtCore import QObject, Signal


class Worker(QObject):
    finished = Signal(object)
    error = Signal(str)

    def __init__(self, service, text, divide, reduce, uppercase):
        super().__init__()
        self.service = service
        self.text = text
        self.divide = divide
        self.reduce = reduce
        self.uppercase = uppercase

    def run(self):
        try:
            result = self.process_text()
            self.finished.emit(result)
        except Exception as e:
            self.error.emit(str(e))

    def process_text(self):
        return self.service.correct(
            self.text,
            divide=self.divide,
            reduce=self.reduce,
            uppercase=self.uppercase,
        )
