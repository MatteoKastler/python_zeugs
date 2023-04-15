package pull;

public class BigScreen implements Observer {
	private Observable obs;

    public BigScreen(Observable obs) {
        this.obs = obs;
        obs.addObserver(this);
    }
    
    public void update() {
        double temperature = obs.getTemperature();
        double humidity = obs.getHumidity();
        screen(temperature, humidity);
    }

    public void screen(double temperature, double humidity) {
    	System.out.println("BIG SCREEN:");
        System.out.println("temperature: " + temperature);
        System.out.println("humidity: " + humidity);
    }

}
