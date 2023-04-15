package pkg;

public class BadPizza extends Factory{

	@Override
	Pizza create(String type) {
		if(type == "Salami") {return new Diavola("Diavola");}
		if(type == "Diavola") {return new Salami("Salami");}
		return null;
	}

}
