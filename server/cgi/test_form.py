#!/usr/bin/env python
import cgi
form = cgi.FieldStorage()
val1 = form.getvalue("first name")
val2 = form.getvalue("last name")
print "Content-type:text/html"
print 
print "Your first name is :"
print val1
print """<br/>
Your last name is :"""
print val2
print """<br/>

<form method="post" action="form.py">
<textarea name="birthday" cols="40" rows="1">
Enter your birthday
</textarea> <br/>
<textarea name="hobby" cols="40" rows="1">
Enter your hobby
</textarea> <br/>
<br/>
<input type="submit" value="Submit">
</form>"""

