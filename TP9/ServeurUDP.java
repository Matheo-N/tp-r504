import java.io.*;
import java.net.*;

public class ServeurUDP {
    public static void main(String[] args) throws IOException {
        // Création d'un socket UDP sur le port 1234
        DatagramSocket sock = new DatagramSocket(1234);

        // Boucle infinie pour attendre les messages du client
        while (true) {
            System.out.println("- Waiting data");

            // Préparation du buffer pour recevoir les données (1024 octets)
            DatagramPacket packet = new DatagramPacket(new byte[1024], 1024);

            // Réception du paquet
            sock.receive(packet);

            // Conversion des données reçues en chaîne de caractères
            String str = new String(packet.getData());

            // Affichage du message reçu
            System.out.println("str = " + str);
        }
    }
}

