import xml.etree.ElementTree as ET

ids = []
firstnames = []
lastnames = []
subjects = []
marks = []

new_ids = []
new_names = []
new_lastnames = []
new_subj = []
new_marks = []

new_ids_deobf = []
new_names_deobf = []
new_lastnames_deobf = []
new_subj_deobf = []
new_marks_deobf = []

c = ''
q = 0

first_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
last_alphabet = 'QWE1ASD2ZXC3RTY4FGH5VBN6UIOP7JKL8M9qwertyuiop0asdfghjklzxcvbnm'


# функция для обфускации строки
def obfuscate(string_to_obf):
    result = ''
    length = len(string_to_obf)
    for k in range(length):
        c = string_to_obf[k]
        index = first_alphabet.index(c)
        result = result + last_alphabet[index]
    return result


# функция для деобфускации строки
def deobfuscate(string_to_deobf):
    result = ''
    length = len(string_to_deobf)
    for k in range(length):
        c = string_to_deobf[k]
        index = last_alphabet.index(c)
        result = result + first_alphabet[index]
    return result


# функция для обфускации xml-файла
def obfuscate_xml(file_name):
    global q
    my_tree = ET.parse('file.xml')
    my_root = my_tree.getroot()

    for x in my_root.findall('student'):
        id = x.find('id').text
        ids.append(id)
        firstname = x.find('firstname').text
        firstnames.append(firstname)
        lastname = x.find('lastname').text
        lastnames.append(lastname)
        subject = x.find('subject').text
        subjects.append(subject)
        mark = x.find('marks').text
        marks.append(mark)

    for p in range(4):
        new_ids.append(obfuscate(ids[p]))
        new_names.append(obfuscate(firstnames[p]))
        new_lastnames.append(obfuscate(lastnames[p]))
        new_subj.append(obfuscate(subjects[p]))
        new_marks.append(obfuscate(marks[p]))

    while q < 4:
        for x1 in my_root.iter('id'):
            x1.text = new_ids[q]
        for x2 in my_root.iter('firstname'):
            x2.text = new_names[q]
        for x3 in my_root.iter('lastname'):
            x3.text = new_lastnames[q]
        for x4 in my_root.iter('subject'):
            x4.text = new_subj[q]
        for x5 in my_root.iter('marks'):
            x5.text = new_marks[q]
            q = q + 1
    my_tree.write('obfuscated_file.xml')


obfuscate_xml('file.xml')


# функция для деобфускации xml-файла
def deobfuscate_xml(file_name):
    global q
    my_tree = ET.parse('file.xml')
    my_root = my_tree.getroot()

    for x in my_root.findall('student'):
        id = x.find('id').text
        ids.append(id)
        firstname = x.find('firstname').text
        firstnames.append(firstname)
        lastname = x.find('lastname').text
        lastnames.append(lastname)
        subject = x.find('subject').text
        subjects.append(subject)
        mark = x.find('marks').text
        marks.append(mark)

    # добавляем деобфусцированные строки в массив
    for p2 in range(4):
        new_ids_deobf.append((deobfuscate(ids[p2])))
        new_names_deobf.append((deobfuscate(firstnames[p2])))
        new_lastnames_deobf.append((deobfuscate(lastnames[p2])))
        new_subj_deobf.append((deobfuscate(subjects[p2])))
        new_marks_deobf.append((deobfuscate(marks[p2])))

    while q < 4:
        for x1 in my_root.iter('id'):
            x1.text = new_ids_deobf[q]
        for x2 in my_root.iter('firstname'):
            x2.text = new_names_deobf[q]
        for x3 in my_root.iter('lastname'):
            x3.text = new_lastnames_deobf[q]
        for x4 in my_root.iter('subject'):
            x4.text = new_subj_deobf[q]
        for x5 in my_root.iter('marks'):
            x5.text = new_marks_deobf[q]
            q = q + 1
    my_tree.write('deobfuscated_file.xml')


deobfuscate_xml('obfuscated_file.xml')
