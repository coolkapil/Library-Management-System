A Simple Library management system in which an admin can perform CRUD part and students can only view the list of books.



                                       *Documentation*

                            TechStacks={Python3, django, mysql}

            

Here we go for authentication part------

The default django user model is being used for students as well as admin user where admin user can perform the CRUD(create,read, update,delete) on Books and students can only view the list of books .The  field is separating those(admin and students) is "is_staff" field like for admin is_staff=True but for students is_staff is False.

Note=There is a mixin in permission.py file for "is_staff".

 
URLs  for signup-

 Admin signup= /staff/signup/

 Students/users signup = /user/signup/


Also we we are using same login page for Admin and Students.

URls for login-

Admin login =  /staff/login/

Students/user login = /user/login/



Urls for admin to perform CRUD(list,create,update,delete) and only view for students-

list-view = ''

details-view = 'book/<int:pk>'

create= 'book/create'

update = 'book/update/<int:pk>'

delete = 'book/delete/<int:pk>'