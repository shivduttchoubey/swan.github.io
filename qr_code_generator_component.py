import qrcode

# Static input for demonstration
# In production, this data would come from the database and API
# Uncomment and implement the API/database fetch logic
# Example API endpoint: https://example.com/api/fetch_data
# Example response: {"alphanum": "1234ABCD"}

# Mock API fetch - replace with real API/database logic
# import requests
# response = requests.get("https://example.com/api/fetch_data")
# alphanumeric_string = response.json().get("alphanum", "default123")

# Static input for trial
alphanumeric_string = "1234ABCD"  # Replace with dynamic fetch when implementing

# Construct the URL with the alphanumeric string
base_url = "https://shivduttchoubey.github.io/swan.github.io/dashboard/"
url_to_encode = f"{base_url}{alphanumeric_string}"

# Generate the QR code
qr = qrcode.QRCode(
    version=1,  # Controls the size of the QR Code (1 is the smallest)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
    box_size=10,  # Size of each QR box
    border=4,  # Border width (minimum is 4)
)

qr.add_data(url_to_encode)
qr.make(fit=True)

# Create the QR code image
qr_image = qr.make_image(fill_color="black", back_color="white")

# Save the QR code to a file
output_file = "qr_code.png"
qr_image.save(output_file)

print(f"QR code generated and saved as '{output_file}' for URL: {url_to_encode}")
