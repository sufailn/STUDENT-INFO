from flask import Flask, render_template, request,jsonify
from DBConnection import Db
from flask import Flask, render_template, request, jsonify

from DBConnection import Db

app = Flask(__name__)


@app.route('/login')
def login():
    return render_template("login.html")


@app.route('/login_post', methods=['post'])
def login_post():
    usrname = request.form['textfield']
    pswrd = request.form['textfield2']
    return 'ok'


@app.route('/adm_home')
def adm_home():
    return render_template('admin/home.html')

#
@app.route('/admin_addcollegenotification')
def admin_addcollegenotification():
    return render_template("admin/Add college notification.html")


@app.route('/admin_addcollegenotification_post', methods=['post'])
def admin_addcollegenotification_post():
    notificationtype = request.form['select3']
    notification = request.form['textfield']
    db = Db()
    qry = "INSERT INTO collegenotification(notification_type, notification)  VALUES( '" +notificationtype+ "', '" +notification+ "')"
    id = db.insert(qry)

    return '''<script>alert('Success');window.location='/admin_addcollegenotification'</script>'''


@app.route('/admin_addcourse')
def admin_addcourse():
    return render_template("admin/Add Course.html")


@app.route('/admin_addcourse_post', methods=['post'])
def admin_addcourse_post():
    course = request.form['text']
    db=Db()
    qry="INSERT INTO course(course_name)VALUES('"+course+"')"
    id=db.insert(qry)
    return 'ok'


@app.route('/admin_addfee')
def admin_addfee():
    db = Db()
    # course = request.form['select']
    # semester = request.form['select2']
    # q1=db.selectOne("select * from fee where course_id='"+course+"' and semester='"+semester+"'  ")
    q = "select * from course"
    res = db.select(q)
    return render_template("admin/Add fee.html",data=res)



@app.route('/admin_addfee_post', methods=['post'])
def admin_addfee_post():
    course = request.form['select']
    # course=request.form['']
    semester = request.form['select2']
    fee = request.form['textfield']
    lastdate = request.form['textfield2']
    submit = request.form['button']
    db = Db()
    qry = "INSERT INTO fee(course_id,semester,fee,date,last_date)VALUES('"+course+"','"+semester+"','"+fee+"','"+lastdate+"','"+lastdate+"')"
    id = db.insert(qry)
    return 'ok'


@app.route('/admin_addstaff')
def admin_addstaff():
    q = "select * from course"
    db = Db()
    res = db.select(q)
    return render_template("admin/Add staff.html",data=res)


@app.route('/admin_addstaff_post', methods=['post'])
def admin_addstaff_post():
    staff_name = request.form['textfield']
    dob = request.form['textfield2']
    gender = request.form.get('gender')
    course = request.form['select']
    email = request.form['textfield3']
    phone_number = request.form['textfield4']
    place = request.form['textfield5']
    city = request.form['textfield6']
    pincode = request.form['textfield7']
    photo = request.files['pic']
    photo.save("C:\\Users\\sufao\\PycharmProjects\\STUDENT INFO\\static\\staff_images\\"+photo.filename)
    path='/static/staff_images/'+photo.filename
    db = Db()
    qry1="insert into login(username,password,type)values('"+email+"','"+phone_number+"','staff')"
    res1=db.insert(qry1)
    qry = "INSERT INTO staff(staff_name,gender,dob,course_id,email_id,photo,phone_number,place,city,pin_code,login_id)VALUES('" +staff_name+ "','" +gender+ "','" +dob+ "','"+course+"','" +email+ "','" +phone_number+ "','" +place+ "','" +city+ "','" +pincode+ "','" +path+ "','"+str(res1)+"')"
    id = db.insert(qry)
    return 'ok'


@app.route('/admin_addstudent')
def admin_addstudent():
    q = "select * from course"
    db = Db()
    res = db.select(q)
    return render_template("admin/Add student.html",data=res)

@app.route('/admin_addstudent_post', methods=['post'])
def admin_addstudent_post():
    name = request.form['textfield']
    dob = request.form['textfield2']
    gender = request.form['gender']
    course = request.form['select']
    semester = request.form['select2']
    email = request.form['textfield3']
    phone_number = request.form['textfield4']
    place = request.form['textfield5']
    city = request.form['textfield6']
    pincode = request.form['textfield7']
    photo = request.files['pic1']
    photo.save("C:\\Users\\sufao\\PycharmProjects\\STUDENT INFO\\static\\student_images\\" + photo.filename)
    path = '/static/staff_images/' + photo.filename
    db = Db()
    qry2 = "insert into login(username,password,type)values('" +email+ "','" +phone_number+ "','student')"
    res1 = db.insert(qry2)
    qry = "INSERT INTO student(student_name,gender,dob,course,semester,email_id,photo,phone_number,place,city,pin_code,login_id)VALUES('" + name + "','" + gender + "','" +dob+ "','" + course + "','"+semester+"','" + email + "','" + path + "','"+phone_number+"','" + place + "','" + city + "','" + pincode + "','"+str(res1)+"')"
    id = db.insert(qry)
    return 'ok'



@app.route('/admin_addsubject')
def admin_addsubject():
    q = "select * from course"
    db = Db()
    res = db.select(q)
    return render_template("admin/Add subject.html",data=res)


@app.route('/admin_addsubject_post', methods=['post'])
def admin_addsubject_post():
    course = request.form['select']
    semester = request.form['select2']
    subject = request.form['textfield']
    db = Db()
    qry = "INSERT INTO subject(course_id,semester,subject)VALUES('"+course+"','"+semester+"','"+subject+"')"
    id = db.insert(qry)

    return 'ok'


@app.route('/admin_addtimetable')
def admin_addtimetable():
    q = "select * from course"
    db = Db()
    res = db.select(q)
    return render_template("admin/Add time table.html",data=res)


@app.route('/get_subject')
def get_subject():
    crs=str(request.args.get("id"))
    sem=str(request.args.get("sem"))
    q2 = "select * from subject where semester='"+sem+"' and course_id='"+crs+"'"
    db = Db()
    res = db.select(q2)

    return jsonify(res)


@app.route('/admin_addtimetable_post', methods=['post'])
def admin_addtimetable_post():
    course = request.form['select']
    semester = request.form['select2']
    subject = request.form['select3']
    day = request.form['select4']
    hour = request.form['select5']
    submit = request.form['button']
    db = Db()
    qry = "INSERT INTO timetable(course_id, semester, day, hour, subject_id)  VALUES( '"+course+"', '"+semester+"', '"+day+"', '"+hour+"', '"+subject+"')"
    id = db.insert(qry)

    return 'ok'


@app.route('/admin_adduniversitynotification')
def admin_adduniversitynotification():
    return render_template("admin/Add University notification.html")
    q = "select * from universitynotification"
    db = Db()
    res = db.select(q)
    return render_template("admin/Add University notification.html",data=res)


@app.route('/admin_adduniversitynotification_post', methods=['post'])
def admin_adduniversitynotification_post():
    notificationtype = request.form['select3']
    notification = request.form['textfield']
    url = request.form['textfield1']
    db = Db()
    qry = "INSERT INTO universitynotification(notification_type, notification, url,ndate)  VALUES( '" +notificationtype+ "', '" +notification+ "', '" +url+ "',curdate())"
    id = db.insert(qry)

    return '''<script>alert('Success');window.location='/admin_adduniversitynotification'</script>'''


@app.route('/admin_changepassword')
def admin_changepassword():
    return render_template("admin/Change password.html")


@app.route('/admin_changepassword_post', methods=['post'])
def admin_changepassword_post():
    currentpassword = request.form['textfield']
    newpassword = request.form['textfield2']
    re_enterpassword = request.form['textfield3']
    save = request.form['button']
    return 'ok'


@app.route('/admin_viewcollegenotification')
def admin_viewcollegenotification():
    q = "select * from collegenotification"
    db = Db()
    res = db.select(q)
    print(res)
    return render_template("admin/View College Notification.html",data=res)

@app.route('/admin_deletecollegenotification/<id>')
def admin_deletecollegenotification(id):

    q = "delete from collegenotification where notification_id='"+id+"'"
    db = Db()
    res = db.delete(q)
    print(res)
    return '''<script>alert('deleted');window.location='/admin_viewcollegenotification'</script>'''

@app.route('/admin_editcollegenotification/<id>')
def admin_editcollegenotification(id):
    q = "select * from collegenotification where notification_id='"+id+"'"
    db = Db()
    res = db.selectOne(q)
    print(res)
    return render_template("admin/edit_collegenotification.html",data=res)

@app.route('/admin_editcollegenotification_post', methods=['post'])
def admin_editcollegenotification_post():
    not_id = request.form['h1']
    Notificationtype = request.form['select3']
    Notification = request.form['textfield']
    d = Db()
    qry = "UPDATE collegenotification SET notification_type='"+Notificationtype+"', notification_date=curdate(), notification='"+Notification+"' WHERE notification_id='"+not_id+"'"
    res = d.update(qry)

    return '''<script>alert('Updated');window.location='/admin_viewcollegenotification'</script>'''




@app.route('/admin_viewcourse')
def admin_viewcourse():
    q="select * from course"
    db=Db()
    res=db.select(q)
    print(res)
    return render_template("admin/View course.html",res=res)

@app.route('/admin_deletecourse/<id>')
def admin_deletecourse(id):

    q = "delete from course where course_id='"+id+"'"
    db = Db()
    res = db.delete(q)
    print(res)
    return '''<script>alert('deleted');window.location='/admin_viewcourse'</script>'''

@app.route('/admin_edit_course/<id>')
def admin_edit_course(id):

    q = "select * from course where course_id='"+id+"'"
    db = Db()
    res = db.selectOne(q)
    print(res)
    return render_template("admin/edit_course.html", data=res)

@app.route('/admin_edit_course_post', methods=['post'])
def admin_edit_course_post():
    course_id = request.form['h1']
    course_name = request.form['text']
    d = Db()
    qry = "UPDATE course SET course_name='"+course_name+"' WHERE course_id='"+course_id+"'"
    res = d.update(qry)

    return '''<script>alert('Updated');window.location='/admin_viewcourse'</script>'''


@app.route('/admin_viewfee')
def admin_viewsfee():
    q = "select fee.*, course.course_name from course inner join fee on fee.course_id=course.course_id"
    db = Db()
    res = db.select(q)
    q2 = "select * from Course"
    db = Db()
    res2 = db.select(q2)
    return render_template("admin/View Fee.html",val=res,data=res2)

@app.route('/admin_deletefee/<id>')
def admin_deletefee(id):

    q = "delete from fee where fee_id='"+id+"'"
    db = Db()
    res = db.delete(q)
    print(res)
    return '''<script>alert('deleted');window.location='/admin_viewfee'</script>'''



@app.route('/adminiedit/<id>')
def adminiedit(id):
    q = "select * from fee where fee_id='"+id+"'"
    db = Db()
    re = db.selectOne(q)
    q = "select * from course"
    res = db.select(q)
    return render_template("admin/edit_fee.html",val=re,data=res,k=id)


@app.route('/admin_addfee_post_edit', methods=['post'])
def admin_addfee_poadmin_addfee_post_editst():
    course = request.form['select']
    semester = request.form['select2']
    fee = request.form['textfield']
    lastdate = request.form['textfield2']
    db = Db()
    n=request.form['b']
    qry = "update fee set course_id='"+course+"',semester='"+semester+"',fee='"+fee+"',last_date='"+lastdate+"' where fee_id='"+n+"'"
    yy = db.update(qry)
    return 'ok'


@app.route('/admin_viewstaff')
def admin_viewstaff():
    q = "select * from staff"
    db = Db()
    res = db.select(q)
    print(res)
    return render_template("admin/View staff.html",data=res)

@app.route('/admin_deletestaff/<id>')
def admin_deletestaff(id):

    q = "delete from staff where staff_id='"+id+"'"
    db = Db()
    res = db.delete(q)
    print(res)
    return '''<script>alert('deleted');window.location='/admin_viewstaff'</script>'''

@app.route('/admin_viewstudent')
def admin_viewstudent():
    q = "select student.*, course.course_name from course inner join student  on student.course=course.course_id"
    db = Db()
    res = db.select(q)
    return render_template("admin/View student.html",data=res)

@app.route('/admin_deletestudent/<id>')
def admin_deletestudent(id):

    q = "delete from student where student_id='"+id+"'"
    db = Db()
    res = db.delete(q)
    print(res)
    return '''<script>alert('deleted');window.location='/admin_viewstudent'</script>'''


@app.route('/admin_editstudent/<id>')
def admin_editstudent(id):
    q="select student.*, course.course_name from course inner join student  on student.course=course.course_id where student_id='"+id+"'"
    db = Db()
    res = db.selectOne(q)
    qry = "select * from course"
    db = Db()
    res1 = db.select(qry)
    print(res1)
    return render_template("admin/editstudent.html", data=res,val=res1)

@app.route('/admin_editstudent_post', methods=['post'])
def admin_editstudent_post():
    student_id = request.form['h1']
    student_name = request.form['text']
    dob = request.form['textfield2']
    gender = request.form['gender']
    course = request.form['select']
    semester = request.form['select2']
    email = request.form['textfield3']
    phone_number = request.form['textfield4']
    place = request.form['textfield5']
    city = request.form['textfield6']
    pincode = request.form['textfield7']
    photo = request.files['pic1']
    photo.save("C:\\Users\\sufao\\PycharmProjects\\STUDENT INFO\\static\\student_images\\" + photo.filename)
    path = '/static/staff_images/' + photo.filename
    d = Db()
    qry = "UPDATE student SET student_name='"+student_name+"','" + gender + "','" +dob+ "','" + course + "','"+semester+"','" + email + "','" + path + "','"+phone_number+"','" + place + "','" + city + "','" + pincode + "', WHERE student_id='"+student_id+"'"
    res = d.update(qry)

    return '''<script>alert('Updated');window.location='/admin_editstudent'</script>'''






@app.route('/admin_viewsubject')
def admin_viewsubject():
    qry="select subject.*, course.course_name from course inner join subject on subject.course_id=course.course_id"
    db = Db()
    res = db.select(qry)
    print(res)
    return render_template("admin/view subject.html",val=res)

@app.route('/admin_deletesubject/<id>')
def admin_deletesubject(id):
    d = Db()
    q = "delete from `subject` where subject_id='"+id+"'"
    print(q)
    res = d.delete(q)
    print(res)
    return '''<script>alert('deleted');window.location='/admin_viewsubject'</script>'''

@app.route('/admin_edit_subject/<id>')
def admin_edit_subject(id):

    q = "select subject.*, course.course_name from course inner join subject on subject.course_id=course.course_id where subject_id='"+id+"'"
    db = Db()
    res = db.selectOne(q)
    print(res)
    qry1 = "select * from course"
    res1 = db.select(qry1)

    return render_template("admin/edit_subject.html", data=res, data1=res1,idd=id)

@app.route('/admin_edit_subject_post', methods=['post'])
def admin_edit_subject_post():
    subid = request.form['h1']
    crsid=request.form['select']
    semester = request.form['select2']
    subject = request.form['textfield']
    d = Db()
    qry = "update `subject` set semester='"+semester+"', `subject`='"+subject+"', course_id='"+crsid+"' where subject_id='"+subid+"'"
    res = d.update(qry)

    return '''<script>alert('Updated');window.location='/admin_viewsubject'</script>'''


@app.route('/admin_viewtimetable')
def admin_viewtimetable():
    q = "select * from timetable"
    db = Db()
    res = db.select(q)
    print(res)
    return render_template("admin/view time table.html")


@app.route('/admin_viewuniversitynotification')
def admin_viewuniversitynotification():
    q = "select * from universitynotification"
    db = Db()
    res = db.select(q)
    print(res)
    return render_template("admin/view University notification.html",data=res)

@app.route('/admin_deleteuniversitynotification/<id>')
def admin_deleteuniversitynotification(id):

    q = "delete from universitynotification where notification_id='"+id+"'"
    db = Db()
    res = db.delete(q)
    print(res)
    return '''<script>alert('deleted');window.location='/admin_viewuniversitynotification'</script>'''

@app.route('/admin_edituniversitynotification/<id>')
def admin_edituniversitynotification(id):
    q = "select * from universitynotification where notification_id='"+id+"'"
    db = Db()
    res = db.selectOne(q)
    print(res)
    return render_template("admin/edit_universitynotification.html",data=res)

@app.route('/admin_edituniversitynotification_post', methods=['post'])
def admin_edituniversitynotification_post():
    not_id = request.form['h1']
    Notificationtype = request.form['select3']
    Notification = request.form['textfield']
    url = request.form['textfield1']
    d = Db()
    qry = "UPDATE universitynotification SET notification_type='"+Notificationtype+"',ndate=curdate(), notification='"+Notification+"', url='"+url+"' WHERE notification_id='"+not_id+"'"
    res = d.update(qry)
    print(qry)

    return '''<script>alert('Updated');window.location='/admin_viewuniversitynotification'</script>'''


# ////////////////////////staff///////////////////////////////
@app.route('/staff_home')
def staff_home():
    return render_template('staff/STAFF_HOME.html')


@app.route('/staff_addspecialclassnotification')
def staff_addspecialclassnotification():
    return render_template("staff/Add special class notification.html")


@app.route('/staff_addspecialclassnotification_post', methods=['post'])
def staff_addspecialclassnotification_post():
    return 'ok'


@app.route('/staff_changepassword')
def staff_changepassword():
    return render_template("staff/Change Password.html")


@app.route('/staff_changepassword_post', methods=['post'])
def staff_changepassword_post():
    return 'ok'


@app.route('/staff_login_post', methods=['post'])
def staff_login_post():
    return 'ok'


@app.route('/staff_staffchatbox')
def staff_staffchatbox():
    return render_template("staff/Staff Chat box.html")


@app.route('/staff_staffchatbox_post', methods=['post'])
def staff_staffchatbox_post():
    return 'ok'


@app.route('/staff_viewattedance')
def staff_viewattedance():
    return render_template("staff/View Attedance.html")


@app.route('/staff_viewattedance_post', methods=['post'])
def staff_viewattedance_post():
    return 'ok'


@app.route('/staff_viewinternalmark')
def staff_viewinternalmark():
    return render_template("staff/View internal mark.html")


@app.route('/staff_viewinternalmark_post', methods=['post'])
def staff_viewinternalmark_post():
    return 'ok'


@app.route('/staff_viewspecialclassnotification')
def staff_viewspecialclassnotification():
    return render_template("staff/View Special class notification.html")


@app.route('/staff_viewspecialclassnotification_post', methods=['post'])
def staff_viewspecialclassnotification_post():
    return 'ok'


@app.route('/staff_viewstudent')
def staff_viewstudent():
    return render_template("staff/view student.html")


@app.route('/staff_viewstudent_post', methods=['post'])
def staff_viewstudent_post():
    return render_template("staff/view student.html")


@app.route('/staff_viewtimetable')
def staff_viewtimetable():
    return render_template("staff/View Timetable.html")


if __name__ == '__main__':
    app.run(debug=True)