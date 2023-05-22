<?php

    session_start();

    require_once 'conn.php';

    $username = $_POST['username'];
    if(empty($username)){
        $errors[] = "Invalide wachtwoord!";
    }

    $name = $_POST['name'];
    if(empty($username)){
        $errors[] = "Invalide wachtwoord!";
    }

    $password = $_POST['password'];
    if(empty($password)){
        $errors[] = "Invalide wachtwoord!";
    }
    $pass = password_hash($password, PASSWORD_DEFAULT);

    if(isset($errors)){
        header("Location: ../login.php?msg='Invalide inloggegevens!");
        die();
    }

    $query = "INSERT INTO users (username, name, password) VALUES (:username, :name, :password)";
    $statement = $conn->prepare($query);
    $statement->execute([
        ":username" => $username,
        ":name" => $name,
        ":password" => $pass
    ]);

    $user = $statement->fetch(PDO::FETCH_ASSOC);
    $_SESSION['user_id'] = $user['id'];
    $_SESSION['username'] = $username;
    $_SESSION['name'] = $name;
    $_SESSION['password'] = $password;
    header("Location: ../logs/index.php?msg=acc-created"); 