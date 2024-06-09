import gdown
def count_word(path):
    with open(path, 'r') as file:
        content = file.read()
        words = content.split()
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else :
            word_count[word] = 1
    return word_count

url = 'https://drive.google.com/uc?id=1IBScGdW2xlNsc9v5zSAya548kNgiOrko'
output = 'P1_data.txt'

gdown.download(url, output, quiet=False)
result = count_word(output)
print(result)
