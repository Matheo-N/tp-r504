import java.io.*;
import java.net.*;

public class ServeurTCP1 {
    public static void main(String[] args) 
	{
        try 
		{
            // Création du serveur socket sur le port 2016
            ServerSocket socketserver = new ServerSocket(2016);
            System.out.println("Serveur en attente");

            // Acceptation de la connexion d'un client
            Socket socket = socketserver.accept();
            System.out.println("Connection d'un client");

            // Récupération du flux de données
            DataInputStream dIn = new DataInputStream(socket.getInputStream());

            // Lecture et affichage du message reçu
            System.out.println("Message : " + dIn.readUTF());

            // Fermeture des sockets
            socket.close();
            socketserver.close();
        } 
		catch (IOException e) 
		{
            e.printStackTrace();
        }
    }
}

