<?php
require_once 'backend/config.php';
session_start();
session_destroy();
header("Location: $base_url/index.php");
exit;