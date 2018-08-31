import gzip

for i in range(0, 13):
    f_out = gzip.open("allmodel_train_feature_delete_"+str(i)+".tar.gz", 'wb')
    with open("../../dump_baseline_train_7day.txt") as file:
        for line in file:
            data = line.split('|')
            label = data[0]
            feature = data[1]
            feature_list = feature.split(',')
            del feature_list[i]
            new_feature = ",".join(feature_list)
            #outfile.write(label+'|'+new_feature+"\n")
            f_out.write(label+'|'+new_feature+"\n")
        f_out.close()
