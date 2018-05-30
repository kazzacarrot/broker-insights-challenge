To run.

Starting it up requires 2 terminals as the front and back ends are independent. 
In one terminal cd into the backEnd directory and use `python manage.py runserver` to start the backend application. 
In another terminal cd into the frontEnd directory and use `ng serve` to start up the angular app on the front end.

Open up localhost:4200 (or whichever port ng serve suggests) and you would be able to see the list of polices.

Features:

You can click on them to see more information.

Improvements:
1.  Take advantage of the API. Its only using one endpoint: http://localhost:8000/api/policy/ and its ignoring the meta data that gets shipped along with the objects. It could be cool to make a chart comparing the number of customers against the number of policies for each insurer. Are aviva customers more likely than QBE customers to buy multiple policies?

2. Add new policy 

3. Update policy

4. Delete policy
