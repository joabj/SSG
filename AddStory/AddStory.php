<HTML>
<head>
<title>Submit Story</title>
</head>
<BODY>



<?php

  // Connect to the database server

  $open = @mysql_connect("localhost","[USERNAME]", "[PASSWORD]");
  if (!$open) {
    echo( "<P>Can't connect to database!</P>" );
    exit();
  }

$FileName = $_POST["FileName"];
$FileLocation = $_POST["FileLocation"];
$Topic = $_POST["Topic"];
$Subtopic1 = $_POST["Subtopic1"];
$Subtopic2 = $_POST["Subtopic2"];
$Subtopic3 = $_POST["Subtopic3"];
$Subject = $_POST["Subject"];
$Headline = $_POST["Headline"];
$Description = $_POST["Description"];
$Published = $_POST["Published"];
$Publication = $_POST["Publication"];
$Type = $_POST["Type"];
$Art = $_POST["Art"];

$db = ("site");

$SQL = "INSERT into SiteStories values('".$FileName."','".$FileLocation."','".$Topic."','".$Subtopic1."','".$Subtopic2."',
'".$Subtopic3."','".$Subject."','".$Headline."','".$Description."',".$Published.",'".$Publication."','".$Type."','".$Art."')";

$doit = mysql_db_query($db, $SQL);

if (!$doit) {
         echo("It didn't work!!!" . mysql_error() . "\n$SQL\n"); 
		}
else
         echo ("Project entered!");

mysql_close($open);

?>
<p>

<FORM METHOD="LINK" ACTION="http://www.joabj.com/Writing/code/SiteSubmit/AddStory.html">
<INPUT TYPE="submit" VALUE="Again?"></form>


<FORM METHOD="LINK" ACTION="http://joabj.com/Writing/code/Story-Gen/Story-Gen.html">
<INPUT TYPE="submit" VALUE="Create Story Shell?"></form>



<FORM METHOD="LINK" ACTION="http://www.joabj.com/House/Home.html">
<INPUT TYPE="submit" VALUE="Home">
</FORM>
</p>

</body>
</html>
