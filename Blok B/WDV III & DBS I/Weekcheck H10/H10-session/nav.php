<div style="display: flex; justify-content: space-between; align-items: center; min-height: 120px;">

    <nav>
        <a href="index.php">Home</a> | 
        <a href="page2.php">Pagina 2</a> | 
        <a href="page3.php">Pagina 3</a> |
        <a href="clear.php">Session leegmaken</a>
    </nav>

    <pre style="border: 1px dashed lightgrey; padding: 3px;"><?php 
        if(isset($_SESSION)) print_r($_SESSION);
        else echo '$_SESSION bestaat niet';
        ?></pre>

</div>