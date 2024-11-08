import tiktoken

def num_tokens_from_string(string: str, encoding_name: str) -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens
    
numTokens = num_tokens_from_string("garibladi fu ferito a una gamba", "o200k_base")
print(numTokens)