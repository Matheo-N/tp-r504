import java.io.*;
import java.net.*;

public class ClientTCP1 
{
    public static void main(String[] args) 
	{
        try 
		{
            // Connexion au serveur localhost sur le port 2016
            Socket socket = new Socket("localhost", 2016);

            // Création du flux de sortie pour envoyer des données
            DataOutputStream dOut = new DataOutputStream(socket.getOutputStream());

            // Envoi du message "message test"
            dOut.writeUTF("message test");

            // Fermeture du socket
            socket.close();
        } catch (IOException e) 
		{
            e.printStackTrace();
        }
    }
}

