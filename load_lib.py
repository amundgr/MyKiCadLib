import sys
import os
import glob 
import re

if len(sys.argv) > 1:
    project_path = sys.argv[1]
else:
    print("No folder path provided.")
    exit()


symbole_file_string = (
"(sym_lib_table\n"
"  (version 7)\n")

cwd = os.getcwd()
for filename in glob.glob("schematic_symbols/*"):
    if filename.endswith(".kicad_sym"):
        name = filename.split("/")[-1].split(".")[0]
        path = os.path.join(cwd, filename)

        symbole_file_string += f'  (lib (name "{name}")(type "KiCad")(uri "{path}")(options "")(descr ""))\n'

symbole_file_string += ")"

with open(os.path.join(project_path, "sym-lib-table"), "w") as outfile:
    outfile.write(symbole_file_string)


footprint_file_string = (
"(fp_lib_table\n"
"  (version 7)\n"
)

cwd = os.getcwd()
for filename in glob.glob("footprints/*"):
    if filename.endswith(".pretty"):
        name = filename.split("/")[-1].split(".")[0]
        path = os.path.join(cwd, filename)
        
        footprint_file_string += f'  (lib (name "{name}")(type "KiCad")(uri "{path}")(options "")(descr ""))\n'

footprint_file_string += ")"

with open(os.path.join(project_path, "fp-lib-table"), "w") as outfile:
    outfile.write(footprint_file_string)
