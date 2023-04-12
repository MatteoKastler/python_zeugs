package proxy_printer;

public class main {

	public static void main(String[] args) {
		 Printer sw = new PrinterProxy("SW");
	        sw.scan("asdf@htl.at");
	        sw.print("Das ist volle das dokument und so");
	}

}
