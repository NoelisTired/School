<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="css/style.css">
    <title>Vragenlijst</title>
</head>
<body>
    <main>
        <h1>Vragenlijst</h1>
        <form action="index.php" class="form" method="post">
            <div class="form-group">
                <label for="Reset">Reset Form</label>
                <input type="submit" name="reset" value="Reset">
            </div>
            <div class="form-group">
                <label for="name">Naam</label>
                <input type="text" name="name" id="name" required>
            </div>
            <div class="form-group">
                <label for="age">Leeftijd</label>
                <input type="number" name="age" id="age" required>
            </div>
            <div class="form-group">
                <label for="email">E-mail</label>
                <input type="email" name="email" id="email" required>
            </div>
            <div class="form-group">
                <label for="password">Password</label>
                <input type="password" name="password" id="password" required>
            </div>
            <div class="form-group">
                <label for="phone">Telefoonnummer</label>
                <input type="tel" name="phone" id="phone" required>
            </div>
            <div class="form-group">
                <div class="check">
                    <input type="radio" name="reason" id="reason" value="1" required>
                    <label for="reason">Ik heb een vraag</label>
                </div>
                <div class="check">
                    <input type="radio" name="reason" id="reason" value="2" required>
                    <label for="reason">Ik wil een klacht indienen</label>
                </div>
            </div>
            <div class="form-group">
                <label for="message">Bericht</label>
                <textarea name="message" id="message" cols="30" rows="10" required></textarea>
            </div>
            <div class="form-group">
                <div class="check">
                    <input type="checkbox" name="check" id="check" required>
                    <label for="check">Ik ga akkoord met de algemene voorwaarden</label>
                </div>
                <div class="check">
                    <input type="checkbox" name="check" id="check" required>
                    <label for="check">Ik ga akkoord met de privacy voorwaarden</label>
                </div>
            </div>
            <input type="submit" class="submission" value="Verstuur">
        </form>
    </main>
</body>
</html>