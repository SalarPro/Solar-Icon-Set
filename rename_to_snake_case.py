#!/usr/bin/env python3
"""
Script to recursively copy and rename all folders and files to snake_case format.
Names will start with [a-z] and contain only [a-z0-9_] characters.
Creates a copy in a "snake_case/" folder instead of modifying originals.
"""

import os
import re
import shutil
from pathlib import Path


def to_snake_case(name):
    """
    Convert a string to snake_case format.
    - Only keeps letters, digits, and converts spaces/special chars to underscores
    - Ensures it starts with a lowercase letter
    - Results in only [a-z][0-9_] characters
    """
    # Get the file extension if it exists
    base_name = name
    extension = ""
    if '.' in name:
        parts = name.rsplit('.', 1)
        base_name = parts[0]
        extension = parts[1] if len(parts) > 1 else ""
    
    # Replace common separators with spaces first
    base_name = base_name.replace(',', ' ')
    base_name = base_name.replace('-', ' ')
    base_name = base_name.replace('_', ' ')
    
    # Remove any non-alphanumeric characters except spaces
    base_name = re.sub(r'[^a-zA-Z0-9\s]', '', base_name)
    
    # Convert to lowercase and replace spaces with underscores
    base_name = base_name.lower()
    base_name = re.sub(r'\s+', '_', base_name)
    
    # Remove leading/trailing underscores
    base_name = base_name.strip('_')
    
    # Ensure it starts with a letter (if it starts with a digit, prefix with 'n')
    if base_name and base_name[0].isdigit():
        base_name = 'n' + base_name
    
    # If base_name is empty, use a default
    if not base_name:
        base_name = 'unnamed'
    
    # Reconstruct with extension if it exists
    if extension:
        # Also convert extension to lowercase
        extension = extension.lower()
        return f"{base_name}.{extension}"
    
    return base_name


def copy_and_rename_recursively(root_path, output_folder="snake_case", dry_run=True):
    """
    Recursively copy all folders and files to snake_case format.
    Creates a new folder structure with renamed items.
    
    Args:
        root_path: Path to the root directory to process
        output_folder: Name of the output folder to create
        dry_run: If True, only print what would be copied without actually copying
    """
    root_path = Path(root_path)
    
    if not root_path.exists():
        print(f"Error: Path {root_path} does not exist")
        return
    
    # Create output directory at the same level as root_path
    output_path = root_path.parent / output_folder
    
    if output_path.exists() and not dry_run:
        print(f"⚠️  Output folder {output_path} already exists.")
        response = input("Do you want to delete it and continue? (yes/no): ")
        if response.lower() != 'yes':
            print("Operation cancelled.")
            return
        shutil.rmtree(output_path)
        print(f"Deleted existing {output_path}\n")
    
    copied_count = 0
    
    print(f"{'DRY RUN - ' if dry_run else ''}Processing files and folders...\n")
    
    # Walk through the directory tree
    for dirpath, dirnames, filenames in os.walk(root_path):
        dirpath = Path(dirpath)
        
        # Calculate the relative path from root
        rel_path = dirpath.relative_to(root_path)
        
        # Convert each part of the path to snake_case
        new_rel_parts = [to_snake_case(part) for part in rel_path.parts]
        new_rel_path = Path(*new_rel_parts) if new_rel_parts else Path('.')
        
        # Create the target directory path
        target_dir = output_path / new_rel_path
        
        # Create the directory if not in dry run mode
        if not dry_run:
            target_dir.mkdir(parents=True, exist_ok=True)
        
        # Copy and rename files
        for filename in filenames:
            old_file = dirpath / filename
            new_filename = to_snake_case(filename)
            target_file = target_dir / new_filename
            
            copied_count += 1
            
            if dry_run:
                print(f"Would copy: {old_file.relative_to(root_path.parent)}")
                print(f"        to: {target_file.relative_to(root_path.parent)}\n")
            else:
                try:
                    shutil.copy2(old_file, target_file)
                    print(f"✓ Copied: {old_file.relative_to(root_path.parent)}")
                    print(f"      to: {target_file.relative_to(root_path.parent)}\n")
                except Exception as e:
                    print(f"✗ Error copying {old_file}: {e}\n")
    
    print(f"\n{'Would copy' if dry_run else 'Copied'} {copied_count} files")
    
    if dry_run:
        print("\n" + "="*60)
        print("This was a DRY RUN. No files were actually copied.")
        print("To apply changes, run the script with dry_run=False")
        print("="*60)
    else:
        print(f"\n✓ All files copied to: {output_path}")


if __name__ == "__main__":
    # Path to the SVG directory
    svg_path = "/Users/salarpro/GitHub/Solar-Icon-Set/icons/SVG"
    
    # First, do a dry run to preview changes
    # print("="*60)
    # print("PREVIEW MODE - Showing what will be copied")
    # print("="*60 + "\n")
    # copy_and_rename_recursively(svg_path, output_folder="snake_case", dry_run=True)
    
    # Uncomment the following lines to actually perform the copying:
    print("\n\n" + "="*60)
    print("APPLYING CHANGES - Copying to solar/")
    print("="*60 + "\n")
    copy_and_rename_recursively(svg_path, output_folder="solar", dry_run=False)
