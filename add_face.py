#!/usr/bin/env python3

import requests
import sqlite3
import json
import sys

# Usage
# ./add_face.py https://raw.githubusercontent.com/ageitgey/face_recognition/master/examples/biden.jpg

conn = sqlite3.connect('face.db')
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS faces (id integer, name string, face_encoding text)')

def add_face(name, url):
  payload = { 'image-url': url }
  # OR { 'image-url': url, 'face-id': 123 } to update url.

  result = requests.post('http://0.0.0.0/face', data=payload).json()

  c.execute(f"INSERT INTO faces VALUES ('{result['faceId']}', '{name}', '{json.dumps(result)}')")

  conn.commit()

if __name__ == '__main__':
  name = sys.argv[1]
  url = sys.argv[2]

  add_face(name, url)
