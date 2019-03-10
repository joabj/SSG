TABLE: SitePhotos

CREATE TABLE SitePhotos (
GalleryID Int NOT NULL AUTO_INCREMENT,
URL varchar(255) NOT NULL,
year Int NOT NULL,
month Int NOT NULL,
Category varchar(3) NOT NULL,
Title varchar(255) NOT NULL,
Description varchar(1000) NOT NULL,
Tag varchar(255) NOT NULL,
Tag varchar(255) NOT NULL,
Tag varchar(255) NOT NULL,
PRIMARY KEY (GalleryID)
)
