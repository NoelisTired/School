<html lang="en">
<head>
    <title>NoelP | My portfolio</title>
    <link rel="shortcut icon" href="favicon.ico" type="image/x-icon">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <link rel="stylesheet" href='css/style.css' />
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js"></script>
    <script src="js/snow.js"></script>
    <script src="js/main.js"></script>
    <script src="https://kit.fontawesome.com/d0514f1901.js" crossorigin="anonymous"></script>
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <meta property="og:type" content="website">
    <meta name="theme-color" content="#9649e8">
    <meta property="og:type" content="website">
    <meta property="og:site_name" content="noelp.live">
    <meta property="og:title" content="NoelP X">
    <meta property="og:description" content="Here my Portfolio">
</head>

<body id="body">
<div class="formPopup" style="display: none; z-index: 9">
    <div class="data info">
        <div class="modal-header">
            <h1 class="white-text hello">Hire Me!</h1>
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><i class="fa-sharp fa-solid fa-circle-xmark" onclick="closeForm();"></i></button>
        </div>
        <div class="modal-body form-credentials form-credentials-modal">
            <form action="/email.php" method="post">
                <div class="form-label-group mt-3">
                    <input type="email" name="email" autocomplete="email" class="form-control" placeholder="Email Address" value="" required="" autofocus="">
                    <label class="form-label-placeholder">Email Address</label>
                </div>
                <br>
                <div class="d-flex justify-content-between align-items-center">
                    <button class="btn btn-primary btn-lg w-20" type="submit" onclick="window.onbeforeunload = null;">Submit</button>
                </div>
                <input type="hidden" name="action" value="login">
            </form>
        </div>
    </div>
    </div>
    <div id="snow" style="display: block;"></div>
    <div class="root">
        <?php
        require_once("db/header.php");
        ?>
        <div class="main continer">
            <div class="info">
                <h3 class="white-text hello">Hallo, ik ben Jerome Populiers 👋</h3>
                <h1 class="white-text maininfo">Participalis BV</h1><span class="gradient gr-1">HEAO propaedeuse</span></h1>
                <div class="white-text socials">
                    <div class="github link">
                        <a href="https://github.com/noelistired" onmouseover="info('github')" onmouseleave="rinfo('github')">
                            <i id="github" class="fa-brands fa-facebook"></i>
                        </a>
                        <span class="linkinfo">
                            GitHub
                        </span>
                    </div>
                    <div class="discord link">
                        <a href="https://discord.com/users/931197476038393937" onmouseover="info('discord')" onmouseleave="rinfo('discord')">
                            <i id="discord" class="fa-brands fa-linkedin"></i>
                        </a>
                        <span class="linkinfo">
                            Discord
                        </span>
                    </div>
                    <div class="telegram link">
                        <a href="https://t.me/NoelP" onmouseover="info('telegram')" onmouseleave="rinfo('telegram')">
                            <i id="telegram" class="fa-brands fa-whatsapp"></i>
                        </a>
                        <span class="linkinfo">
                            Telegram
                        </span>
                    </div>
                    <div class="tiktok link">
                        <a href="https://www.tiktok.com/@noelp_" onmouseover="info('tiktok')" onmouseleave="rinfo('tiktok')">
                            <i id="tiktok" class="fa-brands fa-tiktok"></i>
                        </a>
                        <span class="linkinfo">
                            TikTok
                        </span>
                    </div>
                    <div class="instagram link">
                        <a href="https://www.instagram.com/noelpopuliers.py/" onmouseover="info('instagram')" onmouseleave="rinfo('instagram')">
                            <i id="instagram" class="fa-brands fa-instagram"></i>
                        </a>
                        <span class="linkinfo">
                            Instagram
                        </span>
                    </div>
                </div>
            </div>
        </div>
        <main>
            <div class="projparent">
                <div class="projinfo2">
                    <h2 class="white-text">Over Mij</h2>
                    <p>Find all my experiences, including the position held, the work done and the resources used.</p>
                </div>
                <div id="projects">
                    <!-- <img class="shadow" src="img/logo.png" width="250"> -->
                    <div class="proj">
                        <div class="proj-info">
                            <h1>Transparantie</h1>
                            <p>Om mensen mee te krijgen in mijn plannen, heb ik gemerkt dat door zo open en transparant
als mogelijk is te zijn, ik heel veel tijd bespaar in het wegnemen van mogelijk wantrouwen.
Door eerlijk en open te communiceren, hou je de aandacht van diegenen die je toespreekt
en maakt hen onderdeel van de boodschap. Ik vraag dan ook frequent: “kun je je vinden in
hetgeen zojuist besproken of heb je mogelijk aanvullingen?”. Tevens om ervoor te zorgen
dat beslissingen ook gezamenlijk gedragen worden.</p>
                        </div>
                    </div>
                    <div class="proj">
                        <div class="proj-info">
                            <h1>Vertrouwelijke informatie</h1>
                            <p>Vanzelfsprekend zijn er ook altijd zaken welke een vertrouwelijk karakter hebben, maar dat
geef ik dan ook aan. Bepaalde informatie is gewoon delicaat en vertrouwelijk. Met 30 jaar
ervaring in de financiële sector, waarbij ook de belofte is afgenomen uit hoofde van de Wet
Financieel Toezicht (WFT) vanuit de Autoriteit Financiële Markten (AFM), wordt (zeer)
vertrouwelijke informatie op zeer confidentiële wijze behandeld.</p>
                        </div>
                    </div>
                    <div class="proj">
                        <div class="proj-info">
                            <h1>Begeleiding</h1>
                            <p>Medewerkers van een organisatie die heel succesvol zijn in hun werk, verdienen daar de
credits ook voor. Naast financiële- (bonus of salarisverhoging), organisatorische- (men wordt
‘senior’) of reward-achtige (‘collega van de maand’) beloningen, vraag ik hen om de
ervaringen waardoor iemand er bovenuit steekt te delen vanuit een soort van Mentorschap.
Daarentegen werkt mensen aanspreken op hun disfunctioneren enkel door hen aan te geven
dat ze nooit moeten terugdeinzen om hulp te vragen. Standaard is mijn vraag aan collega’s
die minder functioneren dan anderen: “waarmee kan ik je helpen?”. Niet in de laatste plaats omdat ik oprecht geïnteresseerd ben in mensen en er ontzettend
van kan genieten indien -voor mij- kleine zetjes in de rug, collega’s boven zichzelf kunnen
uitgroeien.</p>
                        </div>
                    </div>
                    <div class="proj">
                        <div class="proj-info">
                            <h1>Pragmatisch</h1>
                            <p>Ik kan gelukkig bogen op een jarenlange ervaring, gecombineerd met een heel sterk netwerk.
Maar wat ik geleerd heb in al die jaren, is dat je telkens tegen moeilijkheden aan kunt lopen, die
op dat moment toch weer anders zijn dan dat ik eerder ben tegen gekomen. Dit soort van
situaties benader ik pragmatisch en zal dat ook overdragen aan diegenen waar ik op dat moment
mee samenwerk. Er is niets mis mee om te zeggen dat je iets niet weet, maar gebaseerd op 30
jaar management ervaring stel ik het volgende voor. Beslissingen moeten genomen worden. Achteraf zal uitwijzen dat het de juiste is.</p>
                        </div>
                    </div>
                </div>
                <div class="projinfo">
                    <h2 class="white-text">My Projects</h2>
                    <p>Find all my experiences, including the position held, the work done and the resources used.</p>
                </div>
            </div>
            <div id="aboutme">
                <div class="aboutmepar">
                    <h2 class="white-text">    Wie is Jerome Populiers</h2>
                    <img src="img/abtme.png" width="450px">
                </div>
                <div class="aboutinfo">
                    <div class="table">
                        <div class="row">
                            <span>In het kort</span>
                            <span>
                            Mijn naam is Jérôme Populiers van Participalis BV en Fiducier BV. Ik ben een autodidactisch
ondernemer, met uitgebreide ervaring in verschillende sectoren. Ik werk voor diverse
opdrachtgevers, in verschillende sectoren op managementniveau, om ondernemingen
operationeel bij te staan. Hierbij kun je denken aan een individuele opdracht tot aan het (tijdelijk) overnemen van het
dagelijks bestuur.
                            </span>
                        </div>
                        <div class="row">
                            <span>Mijn Motto</span>
                            <span>Mijn motto is dat -gebaseerd op het in verschillende keukens te hebben mogen kijken in de
afgelopen 30 jaar- ongeveer 80% van alle managementtaken voor iedere organisatie
vergelijkbaar zijn. De overige 20% aan activiteiten zijn bedrijfsspecifiek. De grote rode draad is dat je als leidinggevende in de gaten moet houden dat je met mensen
omgaat. Mensen, die graag aangestuurd en begeleidt willen worden. Hierbij geef ik mensen
alle ruimte en vertrouwen, waar tegenover staat dat ze dit vertrouwen ook moeten
verdienen. Over het algemeen meen ik dat als je collega’s op een volwassen,
verantwoordelijke manier behandeld, je ook dit ook terug krijgt.
Voor mij is gebleken dat dit model werkt. Waarbij het mijn dagelijkse uitdaging is om
mensen met plezier hun werk te laten uitoefenen: er moet gelachen worden!</span>
                        </div>
                        <div class="row">
                            <span>Afspraak is Afspraak</span>
                            <span>Afspraak is afspraak
Het besturen van vennootschappen is niet veel anders dan het leiding geven aan een afdeling of
aan een team. Alles staat of valt met vertrouwen. Alle betrokkenen dienen ervan uit kunnen gaan
dat afspraak ook echt afspraak is. Overmacht kan natuurlijk altijd, maar helaas zie ik ook dat het
niet nakomen van afspraken een maatschappij-breed probleem geworden is. En dat is heel
jammer.</span>
                        </div>
                        <div class="row">
                            <span>Conflictbemiddeling</span>
                            <span>Ik ben een opgeleid Mediator. Hoewel ik dit niet uitdraag als zijnde praktiserend, is dit de basis
van wat ik elke dag doe. Ik begeleid de omgang tussen mensen, teams. Tussen klanten en
leveranciers of onderhandel bepaalde contracten uit. Nooit met het mes op de keel, maar op een
professionele manier van zaken doen. Rekening houdend met de ‘andere kant van de tafel’.
Het heeft geen enkele zin om een bedrijf verder te pushen, dan dat de reikwijdte is. Ik heb dan
eenmalig een superscherpe prijs, maar van een warme samenwerking zal nooit meer sprake zijn.
Als dit bedrijf het überhaupt overleeft. Een succesvolle onderhandeling kent twee
succesverhalen.</span>
                        </div>
                    </div>
                </div>
            </div>
        </main>
        <?php
        require_once("db/footer.php");
        ?>
    </div>
    <script>
        document.getElementsByClassName("hireme")[0].addEventListener("click", function() {
            openForm();
        });

        function openForm() {
            document.getElementsByClassName("formPopup")[0].style.display = "flex";
        }

        function closeForm() {
            document.getElementsByClassName("formPopup")[0].style.display = "none";
        }
    </script>
</body>

</html>