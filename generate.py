import subprocess
from pathlib import Path
import shutil

COLORS = {
    # Greens
    'mint': '#00FF80',
    'forest': '#008040',
    'sage': '#90B790',
    'emerald': '#50C878',

    # Warm colors
    'rose': '#FF4080',
    'sunset': '#FF8000',
    'coral': '#FF7F50',
    'peach': '#FFCBA4',
    'crimson': '#DC143C',

    # Blues and Purples
    'violet': '#8040FF',
    'ocean': '#0077BE',
    'sky': '#87CEEB',
    'indigo': '#4B0082',
    'periwinkle': '#CCCCFF',

    # Earth tones
    'coffee': '#6F4E37',
    'sienna': '#A0522D',
    'khaki': '#C3B091',
    'sand': '#F4A460',

    # Misc
    'teal': '#008080',
    'mauve': '#E0B0FF',
    'burgundy': '#800020',
    'slate': '#708090',
}

def convert_icon(input_path: str, output_name: str, color: str):
    """Convert a single icon with the given color"""
    output_path = Path(f"output/{output_name}.png")
    # First desaturate, then apply color
    subprocess.run([
        'magick',
        input_path,
        '-modulate', '100,0,100',  # Remove saturation but keep brightness
        '-fill', color,
        '-colorize', '70',         # More aggressive color application
        str(output_path)
    ])
    print(f"Created {output_path} with color {color}")

def copy_generic_icns():
    src = Path("/System/Library/CoreServices/CoreTypes.bundle/Contents/Resources/GenericFolderIcon.icns")
    dst = Path("GenericFolderIcon.icns")
    shutil.copy2(src, dst)

def main():
    copy_generic_icns()
    input_path = "icon.png"

    for name, color in COLORS.items():
        convert_icon(input_path, name, color)

if __name__ == "__main__":
    main()
