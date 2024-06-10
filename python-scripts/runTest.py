import subprocess
import os
import re
import matplotlib.pyplot as plt

mvn_path = "C:/apache-maven-3.9.6/bin/mvn.cmd"

def run_test():
    command = [mvn_path, "test"]
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    decoded_output = stdout.decode('utf-8')

    # Regular expressions to find the sections with failures and errors
    compilation_error_block_regex = re.compile(
        r'\[ERROR\] COMPILATION ERROR :(.*?)\[INFO\] ------------------------------------------------------------------------',
        re.DOTALL)
    failures_section_regex = re.compile(r'\[ERROR\] Failures:(.*?)\[INFO\]', re.DOTALL)
    errors_section_regex = re.compile(r'\[ERROR\] Errors:(.*?)\[INFO\]', re.DOTALL)

    # Extract individual compilation errors
    compilation_error_match = compilation_error_block_regex.search(decoded_output)

    compilation_errors = []
    if compilation_error_match:
        compilation_error_block = compilation_error_match.group(1).strip()
        # Extract individual error messages within the compilation error block
        error_lines = compilation_error_block.split('\n')
        for i, line in enumerate(error_lines):
            if line.startswith("[ERROR]"):
                error_message = line.strip()
                # Check if the next line is indented (continuation of the error message)
                if i + 1 < len(error_lines) and error_lines[i + 1].startswith("    "):
                    error_message += "\n" + error_lines[i + 1].strip()
                compilation_errors.append(error_message)

    # Find the failures section
    failures_section_match = failures_section_regex.search(decoded_output)
    errors_section_match = errors_section_regex.search(decoded_output)

    # Extract individual error messages within the failures section
    failure_issues = []
    if failures_section_match:
        failures_section = failures_section_match.group(1)
        failure_error_regex = re.compile(r'\[ERROR\] +(.+)', re.MULTILINE)
        failure_issues = failure_error_regex.findall(failures_section)

    # Extract individual error messages within the errors section
    error_issues = []
    if errors_section_match:
        errors_section = errors_section_match.group(1)
        error_error_regex = re.compile(r'\[ERROR\] +(.+)', re.MULTILINE)
        error_issues = error_error_regex.findall(errors_section)

    # Combine the results into a single string
    all_issues = compilation_errors + failure_issues + error_issues
    if len(all_issues) > 3:
        all_issues = all_issues[:3]
    if len(compilation_errors) > 0:
        issue_string = "The code is not able to build and I get the following compilation errors: "
    else:
        issue_string = "I get the following errors: "
    issue_string += "\n".join(all_issues)

    return issue_string

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