import java.net.*;
import java.io.*;
import java.util.logging.Logger;

public class GreetingClient {
    public static void main(String[] args) {
        String serverName = args[0];
        int port = Integer.parseInt(args[1]);
        try {
            System.out.println("Connect to server: " + serverName + "\nPort: " + port);
            Socket client = new Socket(serverName, port);
            System.out.println("The remote server IP: " + client.getRemoteSocketAddress());
            OutputStream outToServer = client.getOutputStream();
            DataOutputStream outData = new DataOutputStream(outToServer);

            outData.writeUTF("Hello from" + client.getLocalSocketAddress());
            InputStream inFromServer = client.getInputStream();
            DataInputStream inData = new DataInputStream(inFromServer);

            System.out.println("Server responding: " + inData.readUTF());
            client.close();
        } catch(IOException e) {
            Logger log = Logger.getLogger("2024_8_3_log");
            log.severe(e.toString());
        }
    }
}
