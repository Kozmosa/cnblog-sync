import os

def get_files(path):
    files = os.listdir(path)
    result = []
    for file in files:
        filepath = os.path.join(path, file)
        result.append(filepath)
    return result

def encode(file):
    with open(file, 'rb') as f:
        content = f.read()
        content = bytes(content.decode("gb18030", errors="ignore"), encoding="utf8", errors="ignore")
        return content

def write(file, content):
    with open(file, 'wb') as f:
        f.write(content)

if __name__ == "__main__":
    # test case
    print(get_files("./posts/"))
    files = get_files('./posts/')
    for file in files:
        content = encode(file)
        write(file, content)
