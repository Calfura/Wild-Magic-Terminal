import csv
import d20

# Wild Magic Test sample
def wild_magic(file_name):
    with open(file_name) as f:
        reader = csv.reader(f)
        sample_roll = d20.roll("d20")
        sample_num = (f"{sample_roll.total}")
        
        for row in reader:
            if (sample_num == row[0]):
                print(f"{row[0]} - {row[1]} | {row[2]}")
                if row[3] != "0":
                    # Convert into f-string to allow d20 to pull from CSV file
                    num = (f"{row[3]}")
                    # Rolls from predetermine list inside CSV file
                    r = d20.roll(num)
                    print(r.total)
                break
            elif (sample_num == row[1]):
                print(f"{row[0]} - {row[1]} | {row[2]}")
                if row[3] != "0":
                    # Convert into f-string to allow d20 to pull from CSV file
                    num = (f"{row[3]}")
                    # Rolls from predetermine list inside CSV file
                    r = d20.roll(num)
                    print(r)
                break
