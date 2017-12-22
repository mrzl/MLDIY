a bash file scheduler in python3

it makes sure that only one job (bash script) is running at a time

should be added as a cronjob (crontab -e)
(* * * * * python3 /opt/scheduler/scheduler.py >> /opt/scheduler/cron.log)

jobs are bash files in /opt/scheduler/jobs/ (path can be configured in scheduler.py)
they'll will be run according to the modification date of the file (fifo)
make sure they are executable (chmod a+x job.sh)

done/failed jobs will be moved to a done/failed subfolder

in the bash script, use absolute paths to binaries, crontab
does not know about any environment variables from your .bashrc etc

wanna use a venv?
source /mnt/drive1/virtualenvs/eco_v4/bin/activate
