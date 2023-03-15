<!doctype html>
<html lang="nl">

<head>
    <title>Prikbord</title>
    <?php require_once 'head.php'; ?>
</head>

<body>

    <?php require_once 'header.php'; ?>
    
    <div class="container home">

        <p>Berichten:</p>

        <?php
        require_once 'backend/conn.php';
        $query = "SELECT * FROM berichten";
        $statement = $conn->prepare($query);
        $statement->execute();
        $berichten = $statement->fetchAll(PDO::FETCH_ASSOC);
        ?>

        <ul>
            <?php 
                $idNum = 1;
                foreach($berichten as $bericht){
                    echo "<li><a href='berichten/edit.php?id=$idNum'>{$bericht['title']}</a></li>";
                    $idNum++;
                }
            ?>
        </ul>

    </div>

</body>

</html>
