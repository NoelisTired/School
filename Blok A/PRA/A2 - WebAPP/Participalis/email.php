<?php
session_start();
$message = "User ".$_POST['email']." would like to get in touch with you";
$webhook= 'https://discord.com/api/webhooks/1041454725473763478/ni-k3CgIOPtqbir4ZOiuVJqAPFThhi7Fu-3h3VS45-yzBNUQX8kpriqp3xH_fTNSU55K';

$data = array('content' => $message);
$options = array(
    'http' => array(
        'header'  => "Content-type: application/x-www-form-urlencoded\r\n",
        'method'  => 'POST',
        'content' => http_build_query($data)
        )
);

file_get_contents($webhook, false, stream_context_create($options));
session_destroy();
header("Location: ".$_SERVER['HTTP_REFERER']);
?>