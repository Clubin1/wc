import os
import sys

# TODO add support for reading from stdin
class WC:
    def __init__(self, args):
        self.flag = None
        self.file = None
        self.allowed_flags = {'-c', '--bytes', '-l', '--lines', '-w', '--words', '-m', '--chars'}
        self._parse_args(args)

    def count_bytes(self):
        """Count the number of bytes in a file"""
        file_size = os.path.getsize(self.file)
        print(f"{file_size} bytes in {self.file}")

    def count_lines(self):
        """Count the number of lines in a file"""
        try:
            with open(self.file, "r") as file:
                lines = file.readlines()
                print(f"{len(lines)} lines in {self.file}")
        except FileNotFoundError:
            print(f"File not found: {self.file}")

    def count_words(self):
        """Count the number of words in a file"""
        try:
            with open(self.file, "r") as file:
                content = file.read()
                words = content.split()
                print(f"{len(words)} words in {self.file}")
        except FileNotFoundError:
            print(f"File not found: {self.file}")

    def count_chars(self):
        """Count the number of characters in a file"""
        try:
            with open(self.file, "r") as file:
                content = file.read()
                print(f"{len(content)} characters in {self.file}")
        except FileNotFoundError:
            print(f"File not found: {self.file}")

    def _parse_args(self, args):
        """Parse the command line arguments and run the appropriate function"""
        if len(args) == 1 and os.path.isfile(args[0]):
            self.file = args[0]
            self.count_bytes()
            self.count_lines()
            self.count_words()
            self.count_chars()
            return

        if len(args) < 2 or args[0] not in self.allowed_flags or not os.path.isfile(args[1]):
            self._print_usage()
            return

        self.flag = args[0]
        self.file = args[1]

        if self.flag in {"-c", "--bytes"}:
            self.count_bytes()
        elif self.flag in {"-l", "--lines"}:
            self.count_lines()
        elif self.flag in {"-w", "--words"}:
            self.count_words()
        elif self.flag in {"-m", "--chars"}:
            self.count_chars()

    def _print_usage(self):
        """Utility function to print the usage message"""
        print("Usage: wc [options] [file]")
        print("Options:")
        print("  -c, --bytes    Count the number of bytes in a file")
        print("  -l, --lines    Count the number of lines in a file")
        print("  -w, --words    Count the number of words in a file")
        print("  -m, --chars    Count the number of characters in a file")

def main():
    args = sys.argv[1:]
    wc = WC(args)

if __name__ == "__main__":
    main()
