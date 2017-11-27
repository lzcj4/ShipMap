# Host: localhost  (Version 5.7.19)
# Date: 2017-11-27 22:18:56
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

INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$36000$FvQpmxFquw2r$7n62/Py01psZH9tS15jxrc3OaNCvrJDxwV5VdLLq42g=',X'323031372D31312D32372032323A31373A33332E353730313530',1,'admin','','','admin@icare.com',1,1,X'323031372D31312D31352030373A31323A34372E343033373339'),(3,'pbkdf2_sha256$36000$Hp9yLIHDxrVD$jrOyr/V3QMegPyVxO6QDsTI/2z7kmFGQDZ2mBpVHr2E=',NULL,0,'test','','','test@icare.com',0,1,X'323031372D31312D32372032323A31343A31342E393937373033');

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
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;

#
# Data for table "django_content_type"
#

INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(2,'auth','permission'),(3,'auth','group'),(4,'auth','user'),(5,'contenttypes','contenttype'),(6,'sessions','session'),(7,'sysadmin','carbrand'),(8,'sysadmin','carfeature'),(9,'sysadmin','carmodel'),(10,'sysadmin','markfeature'),(11,'sysadmin','markfile'),(12,'sysadmin','markobject'),(13,'sysadmin','marktask'),(14,'sysadmin','markusertask'),(15,'sysadmin','userinfo');

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
) ENGINE=InnoDB AUTO_INCREMENT=46 DEFAULT CHARSET=utf8;

#
# Data for table "auth_permission"
#

INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add car brand',7,'add_carbrand'),(20,'Can change car brand',7,'change_carbrand'),(21,'Can delete car brand',7,'delete_carbrand'),(22,'Can add car feature',8,'add_carfeature'),(23,'Can change car feature',8,'change_carfeature'),(24,'Can delete car feature',8,'delete_carfeature'),(25,'Can add car model',9,'add_carmodel'),(26,'Can change car model',9,'change_carmodel'),(27,'Can delete car model',9,'delete_carmodel'),(28,'Can add mark feature',10,'add_markfeature'),(29,'Can change mark feature',10,'change_markfeature'),(30,'Can delete mark feature',10,'delete_markfeature'),(31,'Can add mark file',11,'add_markfile'),(32,'Can change mark file',11,'change_markfile'),(33,'Can delete mark file',11,'delete_markfile'),(34,'Can add mark object',12,'add_markobject'),(35,'Can change mark object',12,'change_markobject'),(36,'Can delete mark object',12,'delete_markobject'),(37,'Can add mark task',13,'add_marktask'),(38,'Can change mark task',13,'change_marktask'),(39,'Can delete mark task',13,'delete_marktask'),(40,'Can add mark user task',14,'add_markusertask'),(41,'Can change mark user task',14,'change_markusertask'),(42,'Can delete mark user task',14,'delete_markusertask'),(43,'Can add user info',15,'add_userinfo'),(44,'Can change user info',15,'change_userinfo'),(45,'Can delete user info',15,'delete_userinfo');

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
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;

#
# Data for table "django_migrations"
#

INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial',X'323031372D31312D32372032323A31303A30382E363935333337'),(2,'auth','0001_initial',X'323031372D31312D32372032323A31303A31312E363432303334'),(3,'admin','0001_initial',X'323031372D31312D32372032323A31303A31322E313935353231'),(4,'admin','0002_logentry_remove_auto_add',X'323031372D31312D32372032323A31303A31322E323236373838'),(5,'contenttypes','0002_remove_content_type_name',X'323031372D31312D32372032323A31303A31322E393130393138'),(6,'auth','0002_alter_permission_name_max_length',X'323031372D31312D32372032323A31303A31332E333630353430'),(7,'auth','0003_alter_user_email_max_length',X'323031372D31312D32372032323A31303A31332E383531343639'),(8,'auth','0004_alter_user_username_opts',X'323031372D31312D32372032323A31303A31332E383832373134'),(9,'auth','0005_alter_user_last_login_null',X'323031372D31312D32372032323A31303A31342E323333303730'),(10,'auth','0006_require_contenttypes_0002',X'323031372D31312D32372032323A31303A31342E323438363935'),(11,'auth','0007_alter_validators_add_error_messages',X'323031372D31312D32372032323A31303A31342E323935353733'),(12,'auth','0008_alter_user_username_max_length',X'323031372D31312D32372032323A31303A31342E373630393335'),(13,'sessions','0001_initial',X'323031372D31312D32372032323A31303A31352E313132323935'),(14,'sysadmin','0001_initial',X'323031372D31312D32372032323A31303A31392E323236333330');

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

INSERT INTO `django_session` VALUES ('ebui7nc9ca09uqfs6ebpc0tjfjljvnzt','MjkzNTgwZDk2MTY5Zjk0M2QxMTg5NmU1YmI5ODhhM2MzMWM0YzliZTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJlMzExZTE1ZWI3NGYzZDMxNGVlZWRmYzNiN2ZiZThmNjBhMTIxN2E5In0=',X'323031372D31322D31312032323A31373A33332E363533323635'),('o0tpkqxak8kl7t3q0gjl9prcu5dcvwcy','OTVkYTk4N2E2NDFlM2Q0NmNmYWY4Yjk1NmQzYWNhOTU4MjY5ZGM0ODp7fQ==',X'323031372D31322D31312032323A31343A31352E313934343732');

#
# Structure for table "sysadmin_carbrand"
#

DROP TABLE IF EXISTS `sysadmin_carbrand`;
CREATE TABLE `sysadmin_carbrand` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `index_char` varchar(10) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

#
# Data for table "sysadmin_carbrand"
#


#
# Structure for table "sysadmin_carmodel"
#

DROP TABLE IF EXISTS `sysadmin_carmodel`;
CREATE TABLE `sysadmin_carmodel` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `brand_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `sysadmin_carmodel_brand_id_ac8a7afc_fk_sysadmin_carbrand_id` (`brand_id`),
  CONSTRAINT `sysadmin_carmodel_brand_id_ac8a7afc_fk_sysadmin_carbrand_id` FOREIGN KEY (`brand_id`) REFERENCES `sysadmin_carbrand` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

#
# Data for table "sysadmin_carmodel"
#


#
# Structure for table "sysadmin_carfeature"
#

DROP TABLE IF EXISTS `sysadmin_carfeature`;
CREATE TABLE `sysadmin_carfeature` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `market_year` int(11) NOT NULL,
  `front` varchar(100) NOT NULL,
  `front_photo` varchar(100) NOT NULL,
  `back` varchar(100) NOT NULL,
  `back_photo` varchar(100) NOT NULL,
  `model_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `sysadmin_carfeature_model_id_0f7f41cf_fk_sysadmin_carmodel_id` (`model_id`),
  CONSTRAINT `sysadmin_carfeature_model_id_0f7f41cf_fk_sysadmin_carmodel_id` FOREIGN KEY (`model_id`) REFERENCES `sysadmin_carmodel` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

#
# Data for table "sysadmin_carfeature"
#


#
# Structure for table "sysadmin_marktask"
#

DROP TABLE IF EXISTS `sysadmin_marktask`;
CREATE TABLE `sysadmin_marktask` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `date_created` datetime(6) NOT NULL,
  `user_created_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `sysadmin_marktask_user_created_id_f14eca21_fk_auth_user_id` (`user_created_id`),
  CONSTRAINT `sysadmin_marktask_user_created_id_f14eca21_fk_auth_user_id` FOREIGN KEY (`user_created_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

#
# Data for table "sysadmin_marktask"
#


#
# Structure for table "sysadmin_markfile"
#

DROP TABLE IF EXISTS `sysadmin_markfile`;
CREATE TABLE `sysadmin_markfile` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `file_name` varchar(100) NOT NULL,
  `file_path` varchar(500) NOT NULL,
  `task_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `sysadmin_markfile_task_id_67dc06f1_fk_sysadmin_marktask_id` (`task_id`),
  CONSTRAINT `sysadmin_markfile_task_id_67dc06f1_fk_sysadmin_marktask_id` FOREIGN KEY (`task_id`) REFERENCES `sysadmin_marktask` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

#
# Data for table "sysadmin_markfile"
#


#
# Structure for table "sysadmin_markobject"
#

DROP TABLE IF EXISTS `sysadmin_markobject`;
CREATE TABLE `sysadmin_markobject` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `file_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `sysadmin_markobject_file_id_1dc58096_fk_sysadmin_markfile_id` (`file_id`),
  CONSTRAINT `sysadmin_markobject_file_id_1dc58096_fk_sysadmin_markfile_id` FOREIGN KEY (`file_id`) REFERENCES `sysadmin_markfile` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

#
# Data for table "sysadmin_markobject"
#


#
# Structure for table "sysadmin_markfeature"
#

DROP TABLE IF EXISTS `sysadmin_markfeature`;
CREATE TABLE `sysadmin_markfeature` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `object_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `sysadmin_markfeature_object_id_7c3dc6b5_fk_sysadmin_` (`object_id`),
  CONSTRAINT `sysadmin_markfeature_object_id_7c3dc6b5_fk_sysadmin_` FOREIGN KEY (`object_id`) REFERENCES `sysadmin_markobject` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

#
# Data for table "sysadmin_markfeature"
#


#
# Structure for table "sysadmin_markusertask"
#

DROP TABLE IF EXISTS `sysadmin_markusertask`;
CREATE TABLE `sysadmin_markusertask` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `task_id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `sysadmin_markusertask_task_id_f89c715f_fk_sysadmin_marktask_id` (`task_id`),
  KEY `sysadmin_markusertask_user_id_769f9570_fk_auth_user_id` (`user_id`),
  CONSTRAINT `sysadmin_markusertask_task_id_f89c715f_fk_sysadmin_marktask_id` FOREIGN KEY (`task_id`) REFERENCES `sysadmin_marktask` (`id`),
  CONSTRAINT `sysadmin_markusertask_user_id_769f9570_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

#
# Data for table "sysadmin_markusertask"
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
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

#
# Data for table "sysadmin_userinfo"
#

INSERT INTO `sysadmin_userinfo` VALUES (1,'',3),(2,'',1);
