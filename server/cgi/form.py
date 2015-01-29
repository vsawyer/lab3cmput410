#!/usr/bin/env python
import cgi
print """Content-type:text/html

<form method="post" action="test_form.py">
<textarea name="first name" cols="40" rows="1">
Enter your first name here 
</textarea> <br/>
<textarea name="last name" cols="40" rows="1">
Enter your last name here
</textarea> <br/>
<br/>
<input type="submit" value="Submit">
</form>"""

form = cgi.FieldStorage()
val1 = form.getvalue("birthday")
val2 = form.getvalue("hobby")

print 
print "Your birthday is :"
print val1
print """<br/>
Your hobby is :"""
print val2
print "<br/>"