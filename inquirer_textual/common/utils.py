import sys


def get_cursor_row() -> int | None:
    if sys.platform == 'win32':
        return _get_cursor_row_windows()
    else:
        return _get_cursor_row_unix()


def _get_cursor_row_windows() -> int | None:
    import ctypes
    class COORD(ctypes.Structure):
        _fields_ = [("X", ctypes.c_short), ("Y", ctypes.c_short)]

    class SMALL_RECT(ctypes.Structure):
        _fields_ = [("Left", ctypes.c_short), ("Top", ctypes.c_short),
                    ("Right", ctypes.c_short), ("Bottom", ctypes.c_short)]

    class CONSOLE_SCREEN_BUFFER_INFO(ctypes.Structure):
        _fields_ = [("dwSize", COORD),
                    ("dwCursorPosition", COORD),
                    ("wAttributes", ctypes.c_ushort),
                    ("srWindow", SMALL_RECT),
                    ("dwMaximumWindowSize", COORD)]

    STD_OUTPUT_HANDLE = -11
    h = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
    csbi = CONSOLE_SCREEN_BUFFER_INFO()
    ctypes.windll.kernel32.GetConsoleScreenBufferInfo(h, ctypes.byref(csbi))
    return csbi.dwCursorPosition.Y + 1


def _get_cursor_row_unix() -> int | None:
    import termios
    import tty
    try:
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            sys.stdout.write('\033[6n')
            sys.stdout.flush()
            response = ''
            while True:
                char = sys.stdin.read(1)
                response += char
                if char == 'R':
                    break
            row, col = response[2:-1].split(';')
            return int(row)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    except (termios.error, OSError):
        return None
