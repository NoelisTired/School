
<!doctype html>
<html lang="nl">

<head>
    <title>TimeSheet</title>
    <?php require_once 'head.php'; ?>
</head>

<body>

    <?php require_once 'header.php'; ?>
    
    <div class="container home">
        <div>
            <div class="title">
                <div>
                    <h1>TimeSheet</h1>
                    <p class="subtext">Inleveropdracht H6</p>
                </div>
                <?php if(isset($_SESSION['user_id'])): ?>
                    <a href="logs/create.php" class="btn">Maak nieuwe log</a>
                <?php endif; ?>
            </div>
            <p>In deze applicatie houden werknemers van DeveloperLand hun gewerkte uren bij. Na je dienst kun je een <em><strong>log</strong></em> maken waarin de datum, gewerkte uren en afdeling worden opgeslagen. Regels:</p>
            <ul>
                <li>Rond af op hele uren (dus 6u20min = 6u / 7u31min = 8u).</li>
                <li>Geef aan voor welke afdeling je hebt gewerkt.</li>
                <li>Voor verschillende afdelingen gewerkt? Maak twee logs.</li>
            </ul>
            <p class="code"><em>Developers note;</em> de database-kolommen staan in het Engels. Bijvoorbeeld: afdeling heet 'departement'.</p>
        </div>
        <img style="max-width: 50%;" src="img/clipart.png" alt="timesheet">

    </div>

    <div class="container">
        <h3 style="margin: 0px;">Laatste drie logs</h3>
        <?php
            if(isset($_SESSION['user_id']))
            {
                require_once 'backend/conn.php';
                $query = "SELECT * FROM logs WHERE user = :user LIMIT 0,3";
                $statement = $conn->prepare($query);
                $statement->execute([":user" => $_SESSION['user_id']]);
                $logs = $statement->fetchAll(PDO::FETCH_ASSOC);
                
                echo "<table>";
                foreach($logs as $log)
                {
                    echo "<tr>";
                    echo "<td>{$log['duration']}u</td>";
                    echo "<td>{$log['department']}</td>";
                    echo "<td>{$log['date']}</td>";
                    echo "</tr>";
                }
                echo "</table>";
            }
            else
            {
                echo "<p><a href='login.php' class='btn'>Login om te bekijken</a>";
            }
            
        ?>
    </div>

</body>

</html>
