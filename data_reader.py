import os
import hashlib
from parser import get_aggregate_numbers_from_file

DIRNAME = 'csse_covid_19_daily_reports'


def get_all_data_files_in_order():
    filelist = sorted(os.listdir(DIRNAME))
    filelist = filter(lambda f: f[-4:] == '.csv',
                      filelist)  # filter for csv files
    return filelist


def hash_file_content(filepath):
    m = hashlib.sha256()
    with open(filepath) as f:
        m.update(f.read().encode('utf-8'))
    return m.hexdigest()


def show_time_series_of_aggregates():
    filepaths = get_all_data_files_in_order()
    filepaths = [os.path.join(DIRNAME, f) for f in filepaths]
    timeseries = []
    hashes = []

    for filepath in filepaths:
        filehash = hash_file_content(filepath)
        aggregate = get_aggregate_numbers_from_file(filepath)
        timeseries.append(aggregate)
        hashes.append(filehash)
    print(timeseries)
    print(hashes)


if __name__ == '__main__':
    show_time_series_of_aggregates()
