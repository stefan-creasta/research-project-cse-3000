import subprocess
import os
import re

mvn_path = "C:/apache-maven-3.9.6/bin/mvn.cmd"

def run_test():
    current_path = os.getcwd()
    command = [mvn_path, "test"]
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    # Decode the byte string
    decoded_output = stdout.decode('utf-8')

    # Regular expressions to match error and failure lines
    failure_regex = re.compile(r'\[ERROR\] Failures:\s*\[ERROR\](.*?)\r\n', re.DOTALL)
    error_regex = re.compile(r'\[ERROR\] Errors:\s*\[ERROR\](.*?)\r\n', re.DOTALL)

    # Find all matches
    failures = failure_regex.findall(decoded_output)
    errors = error_regex.findall(decoded_output)

    # Clean up the results
    failures = [f.strip() for f in failures]
    errors = [e.strip() for e in errors]

    # Combine the results into a list
    test_issues = failures + errors

    # Print the list of issues
    string = ""
    for test in test_issues:
        string = string + test + "\n"
    return string