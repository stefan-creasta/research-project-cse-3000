import os
import runPitest

def get_java_files(directory):
    java_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".java"):
                java_files.append(os.path.join(root, file))
    return java_files


def read_file_contents(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def get_java_code(directory):
    java_files = get_java_files(directory)
    java_code_list = []
    for file in java_files:
        java_code = read_file_contents(file)
        java_code_list.append(java_code)
    return java_code_list

def get_root_tests(directory):
    roots = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".java"):
                filename = os.path.basename(file)
                roots.append(os.path.join(root, filename))
    return roots

def get_java_dir(directory):
    java_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".java"):
                filename = os.path.basename(file)
                java_files.append(filename)
    return java_files

first_sentence = "I have Java classes and JUnit tests for them. I am interested in their mutation score and how to improve it."
last_sentence = "Can you provide me with the code for tests for these classes, such that the mutation score is improved?"

def generate_prompt(java_code_main_list, java_classes_main_list, java_code_test_list):
    prompt = first_sentence + " "
    prompt += "Currently, I have " + str(len(java_classes_main_list)) + " Java classes.\n"
    for i in range(len(java_code_main_list)):
        prompt += "This is the " + java_classes_main_list[i] + " class:\n"
        prompt += "\"" + java_code_main_list[i] + "\"\n"
    prompt += "These are the test cases:\n"
    for i in range(len(java_code_test_list)):
        prompt += "\"" + java_code_test_list[i] + "\"\n"
    mutation_score = runPitest.run_pitest()
    prompt += "Currently, I use Pitest to compute the mutation score, which currently is: " + str(mutation_score) + "."
    prompt += " " + last_sentence
    return prompt

def get_prompt():
    src_directory_main = "C:/TU Delft/research_project/java-classes/src/main"
    src_directory_test = "C:/TU Delft/research_project/java-classes/src/test"

    java_code_main_list = get_java_code(src_directory_main)
    java_classes_main_list = get_java_dir(src_directory_main)
    java_code_test_list = get_java_code(src_directory_test)

    root_tests = get_root_tests(src_directory_test)
    print(root_tests)

    prompt = generate_prompt(java_code_main_list, java_classes_main_list, java_code_test_list)
    return prompt

if __name__ == "__main__":
    print(get_prompt())

