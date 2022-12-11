#input file
filename = "v_01_nasr_city_activitygen-example.trips.rou.xml"
if not(filename):
    filename = input()
fin = open(filename, "rt")
#output file to write the result to
fout = open(str("edited_" + filename), "wt")
#for each line in the input file
counter = 1
for line in fin:
	#read replace the string and write to output file
    #
    line_str = str(line)

    start_pos_rand = line_str.find('randUni')
    if(start_pos_rand>0):
        end_pos = line_str.find('"',start_pos_rand)
        # print(line_str[start_pos_rand+len('randUni'):end_pos])
        to_change = line_str[start_pos_rand:end_pos]
        replaced_random_str = line.replace("random", "veh_passenger")
        fout.write(replaced_random_str.replace(to_change, str(counter)))
        counter +=1
    else:
        fout.write(line.replace("random", "veh_passenger"))
        # fout.write(line)


    
    
#close input and output files
fin.close()
fout.close()