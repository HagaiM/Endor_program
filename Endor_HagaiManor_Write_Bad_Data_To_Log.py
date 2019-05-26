import csv

def is_number(s):
    try:
        float(s)
        return s
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass






def write_to_log_bad_data(source_file,log_file):
    with open(source_file) as f:
        reader = csv.reader(f)
        # writer = csv.writer(f)
        for row in reader:
            if is_number(row[1]) is None:
                print(row[0],row[1])
                #writer.writerow(row)
                with open(log_file, "a") as myfile:
                    myfile.write(row[0]+','+row[1] + "\n")


source_file = "/Users/hagaimanor/Downloads/ETH_USD.csv"
log_file = '/Users/hagaimanor/Downloads/ETH_USD_agg_log.csv'
write_to_log_bad_data(source_file,log_file)

