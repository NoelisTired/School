<?php
session_start();
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
    <h1>Dit is page2.php</h1>
    <p>Hallo, <?php echo $_SESSION['name']; ?></p>
    <p>Je email is, <?php echo $_SESSION['email']; ?></p>
    

</body>
</html>