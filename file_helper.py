import csv
import datetime

def dictionary_list_to_csv(dict_list):
    print(dict_list[0])
    keys = dict_list[0].keys()
    csvfile = get_csv_file_name()
    with open(csvfile, "w") as output:
        writer = csv.DictWriter(output, fieldnames=keys, lineterminator='\n')
        writer.writeheader()
        writer.writerows(dict_list)

def get_csv_file_name():
    now = datetime.datetime.now()
    csv_file_name = "csv/anunciosOLX" + str(now.year) + "-" + str(now.month) + "-" + str(now.day) + "_" + str(now.hour) + "h" + str(now.minute) + "min" + str(now.second) + "s" + ".csv"
    return csv_file_name