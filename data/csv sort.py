import csv

with open("daily_sales_data_0.csv", "r") as file1, \
     open("daily_sales_data_1.csv", "r") as file2, \
     open("daily_sales_data_2.csv", "r") as file3, \
     open("../output.csv", "w", newline="") as outfile:
    reader = csv.reader(file1)
    reader2 = csv.reader(file2)
    reader3 = csv.reader(file3)
    writer = csv.writer(outfile)
    writer.writerow(["Sales", "Date", "Region"])

    for row in reader:
        if row[0] == "pink morsel":
            total_profit = float(row[1][1:]) * float(row[2])

            writer.writerow([

                "$"+str(total_profit),
                row[3],
                row[4]
            ])
    for row in reader2:
        if row[0] == "pink morsel":
            total_profit = float(row[1][1:]) * float(row[2])

            writer.writerow([
                "$"+str(total_profit),
                row[3],
                row[4]
            ])
    for row in reader3:
        if row[0] == "pink morsel":
            total_profit = float(row[1][1:]) * float(row[2])

            writer.writerow([
                "$"+str(total_profit),
                row[3],
                row[4]
            ])