from os import listdir, remove, rename, makedirs
from os.path import isfile, join, isdir, getmtime
from os import stat
from pwd import getpwuid
import sys
import time
import subprocess


class Scheduler(object):
    def __init__(self):
        self.continue_on_fail = True
        self._jobs_path = '/opt/scheduler/jobs/'
        #self._jobs_path = '/home/mar/jobs/'
        self._log_file = join(self._jobs_path, 'log.txt')
        self._lock_file = join(self._jobs_path, 'lock.lck')
        self._finished_path = join(self._jobs_path, 'done/')
        self._failed_path = join(self._jobs_path, 'failed/')
        self._overtake_path = join(self._jobs_path, 'overtake/')
        self._logs_path = join(self._jobs_path, 'logs/')

        if not isdir(self._jobs_path):
            makedirs(self._jobs_path)
        if not isdir(self._finished_path):
            makedirs(self._finished_path)
        if not isdir(self._failed_path):
            makedirs(self._failed_path)
        if not isdir(self._logs_path):
            makedirs(self._logs_path)
        if not isdir(self._overtake_path):
            makedirs(self._overtake_path)

        if self.is_locked():
            sys.exit(0)

        try:
            # use überholspur first
            overtake_files = [f for f in listdir(self._overtake_path) if isfile(join(self._overtake_path, f))]
            self.overtake_scripts = [x for x in overtake_files if x.endswith('.sh')]
            self.overtake_scripts = self.sort(self._overtake_path, self.overtake_scripts)

            files = [f for f in listdir(self._jobs_path) if isfile(join(self._jobs_path, f))]
            self.scripts = [x for x in files if x.endswith('.sh')]
            self.scripts = self.sort(self._jobs_path, self.scripts)

            # no scripts found, abort
            if len(self.scripts) is 0 and len(self.overtake_scripts) is 0:
                self.cleanup()

        except OSError as e:
            print("OS error: {0}".format(e))
            self.cleanup()

    def is_locked(self):
        return isfile(self._lock_file)

    def lock(self):
        open(self._lock_file, 'w').close()

    def unlock(self):
        remove(self._lock_file)

    def move_job(self, src, dstdir, dstfile):
        if not isdir(dstdir):
            makedirs(dstdir)
        dst = join(dstdir, dstfile)
        if isfile(dst):
            # if destination file already exists,
            # append current timestamp in order to not overwrite
            dst += str(int(time.time()))
        rename(src, dst)

    def run(self):
        # überholspur first
        if len(self.overtake_scripts) > 0:
            script = self.overtake_scripts[0]
            script_to_run = join(self._overtake_path, script)
        else:
            script = self.scripts[0]
            script_to_run = join(self._jobs_path, script)

        try:
            self.lock()
            self.log(script_to_run + ' started\n')

            # determine the owner of the script
            script_owner = getpwuid(stat(script_to_run).st_uid).pw_name
            # construct a cmd to run the script as the owner
            finished_script_cmd = 'sudo su -c \"' + script_to_run + '\"  -s /bin/bash ' + script_owner

            script_log_file = join(self._logs_path, script) + '.log'
            with open(script_log_file, 'w') as script_log:
                success = subprocess.run([finished_script_cmd], stdout=script_log, shell=True, check=True)
            self.log(str(success) + '\n')

            is_out_of_memory = self.check_out_of_memory(script_log_file)

            if success.returncode is 0:
                self.unlock()
                self.move_job(script_to_run, self._finished_path, script)
            else:
                # unlock and move job to failed
                if self.continue_on_fail:
                    self.unlock()
                    self.move_job(script_to_run, self._failed_path, script)

        except OSError as e:
            print("OS error in run(): {0}".format(e))
            self.cleanup()

    def log(self, msg):
        with open(self._log_file, 'a') as f:
            iso_time = time.strftime("%Y-%m-%dT%H:%M:%S", time.localtime(time.time()))
            f.write(iso_time + ': ' + msg)

    @staticmethod
    def cleanup():
        sys.exit(1)

    def sort(self, path, file_names):
        sort_me = {}
        for filename in file_names:
            sort_me[filename] = getmtime(join(path, filename))

        sorted_scripts = [(k, sort_me[k]) for k in sorted(sort_me, key=sort_me.get, reverse=False)]
        sorted_filenames_only = []
        for tuple in sorted_scripts:
            sorted_filenames_only.append(tuple[0])
        return sorted_filenames_only

    def check_out_of_memory(self, log_file_name):
        with open(log_file_name, 'r') as f:
            text = f.readlines()
            print(text)
        return False


if __name__ == '__main__':
    scheduler = Scheduler()
    scheduler.run()
