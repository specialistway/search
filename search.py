import json
# 文件路径
file_path = 'test_list.txt'
def and_hebing(str1,str2,dict):
    if str1 not in dict or str2 not in dict:
        return set()
    doc_ids1=set(dict[str1]['doc_ids'])
    doc_ids2 = set(dict[str2]['doc_ids'])
    return doc_ids1 & doc_ids2
def load_term_doc_dict(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        term_doc_dict = json.load(f)
    return term_doc_dict
def save_merged_doc_ids(merged_doc_ids, output_file):
    with open(output_file, 'a', encoding='utf-8') as f:  # 以追加模式打开文件
        for doc_id in sorted(merged_doc_ids):  # 对集合进行排序
            f.write(f"{doc_id}\t")  # 在编号之前用空格隔开
        f.write("\n")  # 每次写完一个词条的结果后换行

term_doc_file = 'dict1.json'  # 替换为你的词典表文件路径
output_file='result.txt'
term_doc_dict = load_term_doc_dict(term_doc_file)
num=0
# 打开文件并逐行读取
with open(file_path, 'r', encoding='utf-8') as file:
    for line in file:
        # 去掉行末的换行符
        line = line.strip()
        # 分割字符串
        parts = line.split(' ', 1)  # 只分割第一个空格，以防止行中有多个空格
        if len(parts) == 2:
            str1, str2 = parts
            # 处理读取到的字符串
            merged_doc_ids=and_hebing(str1,str2,term_doc_dict)
            if merged_doc_ids:
                #print(f"{num}:{str1} 和 {str2} 的交集文档ID: {merged_doc_ids}")
                save_merged_doc_ids(merged_doc_ids,output_file)
                num+=1
            else:
                print(f"{str1} 和 {str2} 没有共同的文档。")

        else:
            print(f'Line does not contain two strings separated by a space: {line}')

        print(num)