<?php

if ($_GET['file'])
	include_once($_GET['file']);
else {
header('Location: ' . "http://" . $_SERVER['HTTP_HOST'] . $_SERVER['REQUEST_URI'] . "?file=test.txt");
exit;
}
?>
