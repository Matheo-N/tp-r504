import java.io.*;
import java.net.*;

public class ClientTCP2 {
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

            // Fermeture du socket
            socket.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}

