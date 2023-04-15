package pkg;

public class GoodPizza extends Factory {

	@Override
	Pizza create(String type) {
		if(type == "Salami") {return new Salami("Salami");}
		if(type == "Diavola") {return new Diavola("Diavola");}
		return null;
	}

}
