
import copy
import csv


def parse_csv_with_headers(filepath):
    with open(filepath, newline='') as csvfile:
        cases_reader = csv.reader(csvfile, delimiter=',')
        headers = []
        all_rows = []

        for row_index, row in enumerate(cases_reader):
            if row_index == 0:
                headers = copy.copy(row)
            else:
                row_object = {}
                for col_index, column in enumerate(row):
                    row_object[headers[col_index]] = column
                all_rows.append(row_object)
        return all_rows


def get_aggregate_numbers(reports_by_area):
    total_confirmed = 0
    total_deaths = 0
    total_recovered = 0

    for report in reports_by_area:
        try:
            if report['Confirmed'] != '':
                total_confirmed += int(report['Confirmed'])
            if report['Deaths'] != '':
                total_deaths += int(report['Deaths'])
            if report['Recovered'] != '':
                total_recovered += int(report['Recovered'])
        except:
            import pdb
            pdb.set_trace()

    return total_confirmed, total_deaths, total_recovered


def get_aggregate_numbers_from_file(filepath):
    reports = parse_csv_with_headers(filepath)
    return get_aggregate_numbers(reports)


def print_aggregate():
    reports = parse_csv_with_headers('data.csv')
    print(get_aggregate_numbers(reports))


if __name__ == '__main__':
    print_aggregate()
