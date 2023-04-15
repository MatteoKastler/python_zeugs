package pkg;

public abstract class Factory {
	
	 public Pizza make(String type){
	        Pizza p = create(type);
	        p.prepare();
	        p.packaging();
	        System.out.println("pizza done");
	        return p;
	  }
	 
	 abstract Pizza create(String type);
}
