<?php
    $host='localhost';
    $port=3306;
    $dbname='contact';
    $user='root';
    $pwd='';

    try {
            $newBD=new PDO('mysql:host=localhost;port=$port;dbname=$dbname',$user,$pwd);
            echo "Connexion établie";

    }catch (PDOException $e){
        die('Erreur :'.$e->getMessage());
    }


?>