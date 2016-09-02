from PyQt4.QtGui import QMessageBox


class Message(QMessageBox):
    def __init__(self, mensaje, detailedtext=None):
        super().__init__()
        self.setText(mensaje)
        self.setDetailedText(detailedtext)


class MessageCritical(Message):
    def __init__(self, mensaje, detailedtext=None):
        super().__init__(mensaje, detailedtext)
        self.setIcon(self.Critical)


class MessageInfo(Message):
    def __init__(self, mensaje, detailedtext=None):
        super().__init__(mensaje, detailedtext)
        self.setIcon(self.Information)
