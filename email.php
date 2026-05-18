<?php
use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\Exception;
use PHPMailer\PHPMailer\SMTP;

// Inclure la librairie PHPMailer

require 'PHPMailer/src/PHPMailer.php';
require 'PHPMailer/src/Exception.php';
require 'PHPMailer/src/SMTP.php';
//require 'PHPMailer/PHPMailerAutoload.php';

// Récupérer les données du formulaire
$nom = htmlspecialchars($_POST['nom']);
$email = htmlspecialchars($_POST['email']);
$tel = htmlspecialchars($_POST['tel']);
$objet = htmlspecialchars($_POST['objet']);
$message = htmlspecialchars($_POST['message']);

// Valider les champs
if (empty($nom) || empty($email) || empty($tel) || empty($message)) {
    die('Erreur: Veuillez remplir tous les champs obligatoires');
}

if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
    die('Erreur: adresse e-mail invalide');
}


// Configuration de PHPMailer
$mail = new PHPMailer(true);
$mail->isSMTP();
$mail->Host = 'smtp.gmail.com';
$mail->Port = 465;
$mail->SMTPSecure = 'ssl';
$mail->SMTPAuth = true;
$mail->Username = 'dnmj.dev@gmail.com';
$mail->Password = 'pajqxomnlceeyifb';
$mail->setFrom($email, $nom);
$mail->addAddress('contact@satellite-ngono.com');
$mail->Subject = 'Nouveau message de www.satellite-ngono.com';
$mail->Body = "Bonjour,\n\n";
$mail->Body .= "Vous avez reçu un nouveau message depuis le formulaire de contact de votre site web.\n\n";
$mail->Body .= "Nom : " . $nom . "\n";
$mail->Body .= "Email : " . $email . "\n";
$mail->Body .= "Téléphone : " . $tel . "\n";
$mail->Body .= "Objet : " . $objet . "\n";
$mail->Body .= "Message : " . $message . "\n\n";
$mail->Body .= "Cordialement, $nom\n";
//$mail->Body = $message;

// Envoyer l'e-mail
if(!$mail->send()) {
    echo 'Erreur: ' . $mail->ErrorInfo;
} else {
    // Redirection vers la page du formulaire
    header('Location: contact.html');
    exit();
}
?>

