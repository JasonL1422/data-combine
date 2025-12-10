import pandas as pd
import glob
from datetime import datetime
import os

#Select one of the three functions defined below:
    #combine_csv(), combine_txt(), combine_xlsx()

def combine_csv(output_filename=None):

    files = sorted(glob.glob('*.csv'))
    combined_df = pd.DataFrame()
    
    if len(files) == 0:
        return print("no .csv files found")

    for i, file in enumerate(files):
        
        df = pd.read_csv(file)

        filename_row = pd.DataFrame([ [file] * (df.shape[1])],columns=df.columns)
        header_row = pd.DataFrame([df.columns],columns=df.columns)
        data_row = df
        temp_df = pd.concat([filename_row, header_row, data_row], ignore_index=True)

        combined_df = pd.concat([combined_df, temp_df], axis=1)
    
    nn = os.path.splitext(files[0])[0] #remove extension
    tt = datetime.now().strftime("%m%d_%S")

    combined_df.to_csv(f"csv_comb_{nn}_{tt}.csv", index=False, header=False)

    print("csv combining done")

def combine_txt(output_filename=None):

    files = sorted(glob.glob('*.txt'))
    combined_df = pd.DataFrame()
    
    if len(files) == 0:
        return print("no .txt files found")
    
    for i, file in enumerate(files):
       
        #df = pd.read_table(file)
        df = pd.read_csv(file, sep=r"\s+", engine="python")#we still use 'read_csv'

        filename_row = pd.DataFrame([ [file] * (df.shape[1])],columns=df.columns)
        header_row = pd.DataFrame([df.columns],columns=df.columns)
        data_row = df
        temp_df = pd.concat([filename_row, header_row, data_row], ignore_index=True)

        combined_df = pd.concat([combined_df, temp_df], axis=1)
    
    nn = os.path.splitext(files[0])[0] #remove extension
    tt = datetime.now().strftime("%m%d_%S")

    combined_df.to_csv(f"txt_comb_{nn}_{tt}.csv", index=False, header=False)

    print("txt combining done")

def combine_xlsx(output_filename=None):

    files = sorted(glob.glob('*.xlsx'))
    combined_df = pd.DataFrame()
    
    if len(files) == 0:
        return print("no .xlsx files found")

    for i, file in enumerate(files):
        
        df = pd.read_excel(file)

        filename_row = pd.DataFrame([ [file] * (df.shape[1])],columns=df.columns)
        header_row = pd.DataFrame([df.columns],columns=df.columns)
        data_row = df
        temp_df = pd.concat([filename_row, header_row, data_row], ignore_index=True)

        combined_df = pd.concat([combined_df, temp_df], axis=1)
    
    nn = os.path.splitext(files[0])[0] 
    tt = datetime.now().strftime("%m%d_%S")

    combined_df.to_excel(f"xlsx_comb_{nn}_{tt}.xlsx", index=False, header=False)

    print("xlsx combining done")
    
combine_csv()
combine_txt()
#combine_xlsx()
