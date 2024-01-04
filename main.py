from PyQt5.QtWidgets import *
from PyQt5 import uic
from email import encoders
import smtplib
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

class MyMainWindow(QMainWindow):
    def __init__(self):
        super(MyMainWindow, self).__init__()
        
        # Load the user interface from the form.ui file
        uic.loadUi("form.ui", self)
        self.show()

        # Set a fixed size to the main window
        self.setFixedSize(self.size())

        # Connect buttons to corresponding methods
        self.pushButton.clicked.connect(self.login)
        self.pushButton_2.clicked.connect(self.attach_something)
        self.pushButton_3.clicked.connect(self.send_mail)

    def login(self):
        try:
            # Set up SMTP connection
            self.server = smtplib.SMTP(self.lineEdit_3.text(), self.lineEdit_4.text())
            self.server.ehlo()
            self.server.starttls()
            self.server.ehlo()
            self.server.login(self.lineEdit.text(), self.lineEdit_2.text())

            # Disable login fields after successful login
            self.disable_login_fields()
            
            # Enable mail fields for composing the message
            self.enable_mail_fields()

            # Initialize the email message object
            self.msg = MIMEMultipart()

        except smtplib.SMTPAuthenticationError:
            self.show_error("Login Failed", "Error: Invalid Login Info!")
        except smtplib.SMTPConnectError:
            self.show_error("Login Failed", "Error: Unable to connect to the SMTP server. Check your internet connection.")
        except Exception as e:
            self.show_error("Login Failed", f"Error: {str(e)}")

    def disable_login_fields(self):
        # Disable login-related input fields
        fields_to_disable = [self.lineEdit, self.lineEdit_2, self.lineEdit_3, self.lineEdit_4, self.pushButton]
        for field in fields_to_disable:
            field.setEnabled(False)

    def enable_mail_fields(self):
        # Enable mail-related input fields
        fields_to_enable = [self.lineEdit_5, self.lineEdit_6, self.textEdit, self.pushButton_2, self.pushButton_3]
        for field in fields_to_enable:
            field.setEnabled(True)

    def show_error(self, title, message):
        QMessageBox.critical(self, title, message)

    def attach_something(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        filenames, _ = QFileDialog.getOpenFileNames(self, "Open File", "", "All Files (*.*)", options=options)

        if filenames:
            for filename in filenames:
                self.attach_file(filename)

    def attach_file(self, filename):
        with open(filename, 'rb') as attachment:
            file_data = attachment.read()

        attachment_name = filename.split("/")[-1]

        mime_part = MIMEBase('application', 'octet-stream')
        mime_part.set_payload(file_data)
        encoders.encode_base64(mime_part)
        mime_part.add_header("Content-Disposition", f"attachment; filename={attachment_name}")
        self.msg.attach(mime_part)

        self.update_attachment_label(attachment_name)

    def update_attachment_label(self, attachment_name):
        if not self.label_8.text().endswith(":"):
            self.label_8.setText(self.label_8.text() + ",")
        self.label_8.setText(self.label_8.text() + " " + attachment_name)

    def send_mail(self):
        dialog = QMessageBox()
        dialog.setText("Do you want to send this mail?")
        dialog.addButton(QPushButton("Yes"), QMessageBox.YesRole)
        dialog.addButton(QPushButton("No"), QMessageBox.NoRole)

        if dialog.exec_() == 0:
            try:
                self.prepare_and_send_mail()
                self.show_success_message("Success", "Mail Sent")

            except Exception as e:
                self.show_error("Failed", f"Mail not sent. Error: {str(e)}")

            finally:
                self.cleanup_server()

    def prepare_and_send_mail(self):
        self.msg['From'] = "Anonymous"
        self.msg['To'] = self.lineEdit_5.text()
        self.msg['Subject'] = self.lineEdit_6.text()
        self.msg.attach(MIMEText(self.textEdit.toPlainText(), 'plain'))
        text = self.msg.as_string()

        self.send_mail_smtp(text)

    def show_success_message(self, title, message):
        QMessageBox.information(self, title, message)

    def cleanup_server(self):
        if hasattr(self, 'server') and self.server:
            self.server.quit()

    def send_mail_smtp(self, text):
        try:
            self.server.sendmail(self.lineEdit.text(), self.lineEdit_5.text(), text)
        except smtplib.SMTPException as smtp_error:
            raise Exception(f"SMTP Error: {str(smtp_error)}")

if __name__ == "__main__":
    app = QApplication([])
    window = MyMainWindow()
    window.show()
    app.exec_()
