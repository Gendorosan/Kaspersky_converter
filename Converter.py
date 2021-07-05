import csv
import re

with open("data.csv", encoding='utf-8') as r_file:
    html_str = "<html>\n <head>\n  <style>\n    TABLE {border-collapse: collapse;}\n" \
               "    TD {padding: 3px;border: 1px solid black;}\n  </style>\n </head>\n <body>\n  <table>\n"
    file_reader = csv.reader(r_file, delimiter=",")
    for row in file_reader:
        print(row)
        html_str += "   <tr>\n"
        for word in row:
            print(word)
            html_str += f"    <td> {word} </td>\n"
        html_str += "   </tr>\n"
    html_str += "  </table>\n </body>\n</html>"
    print(html_str)
    with open("file.html", "w", encoding='utf-8') as file:
        file.write(html_str)

with open("data.prn") as file:
    reader = csv.reader(file, delimiter="\n")
    html_str = "<html>\n <head>\n  <style>\n    TABLE {border-collapse: collapse;}\n" \
               "    TD {padding: 3px;border: 1px solid black;}\n  </style>\n </head>\n <body>\n  <table>\n"
    all_text = [row[0] for row in reader]
    print(all_text[0])
    index = [all_text[0].index(letter) for letter in all_text[0] if letter.isupper()]
    print(index)
    html_str += "   <tr>\n"
    html_str += f"    <td> {all_text[0][index[0]:index[1]]} </td>\n"
    html_str += f"    <td> {all_text[0][index[1]:index[2]]} </td>\n"
    html_str += f"    <td> {all_text[0][index[2]:index[3]]} </td>\n"
    html_str += f"    <td> {all_text[0][index[3]:index[4]]} </td>\n"
    html_str += f"    <td> {all_text[0][index[4]:index[5]]} </td>\n"
    html_str += f"    <td> {all_text[0][index[5]:len(all_text[0])]} </td>\n"
    html_str += "   </tr>\n"
    all_text.pop(0)
    for str in all_text:
        html_str += "   <tr>\n"
        html_str += f"    <td> {str[index[0]:index[1]]} </td>\n"
        html_str += f"    <td> {str[index[1]:index[2]]} </td>\n"
        html_str += f"    <td> {str[index[2]:index[3]]} </td>\n"
        html_str += f"    <td> {re.split('  +', str[index[3] - 1 + 1:index[5]])[0]} </td>\n"
        html_str += f"    <td> {re.split('  +', str[index[3] - 1 + 1:index[5]])[1]} </td>\n"
        html_str += f"    <td> {str[index[5]:len(str)]} </td>\n"
        html_str += "   </tr>\n"
    html_str += "  </table>\n </body>\n</html>"
    print(html_str)
    with open("file2.html", "w", encoding='utf-8') as file:
        file.write(html_str)
