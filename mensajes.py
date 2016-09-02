from PyQt4.QtGui import QMessageBox


class Message(QMessageBox):
    """
    Sobreescribe el init de QMessageBox para que la hereden
    clases con mensajes especificos
    :param: mensaje: string con el mensaje principal del box
    :param: detailed_text: string con el texto detallado del error.
            Se puede sacar del objeto error con e.__str__().
    """
    def __init__(self, mensaje, detailed_text=None):
        super().__init__()
        self.setText(mensaje)
        self.setDetailedText(detailed_text)


class MessageCritical(Message):
    def __init__(self, mensaje, detailed_text=None):
        super().__init__(mensaje, detailed_text)
        self.setIcon(self.Critical)


class MessageConfirm(Message):
    def __init__(self, mensaje, detailed_text=None):
        super().__init__(mensaje, detailed_text)
        self.setIcon(QMessageBox.Question)
        self.setStandardButtons(QMessageBox.Yes | QMessageBox.No)


class MessageInfo(Message):
    def __init__(self, mensaje, detailed_text=None):
        super().__init__(mensaje, detailed_text)
        self.setIcon(self.Information)
