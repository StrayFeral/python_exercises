#!/usr/bin/env python

import csv
from pprint import pprint


class LongCSVFileReader:
    """Long CSV file reader.
    2023, Evgueni.Antonov@gmail.com

    This is a generator pipeline, made of two generator
    comprehensions. I made this as an exercise in generator
    functions. This is the memory efficient way to read
    long files.
    """

    def __init__(self, filename, header: bool = True, delimiter: str = ","):
        self._filename = filename
        self._header = header
        self._delimiter = delimiter

    def read(self):
        rows = (row for row in open(self._filename, "r"))
        parsed_rows = (csv.reader([row], delimiter=self._delimiter) for row in rows)

        # Getting the header
        if self._header:
            parsed_row = next(parsed_rows)
            csv_header = list(parsed_row)

        for parsed_row in parsed_rows:
            data = list(parsed_row)
            row = data[0]

            if self._header:
                row = dict(zip(csv_header[0], data[0]))

            yield row


if __name__ == "__main__":
    reader = LongCSVFileReader("techcrunch.csv")
    for row in reader.read():
        pprint(row)
