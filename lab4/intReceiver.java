
import java.net.*;
import java.io.*;
import java.nio.*;

public class intReceiver {

	private final static int PACKETSIZE = 100 ;

	public static void main( String args[] )
	{ 
	      // Check the arguments
	      if( args.length != 1 )
	      {
	         System.out.println( "usage: UDPReceiver port" ) ;
	         return ;
	      }
	      try
	      {
	         // Convert the argument to ensure that is it valid
	         int port = Integer.parseInt( args[0] ) ;

	         // Construct the socket
	         DatagramSocket socket = new DatagramSocket( port ) ;

	         for( int i = 0;i < 10; i++)
	         {
		        System.out.println( "Receiving on port " + port ) ;
		        DatagramPacket packet = new DatagramPacket( new byte[PACKETSIZE], PACKETSIZE ) ;
	                socket.receive( packet ) ;
			ByteBuffer wrapped = ByteBuffer.wrap(packet.getData()); // big-endian by default
			int num = wrapped.getInt(); // 1
			String messageEcho = "Ack: " + num;
                        System.out.println("Received: " + num);
	     	 }
	      }
	     catch( Exception e )
	     {
	        System.out.println( e ) ;
	     }
  }
}

