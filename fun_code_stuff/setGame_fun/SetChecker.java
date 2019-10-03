import java.util.List;
import java.util.ArrayList;

public class SetChecker{
	private List<SetCard> list = new ArrayList<>();

	public static void main(String[] args){
		SetChecker s = new SetChecker();

		s.list.add(new SetCard(2, 'w', 'p', 'f'));
		s.list.add(new SetCard(1, 'b', 'g', 'l'));
		s.list.add(new SetCard(2, 'b', 'p', 'f'));
		s.list.add(new SetCard(3, 'd', 'p', 'f'));
		s.list.add(new SetCard(3, 'd', 'p', 'e'));
		s.list.add(new SetCard(3, 'w', 'g', 'e'));
		s.list.add(new SetCard(3, 'w', 'r', 'l'));
		s.list.add(new SetCard(3, 'b', 'g', 'l'));
		s.list.add(new SetCard(2, 'w', 'r', 'l'));
		s.list.add(new SetCard(1, 'd', 'p', 'f'));
		s.list.add(new SetCard(1, 'd', 'g', 'l'));
		s.list.add(new SetCard(3, 'w', 'p', 'l'));

		System.out.println(s.compare());
	}

	public boolean compare(){
		boolean correct = false;
		int i, j, k;
		for(i = 0; i < list.size()-2 && !correct; i++){
			for(j = i + 1; j < list.size()-1 && !correct; j++){
				for(k = j + 1; k < list.size() && !correct; k++){
					correct = (compareAmount(i,j,k) && compareShape(i,j,k) && compareColor(i,j,k) && compareFill(i,j,k));
				}
			}
		}

		return correct;

	}

	private boolean compareAmount(int c1, int c2, int c3){
		if (list.get(c1).amount() == list.get(c2).amount() && list.get(c1).amount() == list.get(c3).amount())
			return true;
		if (list.get(c1).amount() != list.get(c2).amount() && list.get(c1).amount() != list.get(c3).amount() && list.get(c2).amount() != list.get(c3).amount())
			return true;
		return false;
	}

	private boolean compareShape(int c1, int c2, int c3){
		if (list.get(c1).shape() == list.get(c2).shape() && list.get(c1).shape() == list.get(c3).shape())
			return true;
		if (list.get(c1).shape() != list.get(c2).shape() && list.get(c1).shape() != list.get(c3).shape() && list.get(c2).shape() != list.get(c3).shape())
			return true;
		return false;
	}

	private boolean compareColor(int c1, int c2, int c3){
		if (list.get(c1).color() == list.get(c2).color() && list.get(c1).color() == list.get(c3).color())
			return true;
		if (list.get(c1).color() != list.get(c2).color() && list.get(c1).color() != list.get(c3).color() && list.get(c2).color() != list.get(c3).color())
			return true;
		return false;
	}

	private boolean compareFill(int c1, int c2, int c3){
		if (list.get(c1).fill() == list.get(c2).fill() && list.get(c1).fill() == list.get(c3).fill())
			return true;
		if (list.get(c1).fill() != list.get(c2).fill() && list.get(c1).fill() != list.get(c3).fill() && list.get(c2).fill() != list.get(c3).fill())
			return true;
		return false;
	}
}