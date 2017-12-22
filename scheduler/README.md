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

the jobs are being run as the user who created the file
this is done via

    sudo visudo
    # add these lines at the bottom (already on lyrik)
    marcel  ALL=(ramin) NOPASSWD: ALL # run things as ramin
    marcel  ALL=(gene) NOPASSWD: ALL # run things as gene
    marcel  ALL=(ALL) NOPASSWD: ALL # marcel doesnt need to enter sudo pw

wanna use a venv?
source /mnt/drive1/virtualenvs/eco_v4/bin/activate
