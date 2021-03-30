'''
pandas profiling for size < 100k dataframe file

Example : 
    (py37) joetsai@thor:~/work/poc/poi_meal_recommendation$ python profiling_pandas_frame.py --data data/article_html_20210221.csv --title emma_article_daily --output emma_artile_daily
'''
import pandas as pd
from pandas_profiling import ProfileReport
from absl import app, flags, logging
from absl.flags import FLAGS

flags.DEFINE_string('data', '',
                    'path to csv file you want profiling')
flags.DEFINE_string(
    'output','', 'path to output html report')
flags.DEFINE_string('title', 'Title', 'name of report title')
flags.DEFINE_integer('workers', 4, 'number of workers')


def main(_argv):
    df = pd.read_csv(FLAGS.data)
    profile = ProfileReport(df, title=FLAGS.title,minimal=True, pool_size=FLAGS.workers)
    profile.to_file(f"{FLAGS.output}.html")


if __name__ == '__main__':
    try:
        app.run(main)
    except SystemExit:
        pass
