<?php

$username = $_POST['username'];
$password = $_POST['password'];

//1. Haal gegevens van gebruiker op, aan de hand van email/username
//   Vijfstappenplan:
//      1. Haal de verbinding erbij
require_once 'conn.php';
//      2. Schrijf de query met placeholders (SELECT * FROM users WHERE .......)
$query = "SELECT * FROM users WHERE username = :username";
//      3. Zet om naar een prepared-statement
$statement = $conn->prepare($query);
//      4. Voer het statement uit
$statement->execute([
    ':username' => $username
]);
//      5. Haal de gegevens op (tip: je verwacht één resultaat, niet een lijst)
$user = $statement->fetch(PDO::FETCH_ASSOC);
//2. Check of je een resultaat krijgt (anders: account bestaat niet)
//   If-statement, check of "$statement->rowCount()" kleiner is dan 1
if ($statement->rowCount() < 1){
    die("Error: account bestaat niet");
}

//3. Check of het ingevulde wachtwoord klopt met die uit de DB
//   Gebruik hiervoor password_verify(), zie evt. http://php.net/password_verify
if (!password_verify($password, $user['password'])){
    die("Error: wachtwoord niet juist!");
}

//4. Alles alles klopt: stop gebruikersgegevens in de session
$_SESSION['user_id'] = $user['id'];
$_SESSION['user_name'] = $user['username'];

//5. Leid de gebruiker terug naar de hoofdpagina
header("Location: ../index.php");