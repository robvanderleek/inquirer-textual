import sys


def get_cursor_row() -> int | None:
    if sys.platform == 'win32':
        from ctypes import windll, byref, Structure, c_short, c_ushort
        class COORD(Structure):
            _fields_ = [("X", c_short), ("Y", c_short)]

        class SMALL_RECT(Structure):
            _fields_ = [("Left", c_short), ("Top", c_short),
                        ("Right", c_short), ("Bottom", c_short)]

        class CONSOLE_SCREEN_BUFFER_INFO(Structure):
            _fields_ = [("dwSize", COORD),
                        ("dwCursorPosition", COORD),
                        ("wAttributes", c_ushort),
                        ("srWindow", SMALL_RECT),
                        ("dwMaximumWindowSize", COORD)]

        STD_OUTPUT_HANDLE = -11
        h = windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
        csbi = CONSOLE_SCREEN_BUFFER_INFO()
        windll.kernel32.GetConsoleScreenBufferInfo(h, byref(csbi))
        return csbi.dwCursorPosition.Y + 1
    else:
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
