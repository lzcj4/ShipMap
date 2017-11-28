# Host: localhost  (Version 5.7.19)
# Date: 2017-11-28 18:29:40
# Generator: MySQL-Front 6.0  (Build 2.20)


#
# Structure for table "auth_group"
#

DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

#
# Data for table "auth_group"
#


#
# Structure for table "auth_user"
#

DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

#
# Data for table "auth_user"
#

INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$36000$FvQpmxFquw2r$7n62/Py01psZH9tS15jxrc3OaNCvrJDxwV5VdLLq42g=',X'323031372D31312D32382031373A33373A32392E313534333732',1,'admin','','','admin@icare.com',1,1,X'323031372D31312D31352030373A31323A34372E343033373339'),(3,'pbkdf2_sha256$36000$Hp9yLIHDxrVD$jrOyr/V3QMegPyVxO6QDsTI/2z7kmFGQDZ2mBpVHr2E=',NULL,0,'test','','','test@icare.com',0,1,X'323031372D31312D32372032323A31343A31342E393937373033'),(4,'!DD67zHqHAPW5DFSAIVP9AjRdDqYCVPvvlUtiy589',NULL,0,'AnonymousUser','','','',0,1,X'323031372D31312D32382031383A32383A34312E343336323233');

#
# Structure for table "auth_user_groups"
#

DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

#
# Data for table "auth_user_groups"
#


#
# Structure for table "django_content_type"
#

DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8;

#
# Data for table "django_content_type"
#

INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(2,'auth','permission'),(3,'auth','group'),(4,'auth','user'),(5,'contenttypes','contenttype'),(6,'sessions','session'),(7,'sysadmin','carbrand'),(8,'sysadmin','carfeature'),(9,'sysadmin','carmodel'),(10,'sysadmin','userinfo'),(11,'sysadmin','radar'),(12,'sysadmin','ship'),(13,'sysadmin','shipdefencearea'),(14,'sysadmin','shiproute'),(15,'guardian','groupobjectpermission'),(16,'guardian','userobjectpermission');

#
# Structure for table "django_admin_log"
#

DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

#
# Data for table "django_admin_log"
#


#
# Structure for table "auth_permission"
#

DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8;

#
# Data for table "auth_permission"
#

INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(28,'Can add user info',10,'add_userinfo'),(29,'Can change user info',10,'change_userinfo'),(30,'Can delete user info',10,'delete_userinfo'),(31,'Can add radar',11,'add_radar'),(32,'Can change radar',11,'change_radar'),(33,'Can delete radar',11,'delete_radar'),(34,'Can add ship',12,'add_ship'),(35,'Can change ship',12,'change_ship'),(36,'Can delete ship',12,'delete_ship'),(37,'Can add car brand',7,'add_carbrand'),(38,'Can change car brand',7,'change_carbrand'),(39,'Can delete car brand',7,'delete_carbrand'),(40,'Can add car feature',8,'add_carfeature'),(41,'Can change car feature',8,'change_carfeature'),(42,'Can delete car feature',8,'delete_carfeature'),(43,'Can add car model',9,'add_carmodel'),(44,'Can change car model',9,'change_carmodel'),(45,'Can delete car model',9,'delete_carmodel'),(46,'创建船只',12,'can_create_ship'),(47,'Can add group object permission',15,'add_groupobjectpermission'),(48,'Can change group object permission',15,'change_groupobjectpermission'),(49,'Can delete group object permission',15,'delete_groupobjectpermission'),(50,'Can add user object permission',16,'add_userobjectpermission'),(51,'Can change user object permission',16,'change_userobjectpermission'),(52,'Can delete user object permission',16,'delete_userobjectpermission');

#
# Structure for table "auth_user_user_permissions"
#

DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

#
# Data for table "auth_user_user_permissions"
#


#
# Structure for table "auth_group_permissions"
#

DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

#
# Data for table "auth_group_permissions"
#


#
# Structure for table "django_migrations"
#

DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8;

#
# Data for table "django_migrations"
#

INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial',X'323031372D31312D32382031303A35343A34352E333235383632'),(2,'auth','0001_initial',X'323031372D31312D32382031303A35343A35302E393236333932'),(3,'admin','0001_initial',X'323031372D31312D32382031303A35343A35322E313535383632'),(4,'admin','0002_logentry_remove_auto_add',X'323031372D31312D32382031303A35343A35322E323032383231'),(5,'contenttypes','0002_remove_content_type_name',X'323031372D31312D32382031303A35343A35332E353331373333'),(6,'auth','0002_alter_permission_name_max_length',X'323031372D31312D32382031303A35343A35342E333833303937'),(7,'auth','0003_alter_user_email_max_length',X'323031372D31312D32382031303A35343A35352E353738333632'),(8,'auth','0004_alter_user_username_opts',X'323031372D31312D32382031303A35343A35352E363238323332'),(9,'auth','0005_alter_user_last_login_null',X'323031372D31312D32382031303A35343A35362E323636313631'),(10,'auth','0006_require_contenttypes_0002',X'323031372D31312D32382031303A35343A35362E333033353034'),(11,'auth','0007_alter_validators_add_error_messages',X'323031372D31312D32382031303A35343A35362E333530333837'),(12,'auth','0008_alter_user_username_max_length',X'323031372D31312D32382031303A35343A35372E313838353930'),(13,'sessions','0001_initial',X'323031372D31312D32382031303A35343A35372E373632363537'),(14,'sysadmin','0001_initial',X'323031372D31312D32382031303A35353A30362E383134303233'),(15,'sysadmin','0002_auto_20171128_1054',X'323031372D31312D32382031303A35353A31332E393233353734'),(16,'sysadmin','0003_auto_20171128_1126',X'323031372D31312D32382031313A32363A30372E303432393936'),(17,'sysadmin','0004_shipdefencearea_shiproute',X'323031372D31312D32382031383A32363A30332E373330383232'),(18,'sysadmin','0005_auto_20171128_1825',X'323031372D31312D32382031383A32363A30332E393432303837'),(19,'guardian','0001_initial',X'323031372D31312D32382031383A32383A34312E313033363336');

#
# Structure for table "django_session"
#

DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

#
# Data for table "django_session"
#

INSERT INTO `django_session` VALUES ('ht6lrjp0ynx9elg6qmij37d3yfnuoty5','MjkzNTgwZDk2MTY5Zjk0M2QxMTg5NmU1YmI5ODhhM2MzMWM0YzliZTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJlMzExZTE1ZWI3NGYzZDMxNGVlZWRmYzNiN2ZiZThmNjBhMTIxN2E5In0=',X'323031372D31322D31322031373A33373A32392E333233363139');

#
# Structure for table "sysadmin_radar"
#

DROP TABLE IF EXISTS `sysadmin_radar`;
CREATE TABLE `sysadmin_radar` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `no` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `longitude` double NOT NULL,
  `latitude` double NOT NULL,
  `address` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `no` (`no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

#
# Data for table "sysadmin_radar"
#


#
# Structure for table "sysadmin_ship"
#

DROP TABLE IF EXISTS `sysadmin_ship`;
CREATE TABLE `sysadmin_ship` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `no` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `harbor` varchar(100) NOT NULL,
  `caption` varchar(100) NOT NULL,
  `phone` varchar(100) NOT NULL,
  `address` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `no` (`no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

#
# Data for table "sysadmin_ship"
#


#
# Structure for table "sysadmin_userinfo"
#

DROP TABLE IF EXISTS `sysadmin_userinfo`;
CREATE TABLE `sysadmin_userinfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `department` varchar(100) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `sysadmin_userinfo_user_id_f50d3d69_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

#
# Data for table "sysadmin_userinfo"
#

INSERT INTO `sysadmin_userinfo` VALUES (1,'',3),(2,'',1),(3,'',4);
