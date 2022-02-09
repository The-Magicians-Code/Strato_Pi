#!/bin/sh
read -p 'Upload: u, download: d:' job
echo 'Setting working directory to project Strato_Pi folder'
cd Strato_Pi
echo 'Success! Changed to project directory:' $(pwd)

if [ "$job" = "u" ]
then
	echo 'Initiating upload script:'
	echo 'Starting git processes'

	git add *
	read -p 'Please write a short description of changes that you made:' changes
	git commit -m "changes"
	git push origin "main"

	echo 'Upload complete!'
fi

if [ "$job" = "d" ]
then
	echo 'Connecting to git repo and pulling commits'
	git fetch --all
	git reset --hard origin/main
	echo 'Finished syncing with StratoPi repository'
fi
#/bin/bash #keeps terminal open
echo 'Process terminates in 5 seconds'
sleep 5 #Waiting for 5 seconds

