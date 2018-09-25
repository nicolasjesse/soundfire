
-- CREATE DATABASE soundfire;

CREATE TABLE profile (
    code SERIAL PRIMARY KEY,
    name VARCHAR(150) UNIQUE NOT NULL,
    email VARCHAR(70) UNIQUE NOT NULL,
    password VARCHAR(14) NOT NULL,
    picture TEXT NOT NULL,
    type TEXT NOT NULL
);

CREATE TABLE music (
    code SERIAL PRIMARY KEY,
    name VARCHAR(150) UNIQUE NOT NULL,
    artist VARCHAR(150) UNIQUE NOT NULL,
    content TEXT NOT NULL
);

CREATE TABLE genre (
    code SERIAL PRIMARY KEY,
    description VARCHAR UNIQUE NOT NULL
);

CREATE TABLE playlist (
    code SERIAL PRIMARY KEY,
    name VARCHAR UNIQUE NOT NULL,
    publisher BIGINT,
    FOREIGN KEY (publisher) REFERENCES profile(code)
);

CREATE TABLE playlist_music (
    playlist BIGINT,
    music BIGINT,
    PRIMARY KEY (playlist, music),
    FOREIGN KEY (playlist) REFERENCES playlist(code),
    FOREIGN KEY (music) REFERENCES music(code)
);

-- CREATE TABLE playlist_genre (
--     playlist BIGINT,
--     genre BIGINT,
--     PRIMARY KEY (playlist, genre),
--     FOREIGN KEY (playlist) REFERENCES playlist(code),
--     FOREIGN KEY (genre) REFERENCES genre(code)
-- );

CREATE TABLE music_genre (
    music BIGINT,
    genre BIGINT,
    PRIMARY KEY (music, genre),
    FOREIGN KEY (music) REFERENCES music(code),
    FOREIGN KEY (genre) REFERENCES genre(code)
);

CREATE TABLE followers (
    follower BIGINT,
    followed BIGINT,
    PRIMARY KEY (follower, followed),
    FOREIGN KEY (follower) REFERENCES profile(code),
    FOREIGN KEY (follower) REFERENCES profile(code)
);

CREATE TABLE liked_playlists (
    playlist BIGINT,
    profile BIGINT,
    FOREIGN KEY (playlist) REFERENCES playlist(code),
    FOREIGN KEY (profile) REFERENCES profile(code)
);

INSERT INTO genre (description) VALUES ('Rock');
INSERT INTO genre (description) VALUES ('Pop');
INSERT INTO genre (description) VALUES ('Sertanejo');
INSERT INTO genre (description) VALUES ('Funk');
INSERT INTO genre (description) VALUES ('Tech');
INSERT INTO genre (description) VALUES ('Metal');
INSERT INTO genre (description) VALUES ('Reggae');
