import re


def solution(N):
    # Converting N to binary
    b = bin(int(N)).lstrip('0b')
    # Regex for the rescue
    matches = re.finditer(r'(?=(10{1,}1))', b)
    results = [len(match.group(1).strip('1')) for match in matches]

    if results == []:
        return 0
    else:
        return max(results)
