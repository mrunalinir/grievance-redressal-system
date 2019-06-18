Grievance Redressal System for ESD.
The portal is made using Django 2.0.2.
It can be run on the command line using command "python3 manage.py runserver".

Superuser:
  username: testing
  password: esd@telwap

All other users have password: testing123

4 levels of users:
1. Citizen
  - Can login
  - Lodge a complaint
  - Have a user profile with personal details-ability to edit email and phone number and provision check all complaints posted by them

2. Staff
  - Citizen permissions
  - Have a dashboard of all complaints to view, resolve amd mark as pending/resolved/spam
  - Sort functionality in dashboard

3. Manager
  - Staff permissions
  - Have a dashboard of all complaints logged and resolved/marked as spam with satistics of complaints resolved by staff

  4. Superuser
  - All website access and admin page

  This webiste also comes with registration and forgot password functionality.
  Citizens are intimated by e-mail when a complaint is resolved.



MANAGER AND STAFF LEVELS INSTRUCTIONS:
  The groups and the permissions have been hard coded. But we have to provide the permissions to the groups from the admin page. This is just a one time process.
  Currently user1 has staff access
  User2 has manager access
  user3 has citizen access
  password for all the three users is testing123
