<?php
session_start();
?>

<?php
require_once 'backend/config.php';
if(!isset($_SESSION['user_id']))
{
	$msg = "Je moet eerst inloggen!";
	header("Location: $base_url/login.php?msg=$msg");
	exit;
}

?>


<!doctype html>
<html lang="nl">

<head>
    <title>SecretAnimal</title>
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
        <img src="http://placeimg.com/640/480/animals" alt="logo" class="img-l">
    </div>

</body>

</html>
