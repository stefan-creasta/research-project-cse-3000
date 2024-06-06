import subprocess
import os
import re
import matplotlib.pyplot as plt

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

if __name__ == '__main__':

    # Data arrays
    means = [15, 16.67, 17.28, 18, 19, 20.34, 22.8, 25.34, 20.4, 20.34]
    medians = [15, 15, 17, 18.5, 18, 20, 21, 24, 20, 21]

    # Plotting the data
    plt.figure(figsize=(10, 6))
    plt.plot(means, marker='o', label='Mean', color='blue', linestyle='-')
    plt.plot(medians, marker='s', label='Median', color='red', linestyle='--')

    # Adding titles and labels
    plt.title('Mean and Median values of mutation scores')
    plt.xlabel('Number of prompts sent')
    plt.ylabel('Mutation score')
    plt.legend()
    plt.grid(True)

    # Display the plot
    plt.show()