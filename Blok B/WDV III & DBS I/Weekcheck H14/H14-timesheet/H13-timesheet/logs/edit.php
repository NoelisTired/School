<!doctype html>
<html lang="nl">

<head>
    <title>TimeSheet / Logs / Nieuw</title>
    <?php require_once '../head.php'; ?>
    <?php
        $id = $_GET['id'];
        require_once '../backend/conn.php';
        $query = "SELECT * FROM logs WHERE id = :id";
        $statement = $conn->prepare($query);
        $statement->execute([
            ":id" => $id,
        ]);
        $logs = $statement->fetch(PDO::FETCH_ASSOC);
        ?>
</head>

<body>
<?php
if(!isset($_SESSION['user_id']))
{
 $msg = "Je moet eerst inloggen!";
 header("Location: login.php?msg=$msg"); 
 exit; 
}
?>

    <?php require_once '../header.php'; ?>
    <div class="container">

        <h1>TimeSheet / Logs / Nieuw</h1>

        <form action="../backend/logsController.php" method="POST">
            <input type="hidden" name="action" value="update">
            <input value="<?php echo $_GET['id'];?>" name="id" type="hidden">
        
            <div class="form-group">
                <p>Datum: <?php echo date("Y-m-d"); ?></p>
            </div>

            <div class="form-group">
                <label for="duration">Duur (uren):</label>
                <input type="number" name="duration" id="duration" class="form-input" value="<?php echo $logs['duration']?>">
            </div>
            <div class="form-group">
                <p>afdeling: <?php echo $logs['department']?></p>
            </div>

            <input type="submit" value="Log aanpassen">

            <div class="form-group">
                <form action="../backend/logsController.php" method="POST">
                <input type="hidden" name="action" value="delete">
                    <input type="submit" value="verwijderen">
                </form>
            </div>
            
        </form>

    </div>

</body>

</html>
