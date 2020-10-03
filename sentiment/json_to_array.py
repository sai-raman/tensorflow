with open('Sarcasm_Headlines_Dataset_v2.json') as f:
    with open('sarcasm1.json','a') as sarcasm_file:
        for x in f:
            sarcasm_file.write(x+',')
