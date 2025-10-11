import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    df = actor_director.groupby(['director_id', 'actor_id']).count().reset_index().rename(columns={'timestamp':'count'})
    return df[df['count'] >= 3][['director_id','actor_id']]