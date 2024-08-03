import java.io.*;
import java.net.*;
import java.util.logging.Logger;

public class GreetingServer extends Thread {
    private ServerSocket serverSocket;
    private static Logger log = Logger.getLogger("2024_8_3_log");

    public GreetingServer(int port) throws IOException {
        serverSocket = new ServerSocket(port);
        serverSocket.setSoTimeout(1000);
    }

    public void run() {
        while(true) {
            try{
                System.out.println("Waiting for remote connection, the port is " +
                        serverSocket.getLocalPort() + "...");
                Socket server = serverSocket.accept();
                System.out.println("The remote PC IP is: " + server.getLocalSocketAddress());
                DataInputStream dataIn = new DataInputStream(server.getInputStream());
                System.out.println(dataIn.readUTF());

                DataOutputStream dataOut = new DataOutputStream(server.getOutputStream());
                dataOut.writeUTF("Thank you for connecting me: " + server.getLocalSocketAddress() + "\nGoodbye!");
                server.close();
            } catch (IOException e) {
                log.severe(e.toString());
            }
        }
    }
    public static void main(String[] args) {
        int port = Integer.parseInt(args[0]);
        try {
            Thread thread = new GreetingServer(port);
            thread.run();
        } catch(IOException e) {
            log.severe(e.toString());
        }
    }
}
