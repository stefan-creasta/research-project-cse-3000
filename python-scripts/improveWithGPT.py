from openai import OpenAI
import os
import promptGenerator
import openai
secret_key = "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"
openai.api_key = secret_key

if __name__ == "__main__":
    src_directory_main = "C:/TU Delft/research_project/java-classes/src/main"
    src_directory_test = "C:/TU Delft/research_project/java-classes/src/test"
    prompt = promptGenerator.get_prompt()
    client = OpenAI(api_key=secret_key)

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user",
             "content": f"{prompt}"},
        ]
    )

    response_text = completion.choices[0].message.content

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
            java_test_class_truncated += code_to_be_added
            java_test_class_truncated += "\n}"
            java_test_class_truncated = java_test_class_truncated.replace("java", "", 1)
            tets_directory = promptGenerator.get_root_tests(src_directory_test)
            test_file_path = tets_directory[0]
            with open(test_file_path, "w") as file:
                file.write(java_test_class_truncated)
        else:
            print("No closing brace '}' found in the string.")

    else:
        print("\nNo code found in the response.")