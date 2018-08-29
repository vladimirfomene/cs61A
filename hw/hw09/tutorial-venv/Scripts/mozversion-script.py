#!C:\Users\TempUser\Desktop\cs61A\hw\hw09\tutorial-venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'mozversion','console_scripts','mozversion'
__requires__ = 'mozversion'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('mozversion', 'console_scripts', 'mozversion')()
    )
