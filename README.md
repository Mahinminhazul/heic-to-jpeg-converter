
# HEIC to JPEG Photo Converter

![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

A simple, user-friendly tool that converts Apple HEIC photos to standard JPEG format while preserving maximum quality. Perfect for sharing photos with friends, family, or services that don't support the HEIC format.

## 📸 What This Tool Does

Apple devices save photos in HEIC format, which gives excellent quality with smaller file sizes. However, many applications, websites, and non-Apple devices don't support this format. This tool solves that problem by:

- Converting HEIC photos to standard JPEG format
- Preserving the highest possible quality
- Maintaining folder structure
- Processing multiple files in parallel for speed
- Creating a separate output folder that keeps your original files untouched

## 🚀 Installation

### Option 1: For Regular Users (Easiest)

1. Download this repository by clicking the green "Code" button and select "Download ZIP"
2. Extract the ZIP file to any location on your computer
3. Double-click the `heic_converter.py` file to run it

The script will automatically install any required libraries if they're missing.

### Option 2: For Python Users

1. Clone this repository:
git clone https://github.com/YOUR_USERNAME/heic-to-jpeg-converter.git
cd heic-to-jpeg-converter

2. Install required packages:
pip install -r requirements.txt


3. Run the script:
   python heic_converter.py

   

## 💻 Usage

1. Run the script by double-clicking `heic_converter.py` or using the command line
2. Enter the folder path where your HEIC photos are located (or press Enter to use the default)
3. Enter a name for the output folder (or press Enter to use "JPEG_Output")
4. Wait for the conversion to complete
5. Find your converted JPEG files in the output folder

## ⚙️ Features

- **High-Quality Conversion**: Uses maximum JPEG quality settings
- **Preserves Folder Structure**: Maintains your album organization
- **Fast Processing**: Converts multiple photos simultaneously
- **User-Friendly**: Simple prompts and clear progress indicators
- **Error Handling**: Detailed reporting of any conversion issues
- **Cross-Platform**: Works on Windows, macOS, and Linux

## 📋 Requirements

- Python 3.7 or higher
- Required libraries (automatically installed if missing):
- pillow
- pillow-heif
- pathlib

## 🤝 Contributing

Contributions are welcome! If you'd like to improve this tool:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🛟 Troubleshooting

- **"No module named 'pillow_heif'"**: The script should automatically install required libraries, but if it doesn't, run `pip install pillow pillow-heif pathlib` manually
- **"No HEIC files found"**: Make sure you're pointing to the correct directory and that the files have .HEIC extension
- **Windows shows errors with colors**: The colored text might not display correctly in some Windows terminals



