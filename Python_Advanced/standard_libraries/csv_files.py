import  csv

# Writing
with open("data.cvs", "w") as f:
    writer = csv.writer(f)
    writer.writerow(["transaction_id", "product_id", "price"])
    writer.writerow([1500, 2, 9])
    writer.writerow([1800, 32, 19])

# Reading
with open("data.cvs") as f:
    reader = csv.reader(f)
    # print(list(reader))
    for row in reader:
        print(row)