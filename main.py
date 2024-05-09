import os
import sys

# TODO: Finish supporting running all functions on stdin
# TODO: Clean function code up by making a count helper that uses a lambda
class WC:
    def __init__(self, args):
        self.flag = None
        self.file = None
        self.allowed_flags = {'-c', '--bytes', '-l',
                              '--lines', '-w', '--words', '-m', '--chars'}
        self._parse_args(args)

    def count_bytes(self):
        """Count the number of bytes in a file"""
        if self.file is None:
            content = sys.stdin.read()
            print(f"{len(content)} bytes")
        else:
            file_size = os.path.getsize(self.file)
            print(f"{file_size} bytes in {self.file}")

    def count_lines(self):
        """Count the number of lines in a file or from stdin"""
        try:
            if self.file is None:
                lines = sys.stdin.readlines()
            else:
                with open(self.file, "r") as file:
                    lines = file.readlines()
            print(f"{len(lines)} lines")
        except FileNotFoundError:
            print(f"File not found: {self.file}")

    def count_words(self):
        """Count the number of words in a file or from stdin"""
        try:
            if self.file is None:
                content = sys.stdin.read()
            else:
                with open(self.file, "r") as file:
                    content = file.read()
            words = content.split()
            print(f"{len(words)} words")
        except FileNotFoundError:
            print(f"File not found: {self.file}")

    def count_chars(self):
        """Count the number of characters in a file or from stdin"""
        try:
            if self.file is None:
                content = sys.stdin.read()
            else:
                with open(self.file, "r") as file:
                    content = file.read()
            print(f"{len(content)} characters")
        except FileNotFoundError:
            print(f"File not found: {self.file}")

    def _parse_args(self, args):
        """Parse the command line arguments and run the appropriate function"""
        if not sys.stdin.isatty():
            self.file = None
            if len(args) == 0:
                self._run_all()
            elif len(args) == 1 and args[0] in self.allowed_flags:
                self.flag = args[0]
                self._run_by_flag()
            else:
                self._print_usage()
            return

        if len(args) == 1 and os.path.isfile(args[0]):
            self.file = args[0]
            self._run_all()
            return

        if len(args) < 2 or args[0] not in self.allowed_flags or not os.path.isfile(args[1]):
            self._print_usage()
            return

        self.flag = args[0]
        self.file = args[1]

        self._run_by_flag()

    def _run_all(self):
        """Run all the functions"""
        self.count_bytes()
        self.count_lines()
        self.count_words()
        self.count_chars()

    def _print_usage(self):
        """Utility function to print the usage message"""
        print("Usage: wc [options] [file]")
        print("Options:")
        print("  -c, --bytes    Count the number of bytes in a file")
        print("  -l, --lines    Count the number of lines in a file")
        print("  -w, --words    Count the number of words in a file")
        print("  -m, --chars    Count the number of characters in a file")

    def _run_by_flag(self):
        """Run the function based on the flag"""
        if self.flag in {"-c", "--bytes"}:
            self.count_bytes()
        elif self.flag in {"-l", "--lines"}:
            self.count_lines()
        elif self.flag in {"-w", "--words"}:
            self.count_words()
        elif self.flag in {"-m", "--chars"}:
            self.count_chars()


def main():
    args = sys.argv[1:]
    wc = WC(args)


if __name__ == "__main__":
    main()
