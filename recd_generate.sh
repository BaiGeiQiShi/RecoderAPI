#!/bin/bash -x
CURR=$(pwd)

echo -n '' > time-info-gen.txt

for dir in $(ls $CURR/105_bugs_with_src/)
do
	project=${dir%%[0-9]*}
	if [ ! -d "location/ochiai/$project" ];then
		mkdir -p location/ochiai/$project
	fi
	bugid=${dir#*$project}
	python3 $CURR/fl_reformat.py "$CURR/105_bugs_with_src/$dir/ochiai.ranking.txt" "$CURR/location/ochiai/${project}/$bugid.txt"

	if [ ! -d "patches/" ];then
                mkdir patches
		echo -n '' >patches/${project}${bugid}.txt
	else
		echo -n '' >patches/${project}${bugid}.txt
	fi

	start=$(date +%s.%N)

	python3 APItest.py $project $bugid
	end=$(date +%s.%N)
        runtime=$(echo "$end - $start" | bc)

	echo "${project}${bugid}:${runtime}" >> time-info-gen.txt
done
