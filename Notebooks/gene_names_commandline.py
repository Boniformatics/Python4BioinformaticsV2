import sys
#!/usr/bin/python
import sys
a=sys.argv
numbe_of_arguments=len(a)
script_name=a[0]
input_gene_file=a[1]
out_put_gene_name_file=a[2]

print("This is the name of the script: ", script_name)
print("Number of arguments: ", numbe_of_arguments)
print("The arguments are: " , str(a))


def extract_gene_name(input_gene_file, out_put_gene_name_file):
    with open(input_gene_file, 'r') as file1:
        with open(out_put_gene_name_file, 'w') as file2:
            lines=file1.readlines() #list of strings
            #print(lines)
            #print (range(len(lines)))
            for i in range(36,917):
                gene_lines=(lines[i]).split()
                gene_names=gene_lines[0]
                #print(gene_names)
                file2.write(f'{gene_names}\n')
extract_gene_name(input_gene_file,out_put_gene_name_file)
    
    