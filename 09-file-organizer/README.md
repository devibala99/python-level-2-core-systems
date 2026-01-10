# File Organizer Script (CLI)

## Type

Automation / File System Utility

## Description

A command-line tool that organizes files inside a given folder into
subfolders based on file type (images, documents, videos, etc.).
It supports a dry-run preview before making actual file changes.

## Features

- Scan files in a folder
- Classify files by extension
- Preview movements (dry run)
- Organize files safely
- Prevent file overwriting

## Concepts Used

- File system operations (os, shutil)
- Rule-based classification
- Functions & modular design
- Defensive programming
- CLI menu handling

## How to Run

1. Place `main.py` and `utils.py` in the same folder
2. Run:
   main.py
3. Enter the folder path to organize
4. Choose dry-run or organize option
