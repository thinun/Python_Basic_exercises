with open('txt_1.txt', 'a+') as source_file:
    with open('txt_2.txt', 'a+') as destination_file:
        source_file.seek(0)
        source = source_file.readlines()
        for line in source:
            if line.strip() == 'line5':
                continue
            else:
                destination_file.write(line)
