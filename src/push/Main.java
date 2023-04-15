package push;

public class Main {

	public static void main(String[] args) {
		WeatherStation wts = new WeatherStation();

		
        Display dsp = new Display(wts);
        BigScreen scr = new BigScreen(wts);

        wts.set(0,10);

	}

}
