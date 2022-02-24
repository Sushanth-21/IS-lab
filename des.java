import javax.crypto.*;
import java.util.Scanner;
public class des
{
	public static void main(String[] args) {
		try{
		    KeyGenerator kg=KeyGenerator.getInstance("DES");
		    SecretKey myDESkey=kg.generateKey();
		    Cipher cipher=Cipher.getInstance("DES/ECB/PKCS5Padding");
		    cipher.init(Cipher.ENCRYPT_MODE,myDESkey);
		    Scanner s=new Scanner(System.in);
		    System.out.print("enter message you want to sent:  ");
		    String st=s.nextLine();
            System.out.println("you entered text is ::"+st);
		    byte[] text=st.getBytes();
		    System.out.println("Text in Bytes:  "+text);
		    System.out.println("Text "+new String(text));
		    byte[] textenc=cipher.doFinal(text);
		    System.out.println("Text in Bytes"+textenc);
		    System.out.println("Text Encrypted:   " +new String(textenc));
		    cipher.init(Cipher.DECRYPT_MODE,myDESkey);
		    byte[] textdec=cipher.doFinal(textenc);
		    System.out.println("Text Decrypted:   " +new String(textdec));
		}
		catch(Exception e)
		{
		    System.out.println(e);
		}
	}
}