<?php
session_start();
?>

<!doctype html>
<html lang="nl">

<head>
    <title>SecretAnimal</title>
    <?php require_once 'backend/config.php'; ?>

	<meta charset="utf-8">
	<meta name="description" content="StoringApp voor technische dienst van DeveloperLand">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<link rel="icon" href="<?php echo $base_url; ?>/favicon.ico" type="image/x-icon">
	<link rel="stylesheet" href="<?php echo $base_url; ?>/css/normalize.css">
	<link rel="stylesheet" href="<?php echo $base_url; ?>/css/main.css">
</head>

<body>

    <?php require_once 'header.php'; ?>
    <div class="container home">
        <form action="backend/loginController.php" method="POST">
            <input type="text" name="username" placeholder="user">
            <input type="password" name="password" placeholder="pass">
            <input type="submit" value="Login">
        </form>
    </div>

</body>

</html>
