import os


def get_files():
    for filepath, dirnames, filenames in os.walk('.'):
        for filename in filenames:
            if filename.endswith('.py'):
                yield os.path.join(filepath, filename)


f = get_files()
# print(type(f))
for file in f:
    print(file)
    with open(file, 'r', encoding='utf-8') as fp, open('./test/format.md', 'a', encoding='utf-8') as fp2:
        fp2.write('\n')
        fp2.write('\n\n## '+file+'\n```python\n')
        fp2.write(fp.read())
        fp2.write('\n```\n')
