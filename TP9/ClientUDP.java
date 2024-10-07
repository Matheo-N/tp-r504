import java.io.*;
import java.net.*;

public class ClientUDP
	{
    public static void main(String[] args) throws IOException
	{
        // Adresse du serveur
        InetAddress addr = InetAddress.getLocalHost();
        System.out.println("Adresse = " + addr.getHostName());

        // Chaîne à envoyer
        String s = "Hello World";
        // Conversion de la chaîne en tableau de bytes
        byte[] data = s.getBytes();

        // Création d'un paquet avec les données à envoyer au serveur sur le port 1234
        DatagramPacket packet = new DatagramPacket(data, data.length, addr, 1234);

        // Création d'un socket pour envoyer le paquet
        DatagramSocket sock = new DatagramSocket();
        sock.send(packet); // Envoi du paquet
        sock.close(); // Fermeture du socket
    }
}

