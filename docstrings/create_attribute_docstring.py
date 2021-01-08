import re


def process_docstrings():

    output_str = str()
    text = input("Input code here:")

    # Search for definition line
    for item in text.split("\n"):
        if "def " in item and "(" in item and "):" in item:
            def_str = item.strip()
            # Remove "def "
            func_str = def_str.replace("def ", "")
            # Remove substring between brackets
            regex = '\(.*?\)'
            func_str = re.sub(regex, "()", func_str)
            # Remove ":"
            func_str = func_str.replace(":", "")
            # print(func_str)
            output_str += func_str + "\n"
            # print('func   :',func_str)
        if '"""' in item:
            if item.replace(" ", "")[:3] == '"""':
                # print('item   :', item)
                # First or last line of docstring
                doc_str = item.strip()

                # Remove '"""'
                doc_str = doc_str.replace('"""', "")

                if len(doc_str) == 0:
                    # Last line of docstring
                    continue

                # Add dot on end of sentence if not present
                # print('doc_str:', doc_str)
                if doc_str[-1] != '.':
                    doc_str += '.'

                # Add leading four spaces
                doc_str = ' '*4 + doc_str
                # print(doc_str)
                output_str += doc_str + "\n"

    # Print final ouput
    print(output_str)

process_docstrings()
