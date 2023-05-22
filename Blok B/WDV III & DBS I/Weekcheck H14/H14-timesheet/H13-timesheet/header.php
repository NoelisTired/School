<?php require_once 'backend/config.php'; ?>

<header>
    <div class="container">
        <nav>
            <a href="<?php echo $base_url; ?>/index.php">Home</a> |
            <a href="<?php echo $base_url; ?>/logs/index.php">Logs</a>
        </nav>
        <div class="account">
            <?php if(!isset($_SESSION['user_id'])): ?>
                <p> <a href="<?php echo $base_url; ?>/login.php">Inloggen</a> | </p>
                <p><a href="register.php">registreren</a></p>
            <?php else: ?>
                <?php echo $_SESSION['username'];?>
                <p> | <a href="<?php echo $base_url; ?>/logout.php">Uitloggen</a></p>
            <?php endif; ?>
        </div>
    </div>
</header>
