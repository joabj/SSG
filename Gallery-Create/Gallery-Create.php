<html>
 <head>
  <title>A gallery of photos has been created</title>
 </head>
 <body>
 <?php 
	$Command = "python /var/www/Photos/code/Gallery-Create/Gallery-Create.py ";
	exec($Command);
	print $return_value;
?>

 
 
 
 <p>
    <FORM METHOD="LINK" ACTION="http://www.joabj.com/House/Home.html">
<INPUT TYPE="submit" VALUE="Home">
</FORM>
 
 
 </body>
</html>