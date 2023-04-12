package proxy_printer;

public class ColorPrinter implements Printer {

	@Override
	public void print(String doc) {
		System.out.println("Colorprinting: " + doc);
		
	}

	@Override
	public void scan(String email) {
		System.out.println("Scanning wiht colorprinter and sending to email" + email);
		
	}

}
