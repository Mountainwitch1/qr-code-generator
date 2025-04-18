import qrcode

def txt_to_qr(txt_file, output="menu_qr.png"):
    try:
        with open(txt_file, "r", encoding="utf-8") as file:
            content = file.read()

        # Generate the QR code
        qr = qrcode.make(content)
        qr.save(output)
        print(f"✅ QR code saved as '{output}'")
    except FileNotFoundError:
        print("❌ File not found. Please check the file path.")
    except Exception as e:
        print(f"❌ Something went wrong: {e}")

# Example use
if __name__ == "__main__":
    file_path = input("Enter the path to your .txt file: ")
    txt_to_qr(file_path)
