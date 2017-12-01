# Host: localhost  (Version 5.7.19)
# Date: 2017-12-01 10:57:39
# Generator: MySQL-Front 6.0  (Build 2.20)


#
# Data for table "auth_group"
#


#
# Data for table "auth_user"
#

INSERT INTO `auth_user` (`id`,`password`,`last_login`,`is_superuser`,`username`,`first_name`,`last_name`,`email`,`is_staff`,`is_active`,`date_joined`) VALUES (1,'!IpAoPTW2Ld2qu0bTNn3BIIxtbYo8egCs3InJEjXL',NULL,0,'AnonymousUser','','','',0,1,X'323031372D31312D33302031343A30373A32352E323435313338'),(2,'pbkdf2_sha256$36000$ENgZYSYz6OYZ$x+TRWF8NE//Qcg6XRnrWrorGnlzAwNDH4yYhczVx560=',X'323031372D31312D33302031353A35333A34312E353430303335',1,'admin','','','admin@icare.com',0,1,X'323031372D31312D33302031343A31333A33352E373434363933'),(3,'pbkdf2_sha256$36000$Rrxn2EKrOpD7$w3wNZatI2vlC6Ef8ud7DQBCg+G0ivntl7Tor4Ex8isA=',NULL,0,'test','','','test@icare.com',0,1,X'323031372D31312D33302031343A31333A33392E353831383034');

#
# Data for table "auth_user_groups"
#


#
# Data for table "django_content_type"
#

INSERT INTO `django_content_type` (`id`,`app_label`,`model`) VALUES (1,'admin','logentry'),(2,'auth','permission'),(3,'auth','group'),(4,'auth','user'),(5,'contenttypes','contenttype'),(6,'sessions','session'),(7,'guardian','groupobjectpermission'),(8,'guardian','userobjectpermission'),(9,'map','radar'),(10,'map','ship'),(11,'map','shipdefencearea'),(12,'map','shiproute'),(13,'map','userinfo');

#
# Data for table "django_admin_log"
#


#
# Data for table "auth_permission"
#

INSERT INTO `auth_permission` (`id`,`name`,`content_type_id`,`codename`) VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add group object permission',7,'add_groupobjectpermission'),(20,'Can change group object permission',7,'change_groupobjectpermission'),(21,'Can delete group object permission',7,'delete_groupobjectpermission'),(22,'Can add user object permission',8,'add_userobjectpermission'),(23,'Can change user object permission',8,'change_userobjectpermission'),(24,'Can delete user object permission',8,'delete_userobjectpermission'),(25,'创建船只',10,'can_create_ship');

#
# Data for table "auth_user_user_permissions"
#


#
# Data for table "auth_group_permissions"
#


#
# Data for table "django_migrations"
#

INSERT INTO `django_migrations` (`id`,`app`,`name`,`applied`) VALUES (1,'contenttypes','0001_initial',X'323031372D31312D33302031343A30373A30372E303337393138'),(2,'auth','0001_initial',X'323031372D31312D33302031343A30373A31332E343134373836'),(3,'admin','0001_initial',X'323031372D31312D33302031343A30373A31342E333733323430'),(4,'admin','0002_logentry_remove_auto_add',X'323031372D31312D33302031343A30373A31342E343133373830'),(5,'contenttypes','0002_remove_content_type_name',X'323031372D31312D33302031343A30373A31352E353932313131'),(6,'auth','0002_alter_permission_name_max_length',X'323031372D31312D33302031343A30373A31362E333939393432'),(7,'auth','0003_alter_user_email_max_length',X'323031372D31312D33302031343A30373A31372E313537363632'),(8,'auth','0004_alter_user_username_opts',X'323031372D31312D33302031343A30373A31372E313935333232'),(9,'auth','0005_alter_user_last_login_null',X'323031372D31312D33302031343A30373A31372E383535323136'),(10,'auth','0006_require_contenttypes_0002',X'323031372D31312D33302031343A30373A31372E393630363238'),(11,'auth','0007_alter_validators_add_error_messages',X'323031372D31312D33302031343A30373A31382E303431373134'),(12,'auth','0008_alter_user_username_max_length',X'323031372D31312D33302031343A30373A31382E383633383238'),(13,'guardian','0001_initial',X'323031372D31312D33302031343A30373A32312E333437323430'),(14,'map','0001_initial',X'323031372D31312D33302031343A30373A32332E353132363033'),(15,'sessions','0001_initial',X'323031372D31312D33302031343A30373A32342E353134383737');

#
# Data for table "django_session"
#

INSERT INTO `django_session` (`session_key`,`session_data`,`expire_date`) VALUES ('bbvwarnkn9h14q7tmdve2uz0epj5ye5w','YTc1YTkyNmZiZjJmOGNkN2NlOGJkZGQzMzIyMjMzZDc5ZTBkMGRiYTp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIzNjJiMjk5YTAwODY1MTFjYzVjMmYyODgyNDZlOTlmNGRkMzk5Y2RkIn0=',X'323031372D31322D31342031353A35333A34312E363235313034');

#
# Data for table "guardian_groupobjectpermission"
#


#
# Data for table "guardian_userobjectpermission"
#


#
# Data for table "map_radar"
#


#
# Data for table "map_ship"
#


#
# Data for table "map_shipdefencearea"
#

INSERT INTO `map_shipdefencearea` (`id`,`name`,`longitude`,`latitude`,`radius`) VALUES (2,'1512037546002',120.01561,30.2827,1634),(3,'1512044499922',120.06228,30.261574,1898);

#
# Data for table "map_shiproute"
#


#
# Data for table "map_userinfo"
#

INSERT INTO `map_userinfo` (`id`,`department`,`user_id`) VALUES (1,'',1),(2,'',2),(3,'',3);
