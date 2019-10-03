import java.util.Scanner;

public class Roman{

	/*
	 * Prints the options menu
	 */
	private static void printMenu(){
			System.out.println("Greetings my friend. I offer the following functions:");
			System.out.println("1. Convert a roman numeral number into decimal");
			System.out.println("2. Convert a number from 1 to 4000 intro roman numeral");
			System.out.println("3. Add two roman numerals together");
			System.out.println("4. Subtract one roman numeral from another");
			System.out.println("5. Check if a string represents a valid roman numeral");
			System.out.println("0. Exit the program");
			System.out.println("Please input either 1, 2, 3, 4, 5, or 0 for each respectrive funtion");
	}

	/*
	 * Checks if a string is a valid roman numeral
	 */
	public static boolean isRomanNum(String s){

		int i = 0;
		int orderCheck = 0;
		int vCheck = 0;
		int lCheck = 0;
		int dCheck = 0;
		int iCheck = 0;
		int xCheck = 0;
		int cCheck = 0;
		boolean isRomanNum = true;

		while ((i < s.length()) && isRomanNum){
			switch(s.charAt(i)){
				/*
				 * Checks if larger roman numerals comes before or after smaller ones.
				 * Also checks if there are non-roman-numeral chars.
				 */
				case 'M' : if (orderCheck <= 1)
					orderCheck = 1;
				else
					isRomanNum = false;
				break;

				case 'D' : if ((orderCheck <= 2) && (dCheck < 1)){
					orderCheck = 2;
					dCheck ++;
				}
				else
					isRomanNum = false;
				break;

				case 'C' : if ((orderCheck <= 3) && (cCheck < 4)){
					orderCheck = 3;
					cCheck ++;
				}
					
				else
					isRomanNum = false;
				break;

				case 'L' : if ((orderCheck <= 4) && (lCheck < 1)){
					orderCheck = 4;
					lCheck ++;
				}
					
				else
					isRomanNum = false;
				break;

				case 'X' : if ((orderCheck <= 5) && (xCheck < 4)){
					orderCheck = 5;
					xCheck ++;
				}
				else
					isRomanNum = false;
				break;

				case 'V' : if ((orderCheck <= 6) && (vCheck < 1)){
					orderCheck = 6;
					vCheck ++;
				}
				else
					isRomanNum = false;
				break;

				case 'I' : if ((orderCheck <= 7) && (iCheck < 4)){
					orderCheck = 7;
					iCheck ++;
				}
				else
					isRomanNum = false;
				break;

				default : isRomanNum = false;
				break;
			}
			i++;
		}
		return isRomanNum;
	}

	/*
	 * Converts roman numeral to decimal
	 */
	public static int romanToNum(String s){
		int i = 0;
		int sum = 0;
		while(i < s.length()){
			switch(s.charAt(i)){
				case 'M' : sum = sum + 1000;
				break;

				case 'D' : sum = sum + 500;
				break;

				case 'C' : sum = sum + 100;
				break;
				
				case 'L' : sum = sum + 50;
				break;

				case 'X' : sum = sum + 10;
				break;

				case 'V' : sum = sum + 5;
				break;

				case 'I' : sum = sum + 1;
				break;

				default : break;
			}
			i++;
		}
		return sum;
	}

	/*
	 * Converts decimal number into roman numeral
	 */
	private static String numToRoman(int n){
		String out = "";
		int i = n;

		while(i >= 1000){
			out = out + 'M';
			i = i - 1000;
		}

		while(i >= 500){
			out = out + 'D';
			i = i - 500;
		}

		while(i >= 100){
			out = out + 'C';
			i = i - 100;
		}

		while(i >= 50){
			out = out + 'L';
			i = i - 50;
		}

		while(i >= 10){
			out = out + 'X';
			i = i - 10;
		}

		while(i >= 5){
			out = out + 'V';
			i = i - 5;
		}

		while(i >= 1){
			out = out + 'I';
			i = i - 1;
		}
		return out;
	}

	/*
	 * "Funnels" a big, potentually invalid, roman numeral string, into an ordered
	 * valid roman numeral 
	 */
	private static String funnelString(String s){
		
		int i = s.length() - 1;
		int iCount = 0;
		int vCount = 0;
		int xCount = 0;
		int lCount = 0;
		int cCount = 0;
		int dCount = 0;
		int mCount = 0;

		String newOutput = "";
		
		/*
		 * Checks for amount of each letter
		 */
		while(i >= 0){
			switch(s.charAt(i)){
				
				case 'I' : 
				iCount ++;
				i --;
				break;

				case 'V' : 
				vCount ++;
				i --;
				break;

				case 'X' : 
				xCount ++;
				i --;
				break;

				case 'L' : 
				lCount ++;
				i --;
				break;

				case 'C' : 
				cCount ++;
				i --;
				break;

				case 'D' : 
				dCount ++;
				i --;
				break;


				case 'M' : 
				mCount ++;
				i --;
				break;
			}
		}

		/*
		 * Converts smaller letters into bigger letters
		 */
		while(iCount > 4){
			vCount ++;
			iCount = iCount - 5;
		}

		while(vCount > 1){
			xCount ++;
			vCount = vCount - 2;
		}

		while(xCount > 4){
			lCount ++;
			xCount = xCount - 5;
		}

		while(lCount > 1){
			cCount ++;
			lCount = lCount - 2;
		}

		while(cCount > 4){
			dCount ++;
			cCount = cCount - 5;
		}

		while(dCount > 1){
			mCount ++;
			dCount = dCount - 2;
		}

		/*
		 * Assembles the new string
		 */
		for(int m = mCount; m > 0; m --)
			newOutput = newOutput + 'M';

		for(int d = dCount; d > 0; d --)
			newOutput = newOutput + 'D';

		for(int c = cCount; c > 0; c --)
			newOutput = newOutput + 'C';

		for(int l = lCount; l > 0; l --)
			newOutput = newOutput + 'L';

		for(int x = xCount; x > 0; x --)
			newOutput = newOutput + 'X';

		for(int j = vCount; j > 0; j --)
			newOutput = newOutput + 'V';

		for(int k = iCount; k > 0; k --)
			newOutput = newOutput + 'I';

		return newOutput;
	}

	/*
	 * Adds two numerals together
	 */
	private static String add(String num1, String num2){
		String out = num1 + num2;
		out = funnelString(out);
		return out;
	}

	/*
	 * Subtracts one roman numeral from another
	 */
	private static String diff(String num1, String num2){
		String out = "";

		while(!funnelString(num2 + out).equals(num1))
			out = out + 'I';

		return funnelString(out);
	}
	

	public static void main(String[] args){
		
		Scanner reader = new Scanner(System.in);
		int option;

		do {

			printMenu();
	
			option = reader.nextInt();
			
			switch(option){

				//Option 1: convert roman to decimal
				case 1 : String romanToDecimal;
				System.out.println("Please input a roman numeral IN ALL CAPS");
				romanToDecimal = reader.next();

				if (isRomanNum(romanToDecimal))
					System.out.println(romanToDecimal + " is " + romanToNum(romanToDecimal) + " in decimal");
				else
					System.out.println(romanToDecimal + " is not a valid roman numeral");
				break;

				//Option 2: convert a decimal number between 1 and 4000 to roman numerals
				case 2 : int decimalToRoman;
				System.out.println("Please enter a number between 1 and 4000");
				decimalToRoman = reader.nextInt();
				if(decimalToRoman > 4000)
					System.out.println("The number is bigget than 4000. Please try again");
				else if (decimalToRoman < 1)
					System.out.println("The number must be at least 1. Please try again");
				else
					System.out.println(decimalToRoman + " is " + numToRoman(decimalToRoman) + " in roman");
				break;

				//Option 3: add two roman numerals together
				case 3 : String firstNumber;
				String secoundNumber;
				System.out.println("Please enter two roman numerals");
				firstNumber = reader.next();
				secoundNumber = reader.next();
				
				if(!isRomanNum(firstNumber) && !isRomanNum(secoundNumber))
					System.out.println("These numbers are not valid roman numerals");
				else if(!isRomanNum(firstNumber) && isRomanNum(secoundNumber))
					System.out.println("The first number is not a valid roman numeral");
				else if(isRomanNum(firstNumber) && !isRomanNum(secoundNumber))
					System.out.println("The secound number is not a valid roman numeral");
				else
					System.out.println("The sum is: " + add(firstNumber, secoundNumber));
				
				break;

				//Option 4: subtract two roman numerals
				case 4 : 
				String num1;
				String num2;
				System.out.println("Please enter two roman numerals. The first must be larger than the other");
				num1 = reader.next();
				num2 = reader.next();
				if(isRomanNum(num1) && isRomanNum(num2)){
					if(romanToNum(num1) > romanToNum(num2)){
						System.out.println("The difference is: " + diff(num1, num2));
					}else
					System.out.println("Your first numeral needs to be larger than your secound");
				}else
				System.out.println("One or both of your roman numerals are not valid");
				break;

				//Option 5: check if a roman numeral is valid
				case 5 : String romanNum;
				System.out.println("Please input a roman numeral IN ALL CAPS");
				romanNum = reader.next();
				if(isRomanNum(romanNum))
					System.out.println(romanNum + " is a valid roman numeral");
				else
					System.out.println(romanNum + " is not a valid roman numeral");
			}
		} while (option != 0);
		reader.close();
		System.out.println("Thank you Dave :)");
	}
}