import qrcode
import os

def generate_qr(filename, document_hash):

    data = f"Filename: {filename}\nSHA256: {document_hash}"

    img = qrcode.make(data)

    qr_folder = "static/qr"

    if not os.path.exists(qr_folder):
        os.makedirs(qr_folder)

    qr_path = os.path.join(qr_folder, filename + ".png")

    img.save(qr_path)

    return qr_path