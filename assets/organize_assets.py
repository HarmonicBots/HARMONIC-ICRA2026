#!/usr/bin/env python3
"""
Asset Organization Script for HARMONIC ICRA 2026
This script helps organize and validate assets for the webpage.
"""

import os
import sys
from pathlib import Path

def check_directory_structure():
    """Check if the required directory structure exists."""
    required_dirs = [
        "assets/images/architecture",
        "assets/images/results", 
        "assets/videos/demos",
        "assets/files/papers"
    ]
    
    missing_dirs = []
    for dir_path in required_dirs:
        if not os.path.exists(dir_path):
            missing_dirs.append(dir_path)
    
    if missing_dirs:
        print("❌ Missing directories:")
        for dir_path in missing_dirs:
            print(f"   - {dir_path}")
        return False
    else:
        print("✅ All required directories exist")
        return True

def check_expected_files():
    """Check for expected files in each directory."""
    expected_files = {
        "assets/images/architecture": [
            "harmonic_architecture.png",
            "ontoagent_diagram.png", 
            "behavior_tree_diagram.png"
        ],
        "assets/images/results": [
            "evaluation_metrics.png",
            "performance_charts.png"
        ],
        "assets/videos/demos": [
            "main_demo.mp4",
            "tactical_demo.mp4",
            "evaluation_demo.mp4"
        ],
        "assets/files/papers": [
            "paper.pdf",
            "supplementary.pdf",
            "bibtex.txt"
        ]
    }
    
    missing_files = []
    for directory, files in expected_files.items():
        for file in files:
            file_path = os.path.join(directory, file)
            if not os.path.exists(file_path):
                missing_files.append(file_path)
    
    if missing_files:
        print("⚠️  Missing expected files:")
        for file_path in missing_files:
            print(f"   - {file_path}")
    else:
        print("✅ All expected files present")
    
    return len(missing_files) == 0

def get_file_sizes():
    """Get file sizes for optimization checking."""
    print("\n📊 File sizes:")
    
    for root, dirs, files in os.walk("assets"):
        for file in files:
            if file.endswith(('.png', '.jpg', '.mp4', '.pdf')):
                file_path = os.path.join(root, file)
                size = os.path.getsize(file_path)
                size_mb = size / (1024 * 1024)
                
                status = "✅" if size_mb < 10 else "⚠️"
                print(f"   {status} {file_path}: {size_mb:.1f} MB")

def main():
    """Main function to run all checks."""
    print("🔍 HARMONIC ICRA 2026 - Asset Organization Check")
    print("=" * 50)
    
    # Check directory structure
    if not check_directory_structure():
        print("\n💡 Run this script from the project root directory")
        return
    
    # Check expected files
    check_expected_files()
    
    # Get file sizes
    get_file_sizes()
    
    print("\n📝 Next steps:")
    print("1. Add your media files to the appropriate directories")
    print("2. Update the file paths in index.html")
    print("3. Optimize file sizes for web delivery")
    print("4. Test all links and media files")

if __name__ == "__main__":
    main()
