#install library dengan pip install google-play-scraper

from google_play_scraper import Sort, reviews_all
import pandas as pd

scrapreview = reviews_all(
    'com.dafturn.mypertamina',  # ID aplikasi
    lang='id',  # defaults to 'en'
    country='id',  # defaults to 'us'
    sort=Sort.MOST_RELEVANT,  # defaults to Sort.MOST_RELEVANT
    filter_score_with=None  # defaults to None (means all score)
)

print(scrapreview)

app_reviews_df = pd.DataFrame(scrapreview)
app_reviews_df.to_csv('D:/mypertamina.csv', index=None, header=True)
