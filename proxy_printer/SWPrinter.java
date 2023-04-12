package proxy_printer;

public class SWPrinter implements Printer {

	@Override
	public void print(String doc) {
		System.out.println("SW-printing: " + doc);
		
	}

	@Override
	public void scan(String email) {
		System.out.println("Scanning wiht SWprinter and sending to email" + email);
		
	}

}
