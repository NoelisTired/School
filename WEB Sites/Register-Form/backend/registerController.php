<?php


// ! Ergens zit een error waardoor ik de heletijd de laatste output krijg, en ik krijg hier hoofdpijn van


if(isset($_POST['name']) && isset($_POST['email']) && isset($_POST['password']) && isset($_POST['confirm_password'])) {
    $username = $_POST['name'];
    $email = $_POST['email'];
    $password = $_POST['password'];
    $password2 = $_POST['confirm_password'];

    //If all fields are filled (Advanced validation) [Checking if var is > 0]
    if (strlen($username) > 0 && strlen($email) > 0 && strlen($password) > 0 && strlen($password2) > 0) { 
        if ($password == $password2) {
            $password = password_hash($password, PASSWORD_DEFAULT); //Hashing password
            file_put_contents('users.txt', $username . ',' . $email . ',' . $password . PHP_EOL, FILE_APPEND); //Saving user to file
            if ($result) {
                echo '{"success": "true"}';
                header("Location: login.php");
            }
            else {
                echo '{"success": "false", "error": "Passwords do not match1"}';
            }
        } 
        else {
            echo '{"success": "false", "error": "All fields are required2"}';
        }
    }
    else {
        echo '{"success": "false", "error": "All fields are required3"}';
    }
} 
else {
    echo '{"success": "false", "error": "All fields are required4"}';
}
?>