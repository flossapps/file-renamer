# Compilation mode, support OS-specific options
# nuitka-project-if: {OS} in ("Windows", "Linux", "Darwin", "FreeBSD"):
#    nuitka-project: --onefile
# nuitka-project-else:
#    nuitka-project: --mode=standalonealone

# The PySide6 plugin covers qt-plugins
# nuitka-project: --enable-plugin=pyside6
# nuitka-project: --include-qt-plugins=qml

from file_renamer.cli import main

if __name__ == "__main__":
    main()
