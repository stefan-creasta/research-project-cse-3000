import subprocess
import os
import re

def run_pitest():
    # Change directory to java-classes
    #print(os.getcwd())
    #os.chdir("research_project/python-scripts")
    os.chdir("C:/TU Delft/research_project/java-classes")
    #print(os.getcwd())
    # Run Pitest command
    mvn_path = "C:/apache-maven-3.9.6/bin/mvn.cmd"
    command = [mvn_path, "clean", "test", "org.pitest:pitest-maven:mutationCoverage"]
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    # Check for errors
    if process.returncode != 0:
        error_message = stdout.decode("utf-8")
        error_lines = ""
        for line in error_message.splitlines():
            if line.startswith("[ERROR]"):
                error_lines += line + "\n"
        #print("Error running Pitest:")
        #print(error_lines)
        return error_lines

    # Extract mutation score from the output
    output_lines = stdout.decode("utf-8").split('\n')
    mutation_score = None
    for line in output_lines:
        if "Generated" in line and "mutations Killed" in line:
            match = re.search(r'\((\d+)%\)', line)
            if match:
                mutation_score = float(match.group(1))
                break

    return mutation_score

def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

if __name__ == "__main__":
    mutation_score = run_pitest()
    if mutation_score is not None:
        if is_float(mutation_score) == True:
            formatted_score = "{:.1f}%".format(mutation_score)
            print("Mutation Score:", formatted_score)
        else:
            print(mutation_score)
