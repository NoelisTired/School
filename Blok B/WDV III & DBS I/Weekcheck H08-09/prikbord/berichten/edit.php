<!doctype html>
<html lang="nl">

<head>
    <title>Prikbord / Aanpassen</title>
    <?php require_once '../head.php'; ?>
</head>

<body>

    <?php require_once '../header.php'; ?>

    <div class="container">
        <h1>Aanpassen bericht</h1>

        <?php
        //Haal id uit de URL
        $id = $_GET['id'];

        //Voer query uit
        require_once '../backend/conn.php';
        $query = "SELECT * FROM berichten WHERE id = :id";
        //(maak het 5-stappenplan nog af)
        $statement = $conn->prepare($query);
        $statement->execute([
            ':id' => $id
        ]);
        $bericht = $statement->fetch(PDO::FETCH_ASSOC);
        ?>

        <!-- Formulier voor edit: -->
        <form action="../backend/berichtenController.php" method="POST">
            <input type="hidden" name="action" value="edit">
            <input type="hidden" name="id" value="<?php echo $id; ?>">
            
            <div class="form-group">
                <label for="titel">Titel:</label>
                <input type="text" name="title" value="<?php echo $bericht['title']; ?>">
            </div>
            <div class="form-group">
                <label for="content">Content:</label>
                <input type="text" name="content" value="<?php echo $bericht['content']; ?>">
            </div>
            <div class="form-group">
                <input type="submit" value="Aanpassen">
            </div>
                
        </form>

        <!-- Formulier voor delete: -->
        <form action="../backend/berichtenController.php" method="POST">
            <input type="hidden" name="action" value="delete">
            <input type="hidden" name="id" value="<?php echo $id; ?>">
            <input type="submit" value="Verwijder bericht">
        </form>

    </div>  

</body>

</html>
