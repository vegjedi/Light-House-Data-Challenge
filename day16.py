import sqlite3
import pandas as pd
conn = sqlite3.connect("himalayas.db")

exped = pd.read_sql('select * from exped',conn)     # create expedition full table
members = pd.read_sql('select * from members',conn) # create members full table
peaks = pd.read_sql('select * from peaks',conn)     # create peaks data full table

everest_expeditions=pd.read_sql('''select exped.expid, 
                                          exped.peakid,
                                          peaks.pkname
                                from exped
                                inner join peaks
                                on exped.peakid = peaks.peakid
                                where peaks.pkname == "Everest"
                                ''', conn) # select Expedition ID and Peak ID from expedition table, inner join with Peak ID in peaks table with peak name Everest condition

print('The number of Everest expeditions are', len(everest_expeditions))

everest_members=pd.read_sql('''select  members.expid,
                                       members.peakid,
                                       members.fname || ' ' || members.lname as full_name
                                from members
                                inner join peaks
                                on members.peakid = peaks.peakid
                                where peaks.pkname == "Everest"
                                ''', conn) # select relevant columns plus join full name to count unique name later

print('The number of people went to Everest are', everest_members.full_name.nunique()) # count only unique numbers
