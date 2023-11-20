# Awesome Email Sender App 🚀

Welcome to the Awesome Email Sender App! This PyQt5-based application allows you to send emails effortlessly with cool features like attachments. 📧✨

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [How to Use](#how-to-use)
  - [Login](#login)
  - [Attach Something](#attach-something)
  - [Send Mail](#send-mail)
- [Contributing](#contributing)
- [License](#license)

## Features

- 🌐 **SMTP Email Sending**: Utilizes the power of SMTP for sending emails securely.
- 📎 **Attachment Support**: Easily attach files to your emails.
- 🎨 **Beautiful GUI**: Built with PyQt5, providing an intuitive and user-friendly interface.

## Getting Started

### Prerequisites

Make sure you have the following installed:

- Python 3.x
- PyQt5
- smtplib
- email

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/awesome-email-sender.git
   ```

2. Navigate to the project folder:

   ```bash
   cd awesome-email-sender
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## How to Use

### Login

1. Launch the application:

   ```bash
   python main.py
   ```

2. Fill in your email server details and login credentials.

   - **SMTP Server**: Enter the SMTP server address.
   - **Port**: Provide the port number.
   - **Username**: Your email address.
   - **Password**: Your email password.
> **Note:** The password is required to authenticate your email account with the SMTP server. Ensure you enter the correct password associated with the provided email address.

3. Click the "Login" button.

### Attach Something

1. After successfully logging in, you can attach files to your email.

2. Click the "Attach Something" button.

3. Select the files you want to attach using the file dialog.

4. The attached files will be listed on the UI.

### Send Mail

1. Once you have logged in and attached files, compose your email.

2. Enter the recipient's email address, subject, and your message.

3. Click the "Send Mail" button.

4. A confirmation dialog will appear asking if you want to send the email.

5. Click "Yes" to send the email. If you click "No," the process will be canceled.

## Contributing

Contributions are welcome! Feel free to open issues and pull requests [CONTRIBUTING](CONTRIBUTING.md).

## License

This project is licensed under the [MIT License](LICENSE).

