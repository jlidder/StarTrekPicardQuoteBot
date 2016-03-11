import os, linecache

counter=102

while counter<=277:
    file_name = "tng_scripts/"+str(counter)+".txt"
    with open("tng_scripts/"+str(counter)+".txt") as myfile:
        end_cond = -1
        for line_num, line in enumerate(myfile, 1):
            if "STAR TREK: THE NEXT GENERATION" in line:
                end_cond = line_num + 2 #title will be every 2nd line after the show title in these scripts.
                line = linecache.getline(file_name, end_cond)
                new_file_name = "tng_scripts/"+str(counter)+"-"+line.replace("\"", "").strip().replace(".","")+".txt"
                print 'new file is: ', new_file_name
                os.rename(file_name, new_file_name)
                counter+=1
                break
