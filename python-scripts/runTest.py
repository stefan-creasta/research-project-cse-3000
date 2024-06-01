import subprocess
import os
import re

mvn_path = "C:/apache-maven-3.9.6/bin/mvn.cmd"

def run_test():
    current_path = os.getcwd()
    command = [mvn_path, "test"]
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    return stderr