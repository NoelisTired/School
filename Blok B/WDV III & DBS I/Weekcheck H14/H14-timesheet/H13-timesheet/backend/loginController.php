<?php

session_start();

require_once('conn.php');

$username = $_POST['username'];
    if(empty($username)){
        $errors[] = "Invalide inloggegevens!";
    }

    $password = $_POST['password'];
    if(empty($password)){
        $errors[] = "Invalide inloggegevens!";
    }

    $query = "SELECT * FROM users WHERE username = :username";

    $statement = $conn->prepare($query);
    $statement->execute([
        ":username" => $username
    ]);

    $user = $statement->fetch(PDO::FETCH_ASSOC);

    if($statement->rowCount() < 1){
        die("Invalide inloggegevens!");
    }
    
    if(!password_verify($password, $user['password'])){
        die("Invalide inloggegevens!");
    }
    $_SESSION['user_id'] = $user['id'];
    $_SESSION['username'] = $user['username'];
    $_SESSION['password'] = $password;
    $_SESSION['name'] = $user['naam'];

    header("Location: ../index.php?msg='Logged into " . $username . " succesfully!'"); 