<!doctype html>
<html lang="nl">

<head>
    <meta charset="utf-8">
    <title>Fair play in de VOORBEELD-DIVISIE</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <link rel="stylesheet" href="css/normalize.css">
    <link rel="stylesheet" href="css/main.css">
    <link rel="icon" href="favicon.ico" type="image/x-icon" />
    <link rel="preconnect" href="https://fonts.gstatic.com">
    <link
        href="https://fonts.googleapis.com/css2?family=Faster+One&family=Roboto:ital,wght@0,400;0,500;0,700;1,400;1,500&family=Roboto+Mono:wght@400;500&display=swap"
        rel="stylesheet">
    <?php
    $total = file_get_contents("files/totalovertredingen.txt"); #Informatievraag 1
    $average = file_get_contents("files/average.txt"); // Informatievraag 2
    $zwartboek = file_get_contents("files/zwartboek.txt"); // Informatievraag 3
    $eregalerij = file_get_contents("files/eregalerij.txt"); // Informatievraag 4
    $scheidsrechters = file_get_contents("files/scheidsrechters.txt"); // Informatievraag 5
    $bezoekers = file_get_contents("files/stadion_bezoekers.txt"); // Informatievraag 6
    ?>
</head>

<body>
    <div class="container">
        <header>
            <h1>Voorbeeld Divisie</h1>
            <p class="subtitle">Fair-play website</p>
        </header>

        <main>
            <p>De SPORT-bond ziet toe op een eerlijk verloop van de competitie. Onze topsporters dienen een voorbeeld te
                zijn voor de vele amateurs in de sport. Daarom streven we naar <em>fair play</em>; een sportieve omgang
                met elkaar. Daar hoort ook bij dat er weinig overtredingen plaatsvinden tijdens een wedstrijd. Op deze
                website geven we inzicht in het verloop van de competitie tot nu toe. U ziet de wedstrijden met de
                minste overtredingen, maar voor bewustwording brengen we ook de wedstrijden met de <em>meeste</em>
                overtredingen in beeld.</p>
            <div class="row">
                <div class="box half">
                    <h2>Aantal overtredingen:</h2>
                    <p class="number">
                        <?php echo $total ?>
                    </p>
                </div>
                <div class="box half">
                    <h2>Gemiddeld per wedstrijd:</h2>
                    <p class="number"><?php echo $average ?></p>
                </div>
            </div>
            <div class="row">
                <div class="box">
                    <h2>Wedstrijden met de meeste overtredingen:</h2>
                    <pre><?php echo $zwartboek ?></pre>
                </div>
            </div>
            <div class="row">
                <div class="box">
                    <h2>Wedstrijden met minder dan 2 overtredingen (laatste veertien dagen):</h2>
                    <pre><?php echo $eregalerij ?></pre>
                </div>
            </div>
            <div class="row">
                <div class="box">
                    <h2>Scheidsrechters met de meeste overtredingen:</h2>
                    <pre><?php echo $scheidsrechters ?></pre>
                </div>
            </div>
            <div class="row">
                <div class="box">
                    <h2>Hoeveelheid wedstrijdbezoekers :</h2>
                    <pre><?php echo $bezoekers ?></pre>
                </div>
            </div>
        </main>
        <footer>
            <p>Deze website is gemaakt in het kader van een praktijkopdracht bij de opleiding Software Developer, Curio
                Breda.</p>
            <p>&copy; Team X, Pietje Puk en Jan Smit.</p>
        </footer>

    </div>

</body>

</html>