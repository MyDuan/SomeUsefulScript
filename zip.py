import gzip

f_out = gzip.open("3week_train.tar.gz", 'wb')
with open("3week_train.txt") as file:
    for line in file:
        f_out.write(line)
    f_out.close()
