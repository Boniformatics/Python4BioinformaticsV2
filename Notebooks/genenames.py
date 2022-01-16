#!/usr/bin/python
def extract_gene_name(gene_file, gene_name_file):
    with open(gene_file, 'r') as file1:
        with open(gene_name_file, 'w') as file2:
            lines=file1.readlines() #list of strings
            #print(lines)
            #print (range(len(lines)))
            #for key,value in enumerate(lines):
            #print(key,value)
            for i in range(36,917):
                gene_lines=(lines[i]).split()
                gene_names=gene_lines[0]
                #print(gene_names)
                file2.write(f'{gene_names}\n')
