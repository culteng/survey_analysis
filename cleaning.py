# data cleaning for survey results

# python imports
import pandas as pd
from datetime import datetime
from pathlib import Path
import sys

def main(args):
    df = pd.read_csv('./data/raw/cesa-demo.csv')
    # clean & document original questions
    cols_orig = df.columns
    df.columns = [i.strip().replace('?','') for i in map(str.lower, df.columns)]
    df.rename(columns={
        "submitted at":"datetime_submitted",
        "what grade are you in":"grade",
        "what is your gender":"gender",
        "what is your ethnicity":"ethnicity",
        "how many years have you been a student":"tenure_student",
        "everything that happens on campus is connected to the school's mission statement.":"scl_mission_cnct",
        "the school is very christ-centered.":"scl_christ_centered",
        "school is a \"happy\" place for me.":"scl_happy",
        "i am comfortable to speak up about issues going on at school.":"scl_speakup",
        "it has been explicitly stated how diversity fits into the school's mission statement.":"scl_mission_diverse",
        "the school's leadership is excited about diversity.":"scl_ldrshp",
        "the school celebrates the culture of its students.":"scl_celebr",
        "i feel like i belong at my school.":"scl_belong",
        "i have witnessed or experienced bullying on campus (or online) because of cultural differences.":"scl_neg_bully",
        "students of different backgrounds get along at school.":"scl_getalong",
        "school rules are culturally unbiased":"scl_rules",
        "i regularly attend school-sponsored events (sporting events, student performances, social events, etc.)":"scl_events",
        "students are disciplined the same, despite their cultural background.":"scl_discipline",
        "i am being equipped to thrive in any cultural environment.":"scl_equipped",
        "we learn about minority people groups, authors, and artists outside of their cultural heritage month. ":"scl_learn",
        "i feel cared for by my teachers":"scl_cared",
        "chapel encourages students to engage the christian faith cross-culturally. ":"scl_chapel",
        "i have studied faithful christians from various american cultures and around the world in classes. ":"scl_cultures",
        "the school has christian role models from various cultures on campus as employees or guests.":"scl_rlmdls",
        "any comments":"comments"
        }, inplace=True)
    df.columns = [i.replace(' ','_') for i in df.columns]
    # drop duplicates
    df.drop_duplicates(subset=['ip_address'])
    # convert categoricals, clean others
    df.datetime_submitted = pd.to_datetime(df.datetime_submitted)
    df.grade = df.grade.str.strip('Grade ')
    df.grade = df.grade.astype(int)
    df.gender.replace({'Male':0,'Female':1}, inplace=True)
    df.ethnicity.replace({'African American (black)':'b', 'Anglo/White':'w', 'Asian Descent': 'a', 'Latino/a':'l'}, inplace=True)
    df.ethnicity = df.ethnicity.astype('category')
    df.tenure = ((df.tenure.str[0].astype(int)+1)/2).astype(int)
    df = df.apply(lambda x: x.str[0].astype(int) if x.name.startswith('scl_') and x.dtype == 'object' else x)

    Path('./data/cleaned').mkdir(parents=True, exist_ok=True)
    curtime = datetime.now().strftime('%Y%m%d_%H%M%S')
    with open('./data/cleaned/cols_{}'.format(curtime)) as f:
        f.write(cols_orig)
    
    df.to_csv('./data/cleaned/student-diversity-survey_{}.csv'.format(curtime))


if __name__ == '__main__':
    main(sys.argv[1:])
