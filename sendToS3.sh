#!/bin/bash

for i in $(find ./ -name '*.tar.gz');
do
        num=$(echo $i| tr -dc '0-9')
        #echo $num
        aws s3 cp $i s3://<bucket><folder>;
        #echo $i|grep -o '[0-9]\+'
done
