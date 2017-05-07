# ContactAPI

<p><b>A simple API built with Django Rest Framework</b></p>

<p>
<b>Requirements:</b><br>
Django==1.8<br>
Djangorestframework==3.6.2<br>
</p>
<p>
<b>To create a new contact</b> <br>
curl -H "Content-Type: application/json" -X POST -d '{"contact_name": "Mark", "contact_number": "23456","contact_address": "Dallas"}' http://host/api/v1/contact/
</p>

<p>
<b>To get all contacts:</b><br>
$ curl -X GET http://host/api/v1/contact/
</p>

<p>
<b>To get a single contact:</b><br>
$ curl -X GET http://host/api/v1/contact/1
</p>

<p>
<b>To update a contact:</b> <br>
curl -X PUT -H "Content-Type: application/json" -d '{"contact_name": "Mark cubar", "contact_number": "23456","contact_address": "Dallas"}' http://host/api/v1/contact/6/
</p>

<p>
<b>To delete a contact</b> <br>
curl -X GET http://host/api/v1/contact/6/
</p>
