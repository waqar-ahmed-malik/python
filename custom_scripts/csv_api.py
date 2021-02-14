import csv


class ProcessCSV:
    def __init__(self, csv_file_path: str):
        self.csv_file_path = csv_file_path

    def clean_csv(self, clean_csv_file_path: str):
        with open(self.csv_file_path, 'r') as f:
            row_skips = 0
            reader = csv.reader(f)
            for row in reader:
                if len(''.join(row)) == 0:
                    row_skips += 1
                else:
                    break
            f.seek(0)
            column_count = len(next(reader))
            valid_column_indices = []
            for i in range(column_count):
                f.seek(0)
                if len(''.join([row[i] for row in reader])) == 0:
                    continue
                else:
                    valid_column_indices.append(i)
            f.seek(0)
            for row in reader:
                if (max(valid_column_indices) - min(valid_column_indices)) + 1 == len(list(set(row[min(valid_column_indices): max(valid_column_indices) + 1]))):
                    break
                else:
                    row_skips += 1
            f.seek(0)
            for i in range(row_skips):
                next(reader)
            with open(clean_csv_file_path, 'w') as cf:
                writer = csv.writer(cf)
                for row in reader:
                    writer.writerow(row[min(valid_column_indices): max(valid_column_indices) + 1])