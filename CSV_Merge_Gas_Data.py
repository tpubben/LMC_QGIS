from tkinter import filedialog

import_files = filedialog.askopenfilenames(title='Open Gas File:',filetypes = (("CSV files","*.csv"),("all files","*.*")))
save_file = filedialog.asksaveasfilename(title='Save Export As', defaultextension='.csv', filetypes=(('CSV file', '*.csv'),("all files","*.*")))

for import_file in import_files:
    with open(save_file, 'a') as exportfile:
        exportfile.write('Lat,Long,Gas\n')
        with open(import_file, 'r') as f:
            l = f.readlines()[1:]
            for line in l:
                exportfile.write(line)