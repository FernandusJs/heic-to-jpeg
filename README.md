# HEIC to JPEG Converter

This script converts HEIC image files to JPEG format.

## Prerequisites

- Python 3.x
- Required libraries: `os`, `pyheif`, `PIL`

## Installation

No installation required. Just make sure you have the necessary libraries installed.

## Usage

1. Place your HEIC files in a directory.
2. Run the script and provide the path to that directory by editing the script.


3. The script will convert all HEIC files in the directory to JPEG format.

## Notes

- The pyheif library only functions on linux based systems.
- Only files with the `.heic` extension will be converted.
- Converted JPEG files will have the same name as the original HEIC files but with the `.jpg` extension.
- The script does not delete the original HEIC files.
