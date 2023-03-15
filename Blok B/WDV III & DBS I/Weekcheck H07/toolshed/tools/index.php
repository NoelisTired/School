<!doctype html>
<html lang="nl">

<head>
    <title>Toolshed / Tools</title>
    <?php require_once '../head.php'; ?>
</head>

<body>

    <?php require_once '../header.php'; ?>
    
    <div class="container">
        <h1>Tools</h1>
        <a href="create.php">Nieuwe tool &gt;</a>

        <?php require_once '../backend/conn.php';
            $query = "SELECT * FROM tools";
            $statement = $conn->prepare($query);
            $statement->execute();
            $tools = $statement->fetchAll(PDO::FETCH_ASSOC);
        ?>

        <table>
            <tr>
                <th>Tools</th>
                <th>Gewicht</th>
                <th>Locatie</th>
                <th>Aanschafdatum</th>
            </tr>
            <?php foreach ($tools as $tool): ?>
                <tr>
                    <td><?php echo $tool['title']; ?></td>
                    <td><?php echo $tool['weight']; ?></td>
                    <td><?php echo $tool['location']; ?></td>
                    <td><?php echo $tool['since']; ?></td>
                </tr>
            <?php endforeach; ?>
        </table>



    </div>  

</body>

</html>
