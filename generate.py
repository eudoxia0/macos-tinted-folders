import subprocess
from pathlib import Path
import shutil

COLOURS = {
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

def main():
    Path("output").mkdir(exist_ok=True)
    copy_generic_icns()
    explode_icns()
    for name, colour in COLOURS.items():
        generate(name, colour)

def copy_generic_icns():
    print("Copying GenericFolderIcon.icns")
    src = Path("/System/Library/CoreServices/CoreTypes.bundle/Contents/Resources/GenericFolderIcon.icns")
    dst = Path("GenericFolderIcon.icns")
    shutil.copyfile(src, dst)

def explode_icns():
    print("Exploding .icns")
    subprocess.run(['iconutil', '-c', 'iconset', 'GenericFolderIcon.icns'])

def implode_icns(iconset: Path):
    subprocess.run([
        'iconutil',
        '-c', 'icns',
        str(iconset)
    ])

def generate(name: str, colour: str):
    print(f"Generating {name}.icns")
    # Create .iconset directory
    dirname = name + ".iconset"
    iconset_dir = Path("output") / dirname
    iconset_dir.mkdir(exist_ok=True)
    source_dir = Path("GenericFolderIcon.iconset")
    # Convert each .png
    for png_file in source_dir.glob("*.png"):
        subprocess.run([
            'magick',
            str(png_file),
            '-modulate', '100,0,100',
            '-fill', colour,
            '-colorize', '70',
            str(iconset_dir / png_file.name)
        ])
    # Implode the .iconset directory into an .icns file
    implode_icns(iconset_dir)
    # Delete the .iconset directory
    shutil.rmtree(Path("output") / dirname)

if __name__ == "__main__":
    main()
