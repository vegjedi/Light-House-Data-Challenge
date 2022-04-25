import sqlite3
import pandas as pd

conn = sqlite3.connect('himalayas.db')

peaks = pd.read_sql("""select pkname, heightm 
                        from peaks
                        where heightm > 8000
                    """,conn)

len(peaks) # no of peaks are higher than 8000 metres

members = pd.read_sql("""select membid, fname, lname, sex  
                        from members
                        where sex == 'F'
                    """,conn)

len(members) # no of women climbed Himalayas
