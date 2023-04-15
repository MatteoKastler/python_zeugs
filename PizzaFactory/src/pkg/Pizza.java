package pkg;

public abstract class Pizza{
	String type;
    public void prepare(){
        System.out.println("preparing");
    }
    public void packaging(){
        System.out.println("packaging");
    }

    public String getType() {
    	return this.type;
    }
}