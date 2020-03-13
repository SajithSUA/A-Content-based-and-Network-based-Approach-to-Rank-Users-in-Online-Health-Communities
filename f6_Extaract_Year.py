import pandas as pd


def extract_year_func():

    df = pd.read_csv('csvPiyu/2_support_scores_predicted_for_comments.csv',
                     usecols=['name', 'posted_time', 'Info_score', 'Emo_score'], encoding="utf-8")
    name = df['name']
    # print(name)

    # preprocess usernames
    preprocessed_names = []
    for y in name:
        preprocessed_names.append(str(y).replace('Ã¢â¬Â¦', '').strip())
    date = df['posted_time']

    dataframe = pd.DataFrame(df)

    year = []

    for i in date:
        one_date = i.split()
        for x in one_date:
            if len(x) == 4:
                year.append(x)

    dataframe['posted_year'] = year
    del dataframe['name']
    dataframe['name'] = preprocessed_names
    dataframe.to_csv(r'csvPiyu/3_support_scores_predicted_for_comments_with_year_extracted.csv.csv', encoding="utf-8")

    print("year extracted...")
