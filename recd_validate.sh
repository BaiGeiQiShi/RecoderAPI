#!/bin/bash -x

CURR=$(pwd)

echo -n '' > time-info.txt

for dir in $(ls $CURR/patches/)
do 
	cbug=${dir%%\.*}
	project=${cbug%%[0-9]*} 
        bugid=${cbug#*$project}

	rm -rf 105_bugs_with_src/$cbug
	cp -r 105_bugs_with_src_backup/$cbug 105_bugs_with_src/$cbug

	if [ ! -d "tmp/${cbug}" ];then
		mkdir -p "tmp/${cbug}"
	else
		rm -rf "tmp/${cbug}/*"
	fi


	if [ ! -d "final/" ];then
                mkdir -p "final/"
		echo -n '' >final/${project}${bugid}.txt
	else
		echo -n '' >final/${project}${bugid}.txt
        fi

	while read line
	do
        	if [[ $line =~ "$cbug" ]];then
                	usedTIME=${line#*:}
        	fi
	done<time-info-gen-bu.txt

	TIME=$(echo "18000-$usedTIME" | bc)


	start=$(date +%s.%N)

        timeout -s 9 $TIME python3 APIvalid.py $project $bugid

        end=$(date +%s.%N)
	runtime=$(echo "$end - $start" | bc)
	alltime=$(echo "$runtime + $usedTIME " | bc)
	alltimeMin=$(echo "$alltime / 60 " | bc)

        echo "${project}${bugid}:${alltimeMin}min" >> time-info.txt
done
