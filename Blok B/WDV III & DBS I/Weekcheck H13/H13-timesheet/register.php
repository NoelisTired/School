<!doctype html>
<html lang="nl">

<head>
    <title>TimeSheet</title>
    <?php require_once 'head.php'; ?>
</head>

<body>

    <?php require_once 'header.php'; ?>
    
    <div class="container">

        <h1>TimeSheet / Inloggen</h1>
        <?php
        if(isset($_GET['msg']))
        {
            echo "<div class='msg'>" . $_GET['msg'] . "</div>";
        }
        ?>

        <form action="backend/registerController.php" method="POST">
            <div class="form-group">
                <label for="username">Gebruikersnaam:</label>
                <input type="text" name="username" id="username" placeholder="user...">
            </div>
            <div class="form-group">
                <label for="name">naam:</label>
                <input type="text" name="name" id="name" placeholder="name">
            </div>
            <div class="form-group">
                <label for="password">Wachtwoord:</label>
                <input type="password" name="password" id="password" placeholder="pass">
            </div>
            <input type="submit" value="registreren">
        </form>
    </div>

</body>

</html>
