#!/bin/bash
#this scripts will upload the local files to a github server
#Usage:push_files.sh -f file -m 'tag'
#author:1016551343@qq.com
#create:2016.3.7
Usage(){
echo "Usage:$0 file -m "tag""
}
git add $2
git commit -m $4
git push origin master
if [ $?==0 ] 
then
echo "done"
else
echo "Usage()"
fi
