import csv
import sys

with open("raw_test.tsv", "r", encoding="utf-8") as f:
    reader = csv.reader(f, delimiter="\t")
    lines = []
    for line in reader:
        if sys.version_info[0] == 2:
            line = list(unicode(cell, 'utf-8') for cell in line)
        lines.append(line[-2:])
    with open("test.tsv", "w", encoding="utf-8") as f:
        writer = csv.writer(f, delimiter="\t", lineterminator="\n")
        for line in lines:
            writer.writerow(line)


