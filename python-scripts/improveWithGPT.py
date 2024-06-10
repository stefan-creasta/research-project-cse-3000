from openai import OpenAI
import runPitest
import promptGenerator
import openai
secret_key = "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"
openai.api_key = secret_key

def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

if __name__ == "__main__":
    src_directory_main = "C:/TU Delft/research-project-cse-3000/java-classes/src/main"
    src_directory_test = "C:/TU Delft/research-project-cse-3000/java-classes/src/test"
    #prompt = promptGenerator.get_first_prompt()
    client = OpenAI(api_key=secret_key)
    #mess = [
    #        {"role": "user",
    #         "content": f"{prompt}"},
    #    ]
    mess = []
    steps = 1
    print("Initial mutation score: " + str(runPitest.run_pitest()))
    prev_mut = -1
    while steps < 10:
        if steps == 1:
            prompt = promptGenerator.get_first_prompt()
        else:
            prompt = promptGenerator.generate_seq_prompt(prev_mut)
        prompt += ". Make sure that the name of the class remains the same."
        print(prompt)
        prev_mut = runPitest.run_pitest()
        if is_float(prev_mut) == False:
            prev_mut = -1
        mess.append({"role": "user", "content": prompt})
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=mess
        )
        response_text = completion.choices[0].message.content
        mess.append({"role": "assistant", "content": response_text})
        # Print the full response
        print("Full response:\n", response_text)

        # Extract code from the response (assuming the code is enclosed in triple backticks ``` for markdown formatting)
        import re

        code_snippets = re.findall(r'```(.*?)```', response_text, re.DOTALL)
        code_to_be_added = ""

        if code_snippets:
            for i, code in enumerate(code_snippets):
                code_to_be_added += code.strip()
            java_code_test_list = promptGenerator.get_java_code(src_directory_test)
            java_test_class = java_code_test_list[0]
            last_closing_brace_index = java_test_class.rfind("}")

            if last_closing_brace_index != -1:
                java_test_class_truncated = java_test_class[:last_closing_brace_index]

                #print("Truncated Java Test Class:\n", java_test_class_truncated)
                #java_test_class_truncated += code_to_be_added
                #java_test_class_truncated += "\n}"
                java_test_class_truncated = code_to_be_added
                java_test_class_truncated = java_test_class_truncated.replace("java", "", 1)
                tets_directory = promptGenerator.get_root_tests(src_directory_test)
                test_file_path = tets_directory[0]
                with open(test_file_path, "w") as file:
                    file.write(java_test_class_truncated)
            else:
                print("No closing brace '}' found in the string.")

        else:
            print("\nNo code found in the response.")
            tets_directory = promptGenerator.get_root_tests(src_directory_test)
            test_file_path = tets_directory[0]
            with open(test_file_path, "w") as file:
                file.write(response_text)
        ms = runPitest.run_pitest()
        if is_float(ms) == True:
            print("Step " + str(steps) + ": mutation score of " + str(ms))
        else:
            print("Step " + str(steps) + ": tests crashed")
        #print(response_text)
        steps+=1