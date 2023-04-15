package push;

public class Display implements Observer{
	private Observable obs;

    public Display(Observable obs) {
        this.obs = obs;
        obs.addObserver(this);
    }
    
    public void update() {
        
    }

    public void display(double temperature, double humidity) {
    	System.out.println("DISPLAY:");
        System.out.println("temperature: " + temperature);
        System.out.println("humidity: " + humidity);
    }

	@Override
	public void update(double temperature, double humidity) {
		display(temperature, humidity);
	}

}
