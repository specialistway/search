import os
import json
import re
import string
from collections import defaultdict, OrderedDict

# 正则表达式用于匹配只包含标点符号的词
punctuation_pattern = re.compile(r'^[{}]+$'.format(re.escape(string.punctuation)))


def is_punctuation(word):
    return punctuation_pattern.match(word) is not None


def build_term_doc_dict(directory, num_files):
    term_doc_dict = defaultdict(lambda: {"count": 0, "doc_ids": []})#默认工厂。当我们访问一个不存在的键时，它会返回一个默认值

    for num in range(1, num_files + 1):
        if num%100==0:
            print(f"more 100 has down,now {num}")
        filepath = os.path.join(directory, str(num))
        if not os.path.isfile(filepath):
            print(f"文件不存在: {filepath}")
            continue

        try:
            with open(filepath, 'r', encoding='gbk') as f:
                content = f.read()
                words = content.strip().split()
                for word in words:
                    if is_punctuation(word):
                        continue
                    if num not in term_doc_dict[word]["doc_ids"]:#如果文档号不在字典里就添加
                        term_doc_dict[word]["doc_ids"].append(num)
                        term_doc_dict[word]["count"] += 1#并且数量加1
        except Exception as e:
            print(f"读取文件时出错: {filepath}, 错误: {e}")

    return term_doc_dict


def save_term_doc_dict(term_doc_dict, output_file):
    # 按键（词条）进行排序
    sorted_term_doc_dict = OrderedDict(sorted(term_doc_dict.items()))

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(sorted_term_doc_dict, f, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    directory = '/Users/wangaiyuan/PycharmProjects/search/data'  # 替换为你的文件目录路径
    num_files = 44970  # 文件数量
    output_file = 'dict1.json'

    term_doc_dict = build_term_doc_dict(directory, num_files)
    save_term_doc_dict(term_doc_dict, output_file)
    print(f"词典表已保存到 {output_file}")