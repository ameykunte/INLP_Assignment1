import re

def basic_tokenizer(input_file, output_file):
    # Open the input file for reading
    with open(input_file, 'r') as f:
        text = f.read()

    url_pattern = re.compile(r'https?://\S+')
    hashtag_pattern = re.compile(r'#\w+')
    mention_pattern = re.compile(r'@\w+')

    processed_corpus = re.sub(url_pattern, '<URL>', text)
    processed_corpus = re.sub(hashtag_pattern, '<HASHTAG>', processed_corpus)
    processed_corpus = re.sub(mention_pattern, '<MENTION>', processed_corpus)

    # Remove punctuation and split into tokens
    tokens = re.findall(r'\w+',  text.lower())
    
    # Open the output file for writing
    with open(output_file, 'w') as f:
        # Write each token to a new line in the output file
        for token in tokens:
            f.write('"' + token + '"')


input_file = 'PnP_raw.txt'
output_file = 'PnP_tokenized.txt'
basic_tokenizer(input_file, output_file)
input_file = 'Ulysses_raw.txt'
output_file = 'Ulysses_tokenized.txt'
basic_tokenizer(input_file, output_file)

# Removed italics through regex, since _you_ != you in the tokenized sense 