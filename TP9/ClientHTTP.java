import java.io.*;
import java.net.*;

public class ClientHTTP {
    public static void main(String[] args) {
        if (args.length < 1) {
            System.out.println("Usage: java ClientHTTP <hostname>");
            return;
        }

        String hostname = args[0];
        
        try {
            // Ouverture du socket sur le port 80 (HTTP)
            Socket socket = new Socket(hostname, 80);

            // Création des flux d'entrée et de sortie
            OutputStreamWriter osw = new OutputStreamWriter(socket.getOutputStream());
            InputStreamReader isw = new InputStreamReader(socket.getInputStream());

            BufferedWriter bufOut = new BufferedWriter(osw);
            BufferedReader bufIn = new BufferedReader(isw);

            // Création et envoi de la requête HTTP GET
            String request = "GET / HTTP/1.0\r\nHost: " + hostname + "\r\n\r\n";
            bufOut.write(request);
            bufOut.flush(); // Nécessaire pour envoyer la requête

            // Lecture et affichage de la réponse ligne par ligne
            String line = bufIn.readLine();
            while (line != null) {
                System.out.println(line);
                line = bufIn.readLine();
            }

            // Fermeture des flux et du socket
            bufIn.close();
            bufOut.close();
            socket.close();

        } catch (UnknownHostException e) {
            System.out.println("Hôte inconnu : " + e.getMessage());
        } catch (IOException e) {
            System.out.println("Erreur d'E/S : " + e.getMessage());
        }
    }
}

