# data cleaning for survey results

# python imports
import pandas as pd
from datetime import datetime
from pathlib import Path
import sys

def main(args):
    df = pd.read_csv('./data/raw/student-diversity-survey.csv')
    # clean & document original questions
    cols_orig = df.columns
    df.rename(columns={
        "Submitted At":"datetime_submitted",
        "What Grade are you in?":"grade",
        "What is your Gender?":"gender",
        "What is your Ethnicity?":"ethnicity",
        "How long have you been a student at this school?":"tenure",
        "Everything that happens on campus is connected to the school\'s mission statement.":"scl_mission_cnct",
        "The school is very Christ-Centered.":"scl_christ_centered",
        "School is a \"Happy\" place for me.":"scl_happy",
        "I am comfortable to speak up about issues going on at school.":"scl_speakup",
        "It has been explicitly stated how diversity fits into the school\'s mission statement.":"scl_mission_diverse",
        "The school\'s leadership is excited about diversity.":"scl_ldrshp",
        "The school celebrates the culture of its students.":"scl_celebr",
        "I feel like I belong at my school.":"scl_belong",
        "I have witnessed or experienced bullying on campus (or online) because of cultural differences.":"scl_neg_bully",
        "Students of different backgrounds get along at school.":"scl_getalong",
        "School rules are culturally unbiased":"scl_rules",
        "I regularly attend school-sponsored events (sporting events, student performances, social events, etc.)":"scl_events",
        "Students are disciplined the same, despite their cultural background.":"scl_discipline",
        "I am being equipped to thrive in any cultural environment.":"scl_equipped",
        "We learn about minority people groups, authors, and artists outside of their cultural heritage month. ":"scl_learn",
        "I feel cared for by my teachers":"scl_cared",
        "Chapel encourages students to engage the Christian faith cross-culturally. ":"scl_chapel",
        "I have studied faithful Christians from various American cultures and around the world in classes. ":"scl_cultures",
        "The school has Christian role models from various cultures on campus as employees or guests.":"scl_rlmdls",
        "Any Comments?":"comments"
        }, inplace=True)
    df.columns = [i.replace(' ','_') for i in map(str.lower, df.columns)]
    # visual for empties # sns.heatmap(df.isnull(), cmap='viridis')
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
