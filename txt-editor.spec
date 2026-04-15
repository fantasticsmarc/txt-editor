# PyInstaller spec for TXT Editor
a=Analysis(['main.py'])
exe=EXE(a.pure,a.scripts,name='txt-editor',console=False)
