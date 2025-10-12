import pandas as pd

def accepted_candidates(candidates: pd.DataFrame, rounds: pd.DataFrame) -> pd.DataFrame:
    df = candidates[candidates['years_of_exp']>=2].merge(rounds, on='interview_id', how='inner')
    scores = df.groupby('candidate_id')['score'].sum()
    return scores[scores > 15].reset_index()[['candidate_id']]