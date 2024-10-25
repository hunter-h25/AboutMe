
    CREATE TABLE twitchjan (
        Game VARCHAR(255) NOT NULL,
        WatchTime INT,
        StreamTime INT,
        PeakViewers INT,
        PeakChannels INT,
        UniqueStreamers INT,
        AverageViewers INT,
        AverageChannels INT,
        AverageViewerToChannelRatio DECIMAL(10,2),
        PRIMARY KEY (Game)
    );
    
    CREATE TABLE twitchfeb (
        Game VARCHAR(255) NOT NULL,
        WatchTime INT,
        StreamTime INT,
        PeakViewers INT,
        PeakChannels INT,
        UniqueStreamers INT,
        AverageViewers INT,
        AverageChannels INT,
        AverageViewerToChannelRatio DECIMAL(10,2),
        PRIMARY KEY (Game)
    );
    
    CREATE TABLE twitchmar (
        Game VARCHAR(255) NOT NULL,
        WatchTime INT,
        StreamTime INT,
        PeakViewers INT,
        PeakChannels INT,
        UniqueStreamers INT,
        AverageViewers INT,
        AverageChannels INT,
        AverageViewerToChannelRatio DECIMAL(10,2),
        PRIMARY KEY (Game)
    );
    
    CREATE TABLE twitchapr (
        Game VARCHAR(255) NOT NULL,
        WatchTime INT,
        StreamTime INT,
        PeakViewers INT,
        PeakChannels INT,
        UniqueStreamers INT,
        AverageViewers INT,
        AverageChannels INT,
        AverageViewerToChannelRatio DECIMAL(10,2),
        PRIMARY KEY (Game)
    );
    
    CREATE TABLE twitchmay (
        Game VARCHAR(255) NOT NULL,
        WatchTime INT,
        StreamTime INT,
        PeakViewers INT,
        PeakChannels INT,
        UniqueStreamers INT,
        AverageViewers INT,
        AverageChannels INT,
        AverageViewerToChannelRatio DECIMAL(10,2),
        PRIMARY KEY (Game)
    );
    
    CREATE TABLE twitchjun (
        Game VARCHAR(255) NOT NULL,
        WatchTime INT,
        StreamTime INT,
        PeakViewers INT,
        PeakChannels INT,
        UniqueStreamers INT,
        AverageViewers INT,
        AverageChannels INT,
        AverageViewerToChannelRatio DECIMAL(10,2),
        PRIMARY KEY (Game)
    );
    
    CREATE TABLE twitchjul (
        Game VARCHAR(255) NOT NULL,
        WatchTime INT,
        StreamTime INT,
        PeakViewers INT,
        PeakChannels INT,
        UniqueStreamers INT,
        AverageViewers INT,
        AverageChannels INT,
        AverageViewerToChannelRatio DECIMAL(10,2),
        PRIMARY KEY (Game)
    );
    
    CREATE TABLE twitchaug (
        Game VARCHAR(255) NOT NULL,
        WatchTime INT,
        StreamTime INT,
        PeakViewers INT,
        PeakChannels INT,
        UniqueStreamers INT,
        AverageViewers INT,
        AverageChannels INT,
        AverageViewerToChannelRatio DECIMAL(10,2),
        PRIMARY KEY (Game)
    );
    
    CREATE TABLE twitchsep (
        Game VARCHAR(255) NOT NULL,
        WatchTime INT,
        StreamTime INT,
        PeakViewers INT,
        PeakChannels INT,
        UniqueStreamers INT,
        AverageViewers INT,
        AverageChannels INT,
        AverageViewerToChannelRatio DECIMAL(10,2),
        PRIMARY KEY (Game)
    );
    
    CREATE TABLE twitchoct (
        Game VARCHAR(255) NOT NULL,
        WatchTime INT,
        StreamTime INT,
        PeakViewers INT,
        PeakChannels INT,
        UniqueStreamers INT,
        AverageViewers INT,
        AverageChannels INT,
        AverageViewerToChannelRatio DECIMAL(10,2),
        PRIMARY KEY (Game)
    );
    
    CREATE TABLE twitchnov (
        Game VARCHAR(255) NOT NULL,
        WatchTime INT,
        StreamTime INT,
        PeakViewers INT,
        PeakChannels INT,
        UniqueStreamers INT,
        AverageViewers INT,
        AverageChannels INT,
        AverageViewerToChannelRatio DECIMAL(10,2),
        PRIMARY KEY (Game)
    );
    
    CREATE TABLE twitchdec (
        Game VARCHAR(255) NOT NULL,
        WatchTime INT,
        StreamTime INT,
        PeakViewers INT,
        PeakChannels INT,
        UniqueStreamers INT,
        AverageViewers INT,
        AverageChannels INT,
        AverageViewerToChannelRatio DECIMAL(10,2),
        PRIMARY KEY (Game)
    );
    

CREATE TABLE April2021 (
    Rank VARCHAR(255),
    Channel VARCHAR(255),
    AvgViewers INT,
    TimeStreamed FLOAT,
    AllTimePeakViewers INT,
    HoursWatched FLOAT,
    FollowersGained INT,
    TotalFollowers INT,
    TotalViews INT
);


CREATE TABLE peakviewers(
    Game VARCHAR(255) NOT NULL,
    WatchTime INT,
    StreamTime INT,
    PeakViewers INT,
    PeakChannels INT,
    UniqueStreamers INT,
    AverageViewers INT,
    AverageChannels INT,
    AverageViewerToChannelRatio DECIMAL(10,2),
    PRIMARY KEY (Game)
);