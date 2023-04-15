package pull;

import java.util.ArrayList;
import java.util.List;

//das konkrete Subjekt
public class WeatherStation implements Observable{
	private List<Observer> observers;
    private double temperature;
    private double humidity;

    public WeatherStation() {
        observers = new ArrayList<>();
    }

    public void set(double temperature, double humidity) {
        this.temperature = temperature;
        this.humidity = humidity;
        notifyObservers();
    }

    @Override
    public void addObserver(Observer observer) {
        observers.add(observer);
    }

    @Override
    public void removeObserver(Observer observer) {
        observers.remove(observer);
    }

    @Override
    public void notifyObservers() {
        for (Observer observer : observers) {
            observer.update();
        }
    }
    
    @Override
    public double getTemperature() {
        return temperature;
    }

    @Override
    public double getHumidity() {
        return humidity;
    }

}