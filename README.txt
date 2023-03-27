My project is about tanks. The app allows the user to see a list of tanks, 
to add a new one, to modify the caracterisitics and also to delete one of the tanks. 
(CRUD operations are working). The tank object has 4 caracteristics: The tank name (String), the nationality (String), 
the number of crewmates (Int) and the turret (Boolean). On the app, there are two main links: 
One to see the list of the tanks with their caracteristics (on whiwh we can also update and delete them, and the other is to create new tanks.

Firstly, I created the project and the app on PyCharm, using Django. T
hen, I needed to create a urls.py file in my tanks_app folder to display the content of the views file. 
I also created a models.py file to add all the data fields of my tank object(name, number of crewmates, nationality, turret). 
I made several html pages in order to make the CRUD operations work. 
I had some difficulties to make the update and the delete methods work, but I successed to achieve it in time. 
To make my app more understandable and easy to use, I linked the Create operation to the Home page, 
in order to put the user back in the home page after he has submitted a new tank to Create. 
The Update and the Delete operation are linked to an other html page on which we can see if the update (or the delete) worked, 
and there is a link to come back to the page on which there is the list of the tanks.

After that, I implemented the login, logout, sign up and password reset fonctionnalities. 
I quite struggled to make the password reset part work, but the other parts are working as intended, 
with a login and a sign up html pages which are no more available on the app if the user is arleady logged in, 
so and in that case he can log out by using a provided button.

Tests have also been added, working as intended

Link to the github : https://github.com/victormandelaire/back-end_Dorset