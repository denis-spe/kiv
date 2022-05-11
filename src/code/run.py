# import libraries
import re
import codecs
import subprocess
from subprocess import check_output



def run_code (input_code, get_result, file_name):
    """
    Run code from the file_name path
    :param input_code, code to write in the file:
    :param get_result, some where to display the result:
    :param file_name, the path of the file to write in code:
    """

    # Write in the form.py
    with open(file_name, "+w") as f:
        f.write(input_code.text)

    # File extension from the file to run
    file_extension = file_name.split('.')[-1].lower()

    try:
        if file_extension == "java":
            # Read and executing content from the form.py
            t = check_output(['javac', file_name], stderr=subprocess.STDOUT)# Replace all useless symbols

            # compile java code
            t = check_output([language, file_name.split('.')[0]], stderr=subprocess.STDOUT)# Replace all useless symbols

        elif file_extension == "py":
            t = check_output([language, file_name], stderr=subprocess.STDOUT)# Replace all useless symbols

        elif file_extension == "r":
            t = check_output(["Rscript", file_name], stderr=subprocess.STDOUT)# Replace all useless symbols

        code = re.sub(r"^b", "", str(t).replace("'", ""))

        # Decode the string
        decoding = codecs.decode(code, 'unicode_escape')

        # Display decoded string 
        get_result.text = f"[color=rgb(255, 255, 255)]{decoding}[/color]"

    except subprocess.CalledProcessError as e:
        # Show the error which resulted in your code
        get_result.text = f"[color=rgb(255, 255, 255)]{e.output.decode('utf-8')}[/color]"