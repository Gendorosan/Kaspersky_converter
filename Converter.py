import csv

with open("data.csv", encoding='utf-8') as r_file:
    html_str = "<html>\n <head>\n  <style>\n    TABLE {border-collapse: collapse;}\n" \
               "    TD {padding: 3px;border: 1px solid black;}\n  </style>\n </head>\n <body>\n  <table>\n"
    file_reader = csv.reader(r_file, delimiter=",")
    for row in file_reader:
        html_str += "   <tr>\n"
        for word in row:
            html_str += f"    <td> {word} </td>\n"
        html_str += "   </tr>\n"
    html_str += "  </table>\n </body>\n</html>"
    print(html_str)
    with open("file.html", "w", encoding='utf-8') as file:
        file.write(html_str)
