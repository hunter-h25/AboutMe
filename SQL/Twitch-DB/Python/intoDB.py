



listOfFiles = ['twitchjan.csv','twitchfeb.csv','twitchmar.csv','twitchapr.csv','twitchmay.csv','twitchjun.csv','twitchjul.csv','twitchaug.csv','twitchsep.csv','twitchoct.csv','twitchnov.csv','twitchdec.csv']
listOfTables = ['twitchjan','twitchfeb','twitchmar','twitchapr','twitchmay','twitchjun','twitchjul','twitchaug','twitchsep','twitchoct','twitchnov','twitchdec']

sql = ""
# for i in range(len(listOfTables)):

#     sql += f'''
#     CREATE TABLE {listOfTables[i]} (
#         Game VARCHAR(255) NOT NULL,
#         WatchTime INT,
#         StreamTime INT,
#         PeakViewers INT,
#         PeakChannels INT,
#         UniqueStreamers INT,
#         AverageViewers INT,
#         AverageChannels INT,
#         AverageViewerToChannelRatio DECIMAL(10,2),
#         PRIMARY KEY (Game)
#     );
#     '''
#     f = open("script.sql","w")
#     f.write(sql)
#     f.close()

for i in range(len(listOfFiles)):
    sql += f'''
            LOAD DATA LOCAL INFILE '/home/cs12/Documents/BugBounty/{listOfFiles[i]}'
            INTO TABLE {listOfTables[i]}
            FIELDS TERMINATED BY ','
            ENCLOSED BY '"'
            LINES TERMINATED BY '\n'
            IGNORE 1 ROWS;
          '''

    f = open("insert.sql","w")
    f.write(sql)
    f.close()
