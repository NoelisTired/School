<!doctype html>
<html lang="nl">

<head>
    <title>TimeSheet / Logs</title>
    <?php require_once '../head.php'; ?>
</head>

<body>
<?php
if(!isset($_SESSION['user_id']))
{
 $msg = "Je moet eerst inloggen!";
 header("Location: ../login.php?msg=$msg"); 
 exit; 
}
?>
    <?php require_once '../header.php'; ?>
    <div class="container">
    <?php
        if(isset($_GET['msg']))
        {
            echo "<div class='msg'>" . $_GET['msg'] . "</div>";
        }
        ?>

        <h1>TimeSheet / Logs</h1>
        <a href="create.php">Nieuwe log maken &gt;</a>

        <?php
        require_once '../backend/conn.php';
            if(empty($_GET['department'])){
                $query = "SELECT * FROM logs WHERE user = :user_id ORDER BY date DESC";
                $statement = $conn->prepare($query);
                $statement->execute([
                    "user_id" => $_SESSION['user_id'],
                ]);
            }

            else{
                $query = "SELECT * FROM logs WHERE department = :department";
                $statement = $conn->prepare($query);
                $statement->execute([
                    ":department" => $_GET['department']
                ]);
            }
            $logs = $statement->fetchAll(PDO::FETCH_ASSOC);
        ?>

        <div class="filter">
            <p>Totaal aantal logs: <strong><?php echo count($logs)?></strong></p>
            <div class="filters2">
                <form action="" method="GET">
                    <select name="department" id="department">
                        <option value="">- filter op afdeling -</option>
                        <option value="attracties">attracties</option>
                        <option value="horeca">horeca</option>
                        <option value="techniek">technische Dienst</option>
                        <option value="groen">groen</option>
                        <option value="klantenservice">klantenservice</option>
                        <option value="personeel">personeel</option>
                        <option value="inkoop">inkoop</option>
                    </select>
                    <input type="submit" value="filter">
                </form>
            </div>
            
        </div>

        <table>
            <tr>
                <th>Duur</th>
                <th>Afdeling</th>
                <th>Datum &downarrow;</th>
                <th>Gebruikers-id</th>
                <th>aanpassen</th>
            </tr>
            <?php foreach($logs as $log): ?>
                <tr>
                    <td><p><?php echo $log['duration']; ?>u</p></td>
                    <td><?php echo ucfirst($log['department']); ?></td>
                    <td><?php echo $log['date']; ?></td>
                    <td>#<?php echo $log['user']; ?></td>
                    <td><a href="edit.php?id=<?php echo $log['id'] ?>">aanpassen</a></td>
                </tr>
            <?php endforeach; ?>
        </table>


    </div>

</body>

</html>
