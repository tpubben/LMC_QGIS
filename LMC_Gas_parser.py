from tkinter import filedialog
import pynmea2, os

def LMCParser():
    import_files = filedialog.askopenfilenames(title='Open Gas File:',filetypes = (("Text files","*.txt"),("all files","*.*")))
    gas_lines = []
    for import_file in import_files:
        try:
            with open(import_file, 'r') as gasfile:
                gasdata = gasfile.readlines()
                for line in gasdata:
                    if len(line) > 2 and line[1] == 'E':
                        gasval = line.split(';')[4]
                    elif line.startswith('$GNRMC'):
                        msg = pynmea2.parse(line)
                        gas_lines.append((msg.latitude, msg.longitude, gasval))
            save_file = import_file.split('.')[0] + '.csv'
            with open(save_file, 'w') as exportfile:
                exportfile.write('Lat,Long,Gas')
                for line in gas_lines:
                    exportfile.write('\n{},{},{}'.format(line[0], line[1], line[2]))
            os.remove(import_file)
        except:
            print(import_file)
            continue

LMCParser()
