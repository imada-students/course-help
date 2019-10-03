public class SetCard{

	private int amount;
	private char shape, color, fill;

	public SetCard(int amount, char shape, char color, char fill ){
		this.amount = amount;
		this.shape = shape;
		this.color = color;
		this.fill = fill;
	}

	public int amount(){
		return amount;
	}

	public char shape(){
		return shape;
	}

	public char color(){
		return color;
	}

	public char fill(){
		return fill;
	}

}