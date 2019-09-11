import os
import shutil
from pathlib import Path

from colorama import ansi


def green(text):
    print(ansi.Fore.GREEN + text + ansi.Fore.RESET)


def blue(text):
    print(ansi.Fore.CYAN + text + ansi.Fore.RESET)


def red(text):
    print(ansi.Fore.RED + text + ansi.Fore.RESET)


windows_fonts_path = os.path.join('C:', 'Windows', 'Fonts')
for item in os.listdir(windows_fonts_path):
    src, dst = os.path.join(windows_fonts_path, item), (Path() / 'lib' / 'fonts' / 'db').resolve()
    if os.path.isfile(src) and item.startswith('db'):
        blue(f'Copying {src} to {dst}')
        shutil.copy(src, dst)

green('Copied all db fonts')

fonts = {
    'dbhea': {
        '07': 'Head_Black',
        '37': 'Head_Italic_Black',
        '03': 'Head',
        '33': 'Head_Italic',
    },
    'dbsan': {
        '03': 'Sans',
        '06': 'Sans_Bold',
        '33': 'Sans_Italic',
        '37': 'Sans_Bold_Italic',
    }
}

font_files = {}

for name_prefix, items in fonts.items():
    for number, font_name in items.items():
        font_files.update({name_prefix + number + '.ttf': 'DB_' + font_name + '.ttf'})

fonts_path = os.path.join('lib', 'fonts', 'db')

for ffile in font_files:
    blue(f'Renaming {ffile} to {font_files[ffile]}')
    os.rename(os.path.join(fonts_path, ffile), os.path.join(fonts_path, font_files[ffile]))

green(f'Renamed font files')

for file in os.listdir(fonts_path):
    if not file.startswith('DB'):
        blue(f'Removing unused font file {file}' + ansi.Fore.RESET)
        if os.path.isfile(os.path.join(fonts_path, file)):
            os.remove(os.path.join(fonts_path, file))

green('Removed unused font files')
