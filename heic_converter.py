#!/usr/bin/env python3
"""
HEIC to JPEG Photo Converter
----------------------------
A friendly tool that converts Apple HEIC photos to standard JPEG format
while maintaining the highest possible quality.

Simply run the script and follow the prompts to convert your photos!
"""

import os
import sys
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor

# Try importing required libraries
try:
    from PIL import Image
    from pillow_heif import register_heif_opener
except ImportError:
    print("Required libraries not found. Installing them now...")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pillow", "pillow-heif", "pathlib"])
    
    # Import again after installation
    from PIL import Image
    from pillow_heif import register_heif_opener


def print_color(text, color="green"):
    """Print colored text for better user experience."""
    colors = {
        "green": "\033[92m",
        "red": "\033[91m",
        "yellow": "\033[93m",
        "blue": "\033[94m",
        "end": "\033[0m"
    }
    
    # Only use colors on systems that support them
    if os.name == "nt":  # Windows
        print(text)
    else:
        print(f"{colors.get(color, '')}{text}{colors['end']}")


def convert_single_heic(heic_file, input_dir, output_dir):
    """
    Convert a single HEIC file to JPEG with maximum quality.
    
    Args:
        heic_file: Path to the HEIC file
        input_dir: Base input directory (for relative path calculation)
        output_dir: Base output directory
        
    Returns:
        Tuple of (success, filename)
    """
    try:
        # Create relative path structure to preserve folders
        relative_path = heic_file.relative_to(input_dir).parent
        target_dir = output_dir / relative_path
        target_dir.mkdir(parents=True, exist_ok=True)
         
        # Conversion process
        with Image.open(heic_file) as img:
            # Create output filename with jpg extension
            jpeg_path = target_dir / f"{heic_file.stem}.jpg"
            
            # Convert to RGB mode (required for JPEG)
            rgb_img = img.convert('RGB')
            
            # Save with maximum possible quality
            rgb_img.save(
                jpeg_path,
                format='JPEG',
                quality=100,  # Maximum quality
                subsampling=0,  # Best color subsampling
                optimize=True   # Optimize the file size without quality loss
            )
            
        print_color(f"✓ Converted: {heic_file.name}")
        return (True, heic_file.name)
     
    except Exception as e:
        print_color(f"✗ Error converting {heic_file.name}: {str(e)}", "red")
        return (False, heic_file.name)


def convert_heic_to_jpeg(input_path, output_folder):
    """
    Batch convert all HEIC files in a directory to JPEG with parallel processing.
    
    Args:
        input_path: Directory containing HEIC files
        output_folder: Name of folder to create for output (inside input_path)
    """
    # Register the HEIC file format with Pillow
    register_heif_opener()
     
    # Validate input path
    input_dir = Path(input_path).resolve()
    if not input_dir.exists():
        print_color(f"Input directory not found: {input_dir}", "red")
        return
     
    # Create output directory inside input folder
    output_dir = input_dir / output_folder
    output_dir.mkdir(parents=True, exist_ok=True)
     
    # Find all HEIC files (case insensitive)
    heic_files = list(input_dir.rglob('*.[Hh][Ee][Ii][Cc]'))
    if not heic_files:
        print_color("No HEIC files found in the directory.", "yellow")
        return
     
    print_color(f"Found {len(heic_files)} HEIC files to convert...", "blue")
     
    # Determine the optimal number of workers based on CPU cores
    max_workers = min(32, os.cpu_count() or 4)  # Limiting to 32 even on high-core systems
    
    # Process files in parallel for better performance
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        results = list(executor.map(
            lambda f: convert_single_heic(f, input_dir, output_dir),
            heic_files
        ))
     
    # Count results
    converted = sum(1 for success, _ in results if success)
    errors = len(results) - converted
     
    # Final report with color-coded summary
    print("\n" + "-" * 50)
    print_color(f"Conversion complete!", "blue")
    print_color(f"✓ Successfully converted: {converted}", "green")
    
    if errors > 0:
        print_color(f"✗ Files with errors: {errors}", "red")
        print_color("\nCheck error messages above for problematic files", "yellow")
    
    print_color(f"\nYour converted images are in: {output_dir}", "blue")
    print("-" * 50)


def main():
    """Main function to run the converter with a friendly interface."""
    print("\n" + "=" * 60)
    print_color("  HEIC to JPEG Photo Converter", "blue")
    print("=" * 60)
    print("This tool converts Apple HEIC photos to standard JPEG format\n"
          "while preserving the highest possible quality.\n")
    
    # Get default input directory (user's pictures folder if possible)
    if os.name == "nt":  # Windows
        default_input = os.path.join(os.path.expanduser("~"), "Pictures")
    else:  # macOS/Linux
        default_input = os.path.join(os.path.expanduser("~"), "Pictures")
    
    # Fall back to current directory if Pictures doesn't exist
    if not os.path.exists(default_input):
        default_input = os.getcwd()
     
    # Get input from user
    print_color("Please specify your folders:", "yellow")
    input_folder = input(f"Enter folder with HEIC photos [default: {default_input}]: ").strip()
    input_folder = input_folder if input_folder else default_input
     
    output_folder = input("Name for the output folder [default: JPEG_Output]: ").strip() or "JPEG_Output"
    
    print("\nStarting conversion...")
    convert_heic_to_jpeg(input_folder, output_folder)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print_color("\n\nConversion cancelled by user.", "yellow")
    except Exception as e:
        print_color(f"\nUnexpected error: {str(e)}", "red")
        print("If the problem persists, please report this issue on GitHub.")
    
    # On Windows, keep the window open if run by double-clicking
    if os.name == "nt" and not sys.stdout.isatty():
        input("\nPress Enter to exit...")
