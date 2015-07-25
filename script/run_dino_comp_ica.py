#! /usr/bin/env python
import os

init_files_dir = "/home/simba/Workspace/MPRGP/data/dino/"

init_files = os.listdir(init_files_dir)
init_files.sort()

for inif in init_files:
    if not inif.endswith(".ini"):
        continue
    if inif.find("two_") < 0 or inif.find('mprgp_') < 0 or inif.find('mprgp_h') >= 0:
        continue
    f = init_files_dir + inif + " "
    cmmd = "./bin/release/collision_handle " + f + " > ./tempt/" + inif + ".txt"
    print cmmd
    os.system(cmmd)
