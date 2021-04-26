import re


def hide_email(email):
    part1_email = str(re.findall(r'(\w+.\w+)@', email)).replace('[\'', '').replace('\']', '')
    part2_email = str(re.findall(r'@\w+.\w+', email)).replace('[\'', '').replace('\']', '')

    len_p1 = int(len(part1_email)/2)
    len_p2 = int(len(part2_email)/2)

    new_part1 = part1_email[len_p1:]
    new_part2 = part2_email[1:len_p2]

    part1_email = part1_email.replace(new_part1, '*'*len_p1)
    part2_email = part2_email.replace(new_part2, '*'*len_p2)

    return part1_email+part2_email


email = 'danil.churko@gmail.com'
print(hide_email(email))
