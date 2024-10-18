import java.io.*;
import java.net.*;

public class ServeurTCP3 {
    public static void main(String[] args) {
        try {
            // Création du serveur socket sur le port 2016
            ServerSocket socketserver = new ServerSocket(2016);
            System.out.println("Serveur en attente");

            // Boucle infinie pour garder le serveur actif
            while (true) {
                // Acceptation de la connexion d'un client
                Socket socket = socketserver.accept();
                System.out.println("Connection d'un client");

                // Récupération du flux de données
                DataInputStream dIn = new DataInputStream(socket.getInputStream());

                // Lecture du message reçu
                String messageRecu = dIn.readUTF();
                System.out.println("Message reçu : " + messageRecu);

                // Inversion du message
                String messageInverse = new StringBuilder(messageRecu).reverse().toString();

                // Envoi du message inversé au client
                DataOutputStream dOut = new DataOutputStream(socket.getOutputStream());
                dOut.writeUTF(messageInverse);

                // Fermeture des flux et du socket après traitement
                dIn.close();
                dOut.close();
                socket.close();
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}

