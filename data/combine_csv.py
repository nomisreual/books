import glob
import pandas as pd

# Combines present csv files.
# Caution: loads every file as dataframe into memory.


def main():

    # List of all CSV files:
    csv_files = glob.glob("*.csv")

    # For not combining previous concats:
    try:
        csv_files.remove("data.csv")
    except ValueError:
        print("A combined file is not present. Nothing to remove.")

    df_csv = pd.concat([pd.read_csv(file) for file in csv_files],
                       ignore_index=True)

    df_csv.to_csv("./data.csv", index=False)


if __name__ == "__main__":
    main()
