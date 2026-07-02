import pandas as pd
import glob
from datetime import datetime
import os

#Select one of the three functions defined below:
    #combine_csv(), combine_txt(), combine_xlsx()
#adjust the skiprow depending on your data (below, sr)
sr=0 

def combine_csv(output_filename=None, keywords=("Distance", "F Series")):
    files = sorted(glob.glob("*.csv"))
    combined_df = pd.DataFrame()

    if len(files) == 0:
        print("No .csv files found")
        return

    keywords_lower = [keyword.lower() for keyword in keywords]

    for file in files:
        df = pd.read_csv(file, skiprows=sr)
        selected_cols = [
            col for col in df.columns
            if any(keyword in str(col).lower() for keyword in keywords_lower)
        ]

        if len(selected_cols) == 0:
            print(f"Skipped {file}: no matching columns")
            continue

        df = df[selected_cols]
        filename_row = pd.DataFrame([[file] * df.shape[1]], columns=df.columns)
        header_row = pd.DataFrame([df.columns], columns=df.columns)
        temp_df = pd.concat([filename_row, header_row, df], ignore_index=True)
        combined_df = pd.concat([combined_df, temp_df], axis=1)

    if combined_df.empty:
        print("No matching columns found in any CSV files")
        return

    nn = os.path.splitext(files[0])[0]
    tt = datetime.now().strftime("%m%d_%H%M%S")

    if output_filename is None:
        output_filename = f"csv_comb_{nn}_{tt}.csv"
    combined_df.to_csv(output_filename, index=False, header=False)
    print(f"CSV combining done: {output_filename}")


combine_csv(keywords=("Distance", "F K Series", "Pd L Series", "Pt M series"))
