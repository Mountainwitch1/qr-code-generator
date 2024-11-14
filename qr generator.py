import qrcode
import os

# Path to your photo directory
photos_directory = "/path/to/your/photo/directory"
output_directory = "/path/to/save/qr_codes"

# Make sure the output directory exists
os.makedirs(output_directory, exist_ok=True)

# Generate a QR code for each file in the directory
for filename in os.listdir(photos_directory):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):  # Filter image files
        photo_path = os.path.join(photos_directory, filename)

        # Create a QR code
        qr = qrcode.make(photo_path)  # Automatically creates QR with default settings

        # Save the QR code image
        qr.save(os.path.join(output_directory, f"{filename}_qr.png"))

        print(f"QR code saved for {filename}")
