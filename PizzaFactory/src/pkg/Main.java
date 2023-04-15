package pkg;

public class Main {
	public static void main(String[] args) {
        Factory good = new GoodPizza();
        Factory bad = new BadPizza();
        
        System.out.println("Von beiden Pizzerien als erstes Salami dann diavola bestellen:");

        Pizza g1 = good.create("Salami");
        Pizza g2 = good.create("Diavola");
        
        Pizza b1 = bad.create("Salami");
        Pizza b2 = bad.create("Diavola");
        
        System.out.println();
        
        System.out.println("gute Pizzeria:");
        System.out.println(g1.getType());
        System.out.println(g2.getType());
        
        System.out.println();
        
        System.out.println("schlechte Pizzeria:");
        System.out.println(b1.getType());
        System.out.println(b2.getType());
        
        System.out.println("man sieht: die schlechte Pizzeria vertauscht die Bestellungen während es die gute nicht tut");
    }

}
