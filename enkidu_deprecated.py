import subprocess

import googleapiclient
import uuid

from google.oauth2 import service_account
from googleapiclient.discovery import build
from pygments import highlight
from pygments.formatters.img import GifImageFormatter, JpgImageFormatter
from pygments.lexers import get_lexer_by_name

SCOPES = ['https://www.googleapis.com/auth/chat.bot']
SERVICE_ACCOUNT_FILE = 'cred.json'

credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)


def extract(n):
  return n['name']


chat_service = googleapiclient.discovery.build('chat', 'v1',
                                               credentials=credentials)
spaces_list = chat_service.spaces().list().execute()

all_spaces = map(extract, spaces_list['spaces'])
s = """ 
def get_tasks():
  global words
  global probs
  global word_freq_dict
  global Total

  for k in word_freq_dict.keys():
    probs[k] = word_freq_dict[k] / Total
  cmd = request.form['cmd']
  print("curcommans"+cmd)
  similarities = [(Levenshtein.distance(v, cmd)) for v in
                  word_freq_dict.keys()]
  df = pd.DataFrame.from_dict(probs, orient='index').reset_index()
  df = df.rename(columns={ 0: 'Prob'})
  df['Similarity'] = similarities
  df['cmd'] =  word_freq_dict.keys()
  output = df.sort_values(['Similarity'], ascending=True)

"""



