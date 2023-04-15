package pull;

public class Display implements Observer{
	private Observable obs;

    public Display(Observable obs) {
        this.obs = obs;
        obs.addObserver(this);
    }
    
    public void update() {
        double temperature = obs.getTemperature();
        double humidity = obs.getHumidity();
        display(temperature, humidity);
    }

    public void display(double temperature, double humidity) {
    	System.out.println("DISPLAY:");
        System.out.println("temperature: " + temperature);
        System.out.println("humidity: " + humidity);
    }

}
