import pandas as pd
import glob
#glob: library to search files and directories

def combine_txt_to_xlsx_w_filenames(output_filename='combined_with_filenames.xlsx'):

    # Get txt files in current dir. 
    #'glob.glob': get list of files
    txt_files = sorted(glob.glob('*.txt'))
    
    # Create a list to hold the dataframes (df)
    combined_df = pd.DataFrame()
    
    # Process
    for i, file in enumerate(txt_files):
        # enumerate: adds a counter to any iterable and return both
        # file = variable name
        
        #this gives a table, not list
        df = pd.read_csv(file, delimiter='\t', usecols=[0,1])
        #read_excel: function in pd library
        #read_csv: function in pd library; it reads 'txt' and 'csv' files.
        #delimiter is divider
        #'usecols=[0,1]': only load the column 0 and column 1.
        
        # Create a DataFrame with the filename in the first row
        temp1 = [[file,file]] # list
        temp1 = pd.DataFrame(temp1,columns=[df.columns[0],df.columns[1]]) # dataframe (table)
        
        comb = pd.concat([temp1,df], ignore_index=True) # combine in rows
        #ignore_index is necessary for combing in rows
        
        # Combine horizontally into the final DataFrame
        combined_df = pd.concat([combined_df, comb], axis=1) # combine, side-by-side
    
    
    # Write the combined dataframe to an Excel file
    combined_df.to_excel(output_filename, index=False, header=True)
    # 'to_excel' : function
    # index=False: don't write the row numbers
    # header=False: don't write the column names
    print("done")


combine_txt_to_xlsx_w_filenames()


#practice
"""
txt_files = sorted(glob.glob('*.txt'))

combined_df = pd.DataFrame()
print(combined_df)
print(txt_files[0])

aa = pd.read_csv(txt_files[0],delimiter = '\t', usecols=[0,1])
print(aa)

print(aa.shape)
print(aa.shape[0])
print(aa.shape[1])
print(aa.columns) #.columns returns column names.
print(aa.columns[0])

print("-------------------------------")
#print(txt_files.shape)
#shape works for pandas, not list

#DataFrame makes a list into a structured table
dd = [['Jason', 28, 90],['Jen', 25, 89]]
temp1 = pd.DataFrame(dd, columns=['Name','Age','Score'])
print(temp1)
print(temp1.shape)

filename_row = pd.DataFrame([txt_files[0]] * aa.shape[1])
print(filename_row)
filename_row = pd.DataFrame([txt_files[0]] * aa.shape[1]).T
print(filename_row)

filename_row.columns = aa.columns
print(filename_row.columns)

print("-------------------------------")
print(aa)
temp2 = aa.reset_index(drop=True)
print(temp2)

print("-------------------------------")
t1 = [[txt_files[0],0],[aa.columns[0],aa.columns[1]]]
print(t1)
"""