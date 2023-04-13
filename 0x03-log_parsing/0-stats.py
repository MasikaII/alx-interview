#!/usr/bin/python3
"""
Log parsing
"""

import sys

if __name__ == '__main__':

    filesize = 0
    counter = 0
    codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    stats = {key: 0 for key in codes}

    def print_stats(stats: dict, file_size: int) -> None:
        """A function for outputting stats"""
        print("File size: {:d}".format(filesize))
        for key, value in sorted(stats.items()):
            if value:
                print("{}: {}".format(key, value))

    try:
        for input in sys.stdin:
            counter += 1
            parsed = input.split()
            try:
                status_code = parsed[-2]
                if status_code in stats:
                    stats[status_code] += 1
            except BaseException:
                pass
            try:
                filesize += int(parsed[-1])
            except BaseException:
                pass
            if counter % 10 == 0:
                print_stats(stats, filesize)
        print_stats(stats, filesize)
    except KeyboardInterrupt:
        print_stats(stats, filesize)
        raise
