<?php
session_start();
$action = $_POST['action'];

if($action == 'create')
{
    //Validatie
    $date = $_POST['date'];
    if(empty($date))
    {
        $errors[] = "Vul een datum in!";
    }

    $duration = $_POST['duration'];
    if(empty($duration))
    {
        $errors[] = "Vul een duur in!";
    }

    $department = $_POST['department'];
    if(empty($department))
    {
        $errors[] = "Vul een afdeling in!";
    }

    if(isset($errors))
    {
        var_dump($errors);
        die();
    }

    $user = $_SESSION['user_id'];
    require_once 'conn.php';
    $query = "INSERT INTO logs (department, duration, date, user) VALUES(:department, :duration, :date, :user)";

    $statement = $conn->prepare($query);
    $statement->execute([
        ":date" => $date,
        ":duration" => $duration,
        ":department" => $department,
        ":user" => $user,
    ]);

    header("Location: ../logs/index.php");
    exit;
}

if($action == "update")
{
    $id = $_POST['id'];

    $duration = $_POST['duration'];
    if(empty($duration))
    {
        $errors[] = "Vul een duur in!";
    }

    if(isset($errors))
    {
        var_dump($errors);
        die();
    }

    $user = $_SESSION['user_id'];
    require_once 'conn.php';
    $query = "UPDATE logs SET duration = :duration WHERE id = :id";

    $statement = $conn->prepare($query);
    $statement->execute([
        ":duration" => $duration,
        ":id" => $id,
    ]);

    header("Location: ../logs/index.php");
    exit;
}
if($action == "delete"){
    require_once 'conn.php';

    $id = $_POST['id'];
    $query = "DELETE FROM logs WHERE id = :id";
    $statement = $conn->prepare($query);
    $statement->execute([
        ":id"=>$id,
    ]);


    header("Location: ../logs/index.php");
    exit;
}