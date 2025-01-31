import java.io.*;
import java.net.*;

public class ClientTCP3 {
    public static void main(String[] args) {
        if (args.length < 1) {
            System.out.println("Veuillez fournir un message en argument.");
            return;
        }

        try {
            // Connexion au serveur localhost sur le port 2016
            Socket socket = new Socket("localhost", 2016);

            // Création du flux de sortie pour envoyer des données
            DataOutputStream dOut = new DataOutputStream(socket.getOutputStream());

            // Envoi du message passé en argument
            dOut.writeUTF(args[0]);

            // Création du flux d'entrée pour recevoir la réponse du serveur
            DataInputStream dIn = new DataInputStream(socket.getInputStream());

            // Réception du message inversé du serveur
            String messageRecu = dIn.readUTF();
            System.out.println("Message inversé reçu du serveur : " + messageRecu);

            // Fermeture des flux et du socket
            dIn.close();
            dOut.close();
            socket.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}

