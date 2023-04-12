package proxy_printer;

public class PrinterProxy implements Printer {
	private Printer printer;
	private String printerName;
	
	public PrinterProxy(String name) {
		this.printerName = name;
		
		if(name == "SW") {
			printer = new SWPrinter();
		}else if (name == "CO") {
			printer = new ColorPrinter();
		}
	}

	@Override
	public void print(String doc) {
		printer.print(doc);
	}

	@Override
	public void scan(String email) {
		printer.scan(email);
		
	}
	public void switchTo(String name) {
		if(name == "SW") {
			printer = new SWPrinter();
		}else if (name == "CO") {
			printer = new ColorPrinter();
		}
	}
}
