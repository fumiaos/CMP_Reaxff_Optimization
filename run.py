from format_bracket import *
from format_th import convert_text
from togeo import convert_to_pdb
from totrain import to_train
with open('co0001.xyz', encoding='utf-8') as f:
    data = f.read()
data_lines = data.strip().split('\n')
processed_lines = add_empty_line(data_lines)
print(get_num(data_lines))
num = int(get_num(data_lines))
processed_data = '\n'.join(processed_lines)
output_text = convert_text(processed_data)
pdb_output = convert_to_pdb(output_text)
with open('geo', 'w', encoding='utf-8') as f:
    f.write(pdb_output)
train_output = to_train(output_text,num)
print(train_output)
with open('trainset.in', 'w', encoding='utf-8') as f:
    f.write(train_output)

