<?php

$naam = $_POST['name'];
$age = $_POST['age'];
$email = $_POST['email'];
$phone = $_POST['phone'];
$reason = $_POST['reason'];
$message = $_POST['message'];

file_put_contents('contactgegevens.txt', $naam .", ". $age. ", " . $email .", ". $phone . ", " .  $reason . ", " .  $message . PHP_EOL, FILE_APPEND);
Header("Location: index.php?form=success");
?>