<?php
session_start();
session_destroy();
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Session-voorbeeld</title>
</head>
<body>

    <?php require_once 'nav.php'; ?>
    <h1>De sessie is nu "destroyed".</h1>
    

</body>
</html>