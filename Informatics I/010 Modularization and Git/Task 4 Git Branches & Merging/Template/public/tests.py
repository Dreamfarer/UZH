#!/usr/bin/env python3
from unittest import TestCase
from git import Repo
from shutil import rmtree
import os, subprocess, sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

# Please adopt this variable to test your script with your own repository.
# Please note that interactive authentication does not work with ACCESS,
# so please run the script locally.
YOUR_GIT_REPO_URL="http://use.your.own.repo/url/here"

os.chdir("public")
base_dir = os.getcwd()
path_script = base_dir + "/script.sh"
print("base_dir: {}".format(base_dir))
print("script_location: {}".format(path_script))


class GitTest(TestCase):

    @classmethod
    def tearDownClass(cls):
        try: rmtree(".git")
        except: pass
        for f in ["a.txt", "b.txt"]:
            try: os.unlink(f)
            except: pass

    def test_0_run_script(self):
        os.chmod(path_script, 0o755)

        print("executing '{}'...".format(path_script))
        out = subprocess.Popen('REPO_URL="'+YOUR_GIT_REPO_URL+'" '+path_script,
                               cwd=base_dir,
                               shell=True,
                               stdout=2,
                               stderr=2)
        stdout, _ = out.communicate()  # must be first thing to do

        if stdout:
            stdout = stdout.decode("UTF-8")
            print(stdout)

        if out.returncode != 0:
            m = "@@Script execution failed (return code = {}).@@".format(out.returncode)
            raise AssertionError(m)

    def test_1_this_is_not_really_a_test(self):
        r = Repo(base_dir)
        log = r.head.log()
        eprint("Commit Log has {} Entries:".format(len(log)))
        for l in log:
            eprint("- {}".format(l.message))
