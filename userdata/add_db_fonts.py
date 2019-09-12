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


def add_db_fonts():
    green("Adding DB fonts...")

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

    windows_fonts_path = os.path.join('C:', 'Windows', 'Fonts')
    os.mkdir(Path() / 'lib' / 'fonts' / 'db')
    for item in font_files:
        src, dst = os.path.join(windows_fonts_path, item), (
                    Path() / 'lib' / 'fonts' / 'db' / font_files[item]).resolve()
        if os.path.isfile(src) and not os.path.exists(dst):
            blue(f'Copying {src} to {dst}')
            shutil.copy(src, dst)
        else:
            blue(f'File "{dst.stem}" already exists, skipping')

    green('Copied all DB fonts')


if __name__ == '__main__':
    add_db_fonts()
