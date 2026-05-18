<?php
    /*Vérifier si le formulaire est soumis*/
    if (isset($_POST['submit'])) {
        $id = $_GET['id'];
        $db = DBManagerSingleton::getInstanceDB($GLOBALS['DatabaseCurrentUsed']);
        $params = $db->params;
?>