import pandas as pd

def count_occurrences(files: pd.DataFrame) -> pd.DataFrame:
    bulls = files.content.str.contains(r'\s+bull\s+', case=False).sum()
    bears = files.content.str.contains(r'\s+bear\s+', case=False).sum()

    return pd.DataFrame(
        {
            "word": ["bull", "bear"],
            "count": [bulls, bears]
        }
    )