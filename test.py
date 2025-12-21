import pandas as pd

# Load dataset to pandas Dataframe
df = pd.read_csv("hf://datasets/ailsntua/Chordonomicon/chordonomicon_v2.csv", low_memory=False)


# Drop rows that do not contain spotify song id and chords
mask = df["chords"].notna() & df["spotify_song_id"].notna() & df["genres"].notna()

clean_df = df[mask].copy()

print(clean_df.loc[0, "chords"])