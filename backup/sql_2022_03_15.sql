/*
SQLyog Community Edition- MySQL GUI v8.03 
MySQL - 5.6.12-log : Database - student_info
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`student_info` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `student_info`;

/*Table structure for table `attendance` */

DROP TABLE IF EXISTS `attendance`;

CREATE TABLE `attendance` (
  `attendance_id` int(11) NOT NULL AUTO_INCREMENT,
  `student_id` int(11) NOT NULL,
  `month` int(11) NOT NULL,
  `year` int(11) NOT NULL,
  `percentage` int(11) NOT NULL,
  PRIMARY KEY (`attendance_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `attendance` */

/*Table structure for table `chat` */

DROP TABLE IF EXISTS `chat`;

CREATE TABLE `chat` (
  `chat_id` int(11) NOT NULL AUTO_INCREMENT,
  `from_id` int(11) NOT NULL,
  `to_id` int(11) NOT NULL,
  `message` varchar(200) NOT NULL,
  `date` date NOT NULL,
  `type` varchar(50) NOT NULL,
  PRIMARY KEY (`chat_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `chat` */

/*Table structure for table `collegenotification` */

DROP TABLE IF EXISTS `collegenotification`;

CREATE TABLE `collegenotification` (
  `notification_id` int(11) NOT NULL AUTO_INCREMENT,
  `notification_type` varchar(50) NOT NULL,
  `notification_date` date NOT NULL,
  `notification` varchar(50) NOT NULL,
  PRIMARY KEY (`notification_id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

/*Data for the table `collegenotification` */

insert  into `collegenotification`(`notification_id`,`notification_type`,`notification_date`,`notification`) values (3,'special programs','2022-03-12','cultural programs\r\n'),(6,'Hall Ticket','2022-03-12','wwwwwwwwwwwww'),(8,'Fees','2022-03-15','boomchika vava');

/*Table structure for table `course` */

DROP TABLE IF EXISTS `course`;

CREATE TABLE `course` (
  `course_id` int(11) NOT NULL AUTO_INCREMENT,
  `course_name` varchar(50) NOT NULL,
  PRIMARY KEY (`course_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `course` */

insert  into `course`(`course_id`,`course_name`) values (1,'BCA'),(2,'B.Com'),(6,'BSc');

/*Table structure for table `fee` */

DROP TABLE IF EXISTS `fee`;

CREATE TABLE `fee` (
  `fee_id` int(11) NOT NULL AUTO_INCREMENT,
  `course_id` int(11) DEFAULT NULL,
  `semester` varchar(20) DEFAULT NULL,
  `fee` int(11) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `last_date` date DEFAULT NULL,
  PRIMARY KEY (`fee_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `fee` */

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `password` varchar(10) NOT NULL,
  `type` varchar(20) NOT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`login_id`,`username`,`password`,`type`) values (1,'reo@gmail.com','5465468779','student'),(2,'reo@gmail.com','5465468779','student'),(3,'reo@gmail.com','5465468779','student');

/*Table structure for table `mark` */

DROP TABLE IF EXISTS `mark`;

CREATE TABLE `mark` (
  `mark_id` int(11) NOT NULL AUTO_INCREMENT,
  `subject_id` int(11) NOT NULL,
  `student_id` int(11) NOT NULL,
  `mark` int(11) NOT NULL,
  PRIMARY KEY (`mark_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `mark` */

/*Table structure for table `staff` */

DROP TABLE IF EXISTS `staff`;

CREATE TABLE `staff` (
  `staff_id` int(11) NOT NULL AUTO_INCREMENT,
  `staff_name` varchar(50) DEFAULT NULL,
  `gender` varchar(10) DEFAULT NULL,
  `dob` date DEFAULT NULL,
  `course_id` int(11) DEFAULT NULL,
  `email_id` varchar(50) DEFAULT NULL,
  `photo` varchar(200) DEFAULT NULL,
  `phone_number` bigint(10) DEFAULT NULL,
  `place` varchar(20) DEFAULT NULL,
  `city` varchar(20) DEFAULT NULL,
  `pin_code` bigint(11) DEFAULT NULL,
  `login_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`staff_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `staff` */

/*Table structure for table `student` */

DROP TABLE IF EXISTS `student`;

CREATE TABLE `student` (
  `student_id` int(11) NOT NULL AUTO_INCREMENT,
  `student_name` varchar(50) NOT NULL,
  `gender` varchar(10) NOT NULL,
  `dob` date NOT NULL,
  `course` varchar(11) NOT NULL,
  `semester` varchar(50) NOT NULL,
  `email_id` varchar(50) NOT NULL,
  `photo` varchar(200) NOT NULL,
  `phone_number` bigint(11) NOT NULL,
  `place` varchar(50) NOT NULL,
  `city` varchar(50) NOT NULL,
  `pin_code` bigint(12) NOT NULL,
  `login_id` int(11) NOT NULL,
  PRIMARY KEY (`student_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `student` */

insert  into `student`(`student_id`,`student_name`,`gender`,`dob`,`course`,`semester`,`email_id`,`photo`,`phone_number`,`place`,`city`,`pin_code`,`login_id`) values (2,'sufail','Male','1549-12-06','1','6','reo@gmail.com','/static/staff_images/wallpaperflare.com_wallpaper.jpg',5465468779,'clt','usa',584125,2),(3,'aravind','Male','0454-08-04','1','5','reo@gmail.com','/static/staff_images/wallpaperflare.com_wallpaper.jpg',5465468779,'clt','usa',584125,3);

/*Table structure for table `subject` */

DROP TABLE IF EXISTS `subject`;

CREATE TABLE `subject` (
  `subject_id` int(11) NOT NULL AUTO_INCREMENT,
  `semester` varchar(50) NOT NULL,
  `subject` varchar(50) NOT NULL,
  `course_id` int(11) NOT NULL,
  PRIMARY KEY (`subject_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

/*Data for the table `subject` */

insert  into `subject`(`subject_id`,`semester`,`subject`,`course_id`) values (7,'2','economics',2),(8,'1','Maths',6);

/*Table structure for table `timetable` */

DROP TABLE IF EXISTS `timetable`;

CREATE TABLE `timetable` (
  `table_id` int(11) NOT NULL AUTO_INCREMENT,
  `course_id` int(11) DEFAULT NULL,
  `semester` varchar(50) DEFAULT NULL,
  `day` varchar(50) DEFAULT NULL,
  `hour` int(11) DEFAULT NULL,
  `subject_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`table_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `timetable` */

/*Table structure for table `universitynotification` */

DROP TABLE IF EXISTS `universitynotification`;

CREATE TABLE `universitynotification` (
  `notification_id` int(11) NOT NULL AUTO_INCREMENT,
  `notification_type` varchar(50) NOT NULL,
  `notification` varchar(50) NOT NULL,
  `url` varchar(500) NOT NULL,
  `ndate` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`notification_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `universitynotification` */

insert  into `universitynotification`(`notification_id`,`notification_type`,`notification`,`url`,`ndate`) values (3,'Exam Notification','first sem','http://results.uoc.ac.in/',NULL),(4,'special programs','football match','https://www.epicsports.me/',NULL),(5,'special programs','cricket','http://results.','2022-03-15'),(7,'special programs','arts','http://results.uoc.ac.in/','2022-03-15');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
