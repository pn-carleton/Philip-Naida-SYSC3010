import java.net.*;
import java.util.Scanner;
import java.util.*;
import java.io.*;
import java.nio.*;

public class intSender {
private final static int PACKETSIZE = 100 ;
	public static void main(String[] args) 
   {
	      // Check the arguments
	      if( args.length != 2 )
	      {
	         System.out.println( "usage: java UDPSender host port" ) ;
	         return ;
	      }
	      DatagramSocket socket = null ;
	      try
	      {
	         // Convert the arguments first, to ensure that they are valid
	         InetAddress host = InetAddress.getByName( args[0] ) ;
	         int port         = Integer.parseInt( args[1] ) ;
	         socket = new DatagramSocket() ;
     
	       	 for(int i = 0; i < 10; i++) {
		     Random rand = new Random();
	             int n = rand.nextInt(101);
		     ByteBuffer buf = ByteBuffer.allocate(10);
		     buf.putInt(n);
		     //buf.flip();
		     byte[] data = buf.array();
		     DatagramPacket packet = new DatagramPacket( data, data.length, host, port ) ;
	             socket.send( packet ) ;
		     System.out.println("Sending int: " + n);
		 }
	         System.out.println ("Closing down");
	      }
	      catch( Exception e )
	      {
	         System.out.println( e ) ;
	      }
	      finally
	      {
	         if( socket != null )
	            socket.close() ;
      }
   }
}

