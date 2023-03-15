<?php

$action = $_POST['action'];
if($action == "edit"){
    //Haal variabelen op, doe inputvalidatie
    $title = $_POST['title'];
    if(empty($title))
    {
        die("Vul een titel in");
    }
    $content = $_POST['content'];
    if(empty($content))
    {
        die("Vul een content in");
    }
    $id = $_POST['id'];

    //1. Haal de verbinding erbij
    require_once 'conn.php';

    //2. Schrijf query met placeholders
    $query = "UPDATE berichten SET title = :title, content = :content WHERE id = :id";
    
    //3. Zet query om naar statement
    $statement = $conn->prepare($query);

    //4. Voer statement uit, geef nu waarden mee voor de placeholders
    $statement->execute([
        ':title' => $title,
        ':content' => $content,
        ':id' => $id
    ]);

    //5. Niet van toepassing bij een UPDATE-query

    //Stuur gebruiker terug naar lijst met berichten (index.php in hoofdmap)
    header("Location: ../index.php");

}

if($action == "delete"){
    $id = $_POST['id'];
    require_once 'conn.php';
    $query = "DELETE FROM berichten WHERE id = :id";
    $statement = $conn->prepare($query);
    $statement->execute([
        ':id' => $id
    ]);
    header("Location: ../index.php");
}

