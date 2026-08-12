# 🔐 Blockchain Document Authentication System

## 📖 Project Overview

The Blockchain Document Authentication System is a web application developed using Python Flask to securely authenticate digital documents. The system generates a unique SHA-256 hash for every uploaded document, stores it in a SQLite database, and generates a QR code for easy verification.

Users can later verify a document by uploading it again. The system compares the newly generated hash with the stored hash to determine whether the document is authentic or has been modified.

---

## 🎯 Objectives

- Securely authenticate digital documents.
- Detect document tampering using SHA-256 hashing.
- Generate QR codes for document verification.
- Maintain document records in a database.
- Provide an easy-to-use web interface.

---

## ✨ Features

- User Registration
- User Login
- Upload PDF/Documents
- SHA-256 Hash Generation
- QR Code Generation
- Download QR Code
- Document Verification
- Admin Dashboard
- Search Documents
- Upload Date & Time
- Responsive Bootstrap Interface

---

## 🛠 Technologies Used

- Python
- Flask
- Flask-SQLAlchemy
- SQLite
- HTML
- CSS
- Bootstrap 5
- SHA-256
- QR Code
- Pillow

---

## 📂 Project Structure

```
BlockchainDocumentAuth/
│
├── app.py
├── database.py
├── hashing.py
├── qrcode_generator.py
├── requirements.txt
├── README.md
│
├── instance/
│   └── database.db
│
├── uploads/
│
├── static/
│   └── qr/
│
├── templates/
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── upload.html
│   ├── upload_success.html
│   ├── verify.html
│   ├── verified.html
│   ├── tampered.html
│   └── admin.html
```

---

## ⚙️ Installation

1. Clone or download the project.
2. Install dependencies:

```
pip install -r requirements.txt
```

3. Run the application:

```
python app.py
```

4. Open your browser:

```
http://127.0.0.1:5000
```

---

## 🚀 Workflow

1. Register/Login
2. Upload Document
3. Generate SHA-256 Hash
4. Store Hash in Database
5. Generate QR Code
6. Verify Uploaded Document
7. Display Verification Result

---

## 🔮 Future Enhancements

- Blockchain Integration (Ethereum/Hyperledger)
- Digital Signature Support
- Cloud Storage
- Email Notifications
- Role-Based Access Control
- Mobile Application
- REST API
- Multi-file Verification

---

## 👨‍💻 Developer

**SUJITH M**

Project – 2026

---

## 📜 License

This project is developed for educational purposes as part of an MCA Mini Project.
